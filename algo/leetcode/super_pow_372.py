class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        a = a % 1337
        if len(b) == 0:
            return a

        apn = 1  # ap0
        ret = 1
        l = len(b)

        for i in range(l):
            if i > 0:
                for k in range(10):
                    apn = apn * a
                    apn = apn % 1337

            u = 1
            t = a
            if i > 0:
                t = apn

            for j in range(b[l - 1 - i]):
                u = u * t
                u = u % 1337

            ret = (ret * u) % 1337

        return ret

if __name__ == "__main__":
    s = Solution()
    print s.superPow(2, [1, 0])
    print s.superPow(2147483647, [2,0,0])
