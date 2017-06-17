//===- Hello.cpp - Example code from "Writing an LLVM Pass" ---------------===//
//
//                     The LLVM Compiler Infrastructure
//
// This file is distributed under the University of Illinois Open Source
// License. See LICENSE.TXT for details.
//
//===----------------------------------------------------------------------===//
//
// This file implements two versions of the LLVM "Hello World" pass described
// in docs/WritingAnLLVMPass.html
//
//===----------------------------------------------------------------------===//

#include <map>
#include <utility>
#include <set>
#include <vector>
#include <memory>
#include <fstream>

#include "llvm/ADT/Statistic.h"
#include "llvm/IR/Constant.h"
#include "llvm/IR/Constants.h"
#include "llvm/IR/Function.h"
#include "llvm/IR/Operator.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/CallSite.h"
#include "llvm/Pass.h"
#include "llvm/Support/raw_ostream.h"

using namespace llvm;
using namespace std;

#define DEBUG_TYPE "CGRAPH"
#define ENTRY_FUNC "main"

namespace {

  struct cgraph : public ModulePass {
    static char ID; // Pass identification, replacement for typeid
    cgraph() : ModulePass(ID) {}

    typedef map<Value *, Value *> VariableStore;
    typedef shared_ptr<VariableStore> VariableStore_Ptr;
    typedef pair<BasicBlock *, VariableStore_Ptr> WorkListItem;
    typedef shared_ptr<WorkListItem> WorkListItem_Ptr;
    typedef map<Function *, set<Value*> > CallGraphResult;

  private:
    vector<Function *> functions;
    Function *mainFn = NULL;
    StringRef module_name;

    bool runOnModule(Module &M) override {
      for (Function &Func: M) {
        functions.push_back(&Func);
      }

      // TODO: collect the call graph
      Function *mainFn = M.getFunction(ENTRY_FUNC);
      if (!mainFn) {
        errs() << "No main function defined\n";
        return false;
      }

      CallGraphResult resultMap;
      VariableStore gmap;
      VariableStore lmap;
      map<Function *, int> status;

      collectCallGraph(*mainFn, resultMap, gmap, lmap, status);

      // for (Function* f : functions) {
      //   lmap.clear();
      //   status.clear();
      //   collectCallGraph(*f, resultMap, gmap, lmap, status);
      // }

      // dump the call graph
      dumpCallGraph(resultMap);

      return false;
    }

    bool doInitialization(Module &M) {
      // errs() << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";
      // errs() << "Call Graph pass to initialization\n";
      // errs() << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";
      module_name = M.getName();
      return false;
    }

    bool isGlobal(Value *v) {
      if (isa<GlobalVariable>(v))
        return true;

      if (GEPOperator *gepOp = dyn_cast<GEPOperator>(v)) {
        if (isa<GlobalVariable>(gepOp->getPointerOperand())){
          return true;
        }
      }

      return false;
    }

