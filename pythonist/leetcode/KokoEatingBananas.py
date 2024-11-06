import math
def minEatingSpeed(piles, h):
    l = 1
    r = max(piles)
    res = r

    while l <= r:
        speed = (r + l) // 2
        total_time = 0
        for pile in piles:
            total_time += math.ceil(pile / speed)
        if total_time <= h:
            res = speed
            r = speed - 1
        else:
            l = speed + 1
    return res

def main():
    print('res', minEatingSpeed(piles=[3,6,7,11], h=8))



if __name__ == "__main__":
    main()
