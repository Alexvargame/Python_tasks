import math
def square(side):
    
    perimetr=side*4
    square=side*side
    diag=math.hypot(side, side)
    result=(perimetr, square,diag)
    return result

side=int(input ('side:', ))
print(square(side))
