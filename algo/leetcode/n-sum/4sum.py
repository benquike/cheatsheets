class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if nums == None or len(nums) < 4:
            return []

        def twoSum(ns, target):
            if ns == None or len(ns) <= 1:
                return []
            ret = []
            i = 0
            j = len(ns) - 1
            while i < j:
                if ns[i] + ns[j] == target:
                    ret.append([ns[i], ns[j]])
                    ns_i = ns[i]
                    ns_j = ns[j]
                    i = i + 1
                    while i < j and ns_i == ns[i]:
                        i = i + 1
                    j = j - 1
                    while i < j and ns_j == ns[j]:
                        j = j - 1
                elif ns[i] + ns[j] < target:
                    i = i + 1
                else:
                    j = j - 1
            return ret

        def threeSum(ns, target):
            if ns == None or len(ns) < 3:
                return []
            ret = []

            i = 0
            while i < len(ns):
                first = ns[i]
                for k in twoSum(ns[i+1:], target - first):
                    ret.append([first] + k)

                i = i + 1
                while i < len(ns) and ns[i] == first:
                    i = i + 1

            return ret

        nums.sort()
        ret = []
        i = 0
        while i < len(nums):
            first = nums[i]
            for k in threeSum(nums[i+1:], target - first):
                ret.append([first] + k)

            i = i + 1
            while i < len(nums) and nums[i] == first:
                i = i + 1

        return ret

if __name__ == '__main__':
    s = Solution()
    print s.fourSum([1,0,-1,0,-2,2], 0)
