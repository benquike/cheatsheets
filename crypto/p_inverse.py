p_tbl = [16, 7, 20, 21, 29, 12, 28, 17,
 1, 15, 23, 26, 5, 18, 31, 10,
 2,8,24,4,32,27,3,9,
 19,13,30,6,22,11,4,25]


x = 0x00000202

b = bin(x)[2:]

b1 = '0' * (32 - len(b)) + b


output = ['0' for i in range(32)]

for i in range(32):
    output[i] =  b1[p_tbl[i] - 1]

print ''.join(output)
