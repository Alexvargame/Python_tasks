

def decipherThis(astr):

    alst=astr.split()
   
    
  
    return ' '.join([''.join([chr(int(''.join([b for b in bstr if b.isdigit()])))]+[''.join([b for b in bstr if not b.isdigit()][::-1])]) for bstr in astr.split()])





def diph(bstr):

    char(int(''.join([b for b in bstr if b.isdigit()])))
    





def main():
    
     print(decipherThis('72olle 103doo 100ya'))
     print(decipherThis('82ydae 115te 103o'))


if __name__ == "__main__":
    main()


