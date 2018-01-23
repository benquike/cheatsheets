class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        def isAlphaNum(c):
            if (ord(c) >= ord('0') and ord(c) <= ord('9')) or \
                (ord(c) >= ord('a') and ord(c) <= ord('z')) or \
                (ord(c) >= ord('A') and ord(c) <= ord('Z')):
                    return True
            return False
        
        s = s.lower()

        l = len(s)
        i = 0
        j = l - 1
        
        while i <= j:
            while i < l and not isAlphaNum(s[i]):
                i = i + 1
            while j >= 0 and not isAlphaNum(s[j]):
                j = j - 1

            print 'i=' + str(i) + ',j=' + str(j)
            if i >= l or j < 0 or i > j:
                break

            if s[i] != s[j]:
                return False
                
            i = i + 1
            j = j - 1

        return True
        
if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome('ab')
