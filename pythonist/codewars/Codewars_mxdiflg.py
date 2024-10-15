
def mxdiflg(a1,a2):
    if not a1 or not a2:
        return -1
    a1s=sorted(a1,key=len)
    a2s=sorted(a2,key=len)
    print(len(a1s[0]),len(a2s[-1]),len(a2s[0]),len(a1s[-1]))
    max_=max(abs(len(a1s[0])-len(a2s[-1])),abs(len(a2s[0])-len(a1s[-1])))
    print(max_)
    
    return max_
    
def main():

    print(mxdiflg(["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"], ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]))

    
if __name__ == "__main__":
    main()





