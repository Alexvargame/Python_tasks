
def summ(arr):
    if len(arr)==0:
        return 0
    elif len(arr)==1:
        return arr[0]
    else:
        arrr=arr[1:]
        return arr[0]+summ(arrr)

def countel(arr):
    if len(arr)==0:
        return 0
    elif len(arr)==1:
        return 1
    else:
        arrr=arr[1:]
        return 1+countel(arrr)


def maxel(arr):
    if len(arr)==0:
        return 0
    elif len(arr)==1:
        return arr[0]
    else:
        if arr[0]<arr[1]:
            arrr=arr[1:]
            return maxel(arrr)
        else:
            arrr=arr[0:1]+arr[2:]
            return maxel(arrr)
        
def quick_sort(arr):
 
    if len(arr)<2:
        return arr
    
    else:
        left_arr=[]
        right_arr=[]
        base=arr[0]
        for a in arr[1:]:
            if a<=base:
                left_arr.append(a)
            else:
                right_arr.append(a)
        return quick_sort(left_arr)+[base]+quick_sort(right_arr)
    
        
      
def main():
    print(summ([3,4,5,8,1]))
    print(countel([3,4,5,8,1]))
    print(maxel([3,4,5,12,1]))
    print(quick_sort([3,4,5,12,1]))



if __name__ == "__main__":
    main()




#
