#!/usr/bin/python

'''
282. Expression Add Operators

Given a string that contains only digits 0-9 and a target value, return all 
possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples: 
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
Credits:
Special thanks to @davidtan1890 for adding this problem and creating all test cases.

Subscribe to see which companies asked this question
'''

class Solution(object):

    def addOperators(self, num, target):

        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ret = []
        for exp in self.get_all_exps(num):
            if eval(exp) == target:
                ret.append(exp)

        return ret

    def get_all_exps(self, num):
        ops = ['*', '+', '-']

        if len(num) == 1:
            yield num
        else:
            for op in ops:
                for sub_exp in self.get_all_exps(num[1:]):
                    yield num[0] + op + sub_exp


if __name__ == '__main__':
    sol = Solution()
    print sol.addOperators('123', 6)
