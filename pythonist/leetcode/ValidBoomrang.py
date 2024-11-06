def isBoomerang(points):

    if (points[1][1] - points[0][1]) * (points[1][0] - points[0][0]) == (points[1][1] - points[0][1]) * (
            points[2][0] - points[0][0]):
        return False
    else:
        return True




def main():
    #print('res', maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print('res', isBoomerang([[1,1],[2,2],[3,3]]))


if __name__ == "__main__":
    main()
