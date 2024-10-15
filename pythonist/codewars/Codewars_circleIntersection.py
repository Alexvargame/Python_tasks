from math import * 
def circleIntersection(a,b,r):
    try:
        f=2*acos(sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)/(2*r))
    except:
        return 0
    return floor(r*r*(f-sin(f)))


def main():
    print(circleIntersection([38, -18], [46, -29], 10))


       
if __name__ == "__main__":
    main()
