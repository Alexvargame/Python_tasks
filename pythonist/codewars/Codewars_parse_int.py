def parse_int(string):
    
    divs={'million':'000000','thousand':'000','hundred':'00'}
    ddict={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7',
           'eight':'8','nine':'9','ten':'10','eleven':'11','twelve':'12','thirteen':'13',
           'fourteen':'14','fifteen':'15','sixteen':'16','seventeen':'17','eighteen':'18',
           'nineteen':'19','twenty':'20','thirty':'30','forty':'40','fifty':'50','sixty':'60',
           'seventy':'70','eighty':'80','ninety':'90','zero':'0'}
    lst=string.split()
    if string in ddict.keys():
        return int(ddict[string])
    res=''
    if lst[-1] in divs.keys():
        for i  in range(len(lst)-1):
            print(lst[i:],lst[i:][0])
            if lst[i:][0]!='and':
                if lst[i:][0] not in divs.keys():
                    if '-' not in lst[i:][0]:
                        if i!=0:
                            res+=ddict[lst[i:][0]]
                            print(res)
                            input()
                        else:             
                                            
                            res+=ddict[lst[i:][0]]
                            print('4444',res)
                            input()
                    else:
                        res+=str(int(ddict[lst[i:][0].split('-')[0]])+int(ddict[lst[i:][0].split('-')[1]]))
                        print('333',res)
                        input()
                else:
                    if lst[i+1] in divs.keys():
                        res+=divs[lst[i]]
                        print('etewt',res)
                        if not [key for key in divs.keys() if key in lst[i+1:]]:
                            print('[]',[key for key in divs.keys() if key in lst[i+1:]])
                            res+=divs[lst[i+1]][1:]
                    else:
                        if lst[i+1] in ddict.keys() and lst[i-1] not in divs.keys():
                            print(len(divs[lst[i]])-len(ddict[lst[i+1]]))
                            res+='0'*(len(divs[lst[i]])-len(ddict[lst[i+1]]))
                            print('RE3R',res)
                            input()
                           
        res+=divs[lst[-1]]
    else:
        
         for i  in range(len(lst)):
            print(lst[i:],lst[i:][0])
            if lst[i:][0]!='and':
                if lst[i:][0] not in divs.keys():
                    if '-' not in lst[i:][0]:
                        if i!=0:
                            res+=ddict[lst[i:][0]]
                            print(res)
                            input()
                        else:             
                                            
                            res+=ddict[lst[i:][0]]
                            print('4444',res)
                            input()
                    else:
                        res+=str(int(ddict[lst[i:][0].split('-')[0]])+int(ddict[lst[i:][0].split('-')[1]]))
                        print('333',res)
                        input()
                else:
                
                    if lst[i-1] in divs.keys():
                        res+=divs[lst[i-1]]
                        print('55',res)
                        if not [key for key in divs.keys() if key in lst[i+1:]]:
                            res+=divs[lst[i]][1:]
                    else:
                        print('rwewr')
                        if lst[i+1] in ddict.keys()and lst[i-1] not in divs.keys():
                            
                            print(len(divs[lst[i]])-len(ddict[lst[i+1]]))
                            res+='0'*(len(divs[lst[i]])-len(ddict[lst[i+1]]))
                            print(res)
         
    
    return int(res)
  ##  return int(res)
### переьор по 1 цифре и у мнолдать на тыяси и сотни
## разбить на разряды по 3 цифры

def main():
    #print(parse_int('seven hundred eighty-three thousand nine hundred and nineteen'))
    print(parse_int('two hundred ninety-seven thousand eight hundred eighty-four'))
    
  
    
if __name__ == "__main__":
    main()


##ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
##        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 
##        'eighteen', 'nineteen']
##TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
##
##def parse_int(string):
##    print(string)
##    numbers = []
##    for token in string.replace('-', ' ').split(' '):
##        if token in ONES:
##            numbers.append(ONES.index(token))
##        elif token in TENS:
##            numbers.append((TENS.index(token) + 2) * 10)
##        elif token == 'hundred':
##            numbers[-1] *= 100
##        elif token == 'thousand':
##            numbers = [x * 1000 for x in numbers]
##        elif token == 'million':
##            numbers = [x * 1000000 for x in numbers]
##    return sum(numbers)
