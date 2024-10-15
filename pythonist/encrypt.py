
def encrypt(astr,n):
    while n>0:
        astr=''.join([astr[1::2]+astr[::2]])
        n=n-1
    return astr

def main():
  
     print(encrypt('012345',1))
     print(encrypt('012345',2))
     print(encrypt('012345',3))
     print(encrypt('01234',1))
     print(encrypt('01234',2))
     print(encrypt('01234',3))
     

if __name__ == "__main__":
    main()


