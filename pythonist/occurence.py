



def occurence(astr):

   #[[astr[i-1]:j] for i in range(1,len(astr)) if len(astr[i-1:j]!=astr[i]]
   al=[astr[i-1] for i in range(1,len(astr)) if astr[i-1]!=astr[i]]
   
   bl=[i for i in range(1,len(astr)) if astr[i-1]!=astr[i]]
   bl.insert(0,0)
   bl.append(len(astr))
   print(al)
   if len(al)!=len([bl[i]-bl[i-1] for i in range(1,len(bl))]):
      al.append(astr[-1])
   return ' '.join(list(map(lambda x,y:str((int(x),int(y))),[bl[i]-bl[i-1] for i in range(1,len(bl))],al)))



def main():

   print(occurence('1222311'))
   print(occurence('1222333'))
    

if __name__ == "__main__":
    main()


