


'''
Given an array nums, write a function to move all 0's to the
end of it while maintaining the relative order of the non-zero
elements.

For example, given nums = [0, 1, 0, 3, 12], after calling
your function, nums should be [1, 3, 12, 0, 0].
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        nZ = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i + 1
                while j < len(nums) and nums[j] == 0:
                    j = j + 1

                if j == len(nums):
                    return

                x = j
                while x < len(nums) - nZ:
                    nums[x - (j-i)] = nums[x]
                    x = x + 1
                for u in range(len(nums) - nZ - (j-i), len(nums) - nZ):
                    nums[u] = 0

                nZ = nZ + j - i
            print 'i=' + str(i) + ',' + str(nums)

if __name__ == '__main__':
    s = Solution()
    l0 = []
    # s.moveZeroes(l0)
    # print l0

    l1 = [1, 0, 2]
    # s.moveZeroes(l1)
    # print l1

    l2 = [1, 0, 0, 2]
    # s.moveZeroes(l2)
    # print l2

    l3 = [0,1,0,3,12]
    s.moveZeroes(l3)
    # print l3
    
