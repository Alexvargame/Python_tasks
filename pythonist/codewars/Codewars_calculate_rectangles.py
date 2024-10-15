
from itertools import combinations

def cover(item):
    side_x,side_y=0,0
    if item[0][2]>=item[1][0] and item[0][0]<=item[1][0]:
        if item[1][2]>=item[0][2]:
            side_x=item[0][2]-item[1][0]
        else:
            side_x=item[1][2]-item[1][0]
        print('1sx',side_x)
    if item[0][3]>=item[1][1] and item[0][1]<=item[1][1]:
        if item[1][3]>=item[0][3]:
            side_y=item[0][3]-item[1][1]
        else:
            side_y=item[1][3]-item[1][1]
        print('1sy',side_y)
    elif item[0][3]>=item[1][3] and item[0][1]<=item[1][3]:
        if item[1][1]>=item[0][1]:
            side_y=item[1][3]-item[1][1]
        else:
            side_y=item[1][3]-item[0][1]
        print('2sy',side_y)
    elif item[0][3]<=item[1][3] and item[0][1]>=item[1][1]:
        if item[1][1]>=item[0][1]:
            side_y=item[1][3]-item[1][1]
        else:
            side_y=item[0][3]-item[0][1]
        print('3sy',side_y)
    return side_x*side_y
                                                                               

def square(rect):   
    return (rect[2]-rect[0])*(rect[3]-rect[1])

def calculate(rectangles):

    print('0',[cover(item) for item in combinations(rectangles,2)])   
    return sum([square(rect) for rect in rectangles])-sum([cover(item) for item in combinations(rectangles,2)])

def main():

   print(calculate([(1, 7, 4, 10), (2, 7, 4, 9), (3, 7, 4, 9)]))
#(1, 7, 4, 10), (2, 7, 4, 9), (3, 7, 4, 9
if __name__ == "__main__":
    main()



##    print(item)
##    print('0-2', item[0][2])
##    print('1-0', item[1][0])
##    print('0-0', item[0][0])
##    print('0-3', item[0][3])
##    print('1-1', item[1][1])
##    print('1-3', item[1][3])
##    if (item[0][2]>=item[1][0] and item[0][0]<=item[1][0]):
##        #and (item[0][3]>=item[1][1] and item[0][3]<=item[1][3]):
##        print('s1',item[0][2]-item[1][0])
##        if item[0][3]>=item[1][1] and item[0][1]<=item[1][3]:
##            print('s2',min((item[0][3]-item[1][1]),(item[0][1]<=item[1][3])))
##            print('0-2', item[0][2])
##            print('1-0', item[1][0])
##            print('0-0', item[0][0])
##            print('0-3', item[0][3])
##            print('1-1', item[1][1])
##            print('1-3', item[1][3])
##            print('000',(item[0][2]-item[1][0])*(item[0][3]-item[1][1]))
##            return (item[0][2]-item[1][0])*(item[0][3]-item[1][1])
 #   return 0
#
