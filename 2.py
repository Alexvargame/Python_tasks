def is_year_leap(year):
    
    if year%4==0:
        result=True
    else:
        result=False
    return result

year=int(input ('a:', ))
print(is_year_leap(year))
