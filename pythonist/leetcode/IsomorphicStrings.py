
def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    d =dict.fromkeys(list(s), None)
    d1 = dict.fromkeys(list(t), None)
    for i in range(len(s)):
        if d[s[i]]:
            if d[s[i]] != t[i]:
                return False
        else:
            d[s[i]] = t[i]
        if d1[t[i]]:
            if d1[t[i]] != s[i]:
                return False
        else:
            d1[t[i]] = s[i]
        print(d)
    return True


def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', isIsomorphic(s="bads", t="baba"))



if __name__ == "__main__":
    main()
