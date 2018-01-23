def _eval(tokens):

	print tokens
	if tokens == None or len(tokens) == 0:
		return None

	if len(tokens) == 1:
			return int(tokens[0])

	val_stk = []
	op_stk = []

	assert tokens[0] == '('

	# op_stk.append(tokens[1])

	# if tokens[1] == '*':
	# 	val_stk.append(1)
	# elif token[1] == '+':
	# 	val_stk.append(0)

	i = 0
	while i < len(tokens):

		print i
		print op_stk
		print val_stk
		if tokens[i] == '(':

			if i + 1 >= len(tokens):
				raise Exception

			op_stk.append(tokens[i + 1])

			if tokens[i + 1] == '*':
				val_stk.append(1)
			elif tokens[i + 1] == '+':
				val_stk.append(0)

			i = i + 2
			continue

		elif tokens[i] == ')':
			op_stk.pop()
			v = val_stk.pop()

			if len(op_stk) > 0:
				v1 = val_stk.pop()
				op = op_stk[len(op_stk) - 1]

				if op == '*':
					v = v1 * v
				else: # '+'
					v = v1 + v

			val_stk.append(v)

		else:
			# numbers
			v = val_stk.pop()

			op = op_stk[len(op_stk) - 1]

			if op == '*':
				v = v * int(tokens[i])
			else: # '+'
				v = v + int(tokens[i])

			val_stk.append(v)

		# if tokens[i] == '*' || tokens[i] == '+':
		# 	pass

		i= i + 1


	return val_stk[0]

def eval(_str):
	tokens = _str.split(' ')
	return _eval(tokens)

if __name__ == '__main__':
	test1 = "123"
	print(eval(test1))

	test2 = "( + 1 2 )"
	print(eval(test2))

	test3 = "( + 1 2 4 )"
	print(eval(test3))
