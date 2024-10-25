from datetime import *
import random
"""
txt=input()
str1=''
for i in range(0,len(txt)//2*2,2):
    #txt[i], txt[i+1] =txt[i+1], txt[i]
    str1=str1+txt[i+1]+txt[i]
    print(ord(txt[i]))
print(str1)
"""
gl=['a','e','i','o','u','y']
txt='aseidoyz'
print(txt)
def shifr(txt):
    txtsh=''
    for i in range(len(txt)):
        if txt[i] in gl:
            if txt[i]=='y':
                txtsh=txtsh + 'a'
            else:
                txtsh=txtsh + gl[gl.index(txt[i])+1]
        else:
            if txt[i]=='z':
                txtsh=txtsh + 'b'
            else:
                
                for j in range(1,25):
                    if chr(ord(txt[i])+j) in gl:
                        pass
                    else:
                        txtsh=txtsh + chr(ord(txt[i])+j)
                        break
    return(txtsh)
def deshifr(txt):
    txtsh=''
    for i in range(len(txt)):
        if txt[i] in gl:
            if txt[i]=='a':
                txtsh=txtsh + 'y'
            else:
                txtsh=txtsh + gl[gl.index(txt[i])-1]
        else:
            if txt[i]=='b':
                txtsh=txtsh + 'z'
            else:
                
                for j in range(1,25):
                    if chr(ord(txt[i])-j) in gl:
                        pass
                    else:
                        txtsh=txtsh + chr(ord(txt[i])-j)
                        break
    return(txtsh)
print(shifr(txt))
print(deshifr(shifr(txt)))

txt="fk dfw 24124 asdvs"

l=txt.split(" ")
print((" ").join(l[::-1]))
 
