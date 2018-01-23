class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i in range(k):
            if i < len(nums):
                if nums[i] in d:
                    return True
                d[nums[i]] = 1
        
        for i in range(k, len(nums)):
            d.pop(nums[i-k], None)
            if nums[i] in d:
                return True
            d[nums[i]] = 1
        return False

if __name__ == '__main__':
    l = [1,2,3,4,5, 1]
    s = Solution()
    print s.containsNearbyDuplicate(l, 1)
    print s.containsNearbyDuplicate(l, 2)
    print s.containsNearbyDuplicate(l, 3)
    print s.containsNearbyDuplicate(l, 4)
    print s.containsNearbyDuplicate(l, 5)
    print s.containsNearbyDuplicate(l, 6)
    print s.containsNearbyDuplicate(l, 7)
    print s.containsNearbyDuplicate([-1, -1], 1)
