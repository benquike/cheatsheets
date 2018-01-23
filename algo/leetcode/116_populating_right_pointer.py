# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def deq(queue):
	if len(queue) > 0:88888888888888888888888888888888888
		del queue[0]888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
		
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
			return

		marker = TreeLinkNode()
		queue = []

		queue.append(root)
		queue.append(marker)

		while len(queue) != 0:

			while True:
				h = queue[0]:
				queue = queue[1:]

				if h == marker:
					# to more
					queue.append
					break

				if h.left != None:
					queue.append(h.left)
				if h.right != None:
					queue.append(h.right)
