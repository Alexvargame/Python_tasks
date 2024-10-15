def solution(args):
    t=sorted(args)
    print(t)
    for i  in range(1,len(t)):
        print(i-1,i, t[i-1],t[i])
    temp=[f'{t[i-1]}-{t[i]}'  for i in range(1,len(t)) if abs(t[i-1])-abs(t[i])<2]
    return temp



def main():


    print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
  
  
  
 
if __name__ == "__main__":
    main()


###
