import collections

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = collections.OrderedDict()
        for c in s:
            if c not in m:
                m[c] = 1
            else:
                m[c] = m[c] + 1
        
        ret = ''
        for k,v in m.iteritems():
            ret = ret + v * k
        return  ret


if __name__ == '__main__':
    s = Solution()
    print s.frequencySort("loveleetcode")
