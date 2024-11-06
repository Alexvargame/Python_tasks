

def poorPigs(buckets, minutesToDie, minutesToTest):
    times = minutesToTest // minutesToDie + 1
    res = 0
    while times ** res < buckets:
        res += 1

    return res

def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', poorPigs(buckets = 4, minutesToDie = 15, minutesToTest = 15))



if __name__ == "__main__":
    main()
