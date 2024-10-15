import math
def season(month):
    
    if month==12 or month<3:
        season="winter"
    elif month<6:
        season="spring"
    elif month<9:
        season="summer"
    else:
        season="autumn"
    return season

month=int(input ('month:', ))
print(season(month))

