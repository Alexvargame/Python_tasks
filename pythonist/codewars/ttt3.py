from functools import reduce




#output=[]
n=3
def snail(array,output=[]):
    
    if len(array)<1:
        return output
    print(array)
    print(len(array),len(array[0]))
    if len(array)>2:
        array=[[array[i][j] for i in range(len(array))]
               for j in range(len(array))]
    
    array=list(zip(*array[::-1]))
   
    output.extend(array[0][::-1])
    
    return snail(array[1:],output)


def main():

 
    print(snail([[1,2,3],[4,5,6],[7,8,9]]))
    print(snail([[1,2,3],[4,5,6]]))
    print(snail([[1,2,3]]))
      
    
if __name__ == "__main__":
    main()

