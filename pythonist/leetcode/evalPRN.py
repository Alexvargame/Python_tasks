
def evalPRN(tokens):

    stack = []
    sign = ['+', '-', '/', '*']
    for t in tokens:
        if t not in sign:
            stack.append(int(t))
        else:
            a = stack.pop()
            b = stack.pop()
            if t == '+':
                stack.append(a+b)
            elif t == '-':
                stack.append(b-a)
            elif t == '*':
                stack.append(b*a)
            else:
                stack.append(int(b/a))
        print(stack)
    return stack[0]




def main():

    print(evalPRN(["4","-2","/","2","-3","-","-"]))


    
    
  
    
if __name__ == "__main__":
    main()
