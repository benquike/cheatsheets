class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int

        >>> s = Solution()
        >>> s.compareVersion('', '')
        0
        >>> s.compareVersion('', '0')
        -1

        >>> s.compareVersion('0', '0')
        0

        >>> s.compareVersion('1', '1.1')
        -1

        >>> s.compareVersion('1.1', '1')
        1

        >>> s.compareVersion('1.0', '1')
        1

        >>> s.compareVersion('1.1.0', '1.1')
        1

        """

        if len(version1) == 0 and len(version2) == 0:
            return 0
        elif len(version1) == 0 and len(version2) > 0:
            return -1
        elif len(version1) > 0 and len(version2) == 0:
            return 1

        i1 = version1.find('.')
        i2 = version2.find('.')

        if i1 == -1 or -2 == -1:
            v1 = version1
            if i1 != -1:
                v1 = version1[:i1]
            v2 = version2
            if i2 != -1:
                v2 = version2[:i2]

            if int(v1) < int(v2):
                return -1
            if int(v1) > int(v2):
                return 1

        if i1 != -1 and i2 != -1:
            return self.compareVersion(version1[i1+1], version2[i2+1])

        if i1 == -1 and i2 == -1:
            return 0
        if i1 != -1:
            return 1
        return -1

if __name__ == "__main__":
    import doctest
    doctest.testmod()
