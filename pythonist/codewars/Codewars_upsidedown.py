
def check(r):
    DigitsPaires = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]

    if int(r) != 0 and int(r[-1]) == 0:
        return None
    if len(r) % 2 == 0:
        for i in range(int(len(r) / 2)):
            print(r,'iii',r[:int(len(r) / 2)][i], r[int(len(r) / 2):][::-1][i])
            if (r[:int(len(r) / 2)][i], r[int(len(r) / 2):][::-1][i]) not in DigitsPaires:
                return None
    else:
        if r[int(len(r) // 2)] in ['0', '1', '8']:
            for i in range(int(len(r) // 2)):
                if (r[:int(len(r) // 2)][i], r[int(len(r) // 2) + 1:][::-1][i]) not in DigitsPaires:
                    return None
        else:
            return None

    return r


def solve(x, y):

    Nodigits = ['2', '3', '4', '5', '7']
    res = (str(i) for i in range(int(x), int(y)) if not set(list(str(i))) & set(Nodigits))
    dr = list(r for r in res if check(r))
    print(dr)
    return len(dr)


def main():
    
    print(solve('81','2722'))
    
    
  
    
if __name__ == "__main__":
    main()

# import numpy as np
# import re
#
# def check(r):
#     DigitsPaires=[('0','0'),('1','1'),('6','9'),('8','8'),('9','6')]
#     if len(r)%2==0:
#         #print(r[:int(len(r)/2)])
#         #print(r[int(len(r)/2):])
#         #print([i for i in range(int(len(r)/2)) if (r[:int(len(r)/2)][i],r[int(len(r)/2):][i]) in DigitsPaires])
#         for  i in range(int(len(r)/2)):
#             if (r[:int(len(r)/2)][i],r[int(len(r)/2):][i]) not in DigitsPaires:
#                 return None
#     else:
#         if r[int(len(r)//2)] in ['0','1','8']:
#             for  i in range(int(len(r)//2)):
#                 if (r[:int(len(r)//2)][i],r[int(len(r)//2)+1:][i]) not in DigitsPaires:
#                     return None
#         else:
#             return None
#
#     return r
#
#
# def upsidedown(x,y):
#
#     Nodigits=['2','3','4','5','7']
#     sh=re.compile(('([01689\+])(?![23457\+])'))
#     for i in range(int(x),int(y)):
#         print(sh.match(str(i)))
#         if sh.match(str(i)):
#             print(str(i))
#
#     res=(str(i) for i in range(int(x),int(y)) if not set(list(str(i)))&set(Nodigits))
#     print(list(res))
#     return  list(r for r in res if check(r))