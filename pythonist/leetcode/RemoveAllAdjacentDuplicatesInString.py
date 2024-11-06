def removeDuplicates(s):
    i = 0
    lst = list(s)
    # print(lst)
    if len(set(s)) == 1:
        return s[0] if len(s) % 2 != 0 else ''
    while i < len(lst) - 1:
        # print(lst[i], lst[i + 1], i)
        if lst[i] == lst[i + 1]:
            lst.pop(i)
            lst.pop(i)
            if i != 0:
                i -= 1
            # print('del',lst, i)
        else:
            i += 1
    return ''.join(lst)


def main():
    #print('res', maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print('res', removeDuplicates("abbaca"))


if __name__ == "__main__":
    main()
