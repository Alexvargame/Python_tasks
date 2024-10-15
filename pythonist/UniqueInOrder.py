

def UniqueInOrder(astr):

   res=[]
   res.append(astr[0])
   return [ astr[i] for i in range(len(astr)) if astr[i]!=astr[i-1] or i==0]







def main():
    
     print(UniqueInOrder('AAAABBBCCDAABBB'))
     print(UniqueInOrder('ABBCcAD'))
     print(UniqueInOrder([1,2,2,3,3]))
     print(UniqueInOrder((1,2,2,3,3)))
     print(UniqueInOrder('ABAABBBCCDAABBBA'))
   


if __name__ == "__main__":
    main()


