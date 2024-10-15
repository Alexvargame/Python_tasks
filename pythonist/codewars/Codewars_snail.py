def snail_route(array,output=[]):
    print('Q', array,output)
    if len(array) < 1 or (len(array) == 1 and len(array[0]) < 1):
        return output
    if len(array) > len(array[0]) - 1 and len(output)<1:
        print('d')
        array = [[array[i][j] for i in range(len(array))]
                 for j in range(len(array))]
    print('array',array)
    print('AQ', array[0][::-1], list(zip(*array[::-1])))
    array = list(zip(*array[::-1]))
    print('ARRAY',array)
    print('A', array[0][::-1])
    output.extend(array[0][::-1])
    print('QQ', output)
    return snail_route(array[1:],output)

def snail(array):
    return snail_route(array,output=[])
def main():
    
    print(snail ([[1,2,3],
         [4,5,6],
         [7,8,9]]))
    # print(snail([[1, 2, 3,4],
    #              [5, 6,7,8],
    #              [9,10,11,12],
    #              [13,14,15,16]]))

if __name__ == "__main__":
    main()

# def snail(array, output=[]):
#     print('Q', array, output)
#     if len(array) < 1 or (len(array) == 1 and len(array[0]) < 1):
#         return output
#     if len(array) > len(array[0]) - 1 and len(output)<1:
#         print('d')
#         array = [[array[i][j] for i in range(len(array))]
#                  for j in range(len(array))]
#     print('array',array)
#     print('AQ', array[0][::-1], list(zip(*array[::-1])))
#     array = list(zip(*array[::-1]))
#     print('ARRAY',array)
#     print('A', array[0][::-1])
#     output.extend(array[0][::-1])
#     print('QQ', output)
#     return snail(array[1:], output)

