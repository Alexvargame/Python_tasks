class poww():
    def __init__(self, x,n):
        self.x=x
        self.n=n
    def pow_(self):
        return self.x**self.n
print(poww(2,10).pow_())

class str_w():
    def __init__(self, str_):
        self.str_=str_
    def change(self):
        l=self.str_.split(' ')
        return list(reversed(l))

print(str_w('который имеет два метода get_String').change())

class str_gp():
    def __init__(self):
        #self.str_=str_
        pass
    def get_String(self):
        str_=input("str:", )
        return str_
    def print_String(self, str_):
        print(str_.upper())
str_gp().print_String(str_gp().get_String())

class Rectangle():
    def __init__(self, a,b):
        self.a=a
        self.b=b
    def SQ(self):
        return self.a*self.b
print(Rectangle(3,4).SQ())

class Circle():
    def __init__(self, r):
        self.r=r
        
    def SQ(self):
        return (3.14*self.r**2)/2
    def LE(self):
        return 3.14*2*self.r
    def get_name(self):
        return c._class__
print(Circle(5).SQ(), Circle(5).LE())
c=Circle(3)
print(c.get_name())

