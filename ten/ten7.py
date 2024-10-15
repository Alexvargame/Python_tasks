### Условия
n=1
m=5

steps=0
queue="hello"
# два списка для значений ord и отсортированный для перебора
p=[]
st=[]
for i in queue:
    p.append(ord(i))
st=sorted(p).copy()
# первый шаг на точку отсчета
steps=p.index(st[n-1])
#сам цикл
for i in range(n-1, m-1):
     if st[i+1]==st[i]:
         steps=steps+1
         #не придумал, как решить проблему индекса одинаковый полок
         p[p.index(st[i])]=p[p.index(st[i])]+0.1
     else:
         if p.index(st[i+1])> p.index(st[i]):
             steps=steps+p.index(st[i+1])-p.index(st[i])
         else:
             steps=steps+p.index(st[i+1])-p.index(st[i])+len(p)
print("Кол-во шагов:", steps)
