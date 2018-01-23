class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        print "nums:" + str(nums) + ', S:' + str(S)
        if len(nums) == 1:
            ret = 0
            if nums[0] == S:
                ret = ret + 1
            if -1 * nums[0] == S:
                ret = ret + 1
            return ret

        return self.findTargetSumWays(nums[1:], S - nums[0]) + self.findTargetSumWays(nums[1:], S + nums[0])

if  __name__ == '__main__':
    s = Solution()
    print s.findTargetSumWays([1,1,1,1,1], 3)
    print s.findTargetSumWays([1,0], 1)
