
class Human:
    default_name="A"
    default_age=40
    def __init__(self, name=default_name, age=default_age):
        self.name=name
        self.age=age
        self.house=None
        self.money=0
    def info(self):
        print(self.name, self.age, self.house, self.money)
    def _make_deal(self, h):
        if self.buy_house(h):
            self.house=h
            self.money=self.money-h.final_price(400)
        else: print("not enaugh")
        
    def earn_money(self, add):
        self.money=self.money+add
        
    def buy_house(self, h):
        if h._price<self.money:
            return True
        else:
            return False
        
    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

class House:
    def __init__(self, _area,_price):
        self._area=_area
        self._price=_price
        
    def final_price(self, discount):
        self._price=self._price-discount
        return self._price
    
class SmallHouse(House):
    default_area=40
    def __init__(self, _price,_area=default_area):
        self._price=_price
        self._area=_area
        
    
if __name__ == '__main__':
    Human.default_info()
    hum1=Human("Jack", 35)
    hum2=Human()
   
    hum1.info()
    hum2.info()
    sh1=SmallHouse(5000)
    print(sh1._area, sh1._price)
    h=House(50,10000)
    hum1._make_deal(h)
    hum1.earn_money(3000)
    hum1.earn_money(3000)
    hum1.info()
    hum1._make_deal(h)
    hum1._make_deal(sh1)
    hum1.info()
