import string
from collections import Counter
##>>> string.ascii_uppercase
##'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
##>>> string.ascii_lowercase
##'abcdefghijklmnopqrstuvwxyz'
##>>> string.ascii_letters
##'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def is_pangram(s):
    d=dict(Counter(s.lower()))
    dd={}
    print(d)
    print(list(d.keys()))
    print(Counter(s.lower().replace(' ','')))
    print(string.ascii_lowercase)
    for key,value in d.items():
        if key.isalpha():
            dd[key]=value
    if len(list(dd.keys()))==len(string.ascii_lowercase):
        return True
    return False

def main():
    print(is_pangram("The quick brown fox jumps over the lazy dog."))




if __name__ == "__main__":
    main()




#
