__expansion_table = [
		31,  0,  1,  2,  3,  4,
		 3,  4,  5,  6,  7,  8,
		 7,  8,  9, 10, 11, 12,
		11, 12, 13, 14, 15, 16,
		15, 16, 17, 18, 19, 20,
		19, 20, 21, 22, 23, 24,
		23, 24, 25, 26, 27, 28,
		27, 28, 29, 30, 31,  0
	]

num = 0x40000000
b = bin(num)[2:]

b = '0' + b

e = ['0' for i in range(48)]

for i in range(48):
    e[i] = b[__expansion_table[i]]


print hex(int('0b' + ''.join(e), base=2))
