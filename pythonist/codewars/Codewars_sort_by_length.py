def spin_words(sentence):

    return ' '.join([s if len(s)<5 else s[::-1] for s in sentence.split() ])
    

def main():

    print(spin_words("Hey fellow warriors"))




if __name__ == "__main__":
    main()




#
