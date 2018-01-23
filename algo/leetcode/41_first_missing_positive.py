class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        n = len(nums)
        if n == 0:
            return 1

        def repose(nums, i):
            if nums[i] > 0 and nums[i] <= n and i != nums[i] - 1 and nums[i] != nums[nums[i] - 1]:
                t = nums[nums[i] - 1]  # original
                nums[nums[i] - 1] = nums[i]
                nums[i] = t

                repose(nums, i)

        for i  in range(n):
            repose(nums, i)

        print nums
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1        
        return n + 1

if __name__ == "__main__":
    s = Solution()
    # print s.firstMissingPositive([1])
    # print s.firstMissingPositive([-1, 0, 1])
    print s.firstMissingPositive([1, 1])
