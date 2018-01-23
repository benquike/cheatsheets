#include <iostream>
using namespace std;

/**
 * Definition for singly-linked list.
 */
class ListNode {
public:
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

int listLen(ListNode *h) {
  if (h == NULL)
    return 0;
  
  int ret = 1;
  ListNode *t = h->next;

  while (t != NULL) {
    ret ++;
    t = t->next;
  }

  return ret;
}

ListNode *goNStep(ListNode *h, int n) {
  while (h != NULL && n) {
    h = h->next;
    n--;
  }

  return h;
}

class Solution {
public:
    int cycleSize(ListNode *head) {
        int size = 0;
        ListNode *t1 = head, *t2 = head;

        while (t2 != None) {
            t2 = t2->next;

            if (t2 == NULL)
                break;

            t2 = t2->next;
            t1 = t1->next;

            if (t1 == t2)
                break;
        }

        if (t2 == NULL) {
            return ret;
        }

        // break out with t1 == t2
        t1 = t1->next;
        ret ++;
        while (t1 != t2) {
            ret ++;
            t1 = t1->next;
        }
        return ret;
    }
  ListNode *detectCycle(ListNode *head) {
    ListNode *t1 = head, *t2 = head;

    while (t2 != NULL) {
      t2 = t2->next;
      if (t2 == NULL)
	break;
      t2 = t2->next;
      t1 = t1->next;

      if (t1 == t2)
	break;
    }

    if (t1 == NULL)
      return  NULL;
    
    // use t1 as the tail
    t2 = t1->next;
    t1->next = NULL;  
  }

  int l1 = listLen(head);
  int l2 = listLen(t2);
  ListNode *x1 = head;
  ListNode *x2 = t2;

  if (l1 > l2) {
    x1 = goNStep(x1, l1 - l2);
  } else if (l1 < l2) {
    x2 = goNStep(x2, l2 - x1);
  }

  while (x1 != x2) {
    x1 = x1->next;
    x2 = x2->next;
  }

  return x1;
};


int main() {
  ListNode n1(1), n2(2), n3(3),n4(4), n5(5), n6(6), n7(7);
  n1.next = &n2;
  n2.next = &n3;
  n3.next = &n4;
  n4.next = &n5;
  n5.next = &n6;
  n6.next = &n6;
  n7.next = &n3;

  Solution s;
  ListNode *x = s.detectCycle(&n1);

  cout << x->val << endl;
}
