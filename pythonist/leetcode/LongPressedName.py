def isLongPressedName(name, typed):
    print(name, typed)
    idx_1 = 0
    if name[-1] != typed[-1]:
        return False
    for idx, l in enumerate(name):
        if l == typed[idx_1]:
            if idx_1 == len(typed) - 1:
                if idx == len(name) - 1:
                    return True
                else:
                    return False
            if idx + 1 < len(name) - 1 and l == name[idx + 1]:
                idx_1 += 1
                continue
            while typed[idx_1] == l:
                if idx_1 < len(typed) - 1:
                    idx_1 += 1
                else:
                    break
        else:
            return False
    return True if idx_1 == len(typed) - 1 else False



def main():
    #print('res', maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print('res', isLongPressedName( name="saeed", typed="ssaaedd"))


if __name__ == "__main__":
    main()
