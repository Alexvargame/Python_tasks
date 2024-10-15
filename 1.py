def arithmetic(a,b,operation):
    
    if operation =='+':
        result=a+b
    elif operation=='-':
        result=a-b
    elif operation=='*':
        result=a*b
    elif operation=='/':
        result=a/b
    return result

a=int(input ('a:', ))
b=int(input ('b:', ))
operation=input ('operation:', )

print(arithmetic(a,b,operation))
