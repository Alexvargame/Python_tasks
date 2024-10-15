from itertools import combinations
from math import sqrt

def two(number,awesome_phrases):
     print('TWO',number+1,number+2)
     for num in [number+1,number+2]:
        astr=str(num)[::-1]
        if num in awesome_phrases or len(set(list(str(num))))==1:
            print('11',set(str(num).split()))
            return 1
        if set(list(str(num))[1:])=={'0'}:
            print('21',set(list(str(num))[1:]))
            return 1
        if str(num)==astr:
            print('51')
            return 1
        if '0' not in str(num):
            if ''.join(sorted(list(set(str(num)))))==str(num) and (abs(int(str(num)[0])-int(str(num)[-1]))==len(str(num))-1):
                print(int(str(num)[0])-int(str(num)[-1]),(abs(int(str(num)[0])-int(str(num)[-1]))==len(str(num))-1))
                print('31',sorted(list(str(num))))
                return 1
            if ''.join(reversed(sorted(list(set(str(num))))))==str(num) and (abs(int(str(num)[0])-int(str(num)[-1]))==len(str(num))-1):
                print('41',reversed(sorted(list(str(num)))))
                return 1
        else:
            if not (str(num)[-1]=='0' and str(num)[-2:] not in ['90','10']) and not (str(num)[1]=='0' and str(num)[:2]!='90'):
                print(str(num)[-1],str(num)[-2:],str(num)[:2])
                print('else111',num)
                mm=[m for m in str(num).split('0') if m]
                m1=[1 for m in mm if ''.join(sorted(list(m)))==str(m) and (abs(int(str(m)[0])-int(str(m)[-1]))==len(str(m))-1)]
                m2=[1 for m in mm if ''.join(reversed(sorted(list(m))))==str(m) and (abs(int(str(m)[0])-int(str(m)[-1]))==len(str(m))-1)]
                print(mm,m1,m2)
                if len(m1)==len(mm):
                    print('els1111')
                    for i in range(0,len(mm)):              
                        if mm[i][-1]!='9':
                            break
                    for i in range(1,len(mm)):
                        if mm[i][0]!='1':
                            break
                    return 1
                elif len(m2)==len(mm):
                    print('els2111')
                    for i in range(0,len(mm)):              
                        print(mm[i],mm[i][-1])
                        if mm[i][-1]!='1':
                            break
                    for i in range(1,len(mm)):
                        if mm[i][0]!='9':
                            break
                    return 1
     return 0
          
def is_interesting(number, awesome_phrases):
    astr=str(number)[::-1]
    print(list(str(number)),astr)
    if number<=97:
        return 0
    if number>97 and number<100:
        return two(number,awesome_phrases)
    if number>99:
        if number in awesome_phrases or len(set(list(str(number))))==1 :
            print('1',set(str(number).split()))
            return 2
        if set(list(str(number))[1:])=={'0'}:
            print('2',set(list(str(number))[1:]))
            return 2
        if str(number)==astr:
            print('5')
            return 2
        if '0' not in str(number):
            if ''.join(sorted(list(set(str(number)))))==str(number) and (abs(int(str(number)[0])-int(str(number)[-1]))==len(str(number))-1):
                print(int(str(number)[0])-int(str(number)[-1]))
                print('3',sorted(list(str(number))))
                return 2
            if ''.join(reversed(sorted(list(set(str(number))))))==str(number) and (abs(int(str(number)[0])-int(str(number)[-1]))==len(str(number))-1):
                print(abs(int(str(number)[0])),int(str(number)[-1]))
                print('4',list(reversed(sorted(list(set(str(number)))))),sorted(list(str(number))))
                return 2#two(number,awesome_phrases)
        else:
            if not (str(number)[-1]=='0' and str(number)[-2:] not in ['90','10']) and not (str(number)[1]=='0' and str(number)[:1]!='90'):
                print('else')
                mm=[m for m in str(number).split('0') if m]
                m1=[1 for m in mm if ''.join(sorted(list(set(m))))==str(m) and (abs(int(str(m)[0])-int(str(m)[-1]))==len(str(m))-1)]
                m2=[1 for m in mm if ''.join(reversed(sorted(list(set((m))))))==str(m) and (abs(int(str(m)[0])-int(str(m)[-1]))==len(str(m))-1)]
                print(mm,m1,m2)
                # for mmm in mm:
                #     if ''.join(sorted(list(set(str(mmm)))))==str(mmm) and (abs(int(str(mmm)[0])-int(str(mmm)[-1]))==len(str(mmm))-1):
                #         print('MMM',mmm)
                if len(m1)==len(mm):
                    print('els1')
                    for i in range(0,len(mm)):              
                        if mm[i][-1]!='9':
                            return two(number, awesome_phrases)
                    for i in range(1,len(mm)):
                        if mm[i][0]!='1':
                            return two(number, awesome_phrases)
                    return 2
                elif len(m2)==len(mm):
                    print('els2')
                    for i in range(0,len(mm)):              
                        print(mm[i],mm[i][-1])
                        if mm[i][-1]!='1':
                            print('1i')
                            return two(number, awesome_phrases)
                    for i in range(1,len(mm)):
                        if mm[i][0]!='9':
                            print('9i')
                            return two(number,awesome_phrases)
                    return 2
                else:
                    return 2
    return two(number, awesome_phrases)
       
    
                   
                                                    
def main():

   
    print(is_interesting(3209, []))
    


   


if __name__ == "__main__":
    main()

# def is_good(n, awesome):
#     return n in awesome or str(n) in "1234567890 9876543210" or str(n) == str(n)[::-1] or int(str(n)[1:]) == 0
#
# def is_interesting(n, awesome):
#     if n > 99 and is_good(n, awesome):
#         return 2
#     if n > 97 and (is_good(n + 1, awesome) or is_good(n + 2, awesome)):
#         return 1
#     return 0