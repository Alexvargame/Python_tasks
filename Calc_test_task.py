from datetime import datetime, date, time, timedelta



class Record:

    def __init__(self, cost, description,date=date.today()):

        self.date=date
        self.cost=cost
        self.description=description

    def __str__(self):
        return f'Дата {self.date} Потрачено {self.cost}-Комментарий {self.description}'

class Calculator:

    def __init__(self, limit):
        self.limit=limit
        self.record=[]

    def add_record(self,rec):
       
        self.record.append(rec)
        return self.record

##    def add_record(self,cost,description, date=date.today()):
##        rec=Record(cost, description,date)
##        self.record.append(rec)
##        return self.record


    def get_today_stats(self):
        return sum([rec.cost for rec in self.record if rec.date==date.today()])

    def get_week_stats(self):
        daterange=[date.today()-timedelta(days=x) for x in range(0,7)]
        return sum([rec.cost for rec in self.record if  rec.date in daterange])
        
        

    def __str__(self):
        return str(self.limit)

class CashCalculator(Calculator):

    def __init__(self, limit):
        super().__init__(limit)
        #self.record=[]
        self.currency={'grv':1, 'USD':40, 'EURO':50}

    def get_today_cash_remained(self,currency):
        
        if (self.limit-self.get_today_stats())/self.currency[currency]>0:
            return f" На сегодня осталось {(self.limit-self.get_today_stats())/self.currency[currency]} {currency}"
        elif (self.limit-self.get_today_stats())/self.currency[currency]<0:
            return f" Лимит превышен.Ваш долг {(self.limit-self.get_today_stats())/self.currency[currency]} {currency}"
        else:
            return f" На сегодня лимит исчерпан"
            
                                                            

class CaloryCalculator(Calculator):

    def __init__(self, limit):
        super().__init__(limit)
        #self.record=[]
        

    def get_calories_remained(self):
        
        if self.limit-self.get_today_stats()>0:
            return f" На сегодня можно съесть что-нибудь, с общей калорийностью не более {self.limit-self.get_today_stats()} кКал"
        else:
            return f" Хватит есть!"
            


def main():

    
    c=CashCalculator(1030)
    c.add_record(Record(323,'Еда'))
    c.add_record(Record(100,'Еда',date(2023,4,22)))
    c.add_record(Record(747,'Еда'))
   
    print(*c.record)
    print(c.get_today_stats())
    print(c.get_today_cash_remained('USD'))
    print(c.get_week_stats())

    print('---')

    cal=CaloryCalculator(1000)
    cal.add_record(Record(323,'Еда'))
    cal.add_record(Record(100,'Еда'))
    #cal.add_record(Record(747,'Еда'))
   
    print(*cal.record)
    print(cal.get_today_stats())
    print(cal.get_calories_remained())
    print(cal.get_week_stats())

   

    
 

if __name__ == "__main__":
    main()
