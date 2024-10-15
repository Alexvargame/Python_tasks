

digit_dict={'1':'1','0':'0','6':'9','9':'6','8':'8'}
def not_digit(a):
    for i in ['2','3','4','5','7']:
        if i in str(a):
            return False
    return True
def reverse_digit(a):
    #print('aAAA',a)
    if len(str(a))%2==0:
        # print(a,'S',str(a)[:int(len(str(a))/2)],'S1',str(a)[int(len(str(a))/2):])
        # print(''.join([digit_dict[i] for i in str(a)[int(len(str(a))/2):]]))
        # print(str(a)[:int(len(str(a))/2)][::-1]==''.join([digit_dict[i] for i in str(a)[int(len(str(a))/2):]]))
        return str(a)[:int(len(str(a))/2)][::-1]==''.join([digit_dict[i] for i in str(a)[int(len(str(a))/2):]])
    else:
        if str(a)[int(len(str(a))/2)] in ['0','1','8']:
            # print('S', str(a)[:int(len(str(a)) / 2)], 'S1', str(a)[int(len(str(a)) / 2)+1:], 'S2',
            #       ''.join([digit_dict[i] for i in str(a)[int(len(str(a)) / 2)+1:].split()]))
            # print(str(a)[:int(len(str(a)) / 2)] == ''.join([digit_dict[i] for i in str(a)[int(len(str(a)) / 2)+1:]]))
            return str(a)[:int(len(str(a))/2)][::-1] == ''.join([digit_dict[i] for i in str(a)[int(len(str(a))/2)+1:]])
        else:
            return False
def solve(a,b):
    #digit_dict={'1':'1','0':'0','6':'9','9':'6','8':'8'}
    if b<=10:
        return len([i for i in [0,1,8] if i>=a])
    else:
        if a>=10:
            return [i for i in range(a,b+1) if not_digit(i) and reverse_digit(i)]
        else:
            return [i for i in range(a,b+1) if not_digit(i) and reverse_digit(i)]

    
                   
                                                    
def main():

   
    print(solve(93, 19161))
    


   


if __name__ == "__main__":
    main()
