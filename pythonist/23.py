from functools import wraps
from time import time
from collections import Counter


LOREM_TEXT = '''Etincidunt amet tempora tempora porro. Adipisci neque voluptatem ut 
velit dolore voluptatem. Dolor porro voluptatem quisquam. Dolorem dolorem dolorem 
etincidunt. Etincidunt eius dolor magnam adipisci labore porro numquam. Labore 
sed sed est.

Quisquam adipisci aliquam neque velit ipsum. Consectetur consectetur 
ut voluptatem. Sed velit non dolore quisquam amet ipsum sit. Dolore adipisci sed 
dolore adipisci amet. Neque neque labore dolorem etincidunt modi adipisci amet. 
Dolorem dolore ut velit neque ut quaerat. Ut porro voluptatem voluptatem sit neque 
eius labore. Quisquam magnam sit numquam numquam labore etincidunt. Ipsum modi sed 
dolor voluptatem. Quisquam dolore velit quisquam velit modi dolore.

Est amet neque quiquia adipisci. Non aliquam adipisci ipsum. Est porro quaerat labore 
adipisci. Non velit consectetur ipsum aliquam velit dolorem. Numquam tempora 
modi est quiquia. Eius velit tempora quiquia eius. Ipsum dolor aliquam tempora 
aliquam aliquam magnam.

Sit amet dolore adipisci. Tempora porro non ut ipsum 
dolore labore est. Etincidunt aliquam tempora sit etincidunt etincidunt dolor quiquia. 
Quisquam dolor dolorem numquam eius est non quiquia. Aliquam non etincidunt dolore 
dolore est aliquam. Labore eius consectetur sit dolorem consectetur tempora sed.

Dolor labore quaerat ipsum adipisci dolore sit velit. Modi labore adipisci etincidunt. 
Labore quisquam labore quiquia est labore etincidunt ut. Aliquam dolore neque etincidunt. 
Porro numquam consectetur sit quiquia. Velit non eius magnam. Adipisci quaerat 
etincidunt non adipisci dolor. Numquam sed neque numquam.

Non magnam etincidunt dolore dolor non dolore magnam. Quiquia modi dolor consectetur 
amet non. Porro sed sed numquam est porro aliquam. Labore voluptatem non voluptatem. 
Porro consectetur dolore tempora aliquam voluptatem. Ipsum adipisci velit dolore ut 
labore tempora. Sed tempora voluptatem ipsum sit adipisci dolorem. Sit porro neque 
tempora. Dolorem quaerat quiquia sit voluptatem ipsum magnam. Quaerat magnam velit neque est.
'''

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


@Timing('Use Counter')
def can_construct01(ransom_note):
    lis=['a','e','i','o','u','y']
    sum_=0
    rcnt = Counter(ransom_note)
    print(rcnt)
    print("------------")
    for rk, rv in rcnt.items():       
        if  rk in lis:
            sum_=sum_+rcnt[rk]
           
    return sum_




@Timing('Use in operator')
def can_construct04(ransom_note):
    lis=['a','e','i','o','u','y']
    rl = list(ransom_note)
    sum_ = 0
    for i in rl:
      if i in lis:
            sum_=sum_+1
        
    return sum_


def main():
    text = LOREM_TEXT*100
    note = "a"*300 + 'b'*300

    print(f"len(note): {len(note)} len(text): {len(text)}")

    print(can_construct01(text))
    print(can_construct04(text))


if __name__ == "__main__":
    main()


