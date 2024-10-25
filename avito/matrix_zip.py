output=[]
#matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix=[[1,2,3],[4,5,6],[7,8,9]]

def m(matrix):
    if len(matrix)==1:
        return output#matrix[0]
    print(matrix)
    matrix=list(zip(*matrix[::-1]))
    print(matrix)
    print(matrix[0][::-1])
    output.extend(matrix[0][::-1])
    print(matrix[1:])
    print()
    print('OUT',output)
    input()
    return m(matrix[1:])
m(matrix)


