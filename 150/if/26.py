#n=int(input("n",))
n=7
if n<2:
    age=n*10.5
else: age=10.5*2+(n-2)*4
print(age)
print("--------")
import calendar
month_=['Январь','Февраль','Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь','Октябрь', 'Ноябрь', 'Декабрь']
c=calendar.Calendar()
#m=input("m", )
#for i in range(len(month_)):
 #   if month_[i]==m:
 #       num=i
#print(c.days(num))
l=[4,9,1,2,3,3,8,4,3,4,4,2,4,7,8]
if len(l)%2!=0:
    l.sort()
    print(l[int((len(l)-1)/2)+1])
n=int(input("n", ))
for i in range(1,11):
    str_=str(n)+'x'+str(i)+'='+str(n*i)
    print(str_)
for i in range(10):
    print(str(i)*i)
    

