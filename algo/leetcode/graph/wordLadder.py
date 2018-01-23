class GraphNode(object):
    def __init__(self, w):
        self.label = w
        self.neighbors = []

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """

        def isDiff1(w1, w2):
            if len(w1) != len(w2):
                return False

            numDiff = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    if numDiff == 1:
                        return False
                    numDiff = numDiff + 1
            if numDiff != 1:
                return False
            return True

        def buildGraph(w, l, d):
            if w not in d:
                gn = GraphNode(w)

                for wx in l:
                    if isDiff1(w, wx):
                        gn.neighbors.append(buildGraph(wx, l, d))

                d[w] = gn

            return d[w]

        d = []
        l = [beginWord, endWord] + wordList

        for w in l:
            buildGraph(w, l, d)

        # we need to use shortest graph algo to solve this
