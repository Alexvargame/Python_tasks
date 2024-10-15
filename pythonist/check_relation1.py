#https://github.com/appKODE/2018-internship-backend
from functools import reduce

def check_relation(net,first,second):
    #f=[n for n in list(net) if (first in n or second in n )]
    #f1=[set(n)-{first} for n in list(net) if (first in n)]
    #f2=[set(n)-{second} for n in list(net) if (second in n )]
    #ff=list(map(lambda a,b:set(a)&set(b), [n for n in list(net) if (first in n)],f2=[n for n in list(net) if (second in n )]))
    #reduce(lambda a,b: 1 if (len(set(a)&set(b))>0) else 0, f)
    print([list(set(n)-{first})[0] for n in list(net) if (first in n)],[list(set(n)-{second})[0] for n in list(net) if (second in n )])
    #print(list(map(lambda a,b:True if(len(set(a)&set(b))>0) else False, [n for n in list(net) if (first in n)],[n for n in list(net) if (second in n )])))
    
   
    input()
    return set([list(set(n)-{first})[0] for n in list(net) if (first in n)])&set([list(set(n)-{second})[0] for n in list(net) if (second in n )])
#any(list(map(lambda a,b:True if(len(set(a)&set(b))>0) else False, [n for n in list(net) if (first in n)],[n for n in list(net) if (second in n )])))





def main():
     net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )
     print(check_relation(net, "Петя", "Стёпа"))
     print(check_relation(net, "Ваня", "Дима"))
     print(check_relation(net, "Ваня", "Катя"))
     print(check_relation(net, "Лёша", "Настя"))
     print(check_relation(net, "Стёпа", "Маша"))
     print(check_relation(net, "Лена", "Маша"))
     print(check_relation(net, "Вова", "Лена"))


if __name__ == "__main__":
    main()


