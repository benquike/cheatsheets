class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if s == None or s == '':
            return 0
        l = len(s)
        if l == 1:
            return 0
            
        dp = []
        sdp = []
        for i in range(l + 1):
            dp.append([])
            sdp.append([])
            for j in range(l + 1):
                dp[i].append(False)
                sdp[i].append(-1)
        
        for i in range(l):
            dp[i][i] = True
            dp[i][i+1] = True
            sdp[i][i] = 0
            sdp[i][i+1] = 0
        
        for step in range(2, l+1):
            for i in range(0, l - step + 1):
                # figure out whether s[i:i+step] is a palindrome or not
                if dp[i+1][i+step-1] and s[i] == s[i+step-1]:
                    dp[i][i+step] = True
                    sdp[i][i+step] = 0
                else:
                    dp[i][i+step] = False
                    sdp[i][i+step] = min([sdp[i][k] + sdp[k][i+step] for k in range(i+1, i+step)]) + 1

        print sdp[0][l]

if __name__ == '__main__':
    s = Solution()
    s.minCut("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp")
