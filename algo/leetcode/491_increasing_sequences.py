class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def __sol(nums, i, d):
            if i == 0:
                d.append([[nums[i]]])
                return

            assert i > 0 and i < len(nums)
            p = [[nums[i]]]

            for l in d[i-1]:
                p.append(l)
                if nums[i] >= l[len(l)-1]:
                    p.append(l + [nums[i]])

            d.append(p)
            return

        d = []
        for i in range(len(nums)):
            __sol(nums, i, d)

        res = {}

        for i in range(len(nums)):
            for x in d[i]:
                if len(x) >= 2 and tuple(x) not in res:
                    res[tuple(x)] = True

        return [list(x) for x in res.keys()]

if __name__ == '__main__':
    s = Solution()
    print s.findSubsequences([4, 6, 7, 7])
