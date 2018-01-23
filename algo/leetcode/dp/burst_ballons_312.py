class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def list_to_str(l):
            if l == None or len(l) == 0:
                return "None"
            return '-'.join([str(x) for x in l])

        def max_coins(nums, d):
            s = list_to_str(nums)
            if s in d:
                return d[s]

            if nums == None or len(nums) == 0:
                # print 'd[-] set to 0'
                d[s] = 0
            elif len(nums) == 1:
                d[s] = nums[0]
            else:
                m = -0xFFFFFFFF
                for i in range(len(nums)):
                    l = 1
                    if i - 1 >= 0:
                        l = nums[i-1]
                    r = 1
                    if i+1 < len(nums):
                        r = nums[i+1]
                    current = l * r * nums[i] + max_coins(nums[:i] + nums[i+1:], d)
                    # print 'current:' + str(current)
                    if m < current:
                        m = current
                d[s] = m

            # print s + ':' + str(d[s])
            return d[s]

        d = {}
        max_coins(nums, d)
        return d[list_to_str(nums)]

if __name__ == '__main__':
    s = Solution()
    # print s.maxCoins([3,1,5,8])
    # print s.maxCoins([])
    print s.maxCoins([2,4,8,4,0,7,8,9,1,2,4,7,1,7,3,6])
