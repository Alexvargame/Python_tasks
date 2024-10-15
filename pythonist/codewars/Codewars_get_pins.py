pins_dict ={'1':['1','2','4'],
            '2':['2','1','3','5'],
            '3':['3','2','6'],
            '4':['4','1','5','7'],
            '5':['5','2','4','6','8'],
            '6':['6','3','5','9'],
            '7':['7','8','4'],
            '8':['8','7','5','9','0'],
            '9':['9','8','6'],
            '0':['0','8'],
            }

def get_pins(observed):
    if len(observed)<1 or len(observed)>8:
        return None
    pins_list=[]
    observed=observed+'*'*(8-len(observed))
    for key in observed:
        if key=='*':
            pins_list.append(['*'])
        else:
            pins_list.append((pins_dict[key]))
    pin=[]
    for k in range(len(pins_list)):
        for i in pins_list[k]:
            for ii in pins_list[k+1]:
                for j in pins_list[k+2]:
                    for jj in pins_list[k+3]:
                        for a in pins_list[k+4]:
                            for aa in pins_list[k+5]:
                                for b in pins_list[k+6]:
                                    for bb in pins_list[k+7]:
                                        pin.append((i+ii+j+jj+a+aa+b+bb).strip('*')) 
        return pin   
        
   


def main():


    print(get_pins('8'))
   
if __name__ == "__main__":
    main()




#
