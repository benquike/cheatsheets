class Node:
    def __init__(self, name):
		self.name = name
		self.counter = -1
		self.visited = False
		self.succ = []

N = 7

def R_DFS_Search(node):
	node.visited = True

	global N
	for n in node.succ:
		if not n.visited:
			R_DFS_Search(n)

	node.counter = N
	N = N - 1

def main():
	b7 = Node('B7')
	b6 = Node('B6')
	b5 = Node('B5')
	b4 = Node('B4')
	b3 = Node('B3')
	b2 = Node('B2')
	b1 = Node('B1')
	b0 = Node('B0')

	b7.succ.append(b6)
	b6.succ.append(b5)
	b5.succ.append(b3)

	b3.succ.append(b4)
	b4.succ.append(b3)
	b3.succ.append(b2)
	b2.succ.append(b5)
	b2.succ.append(b1)
	b1.succ.append(b0)


	R_DFS_Search(b7)

	nodes = [b0, b1, b2, b3, b4, b5, b6, b7]

	for n in nodes:
		print("%s: %d" % (n.name, n.counter))

if __name__ == '__main__':
    main()
