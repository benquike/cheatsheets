#!/usr/bin/env python

def possible_next_states(s):
    ret = []
    for i in range(len(s) - 1):
        if s[i] == '+' and s[i+1] == '+':
            ret.append(s[:i] + '--' + s[i+2:])

    return ret

def first_player_winnable(s):
    pstate = possible_next_states(s)
    if len(pstate) == 0:
        return False

    for o in possible_next_states(s):
        if len(possible_next_states(o)) == 0:
            return True

    return False

def main():
    testcase = "++++"

    for o in possible_next_states(testcase):
        print o

    if (first_player_winnable(testcase)):
        print 'YES'
    else:
        print 'NO'

if __name__ == '__main__':
    main()
