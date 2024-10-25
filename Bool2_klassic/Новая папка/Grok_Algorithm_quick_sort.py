import random
import datetime

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
    #print('len',len(arr))
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
def lineary_contains(arr,key):
    for a in arr:
        if a==key:
            return True
    return False
def binary_contains(arr,key):
    low=0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)//2
        if arr[mid]<key:
            low=mid+1
        elif arr[mid]>key:
            high=mid-1
        else:
            return True
    return False

      
def main():
    # print(summ([3,4,5,8,1]))
    # print(countel([3,4,5,8,1]))
    # print(maxel([3,4,5,12,1]))
    als = [random.randint(1, 100000) for i in range(1000000)]
    key = als[17609]
    t_b=datetime.datetime.now()
    print(binary_contains(quick_sort(als),key))
    t_e=datetime.datetime.now()
    #print(quick_sort(als))
    print('bin',t_e-t_b)
    t_b = datetime.datetime.now()
    print(lineary_contains(als, key))
    t_e = datetime.datetime.now()
    # print(quick_sort(als))
    print('lin',t_e - t_b)


if __name__ == "__main__":
    main()




#
