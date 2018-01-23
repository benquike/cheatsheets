class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return True
        d1 = [] # the first player win?
        d2 = [] # the second player win?
        l = len(nums)
        for i in range(l):
            d1.append([])
            d2.append([])
            for j in range(l):
                d1[i].append(None)
                d2[i].append(None)

        # def sol(nums, i, j, s1, s2, d1, d2, player):

        #     if i > j:
        #         if s1 > s2:
                    
        #     if player == 1:
        #         if d1[i][j] == None:
        #             if sol(nums, i + 1, j, s1 + nums[i], s2 d1, d2, 2) == True or sol(nums, i, j-1, s1 + nums[j], s2 d1, d2, 2) == True:
        #                 d1[i][j] = True
        #             else:
        #                 d1[i][j] = False
        #         return d1[i][j]
        #     else:
        #         if d2[i][j] == None:
        #             if sol(nums, i+1, j, s1, s2 + nums[i], d1, d2, 1) == True or sol(nums, i, j-1,s1, s2 + nums[j],  d1, d2, 2) == True:
        #                 d2[i][j] = True
        #             else:
        #                 d2[i][j] == False

        #         return d2[i][j]

        def sol(nums, i, j, s1, s2, player):
            if i > j:
                
