def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    minstr = sorted(strs, key=len)[0]
    lenstr = len(minstr)
    for i in range(lenstr):
        count = 0
        print(lenstr, i, minstr[:lenstr - i])
        for st in strs:
            if st.startswith(minstr[:lenstr - i]):
                count += 1
            else:
                break
        if count == len(strs):
            return minstr[:lenstr - i]
    return ''


def main():
    print('res', longestCommonPrefix(["flower","flow","flight"]))



if __name__ == "__main__":
    main()
