class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return 
        if len(nums) == 0:
            return
        l = len(nums)
        for i in range(k):
            f = nums[l-1]
            for j in range(l-1, 0, -1):
                nums[j] = nums[j-1]
            nums[0] = f

if __name__ == '__main__':
    l0 = []
    s = Solution()
    s.rotate(l0, 1)
    print l0

    l1 =  [1,2,3,4]
    s.rotate(l1, 0)
    print l1

    l2 = [1, 2, 3, 4]
    s.rotate(l2, 1)
    print l2


    l3 = [1]
    s.rotate(l3, 0)
    print l3

    s.rotate(l3, 1)
    print l3

    s.rotate(l3, 2)
    print l3

    s.rotate(l3, 3)
    print l3


    l4 = [1,2]
    s.rotate(l4, 1)
    print l4
