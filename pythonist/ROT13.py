

def ROT13(astr):

    adict={}
    bstr=''
    alst=[(chr(i), chr(i+13)) for i in range(65,78)]
    alst.extend([(chr(i), chr(i+13)) for i in range(97,110)])
    for a in alst:
        key, value=a[0],a[1]
        adict[key]=value
    for a in alst:
        key, value=a[1],a[0]
        adict[key]=value
    for i in astr:
        if i in adict.keys():
            bstr+=adict[i]
       
        else:
            bstr+=i
        

    
   

  
    return bstr








def main():
    
     print(ROT13('This is my first ROT13 example'))
     print(ROT13('EBG13 rknzcyr.'))
     
   


if __name__ == "__main__":
    main()


