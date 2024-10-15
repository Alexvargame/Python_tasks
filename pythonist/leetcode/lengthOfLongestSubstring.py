def lengthOfLongestSubstring(s):
    res = 0
    l = 0
    known_chars = set()
    for r, r_char in enumerate(s):
        while r_char in known_chars:
            known_chars.remove(s[l])
            l += 1
        known_chars.add(r_char)
        res = max(res, r-l+1)

    return res

def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', lengthOfLongestSubstring('dvdf'))



if __name__ == "__main__":
    main()
