class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = ''
        
        if len(strs) == 0:
            return ''
        
        i = 0
        
        while True:
            if i >= len(strs[0]):
                break
            c = strs[0][i]
            
            brk = False
            for s in strs[1:]:
                if len(s) <= i or s[i] != c:
                    brk = True
                    break
            
            if brk:
                break

            i = i + 1
    
        return strs[0][0:i]

s = Solution()
    
def test_empty():

    strs = []
    assert s.longestCommonPrefix(strs) == ''

    strs=['', 'aaa', 'aaa', 'aaa']
    assert s.longestCommonPrefix(strs) == ''

    strs = ['a', 'a', 'a', 'a']
    assert s.longestCommonPrefix(strs) == 'a'

    strs = ['aaa', 'a', 'a', 'a', 'a']
    assert s.longestCommonPrefix(strs) == 'a'

    strs = ['aaa', 'aab', 'aac', 'aad', 'aae']
    assert s.longestCommonPrefix(strs) == 'aa'
