

def CountDuplicate(astr):

  
   return len(set([s for s in astr.lower() if astr.lower().count(s)>1]))







def main():
    
     print(CountDuplicate('aabbcde'))
     print(CountDuplicate('indivisibility'))
     print(CountDuplicate('indivisibilities'))
     print(CountDuplicate('aA11'))
     print(CountDuplicate('AABB'))
    
   


if __name__ == "__main__":
    main()


