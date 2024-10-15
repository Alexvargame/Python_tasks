from itertools import combinations



class Primes:
    @staticmethod
    def stream():
        
    for i in range(2,a//2+1):
        if a%i==0:
            return False
    return True
        
       



def main():

   pass

if __name__ == "__main__":
    main()


def gen1(s):
    for i in s:
        yield i


def gen2(n):
    for i in range(n):
        yield i
g1=gen1('alex')
g2=gen2(5)


tasks=[g1,g2]
while tasks:
    task=tasks.pop(0)
    try:
        i=next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass



def is_prime(a):
    for i in range(2,a//2+1):
        if a%i==0:
            return False
    return True
