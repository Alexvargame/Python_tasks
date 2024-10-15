print("Введите время")
hour=int(input("Часы:",  ))
minute=int(input("Минуты:",    ))

def angle(minute,hour):
    a_minute=6*minute
    if hour<12:
        a_hour=(hour+minute/60)*30
    else: a_hour=((hour-12)+minute/60)*30
    print(a_minute, a_hour)
    return abs(a_minute-a_hour)
print("Угол между стрелками:", angle(minute, hour))
