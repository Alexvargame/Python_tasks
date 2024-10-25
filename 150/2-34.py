from calendar import *
from datetime import *
"""

eq1="ах + b = с"
eq2="dх + ey = f"

a=int(input(" ", ))
b=int(input(" ", ))
c=int(input(" ", ))
d=int(input(" ", ))
e=int(input(" ", ))
f=int(input(" ", ))
x=(c-b)/a
y=f-(c-b)/a/d

print(x,y)

n=int(input(" ", ))
lst1=[0,1,2,3,4,5,6,7,8,9]
lst2=[]
for i in range(len(lst1)):
   for j in range(len(lst1)):
      for k in range(len(lst1)):
          for l in range(len(lst1)):
             if lst1[i]+lst1[j]+lst1[k]+lst1[l]==n:
                t=(lst1[i],lst1[j], lst1[k], lst1[k])
                lst2.append(t)
print(len(lst2))


print("Input the value of x1, y1, x2, y2, x3, y3:")
x1, y1, x2, y2, x3, y3 = map(float, input().split())
c = (x1-x2)**2 + (y1-y2)**2
a = (x2-x3)**2 + (y2-y3)**2
b = (x3-x1)**2 + (y3-y1)**2
s = 2*(a*b + b*c + c*a) - (a*a + b*b + c*c) 
px = (a*(b+c-a)*x1 + b*(c+a-b)*x2 + c*(a+b-c)*x3) / s
py = (a*(b+c-a)*y1 + b*(c+a-b)*y2 + c*(a+b-c)*y3) / s 
ar = a**0.5
br = b**0.5
cr = c**0.5 
r = ar*br*cr / ((ar+br+cr)*(-ar+br+cr)*(ar-br+cr)*(ar+br-cr))**0.5
print("Radius of the said circle:")
print("{:>.3f}".format(r))
print("Central coordinate (x, y) of the circle:")
print("{:>.3f}".format(px),"{:>.3f}".format(py))

n1=int(input(" ", ))
n2=int(input(" ", ))

if len(str(n1))>10 or len(str(n2))>10:
    print("Over")
else: print(n1+n2)
"""


d=int(input(" ", ))
m=int(input(" ", ))
y=2016
c=Calendar()
day_w=''
month_={1: 'Января', 2: 'Февраля', 3: 'Марта', 4: 'Апреля', 5: 'Мая', 6: 'Июня', 7: 'Июля', 8: 'Августа', 9: 'Сентября', 10: 'Октября', 11: 'Ноября', 12: 'Декабря'}
days={1:"Mon",2:"Tu",3:"Thu",4:"Wen",5:"Fri",6:"Sat",7:"Son",}
date_=datetime(2016, m, d)
date_format='%d %m %Y'
l=c.monthdays2calendar(2016,m)
for i in range(len(l)):
    print(l[i])
    for j in range(len(l[i])):
        if d==l[i][j][0]:
            day_w=l[i][j][1]
date_format='%d  %month_[date_.month] %Y'

print(str(date_.day)+" "+month_[date_.month]+" "+str(date_.year)+"года-"+days[day_w+1])
print(datetime.strftime(date_, date_format))
