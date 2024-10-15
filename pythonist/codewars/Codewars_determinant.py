from math import sqrt
from copy import deepcopy
def determinant(matrix):

    if len(matrix)==2:
        

        return abs(matrix[0][0]*matrix[len(matrix)-1][len(matrix)-1]-matrix[0][len(matrix)-1]*matrix[len(matrix)-1][0])
    if len(matrix)==3:
        
        for j in range(len(matrix)):
            matrix1=deepcopy(matrix)
        
            matrix1.pop(0)
            print(matrix, matrix1)
            for i in range(len(matrix1)):
                print(matrix1)
                print('i',i,)
                print(matrix1[i].pop(j),matrix1[i:])
                print(matrix1[:i][j+1:]+matrix1[i:][j+1:])
                print(matrix1)
                input()
            det=matrix[0][j]*abs(matrix1[0][0]*matrix1[len(matrix1)-1][len(matrix1)-1]-matrix1[0][len(matrix1)-1]*matrix1[len(matrix1)-1][0])
            print('DET;',det)
        #return sum([matrix[i][i]*detrminant(matrix[i+1:i])])
##        
##    if n not in mem:
##        mem[n]=fibonacci(n - 1) + fibonacci(n - 2)
##    return mem[n]
##





def main():

    
    print(determinant([[1,2],[3,4]]))
    print(determinant([[1,2,3],[4,5,6],[7,8,9]]))
  
    
if __name__ == "__main__":
    main()



##def memoized(f):
##    cache = {}
##    def wrapped(k):
##        v = cache.get(k)
##        if v is None:
##            v = cache[k] = f(k)
##        return v
##    return wrapped
##
##@memoized
##def fibonacci(n):
##    if n in [0, 1]:
##        return n
##    return fibonacci(n - 1) + fibonacci(n - 2)

##mem={0:0,1:1}
##def fibonacci(n):
##
##    if n not in mem:
##        mem[n]=fibonacci(n - 1) + fibonacci(n - 2)
##    return mem[n]
##
##def alphanumeric(password):
##    if password.isspace() or ' ' in password or len(password)<1:
##        return False
##    else:
##        for l in password:
##            if not l.isnumeric() and not l.isalpha():
##                return False
##        return True
