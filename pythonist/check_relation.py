#https://github.com/appKODE/2018-internship-backend
from functools import reduce
from collections import deque

def check_relation(net,first,second):
    adict={}
    dict_list=[]
    for n in list(set(net)):
        dict_list.extend(list(n))
##    print(dict_list)
##    print(list(set(dict_list)))
##    input()
  #  print(set(dict_list))
    for a in list(set(dict_list)):
        key,value=a,[list(set(n)-{a})[0] for n in list(net) if a in n]
        l=adict.get(key,[])
        l.extend(value)
        adict[key]=l
##    print("dict",adict)
##    input()
##    #list_first=[]
##    print(adict[first])
   # print(adict)
    search_queue=deque()
    #print(search_queue)
    search_queue+=adict[first]
    searched=[]
    while search_queue:
        person=search_queue.popleft()
        if not person in searched:
            if person==second:
                print(searched)
                return True
            else:
                search_queue+=adict[person]
                searched.append(person)
        
    return False




    


##def f_list(first_list, first,second):
##     for fl in first_:
##        print(fl)
##        first=fl
##        
##        return check_relation(first_list,first,second)
##    



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


