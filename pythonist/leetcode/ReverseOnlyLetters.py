def reverseOnlyLetters(s):
    print('S', s)
    res = ''
    lstr = len(s)
    tmp = list([l for l in s if l.isalpha()])
    tmp.reverse()
    print(tmp)
    idx_tmp = 0
    for idx, l in enumerate(s):
        if l.isalpha():
            res += tmp[idx_tmp]
            idx_tmp += 1
        else:
            res += l
    print(res)

    # l = 0
    # r = len(s) - 1
    # rlst = []
    # while l < r:
    #     if s[l].isalpha():
    #         if s[r].isalpha():
    #             res += s[r]
    #             r -= 1
    #         else:
    #             while not s[r].isalpha():
    #                 rlst.append(r)
    #                 r -= 1
    #             res += s[r]
    #     else:
    #         res += s[l]
    #     l += 1
    # print(l, r, s[r])
    #
    # while r > 0:
    #     if s[r].isalpha():
    #         if s[l-1].isalpha():
    #             res += s[l-1]
    #         else:
    #             while not s[r].isalpha():
    #                 rlst.append(r)
    #                 l -= 1
    #             res += s[l]
    #     else:
    #         res += s[r]
    #     r += 1

    return res



def main():
    #print('res', maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print('res', reverseOnlyLetters(s="a-bC-dEf-ghIj"))


if __name__ == "__main__":
    main()
