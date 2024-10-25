a=int(input("a:", ))
b=int(input("b:", ))
operation=input()
def calc(a,b,operation):
   
    if operation=='+':
        print(a+b)
    elif operation=='-':
        print(a-b)
    elif operation=='*':
        print(a*b)
    elif operation=="/":
        print(a/b)
    else: print("non")
calc(a,b,operation)     
