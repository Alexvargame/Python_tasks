#https://pythonist.ru/futbolisty/
from functools import reduce
from collections import deque


class Player():

    def __init__(self,name, age, height, weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight

    def __str__(self):
        return self.name


    def get_age(self):
        return f"{self.name} is age {self.age}"

    def get_height(self):
        return f"{self.name} is height {self.height}"
    def get_weight(self):
        return f"{self.name} is weight {self.weight}"



def main():
  
    A=Player("Jhon", 25,180, 80)
    print (A)
    print(A.get_age())
    print(A.get_height())
    print(A.get_weight())
    


if __name__ == "__main__":
    main()


