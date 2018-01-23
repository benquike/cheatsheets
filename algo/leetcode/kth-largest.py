class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # print "== nums: " + str(nums) + ", k = " + str(k)
        if len(nums) == 0:
            return -1

        sentinal = nums[0]
        i = 1
        j = len(nums) - 1
        while True:
            while i < len(nums) and nums[i] >= sentinal:
                i = i + 1
            while j > 0 and nums[j] < sentinal:
                j = j - 1

            if j <= i:
                break

            # swap
            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t

            i = i + 1
            j = j - 1

        # print "nums:" + str(nums)
        # print "j:" + str(j)
        if j + 1 == k:
            return sentinal
        elif j + 1 > k:
            return self.findKthLargest(nums[1:i], k)
        else:
            return self.findKthLargest(nums[i:], k - j - 1)


if __name__ == '__main__':
    l = [3,2,1,5,6,4]
    s = Solution()
    print s.findKthLargest(l, 2)

    l = [1, 1, 1, 2, 2, 2]
    print s.findKthLargest(l, 1)
    print s.findKthLargest(l, 2)
    print s.findKthLargest(l, 3)
    print s.findKthLargest(l, 4)
    print s.findKthLargest(l, 5)
    print s.findKthLargest(l, 6)
