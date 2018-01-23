
def bs0(l):
    '''
    list l: zero or some number of trues followed by
    zero or some number of falses

    find the first index i where l[i] == true and l[i+1] = false
    if all trues, then i = len(l) - 1
    if all falses then i = 0
    
    >>> l = [True]
    >>> bs0(l)
    0
    >>> l = [True, True]
    >>> bs0(l)
    1
    >>> l = [True, True, True]
    >>> bs0(l)
    2

    >>> l = [False]
    >>> bs0(l)
    0
    >>> l = [False, False]
    >>> bs0(l)
    0
    >>> l = [False, False, False]
    >>> bs0(l)
    0

    >>> l = [True, False]
    >>> bs0(l)
    0
    '''

    start = 0
    end = len(l) - 1
    mid = (start + end)/2

    while start < end:
        if l[mid] == False:
            end = mid - 1
        else:
            start = mid
        mid = (start + end)/2
        if start == mid:
            if l[end]:
                return end
            return start

    return start

def bs1(l, x):
    '''
    This version returns the lower bound
    Meaning that:
    - if there are multiple elements equal
       to x, return the index of the first one;
    - if there is no element equal to x, return
      the index of the biggest number less than x
    
    >>> l = [1, 1, 2, 2, 3, 3, 4, 4]
    >>> bs1(l, 1)
    0
    >>> bs1(l, 4)
    6

    >>> l = [1, 2, 3, 5,8]
    >>> bs1(l, 4)
    3

    >>> l = [1,1,1,1,1,1,1,1]
    >>> bs1(l, 1)
    0

    >>> bs1(l, 2)
    7
    '''
    
    start = 0
    end = len(l) - 1
    mid = (start + end)/2

    while start < end:
        if l[mid] < x:
            start = mid + 1
        else:
            end = mid

        mid = (start + end)/2

    return start
        
def bs2(l, x):
    '''
    This version returns the upper bound
    Meaning that:
    - if there are multiple elements equal
       to x, return the index of the first one;
    - if there is no element equal to x, return
      the index of the biggest number less than x
    
    >>> l = [1, 1, 2, 2, 3, 3, 4, 4]
    >>> bs2(l, 1)
    1

    >>> bs2(l, 4)
    7
    '''

    start = 0
    end = len(l) - 1
    mid = (start + end)/2

    while start < end:
        if l[mid] > x:
            end = mid - 1
        else:
            start = mid

        mid = (start + end)/2

        if mid == start:
            if l[end] == x or l[start] != x:
                return end
            return start

    return start

if __name__ == "__main__":
    import doctest
    doctest.testmod()
