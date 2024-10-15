import re
def calc(expression):
    print(re.findall(r'\d.*?\d',expression))

    if not re.findall(r'\d(?:\s|)(?:\-|\+)\s(?:\-|\+)\s\d',expression) and not re.findall(r'\d(?:\s|)(?:\-|\+)\s(?:\-|\+)(?:\s|)\((?:\-\s|)\d\)',expression):
        lst_digit=[]#re.split(r'[+-]',expression)
        for s in expression:
            if s.isdigit():
                lst_digit.append(int(s))
        print(lst_digit)
        lst_sign=[]#re.split(r'[\d\(\)]',expression)
        for s in expression:
            if s in ['+','-','/']:
                lst_sign.append(s)
        print(lst_sign)
        sign=lst_sign[0]
        for i in range(len(lst_digit)):
            pass
        for j in range(1,len(lst_sign)):
            print('s',lst_sign[j])
            if lst_sign[j] in ['-','+']:
                if lst_sign[j]=='-' and lst_sign[j-1]=='-':
                    sign='+'
                else:
                    sign='-'
        print('sss',sign)
        if sign=='+':
            return lst_digit[0]+lst_digit[1]
        else:
            return lst_digit[0]-lst_digit[1]
     
        
def main():
    print(calc('10- 2- -5'))
    

    
if __name__ == "__main__":
    main()




#
