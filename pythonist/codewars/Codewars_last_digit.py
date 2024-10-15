
def power_choice(a,p):
    print('AP',a,p)
    if a==2 or a==8:
        if p%2!=0:
            return p%4
        else:
            if p%4==2:
                return 4
            else:
                return 6
    elif a==3 or a==7:
        print(p%4)
        return p%4
    elif a==4:
        if p%2==0:
            return 6
        else:
            return 4
    elif a==5 or a==6:
        return a
    elif a==9:
        if p % 2 != 0:
            return 9
        else:
            return 1
    else:
        return 10






def last_digit(lst):
    #mem={'1':0,'2':0,'3','4','5','6','7','8','9','0'}
    print([str(2**i)[-1] for i in range(1,101)])
    print([str(3**(i%4))[-1] for i in range(1,100)])
    lst=lst[::-1]
    pow=power_choice(int(str(lst[1])[-1]),lst[0])
    print(pow)
    print(lst)
    for i in range(1,len(lst[:-1])):
        print('p',lst[i],pow)
        tmp=lst[i]**pow#int(str(l)[-1])**pow
        pow=max(0,power_choice(int(str(lst[i+1])[-1]),tmp))
        print('TMP',lst[i+1],tmp,pow)
    print('L',lst[-1])
    return int(str(lst[-1])[-1])**pow
def main():

    
    print(last_digit([4, 3, 6]))


    
if __name__ == "__main__":
    main()


