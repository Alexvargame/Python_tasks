def maxArea(height):
    l = 0
    r = len(height)-1
    tmp_value = 0

    while l < r:
        print(l, r , height[l], height[r])
        tmp_value = max(tmp_value, min(height[l], height[r])*(r-l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
        print(tmp_value, l, r)
    return tmp_value




def main():
    #print('res', maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print('res', maxArea([8, 7, 2, 1]))


if __name__ == "__main__":
    main()
