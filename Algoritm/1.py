"""
def binary_search(lst,item):
    low=0
    high=len(lst)-1
    while low<=high:
        mid=( low + high ) // 2
        quess=lst[mid]
        if quess==item:
            return mid
        elif quess>item:
            high=mid-1
        else:
            low=mid+1
    return None
lst=[1,2,3,4,5,6,9]
print(binary_search(lst,3))
print(binary_search(lst,-1))

        
def find_smallest(arr):
    small=arr[0]
    small_index=0
    for i in range(1, len(arr)):
        if arr[i]<small:
            small=arr[i]
            small_index=i
    return small_index

def SelectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        small=find_smallest(arr)
        newArr.append(arr.pop(small))
    return newArr

print(SelectionSort([4,1,3,0,9]))
"""

def sum_(arr):
    total=0
    for x in arr:
        total+=x
    return total
print(sum_([1,2,3,4]))

def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        less=[i for i in array[1:] if i<=pivot]
        greater=[i for i in array[1:] if i>pivot]
        return quicksort(less)+[pivot]+quicksort(greater)

print(quicksort([10,5,2,4]))
