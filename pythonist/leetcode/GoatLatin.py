def toGoatlatin(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res_str = ''
    suffiks = 'ma'
    for idx, word in enumerate(sentence.split()):
        print(idx, word)
        if word[0].lower() in vowels:
            res_str += word + suffiks + 'a' * (idx + 1) + ' '
        else:
            res_str += word[1:] + word[0] + suffiks + 'a' * (idx + 1) + ' '
    return res_str





def main():

    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', toGoatlatin("I speak Goat Latin"))



if __name__ == "__main__":
    main()