    /***
     * how to get elements of a struct initializer
     *  - GlobalVariable::hasInitilizer()
     *  - GlobalVariable::getInitilizer() returns a Constant pointer
     *    How can we get individual parts of the initializer?
     */
    void collectCallGraph(Function &func, CallGraphResult &result,
                          VariableStore &globalMap, VariableStore &localMap,
                          map<Function *, int> &status) {

      // errs() << "~~~ Start handling " << func.getName() << " ~~~\n";
      if (func.isDeclaration()) {
        errs() << func.getName() << " is just a declaration, skipping\n";
        return;
      }

      if (status.find(&func) != status.end() && status[&func] == 1) {
        errs() << "recursion detected\n";
        return;
      }

      status[&func] = 1;
      vector<WorkListItem_Ptr> worklist;
      set<BasicBlock *> visited;

      if (result.find(&func) == result.end()) {
        result[&func] = set<Value *>();
      }
      // worklist algorithm
      BasicBlock *entryBlock = &func.getEntryBlock();
      VariableStore_Ptr initStore = VariableStore_Ptr(new VariableStore(localMap));
      WorkListItem_Ptr initItem = WorkListItem_Ptr(new WorkListItem(entryBlock, initStore));
      worklist.push_back(initItem);

      while (!worklist.empty()) {
        // extract an unexplored path
        WorkListItem_Ptr item = worklist.back();
        worklist.pop_back();
        BasicBlock *bb1 = item->first;
        VariableStore_Ptr p_VariableStore = item->second;
        BasicBlock *nextBlk = NULL;

        while (true) {

          nextBlk = NULL;

          for (Instruction &inst: *bb1) {

            switch (inst.getOpcode()) {
            case Instruction::Call: {
              // errs() << "Handling call instruction\n";
              CallSite cs(&inst);

              Value* called = cs.getCalledValue()->stripPointerCasts();
              // errs() << "called:" << *called << "\n";
              Function *f = dyn_cast<Function>(called);
              if (!f){
                // indirect call
                Value *lv = NULL;
                if (isGlobal(called)) {
                  // errs() << "called is global\n";
                  if (globalMap.find(called) == globalMap.end()) {
                    errs() << "Could not find the calle function\n";
                  } else {
                    lv = globalMap[called];
                  }
                } else {
                  // errs() << "called is local\n";
                  if (p_VariableStore->find(called) == p_VariableStore->end()) {
                    errs() << "Could not find the calle function\n";
                  } else {
                    lv = (*p_VariableStore)[called];
                  }
                }

                if (lv == NULL) {
                  errs() << "lv: is NULL\n";
                } else {
                  f = dyn_cast<Function>(lv);
                  if (!f) {
                    errs() << "called destination is not a function " <<  *lv <<  "\n";
                    // exit here
                  }
                }
              }

              if (f != NULL) {
                // add it to the called functions
                result[&func].insert(f);

                VariableStore lm;
                int i = 0;
                // construct the arg map;
                for (Function::arg_iterator it = f->arg_begin(); it != f->arg_end(); it++) {
                  // lm[&(*it)] = cs.getArgOperand(i++);
                  // bind args
                  // TODO: var arg support

                  // errs() << "it:" << *it << "\n";
                  Value *v = cs.getArgOperand(i++);

                  if (ConstantExpr *ce = dyn_cast<ConstantExpr>(v)) {
                    if (ce->getOpcode() == Instruction::BitCast)
                      v = ce->getOperand(0);
                  }
                  // errs() << "v:" << *v << "\n";

                  if (isa<Function>(v)) {
                    // errs() << "==== Function\n";
                    lm[&(*it)] = v;
                  } else if (isGlobal(v)) {
                    // errs() << "==== from global store\n";
                    lm[&(*it)] = globalMap[v];
                  } else {
                    // errs() << "==== Not from global store\n";
                    lm[&(*it)] = (*p_VariableStore)[v];
                  }
                }
                // FIXME: recursive functions
                collectCallGraph(*f, result, globalMap, lm, status);
              }

              break;
            }

            case Instruction::Br: {
              // the end of a basic block
              // i.e. there should be no Instruction after this
              BranchInst *branchInst = dyn_cast<BranchInst>(&inst);
              if (branchInst->isUnconditional()) {
                nextBlk = branchInst->getSuccessor(0);
              } else {
                // very important part
                BasicBlock *b0 = branchInst->getSuccessor(0);
                BasicBlock *b1 = branchInst->getSuccessor(1);

                // handle branch instruction only if its successors
                // are not visited
                if (visited.find(b0) == visited.end() &&
                    visited.find(b1) == visited.end()) {
                  nextBlk = b0;

                  VariableStore_Ptr tmp_vs_p = VariableStore_Ptr(new VariableStore(*p_VariableStore));
                  worklist.push_back(WorkListItem_Ptr(new WorkListItem(b1, tmp_vs_p)));

                  // mark them as visited
                  visited.insert(b0);
                  visited.insert(b1);
                }
              }
              break;
            }

            case Instruction::Switch: {

              break;
            }

            case Instruction::Load: {
              LoadInst *loadInst = dyn_cast<LoadInst>(&inst);
              Value *src = loadInst->getOperand(0);

              if (isGlobal(src)) {
                (*p_VariableStore)[loadInst] = globalMap[src];
              } else {
                (*p_VariableStore)[loadInst] = (*p_VariableStore)[src];
              }

              // errs() << "load src:"<< *src << "==> " << *(*p_VariableStore)[loadInst] << "\n";

              break;
            }

            case Instruction::Store: {

              StoreInst *storeInst = dyn_cast<StoreInst>(&inst);
              Value *from = storeInst->getOperand(0);
              Value *to = storeInst->getOperand(1);

              // errs() << "from:" << *from << "\n";
              // errs() << "to:" << *to << "\n";
              if (isa<Constant>(from)) {
                // errs() << "from is constant\n";
                if (ConstantExpr *ce = dyn_cast<ConstantExpr>(from)) {
                  // we are only interested in function pointers
                  if (ce->getOpcode() == Instruction::BitCast) {
                    // ugly code
                    if (isGlobal(to)) {
                      // errs() << "to is global\n";
                      globalMap[to] =  ce->getOperand(0);
                    } else {
                      // errs() << "to is local, " << *to <<" -> " <<  *(ce->getOperand(0)) <<"\n";
                      (*p_VariableStore)[to] = ce->getOperand(0);
                    }
                  }
                }
              } else {
                // errs() << "from is not constant\n";
                // it is an indirect store
                if (isGlobal(to)) {
                  // errs() << "to is global\n";
                  if (isGlobal(from)) {

                    // errs() << "from is global\n";
                    // TODO: refractor this part
                    if (globalMap.find(from) != globalMap.end()) {
                      globalMap[to] = globalMap[from];
                    } else {
                      errs() << "No corresponding mapping for:" << *from << "\n";
                    }
                  } else {
                    // errs() << "from is local\n";
                    globalMap[to] = (*p_VariableStore)[from];
                  }

                } else {
                  // errs() << "to is local\n";
                  if (isGlobal(from)) {
                    // errs() << "from is global\n";
                    (*p_VariableStore)[to] = globalMap[from];
                  } else {
                    // errs() << "from is local\n";
                    (*p_VariableStore)[to] = (*p_VariableStore)[from];
                  }
                }
              }

              break;
            }
            default:

              break;
            }
          }

          if (nextBlk == NULL) {
            break;
          }

          bb1 = nextBlk;
        }
      }

      status[&func] = 2;
      // errs() << "=== End handling " << func.getName() << " ===\n";
    }

