# 14. Longest Common Prefix

## description

```
Write a function to find the longest common prefix string amongst an array of strings.
```


## naive implementation

```
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
```


