

def spinWords(astr):

    
   
    
  
    return ' '.join([''.join(reversed(a)) if len(a)>5 else a for a in astr.split()])








def main():
    
     print(spinWords('Hey fellow warriors'))
     print(spinWords('This is the test'))
     print(spinWords('This is another test'))
   


if __name__ == "__main__":
    main()


