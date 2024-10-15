def isValid(s):
    adict = {
        '}': '{',
        ']': '[',
        ')': '(',
        }

    stack = []

    for c in s:
        if c in adict:
            if not (stack and stack.pop() == adict[c]):
                return False
        else:
            stack.append(c)
    return not stack

def main():
    print('res', isValid("([)]"))



if __name__ == "__main__":
    main()
