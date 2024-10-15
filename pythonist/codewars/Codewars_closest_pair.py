from math import sqrt
import statistics
#from matplotlib import pyplot as plt\
#import matplotlib
from time import time
MAX=10000000
def calc_n2(lst):
    ans=(MAX,-1,-1)
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if get_distance(lst[i],lst[j])<ans[0]:
                ans=(get_distance(lst[i],lst[j]),lst[i],lst[j])
    return ans
def recurs(points,l,r):
    print('LR',points[l:r])
    if r-l<=3:
        ans=calc_n2(points[l:r])
        points[l:r] = sorted(points[l:r], key=lambda p: p[1])
        print('ans_sl',ans)
        return ans
    else:
        mid=(l+r)//2
        mid_x=points[mid][0]
        midd=statistics.median([p[0] for p in points])
        print(midd)
        print('RREMMM',l,r,mid,mid_x)
        ans=min(recurs(points,l,mid),recurs(points,mid,r))
        print('ans',ans)
        merge(points,l,r)
        #print('LLLL_e', points[l:r])
        print('merge',points,l,r)
        min_d=ans[0]

        c_points=list(filter(lambda p:abs(p[0]-mid_x)<min_d,points))
        print('cp',min_d,c_points,len(c_points),)
        for i in range(len(c_points)):
            print('I',i,range(i-1,0,-1))
            for j in range(i-1,-1,-1):
                p1=c_points[i]
                p2=c_points[j]
                print(i,j,'p12',p1,p2,get_distance(p1,p2),min_d)
                if get_distance(p1,p2)>min_d:
                    print('break')
                    break
                ans=min(ans,(get_distance(p1,p2),p1,p2))
    return ans

# def draw_points(points,mark=None):
#     xs=list(map(lambda p:p[0],points))
#     ys=list(map(lambda p:p[1],points))
#     colors=['blue']*len(points)
#     for i in mark:
#         colors[i]='red'
#     plt.scatter(xs,ys,color=colors)
#     plt.show()


def get_distance(a,b):
    return sqrt((b[1]-a[1])**2+(b[0]-a[0])**2)
def merge(points,l,r):
    m=(l+r)//2
    tmp=[]
    i=l
    j=m
    #print('LLLL_b',points[l:r])
    while i<m or j<r:
        if j==r or (i<m and points[i][1]<points[j][1]):
            tmp.append(points[i])
            i+=1
        else:
            tmp.append(points[j])
            j+=1
    points[l:r]=tmp

def closest_pair(points):

    points=sorted(points,key=lambda p:p[0])
    print(points)
    print('TIME',time())

    return recurs(points,0,len(points))

def main():
    #print(dir(matplotlib))
    d,p1,p2=closest_pair(((2,2), (9,8), (5,5), (6,3), (6,7), (7,4), (7,9)))
    print('AAAAAA',d,p1,p2)
    #draw_points(((2, 2), (9, 8), (5, 5), (6, 3), (6, 7), (7, 4), (7, 9)),p1,p2)
    #print('AAAAAA',closest_pair(((2,2), (2,8), (5,5), (6,3), (6,7), (7,4), (7,9))))
    #print('aaaaa',closest_pair(((1, 1), (100, 1), (40, 40),(1,100),(100,100),(60,60))))


    
if __name__ == "__main__":
    main()




