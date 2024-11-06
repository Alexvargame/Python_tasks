def numberOfLines(widths, s):
    dlist = {}
    for idx, l in enumerate("abcdefghijklmnopqrstuvwxyz"):
        dlist[l] = widths[idx]
    num = 0
    len_str = 0
    min_len = 100
    for idx, l in enumerate(s):
        print(l, dlist[l])
        if len_str +dlist[l] <= 100:
            len_str += dlist[l]
            print(len_str)
        else:
            num += 1
            min_len = min(min_len, len_str)
            len_str = dlist[l]

    min_len = min(min_len, len_str)
    return num + 1, min_len




def main():

    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', numberOfLines(widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                               s = "bbbcccdddaaa"))



if __name__ == "__main__":
    main()
