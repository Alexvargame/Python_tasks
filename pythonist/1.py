from functools import wraps, reduce
from time import time
from random import sample
from hashlib import md5


def find_values(*args):
    t1=time()
    count=0
    l=[]
    for i in range(len(args[0])):
         for j in range(len(args)):
             if args[0][i] in args[j]:
                 count=1
             else:
                 count=0
                 break
         if count==1:
             l.append(args[0][i])
    t2=time()
    print(t2-t1, "c")
    return l
 


class Timing():
    def __init__(self, desc = ""):
        self.desc = desc

    def __call__(self, f):
        @wraps(f)
        def wrap(*args, **kw):
            ts = time()
            result = f(*args, **kw)
            te = time()
            print(f"Function: {f.__name__} ({self.desc}) takes: {(te-ts):2.4f} sec")
            return result

        return wrap


@Timing("Use reduce")
def find_values01(*args):
    return list(reduce(lambda x, y: x & set(y), args[1:], set(args[0]))) if args else []


@Timing("Use set.intersection")
def find_values02(*args):
    return list(set.intersection(*[set(i) for i in args])) if args else []


@Timing("Use pure loop")
def find_values03(*args):
    if not args:
        return []
    res = set(args[0])
    for i in args[1:]:
       res &= set(i)
    return list(res) 
 
 
def main():
    lst = [sample(range(0, 1000), 100)] * 100_000
    res1 = find_values01(*lst)
    res2 = find_values02(*lst)
    res3 = find_values03(*lst)
    
    
    print(len(res1), md5(str(res1).encode('utf-8')).hexdigest())
    print(len(res2), md5(str(res2).encode('utf-8')).hexdigest())
    print(len(res3), md5(str(res3).encode('utf-8')).hexdigest())
    print(find_values(*lst))
    input()

if __name__ == "__main__":
    main()    
