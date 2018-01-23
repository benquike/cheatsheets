class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        if input.find('+') == -1 and \
            input.find('-') == -1 and \
            input.find('*') == -1:
                return [int(input)]

        if len(input) == 0:
            return []

        def comp(op, n1, n2):
            if op == '+':
                return n1 + n2
            if op == '-':
                return n1 - n2

            if op == '*':
                return n1 * n2

        ret = []
        d = {}
        for i in range(len(input)):
            if input[i] == '+' or input[i] == '-' or input[i] == '*':
                if input[0:i] not in d:
                    d[input[0:i]] = self.diffWaysToCompute(input[0:i])

                if input[i+1:len(input)] not in d:
                    d[input[i+1:len(input)]] = self.diffWaysToCompute(input[i+1:len(input)])

                for n1 in d[input[0:i]]:
                    for n2 in d[input[i+1:len(input)]]:
                        ret.append(comp(input[i], n1, n2))
            else:
                continue

        return ret

if __name__ == '__main__':
    s = Solution()
    print s.diffWaysToCompute('2-1-1')
