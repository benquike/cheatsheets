class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 2:
            return []

        def __sol(nums, i, d):
            # print "nums:" + str(nums) + ', i:' + str(i) + ',d:' + str(d)
            if i >= len(nums):
                d[i] = []
                return d[i]

            if i not in d:
                # find all increasing subsequence
                j = i + 1
                u = [[nums[i]]]
                while j < len(nums):
                    while j < len(nums) and nums[j] < nums[i]:
                        j = j + 1
                    if j == len(nums):
                        break
                    x = __sol(nums, j, d)
                    print "XXXX, i:" + str(i) + ", d:" + str(d)
                    y = [[nums[i]] + sn for sn in x]
                    u = u + y
                    v = j + 1
                    while v < len(nums) and nums[v] == nums[j]:
                        v = v + 1
                    j = v
                d[i] = u
            return d[i]

        d = {}
        for i in range(len(nums)):
            __sol(nums, i, d)

        res = []

        for i in range(len(nums)):
            for x in d[i]:
                if len(x) >= 2:
                    res.append(x)
        return res

if __name__ == '__main__':
    s = Solution()
    print s.findSubsequences([4,6,7,7])
