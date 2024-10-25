import collections
import string
def ladderLength(beginWord, endWord, wordList):

    word_set = set(wordList)
    if endWord not in word_set:
        return 0
    transformations = collections.deque()
    transformations.append(beginWord)
    result = 0
    while transformations:
        result += 1
        for _ in range(len(transformations)):
            word_chars = list(transformations.popleft())
            for idx, orig_char in enumerate(word_chars):
                for new_char in string.ascii_lowercase:
                    word_chars[idx] = new_char
                    word = "".join(word_chars)
                    if word == endWord:
                        return result + 1
                    if word in word_set:
                        transformations.append(word)
                        word_set.remove(word)
                word_chars[idx] = orig_char

    return 0


def main():

    print('res', ladderLength(beginWord="hit", endWord="cog", wordList=["hot","dot","dog","lot","log","cog"]))



if __name__ == "__main__":
    main()
