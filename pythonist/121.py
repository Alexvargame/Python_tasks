from time import time
from random import *

class Binner:
    def __init__(self, binwidth, binmax):
        self.binwidth, self.binmax = binwidth, binmax
        
        nbins = int(binmax / float(binwidth) + 1)
    
        self.bins = [0] * nbins
    def add(self, value):
        bin = int(value / self.binwidth)
        self.bins[bin] += 1
        
    def __getitem__(self, index):
        return self.bins[index]

    def __len__(self):
         return len(self.bins)
binner =Binner(5, 20)
for i in range(0,20):
         binner.add(i)
print(binner.bins)

for i in range(len(binner)):
    print(i, binner[i])

for n in binner:
    print (n)

def divides(primes, n):
 for trial in primes:
     if n % trial == 0: return True
 return False

def prime_sieve():
     p, current = [], 1
     while 1:
          current += 1
          if not divides(p, current): # if any previous primes divide, cancel
              p.append(current)
              print(p, current)
              yield current
              print(p, current)
for i in prime_sieve():
  print (i)
  if i > 10:
      break

a = 1
def check_something():
   global a
   a = 5
   return True
assert check_something()

