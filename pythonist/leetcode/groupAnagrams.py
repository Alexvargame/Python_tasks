def groupAnagrams(strs):
    result = {}

    for word in strs:
        counts = [0]*26
        for char in word:
            counts[ord(char)-ord('a')] += 1
        key = tuple(counts)
        if key not in result:
            result[key] = []
        result[key].append(word)

    return result.values()













def main():
    print('res', groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))



if __name__ == "__main__":
    main()
