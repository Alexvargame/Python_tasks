def rotateString( s: str, goal: str) -> bool:
    i = 0
    while i < len(s):
        if s[i:]+s[:i] == goal:
            return True
        i += 1
    return False

def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', rotateString(s="abcde", goal="cdeab"))



if __name__ == "__main__":
    main()
