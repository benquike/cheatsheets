# class TrieNode(object):
# 	def __init__(self):

# 		# assume all characters are 'a' - 'z'
# 		self._sub_trees = [None for i in range(26)]
# 		self._final = False

# 	def insert(self, _str):
# 		if len(_str) == 0:
# 			self._final = True
# 			return

# 		i = ord(_str[0]) - ord('a')

# 		if self._sub_trees[i] == None:
# 			self._sub_trees[i] = TrieNode()

# 		c_node = self._sub_trees[i]
# 		c_node.insert(_str[1:])


# 	def find(self, _str):
# 		if len(_str) == 0:
# 			return True, self._final

# 		i = ord(_str[0]) - ord('a')

# 		if self._sub_trees[i] == None:
# 			return False, False

# 		return self._sub_trees[i].find(_str[1:])

class Trie(object):
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
        self._subtrees = [None for i in range(26)]
        self._final = False


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """

        if len(word) == 0:
            self._final = True
            return

        i = ord(word[0]) - ord('a')

        if self._subtrees[i] == None:
            self._subtrees[i] = Trie()

        c_node = self._subtrees[i]
        c_node.insert(word[1:])

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        if len(word) == 0:
            return self._final

        i = ord(word[0]) - ord('a')

        c_node = self._subtrees[i]

        if c_node == None:
            return False

        return c_node.search(word[1:])


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
		:type prefix: str
        :rtype: bool
        """

		print(prefix)

		if len(prefix) == 0:
            return True

        i = ord(prefix[0]) - ord('a')
        c_node = self._subtrees[i]

        if c_node == None:
            return False

        return c_node.startsWith(prefix[1:])

def main():
	trie = Trie()

	# trie.insert('a')
	# trie.insert('ab')
	# trie.insert('aba')
	# trie.insert('abac')
	# trie.insert('abaca')
	# trie.insert('abacab')

	# print(trie.startsWith(''))
	# print(trie.search(''))
	# print(trie.search('ab'))

	# print(trie.search('b'))
	# print(trie.search('ba'))

	trie.insert('ab')
	# print(trie.search('a'))
	# print(trie.search('ab'))
	# print(trie.startsWith('a'))
	print(trie.startsWith('ab'))

if __name__ == '__main__':
	main()
