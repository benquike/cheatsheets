# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        def __cmp(x1, x2):
            if x1.end < x2.end:
                return -1
            elif x1.end > x2.end:
                return 1
            else:
                if x1.start < x2.start:
                    return -1
                elif x1.start > x2.start:
                    return 1
                return 0

        sint = sorted(intervals)

        e = -0xFFFFFFF0
        x = 0
        for xi in sint:
            if e <= xi.start:
                x = x + 1
            e= xi.end

        return len(intervals) - x

if __name__ == '__main__':
    s = Solution()
    invs = [Interval(1, 2), Interval(2,3)]
    print s.eraseOverlapIntervals(invs)
