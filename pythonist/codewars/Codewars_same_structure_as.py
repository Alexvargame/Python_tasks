def same_structure_as(original, other):
    print('O', original, 'oth', other)
    # print(sorted(original),sorted(other))
    # print(original==other
    if type(original) != type(other) or len(original) != len(other):
        return False

    print('---2', original, other[::-1])
    for i in range(len(original)):
        # print('i', original[i], 'io', other[i])
        print('type', type(original[i]), type(other[i]))
        if type(other[i]) == str:
            print('l', list(other[i]))
        if type(original[i]) != type(other[i]):  # or (type(original[i])==list and len(original[i])!=len(other[i])):
            return False
        if type(original[i]) == list:
            if len(original[i]) != len(other[i]):
                return False
            else:
                for j in range(len(original[i])):
                    if type(original[i][j]) != type(other[i][j]):
                        return False

    return True


def main():
    print(same_structure_as([1,'[',']'],['[',']',1] ))
   # print(same_structure_as([1,[1,1]],[2,[2,2]]))

    #print(same_structure_as([1, 1, 1], [2, 2, 2]))
  
  
  
 
if __name__ == "__main__":
    main()


###
