def solution(args):
    new_str=''
    new_arr=[]
    for i in range(2,len(args)):
        if args[i-2] not in new_arr:
            print(i,args[-1],args[i-2],len(args[i-2:]))
            if args[-1]-args[i-2]!=len(args[i-2:])-1:
                print(args[i-2],args[i])
                if args[i]!=args[i-2]+2:
                    if i!=len(args)-1:
                        new_str+=str(args[i-2])+','
                        new_arr.append(args[i-2])
                        print('NA', new_arr)
                        print('na',new_str)
                        input()
                    else:
                        new_str+=str(args[i-2])+','+str(args[i-1])+','+str(args[i])
                
                else:
                    for j in range(i+1,len(args)):
                        print('JJ',args[j-1],args[j])
                        if args[j]!=args[j-1]+1:
                            print('QQQQ', args[i-2:j+1],i-2,j+1,args[j])
                            new_str+=str(args[i-2])+'-'+str(args[j-1])+','
                            new_arr.extend(args[i-2:j])
                            if j>len(args)-2:
                                new_str+=str(args[j])
                                return new_str
                            elif j>len(args)-3:
                                print("ASEEW")
                                new_str+=str(args[j])+str(args[j+1])
                                return new_str
                                
                            print('NAA', new_arr)
                            print('naa',new_str)
                            input()
                            break
            else:
                new_str+=str(args[i-2])+'-'+str(args[-1])
                return new_str
##                new_str+=str(args[i-3])+'-'+str(args[-1])
##                new_arr.extend(args[i-3:])
##                print('naaend',new_str)
                        
    return new_str
            
        
    
 
def main():


    print(solution([-86, -83, -81, -78, -75, -72, -70, -69, -67, -65, -64, -61, -58, -56, -55, -54, -52]))
    
  
  
 
if __name__ == "__main__":
    main()


###
