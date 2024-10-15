from string import ascii_lowercase,ascii_uppercase

def rot13(message):
    ldict=dict(zip(ascii_lowercase+ascii_uppercase,ascii_lowercase[13:]+ascii_lowercase[:13]+ascii_uppercase[13:]+ascii_uppercase[:13]))
    print(ldict)
    print(' '.join([''.join([ldict[l] if l.isalpha() else l for l in word ]) for word in message.split()]))
        

def main():
    print(rot13("This is my first ROT13 excercise!"))



if __name__ == "__main__":
    main()




#
