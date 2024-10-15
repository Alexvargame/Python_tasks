import re
PATTERN = r'[0,1]*'#r'0|(101(0)*)$'

def solution(s):
    if int(re.fullmatch(PATTERN,s)[0],2)%5==0:
        return True
    return False



def main():

    print(solution('101'))

if __name__ == "__main__":
    main()

#
