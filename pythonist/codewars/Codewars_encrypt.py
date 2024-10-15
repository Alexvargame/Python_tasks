from string import ascii_lowercase

def encrypt(text, n):
    for i in range(n):           
        text=''.join([text[i] for i in range(1,len(text),2)])+''.join([text[i] for i in range(0,len(text),2)])
     
    return text

def decrypt(encrypt_text,n):
    if encrypt_text is None:
        return None
    print(encrypt_text)
    text=''
    text1=encrypt_text[:len(encrypt_text)//2]
    text2=encrypt_text[len(encrypt_text)//2:]
    print('T',text1,len(text1),'T1',text2,len(text2))
    for i in range(n):
        for j in range(len(encrypt_text)//2):
            text+=text2[j]+text1[j]
        if len(text1)!=len(text2):
            text+=text2[-1]
        text1=text[:len(encrypt_text)//2]
        text2=text[len(encrypt_text)//2:]
        print('T',text1,len(text1),'T1',text2,len(text2))
        encrypt_text=text
        text=''
    return encrypt_text

def main():
    #print(encrypt("This is a test!", 1 ))
    print(decrypt(encrypt("This is a test!", 1),1))
  
##    print(encrypt("0RMIM$h?qeLyW\f:Y%S", 350 ))
##    print(decrypt(encrypt("0RMIM$h?qeLyW\f:Y%S", 350 ),350))
  

if __name__ == "__main__":
    main()

#
