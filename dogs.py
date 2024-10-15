import random
class Dog:

    def __init__(self,name):
        self.name=name

    def sound(self):
        return f"woof"

    def hunt(self):
        return f"rrrr"
    def __str__(self):
        return self.name

class Mops(Dog):
    def __init__(self,name):
        super().__init__(name)

    def sound(self):
        return f'woo-woo'
    def hunt(self):
        i=random.randint(1,10)
        if i%3==0:
            return f"rrr"
        return None

class Siba_Inu(Dog):
    def __init__(self,name):
        super().__init__(name)

    def sound(self):
        return f'woo-woo'
    def hunt(self):
        return f"rrr"



def main():
    a=Dog('rex')
    print(a)
    print(a.sound())
    print(a.hunt())
    b=Mops('tom')
    print(b)
    print(b.sound())
    print(b.hunt())

if __name__ == "__main__":
    main()