import re
#PATTERN = r'0|(101(0)*)$'
PATTERN = r'(0|1)*$'

def solution(s):
    print('DDDDDDDDDDDD')
    print(re.fullmatch(PATTERN,s))
    if int(re.fullmatch(PATTERN,s)[0],2)%5==0:
        return True
    return False
def main():

    print(solution('10110101'))

if __name__ == "__main__":
    main()

#
