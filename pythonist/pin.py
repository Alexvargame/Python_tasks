from collections import Counter
   
def pin(astr):
        if astr.isdigit() and (len(astr)==4 or len(astr)==6):
                return True
        return False
   
def main():
 
    print(pin('1233'))
    print(pin('1233'))
    print(pin('12e3'))
    print(pin('12434'))
    print(pin('123455'))


      
if __name__ == "__main__":
    main()


