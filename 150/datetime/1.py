from  datetime import *
import time
import calendar
d=datetime.today()
print(datetime.today())
print(datetime.today().year)
print(datetime.today().month)

print("vac" if datetime.today().weekday() in [5,6] else "work")
#print(calendar.Calendar().monthdayscalendar(datetime.datetime.today().year, datetime.datetime.today().month))


#print(datetime.datetime.today().monthday())
print(datetime.today().weekday())


print("Current date and time: " , datetime.now())
print("Current year: ",date.today().strftime("%Y"))
print("Month of year: ", date.today().strftime("%B"))
print("Week number of the year: ", date.today().strftime("%W"))
print("Weekday of the week: ", date.today().strftime("%w"))
print("Day of year: ", date.today().strftime("%j"))
print("Day of the month : ", date.today().strftime("%d"))
print("Day of week: ", date.today().strftime("%A"))

print(datetime.today().weekday())

print("---")

d=date.today()
d1=d-timedelta(days=5)
print(d1)
print("----")

print(date.today(), (date.today()-timedelta(days=1)), (date.today()+timedelta(days=1)))
    

base = datetime.today()
for x in range(0, 5):
      print(base + timedelta(days=x))

d=date(2000,2,28)
d1=date(2001,2,28)
print(d1-d)

def last_thi(year):
    d=date(year,1,1)
    d1=d+timedelta(days=8-d.weekday())
    while d.year==year:
        if d1+timedelta(days=7)<date(year+1,1,1):
            d1=d1+timedelta(days=7)
        else: break
    return d1
print(last_thi(2021))
def third_thi(year,month):
    i=1
    d=date(year,month,1)
    d1=d+timedelta(days=8-d.weekday())
    while d.month==month:
        if d1+timedelta(days=7)<date(year, month+1,1) and i<3:
            d1=d1+timedelta(days=7)
            i=i+1
        else: break
    return d1
print(third_thi(2021,1))
print("---")
def last_d_m(year,month):
    d=date(year,month,1)
    
    if d.month==(d+timedelta(days=30)).month:
  
        print(d+timedelta(days=30))
    elif d.month==(d+timedelta(days=29)).month:
     
         print(d+timedelta(days=29))
    else:

        print(d+timedelta(days=27))
last_d_m(2021,1)
last_d_m(2021,2)
last_d_m(2021,4)


print("--")
d=date(2021,3,21)
day=0
for i in range(d.month, d.month+6):
      day=calendar.monthrange(d.year,i)[1]+day
print(d+timedelta(days=day))
print("---")
for i in range(2):
      print("erer")
      time.sleep(1)

d=date(2021,2,1)
d1=date(2021,3,3)
print(d1-d)
print((d1-d).days*24*3600)


print()
print("Time in seconds since the epoch: %s" %time.time())
print("Current date and time: " , datetime.now())
print("Alternate date and time: " ,datetime.now().strftime("%y-%m-%d-%H-%M"))
print("Current year: ", date.today().strftime("%Y"))
print("Month of year: ", date.today().strftime("%B"))
print("Week number of the year: ", date.today().strftime("%W"))
print("Weekday of the week: ", date.today().strftime("%w"))
print("Day of year: ", date.today().strftime("%j"))
print("Day of the month : ",date.today().strftime("%d"))
print("Day of week: ", date.today().strftime("%A"))
print()
c=calendar.TextCalendar()
c.pryear(2021,1,2,3,3)

print(calendar.firstweekday())
def second_sat_year(year,month):
    d=date(year,month,1)
    d1=d+timedelta(days=12-d.weekday())
    """
    while d.month==month:
        if d1+timedelta(days=7)<date(year, month+1,1):
            d1=d1+timedelta(days=7)
        else: break
    """
    return d1
for i in range(1,13):
      print(second_sat_year(2021,i))
print("---")
