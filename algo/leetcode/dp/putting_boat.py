
def put_boat(l1, l2, cars, _from, notebook):

    k = (l1, l2, _from)
    if k in notebook:
        return notebook[k]

    res = None
    if l1 < cars[_from] and l2 < cars[_from]:
        notebook[k] = 0
        return 0

    if l1 < cars[_from] and l2 >= cars[_from]:
        res =  1 + put_boat(l1, l2 - cars[_from], cars, _from + 1, notebook)
        notebook[k] = res
        return res

    if l1 >= cars[_from] and l2 < cars[_from]:
        res =  1 + put_boat(l1 - cars[_from], l2 , cars, _from + 1, notebook)
        notebook[k] = res
        return res

    res = 1 + max([put_boat(l1 - cars[_from], l2 , cars, _from + 1, notebook),
                   put_boat(l1, l2 - cars[_from], cars, _from + 1, notebook)])
    notebook[k] = res

    return res


import time
# def put_boat(l1, l2, cars, _from):

#     if l1 < cars[_from] and l2 < cars[_from]:
#         return 0

#     if l1 < cars[_from] and l2 >= cars[_from]:
#         return 1 + put_boat(l1, l2 - cars[_from], cars, _from + 1)

#     if l1 >= cars[_from] and l2 < cars[_from]:
#         return 1 + put_boat(l1 - cars[_from], l2 , cars, _from + 1)

#     return  1 + max([put_boat(l1 - cars[_from], l2 , cars, _from + 1),
#                    put_boat(l1, l2 - cars[_from], cars, _from + 1)])


def read_cars():
    ret = []
    with open('cars5000.txt', 'r') as f:
        for l in f.readlines():
            l = l.strip()
            if l == "":
                continue

            ret.append(int(l))

    return ret

cars = read_cars()

def test(l, expected):

    print("l == %d" % (l))
    notebook = {}

    start = time.time()
    res = put_boat(l, l, cars, 0, notebook)
    end = time.time()

    # res = put_boat(l, l, cars, 0)
    
    print("result = %d" % (res))
    print("expected = %d" % (expected))
    print("time = " + str(end - start))
    print "=================================="


def main():
    # cars = [19, 40, 49, 37, 37, 37, 30, 45]

    tests = [(100, 5), (200, 11), (500, 34), (1000, 71),
             (2000, 145),
             (5000, 353),
             (10000,713),
             (20000, 1381),
             (50000, 3474)
    ]


    for l, exp in tests:
        test(l, exp)

    # print "l == 100"
    # l = 100
    # print put_boat(l, l, cars, 0)
    # print "=================================="

    # print "l == 200"
    # l = 200
    # print put_boat(l, l, cars, 0)
    # print "=================================="


    # print "l == 500"
    # l = 500
    # print put_boat(l, l, cars, 0)
    # print "=================================="

if __name__ == "__main__":
    main()
