class GraphNode(object):
    def __init__(self, s):
        self.label = s
        self.neighbors = []

    def __str__(self):
        ret = self.label + '['
        for n in self.neighbors:
            ret = ret + n.label + ','
        ret = ret + ']'
        return ret

    def __repr__(self):
        return self.__str__()

class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """

        def isDiff1(w1, w2):
            if len(w1) != len(w2):
                return False

            if w1 == '' and w2 == '':
                return False

            diff = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff = diff + 1
                    if diff > 1:
                        return False
            if diff != 1:
                return False
            return True

        def createGraph(w, d, wl):
            if w in d:
                return d[w]
            n = GraphNode(w)
            d[w] = n
            for w1 in wl:
                if w == w1:
                    continue
                if isDiff1(w, w1):
                    n.neighbors.append(createGraph(w1, d, wl))

            return d[w]

        l = wordlist + [beginWord, endWord]
        d = {}

        for w in l:
            createGraph(w, d, l)


        print d
        

if __name__ == '__main__':
    s = Solution()
    print s.findLadders("hit", "cog", ["hot","dot","dog","lot","log"])
