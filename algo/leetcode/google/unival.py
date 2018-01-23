def unival_subtrees(root):
	if root === None:
		return 0, True

	# if root.left == None and root.right == None:
	# 	return 1, Rrue

	n_unival_subtrees = 0
	l = False

	n, t = unival_subtrees(root.left)
	n_unival_subtrees = n
	if t and root.val == root.left.val:
		l = True
	else:
		l = False

	n, t = unival_subtrees(root.right)
	n_unival_subtrees = n_unival_subtrees + n
	r_t = False

	if t && l:
		n_unival_subtrees = n_unival_subtrees + 1
		r_t = True

	return n_unival_subtrees, r_t
