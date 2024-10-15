def searchMatrix(matrix, target):

    l = 0
    r = len(matrix)-1
    print(l, r, (l+r)//2)
    mid = 0
    while l <= r:
        mid = (r + l) // 2
        print(mid, matrix[mid][0])
        row = matrix[mid]
        if row[0] == target:
            return True
        elif row[0] > target:
            r = mid - 1
        elif row[-1] < target:
            l = mid + 1
        else:
            break
    else:
        return False
    l = 0
    r = len(row) - 1
    print(l, r , row)
    while l <= r:
        mid = (l + r) // 2
        if row[mid] == target:
            return True
        elif row[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return False

def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))



if __name__ == "__main__":
    main()
