
l_result=[]



def snail(matrix,n):
    
    if 2*n-len(matrix)>0:
        f=len(matrix)-n
        for i in range(f,n):
            l_result.append(matrix[f][i])
            print(l_result)
     
        for i in range(f+1,n):
            l_result.append(matrix[i][n-1])
            print(l_result)
        
        for i in range(f+1,n):
            l_result.append(matrix[n-1][n-1-i+f])
            print(l_result)
        
        for i in range(f+1, n-1):
            l_result.append(matrix[n-1-i+f][f])
            print(l_result)
        print(len(matrix))
        return snail(matrix,n-1)
    else: return l_result
def main():

 
    #print(snail([[1,2,3],[4,5,6],[7,8,9]],3))
    print(snail([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],4))
##    print(snail([[1,2,3],[4,5,6]],2))
##    print(snail([[1,2,3]],1))
      
    
if __name__ == "__main__":
    main()

