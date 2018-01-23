import collections

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        d1 = collections.defaultdict(int)
        for c in p:
            d1[c] = d1[c] + 1
        
        d2 = collections.defaultdict(int)
        
        for i in range(len(p)):
            d2[s[i]] = d2[s[i]] + 1
        ret = []
        if d1 == d2:
            ret.append(0)
    
        for i in range(len(p), len(s)):
            d2[s[i]] = d2[s[i]] + 1
            d2[s[i - len(p)]] = d2[s[i - len(p)]] - 1
            print d1
            print d2
            if d1 == d2:
                ret.append(i - len(p) + 1)
    
        return ret

if __name__ == '__main__':
    s = Solution()
    print s.findAnagrams('cbaebabacd', 'abc')
