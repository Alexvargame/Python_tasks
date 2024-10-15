
from string import ascii_lowercase

def alphabet_position(text):
    return ' '.join([str(ascii_lowercase.index(l)+1) for l in text.lower() if l.isalpha()])



def main():

    print(alphabet_position("The sunset sets at twelve o' clock."))

if __name__ == "__main__":
    main()

#
