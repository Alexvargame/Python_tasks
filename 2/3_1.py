str_="Сидел барсук в своей норе и ел картошечку пюре"
print(str_)
print(len(str_))
print(str_ +".")
print(str_.find('ре'))
count=0
i=0
while i in range(len(str_)):
            if str_.find("ре",i)==-1:
                    break
            else:
                    count+=1
                    i=str_.find("ре",i)+len("ре")
                    print( count, str_.find("ре", i), i)
                    
print(count)                
print(str_[-2:-1])
for i in range(1, len(str_),2):
    print(str_[i])
lst=str_.split(' ')
print(len(lst))
