from time import time

def sum_pairs(ints, s):
    print(ints,s)
    if ints[0] + ints[1] == s:
        return [ints[0], ints[1]]
    tmp=[ints[0],ints[1]]
    tmp1=[ints[0],ints[1]]
    t1 = time()

    for i in range(2,len(ints)):


        if ints[i] in tmp:
            if 2 * ints[i] == s:
                t2 = time()
                print('T2', t2 - t1)
                return [ints[i], ints[i]]

        else:
            for j in range(len(tmp) - 1, -1, -1):
                if ints[i] + tmp[j] == s:
                    t2 = time()
                    print('T2', t2 - t1)
                    return [tmp[j], ints[i]]
            if ints[i] not in tmp:
                tmp.append(ints[i])
            #tmp.append(ints[i])
    t2=time()
    print('T2', t2 - t1)
    return None

        


def main():
    # l9 = [1] * 100000000
    # l9[len(l9) // 2 - 1] = 6
    # l9[len(l9) // 2] = 7
    # l9[len(l9) - 2] = 8
    # l9[len(l9) - 1] = -3
    l9=[12, 18, 2, -6, -9, 4, 8, 7, 0, -4, 18, 7, -4, 12, 9, 19, -18, 4, 7, 10, -14, 17, 19, 0, 3, -9, -14, 11, -9, 10, 5, 3, 11, 16, -17, 15, -14, 9, -13, -14, 5, 10, -8, 18, 19, -17, 18, 20, -8, -2, 1, 5, -2, -3, 20, 5, 18, 20, 17, 18, -11, 8, 1, -6, 0, 12, 2, 6, -20, -3, 1, -6, 11, -16, -13, 17, -6, 13, -19, -1, 2, -17, 20, -2, -4, -1, 18, 7, -10, -14, 19, -12, -20, -4, 0, -6, 12, 2, -17, 12, -16, 1, 2, 18, -13, -7, -13, -15, -4, 3, -6, -12, 15, 12, 13, -18, 10, 19, -2, -10, 6, -12, 0, 14, -4, -1, -5, 13, 18, -19, 2, -11, 14, -19, -15, -19, -20, -10, -16, 1, -19, -6, -2, 17, -8, -7, 13, -10, 13, 16, 4, -10, -18, 7, 0, 19, -16, 2, -19, -2, -1, -5, 18, 7, -18, -15, -4, 20, 16, 18, -16, -15, -3, -4, -6, -2, 9, 15, 0, 17, -12, 7, 13, 7, 6, -6, 15, 11, 14, 12, 13, -4, -12, -4, 16, 11, -10, -18, 13, 4, 8, -8, -13, 20, 20, -16, 18, 4, -12, 11, -16, 2, 15, -10, 13, 16, 15, -9, -6, -5, 6, -10, 16, 12, -9, -20, 13, -4, -9, -18, 15, -1, -5, -8, 12, -8, -11, 16, 2, 19, -13]

    print(sum_pairs(l9[:30] , -8))
##    print(next_bigger(9))
##    print(next_bigger(111))
##    print(next_bigger(144))
##    print(next_bigger(414))
##    print(next_bigger(9091420762))
##    print(next_bigger(598848484))
    
   
    
if __name__ == "__main__":
    main()

from itertools import groupby


# def sum_pairs(ints, s):
#     res = []
#     res1 = []
#
#     def checksum(a, b):
#         # print(a,b)
#         # input()
#         if a + b == s:
#             return [a, b]
#
#     def sort(l):
#         return l[2]
#
#     for i in range(len(ints)):
#         # print(list(map(lambda x,y:checksum(x,y) ,ints,ints[i+1:])))
#         # print('rrr',list(checksum(x,y) for x,y in zip(ints,ints[i+1:]) if checksum(x,y) is not None))
#         # if list(map(lambda x,y:checksum(x,y) ,ints,ints[i+1:]))[0] is not None:
#         res.extend(list(checksum(x, y) for x, y in zip(ints, ints[i + 1:]) if checksum(x, y) is not None))
#         # res.extend(map(lambda x,y:checksum(x,y) ,ints,ints[i+1:]))
#         res = list(filter(None, res))
#         # print('l',list(res.extend(list(map(lambda x,y:checksum(x,y) ,ints,ints[i+1:]))) for i in range(len(ints))))
#     # print(res)
#     # input()
#
#     print('l', list(res1.extend(list(map(lambda x, y: checksum(x, y), ints, ints[i + 1:]))) for i in range(len(ints))))
#     print(res1)
#     res = list(filter(None, res))
#     print(res)
#     if res:
#         return res[0]
#         # return [el for el , _ in groupby(res)][0]
#     return None
#
