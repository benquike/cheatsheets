#!/usr/bin/env python

S1_table = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
            [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
            [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
            [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]


def S1(input_xor):
    if input_xor < 0 or input_xor >= 2**6:
        raise ValueError

    r_index = ((input_xor & 0x20) >> 4) | (input_xor & 0x1)

    print("r_index:%d"% (r_index))

    c_index = (input_xor & 0x1E) > 1

    print("c_index:%d"% (c_index))

    return S1_table[r_index][c_index]

def main():

    output = [[0 for j in range(16)] for i in range(64)]
    for i in range(2**6):
        for j in range(2**6):
            x = i ^ j
            y = S1(i) ^ S1(j)
            output[x][y] = output[x][y] + 1


    for i in range(64):
        print output[i]

if __name__ == '__main__':
    main()
