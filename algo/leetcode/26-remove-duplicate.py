class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        e = len(nums) - 1
        ret = 0
        while i <= e:
            x = nums[i]
            j = i + 1
            while nums[j] == x:
                j = j + 1
            if j != i + 1:
                s = 0
                while s <= e-j:
                    nums[i+1 + s] = nums[j+s]
                    s = s + 1
                e = j - i - 1
                ret = ret + j - i - 1
            i = i + 1
        return  ret

if __name__ == '__main__':
    s = Solution()
    l = [1,1,1,2, 2, 2, 3,3]
    print s.removeDuplicates(l)
    print l
