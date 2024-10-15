def isLongPressedName(name, typed):
    """
    :type name: str
    :type typed: str
    :rtype: bool
    """
    j = 0
    for i in range(len(name)):
        count = 0
        if name[i] == typed[j]:
            print('IIII', i, 'JJJ', j)
            while name[i] == typed[j]:
                print(i, name[i], j, typed[j])
                if name[i] == typed[j]:
                    j += 1
                    print('J@@@@', j)
                    if j >= len(typed) - 1:
                        break
        elif name[i] == name[i - 1] and i<j:
            continue
        else:
            print('False', i, j)
            return False
    return True


def main():
    print('res', isLongPressedName("leelee","lleeelee"))



if __name__ == "__main__":
    main()
