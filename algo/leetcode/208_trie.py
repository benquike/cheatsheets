class TrieNode(object):
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isWord = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.root = TrieNode()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        n = self.root
        for c in word:
            x = ord(c) - ord('a')
            if n.children[x] == None:
                n.children[x] = TrieNode()
            n = n.children[x]
        n.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        n = self.root
        for c in word:
            x = ord(c) - ord('a')
            if n.children[x] == None:
                return False
            n = n.children[x]

        return n.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        n = self.root

        for c in prefix:
            x = ord(c) - ord('a')
            if n.children[x] == None:
                return False
            n = n.children[x]

        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
