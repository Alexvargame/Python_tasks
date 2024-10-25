time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

num=int(input("num:", ))
sum_=0
for i in list(str(num)):
    sum_=sum_+int(i)
print(i)

a=34
b=343
c=231
lst=[]
lst.append(a)
lst.append(b)
lst.append(c)
print(sorted(lst))

import glob
file_list = glob.glob('*.*')
print(file_list)


    