    void dumpCallGraph(CallGraphResult &result) {
      ofstream dotfile;
      dotfile.open(module_name.str() +  "_callgraph.dot", ios::out | ios::trunc);

      dotfile << "digraph callgraph {" << endl;
      for (CallGraphResult::iterator it = result.begin(); it != result.end(); it ++) {
        errs() << it->first->getName() << ":";

        for (set<Value *>::iterator its = it->second.begin(); its != it->second.end(); its ++) {
          if (Function *f = dyn_cast<Function>(*its)) {
             errs() << f->getName() << ",";
             dotfile << "\t" << it->first->getName().str() << " -> " << f->getName().str() << ";" << endl;
             continue;
          }

          if (ConstantExpr *ce = dyn_cast<ConstantExpr>(*its)) {
            errs() << *ce << ",";
          } else {
            errs() << "N/A,";
          }
        }

        errs() << "\n";
      }

      dotfile << "}" << endl;
      errs() << "Call graph dot file was written to " << module_name << "_callgraph.dot\n";

      dotfile.close();
    }

    bool doFinalization(Module & M) {
      return false;
    }

    // We don't modify the program, so we preserve all analyses.
    void getAnalysisUsage(AnalysisUsage &AU) const override {
      AU.setPreservesAll();
    }
  };
}

char cgraph::ID = 0;
static RegisterPass<cgraph> CGRAPH("cgraph", "Call Graph Pass");
