def solution(roman : str) -> int:
    roman_dict={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1, 'CD': 400, 'CM': 900, 'XL': 40, 'XC': 90, 'IX':9, 'IV':4}
    result=0
    i=0
    while i<len(roman):

        if roman[i:i+2] in roman_dict:
            print(roman[i:i + 2])
            result+=roman_dict[roman[i:i+2]]
            i=i+2
        else:
            print(roman[i])
            result+=roman_dict[roman[i]]
            i=i+1
        # print('res_1',result)
        # input()
    return result
        


def main():
    
    print(solution('MMMDCCCLXXXVIII'))
    

if __name__ == "__main__":
    main()

#
