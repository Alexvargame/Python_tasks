from enum import Enum
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
l=[]
l1=[]
for data in Country:
    
    l.append(data.value)
    l1.append(data.name)
print (sorted(l1), l)
