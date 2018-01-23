class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        def twoSum(ns, target):
            if ns == None or len(ns) <= 1:
                return []
            ret = []
            i = 0
            j = len(ns) - 1
            while i < j:
                if ns[i] + ns[j] == target:
                    ret.append([ns[i], ns[j]])
                    i = i + 1
                    j = j - 1
                elif ns[i] + ns[j] < target:
                    i = i + 1
                else:
                    j = j - 1
            return ret

        i = 0
        ret = []
        l = len(nums)
        while i < l:
            first = nums[i]
            del nums[i]
            for k in twoSum(nums, -1 * first):
                ret.append([first] + k)
            nums.insert(i, first)
            j = i + 1
            while j < l and nums[j] == first:
                j = j + 1

            i = j

        return ret

if __name__ == '__main__':
    s = Solution()
    print s.threeSum([-1,0,1,2,-1,-4])
