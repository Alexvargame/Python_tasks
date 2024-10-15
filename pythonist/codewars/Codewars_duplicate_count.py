from string import ascii_lowercase

def duplicate_count(text):
    res=[]
    res1=[]
    text=text.lower()
    base_lst=[l for l in (ascii_lowercase+'0123456789')]
    print(base_lst)
    i=0
    for i in range(len(text)):
        print(text[i])
        if not text[i] in res:
            res.append(text[i])
        elif not text[i] in res1:
            res1.append(text[i])
            base_lst.remove(text[i])
        else:
            continue
        print(res,res1)
        print(base_lst,len(base_lst))
        input()
        if len(base_lst)==0:
            break
    return len(res1)
                
                
        


def main():
    print(duplicate_count("aA11"))
  

if __name__ == "__main__":
    main()

#
