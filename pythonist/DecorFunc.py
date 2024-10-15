
dct={}


def new_func(func):
   def inner(a,b):
      if func.__name__ in dct.keys():
         #print(dct[func.__name__])
         
         if (a in [al[0] for al in dct[func.__name__]]) and (b in [bl[1] for bl in dct[func.__name__]]):
            print(f"Функция {func.__name__} с аргументами   {a},{b} уже вызывалась")
         else:
            dct[func.__name__].append((a,b))
            #print(dct)
      else:
         dct[func.__name__]=[]
         dct[func.__name__].append((a,b))
         #print(dct)
   return inner



def main():


   @new_func
   def func1(a,b):
      print("func1")
   @new_func
   def func2(a,b):
      print("func2")
   func1(1,2)
   func1(2,2)
   func1(1,2)
   func2(2,4)
   func2(2,4)
   func2(2,2)
   
    

if __name__ == "__main__":
    main()


