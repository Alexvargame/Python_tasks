from functools import reduce
def numEquivDominoPairs(dominoes):
    dct = {}
    for i in range(len(dominoes)):
        print(dominoes[i], dominoes[i][::-1])
        # print(tuple(dominoes[i]) not in dct.keys(), tuple(dominoes[i][::-1]) not in dct.keys())
        # print(tuple(dominoes[i]) not in dct.keys() and tuple(dominoes[i][::-1]) not in dct.keys())
        if tuple(dominoes[i]) not in dct.keys() and tuple(dominoes[i][::-1]) not in dct.keys():
            print('NEW')
            dct[tuple(dominoes[i])] = []
        else:
            print("Add")
            if tuple(dominoes[i]) in dct.keys():
                print('1111')
                dct[tuple(dominoes[i])].append(dominoes[i])
            elif tuple(dominoes[i][::-1]) in dct.keys():
                print('2222')
                dct[tuple(dominoes[i][::-1])].append(dominoes[i])

        print('DICFT',dct)
    sum = 0
    for key, value in dct.items():
        if value != []:
            sum += reduce(lambda x, y: x+y, range(1, len(value) + 1))
    print(sum)

def main():
    #print('res', maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print('res', numEquivDominoPairs(dominoes= [[1,2],[1,2],[1,1],[1,2],[2,1], [2,2]]))


if __name__ == "__main__":
    main()
