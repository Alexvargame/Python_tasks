from itertools import combinations

def eq(t1,t2):
    if t1[0]!=t2[0] and t1[1]!=t2[1]:
        return True

def build_matches_table(teams):

    lst=[item for item in combinations([i for i in range(1,teams+1)],2)]
    print(lst)
    print()
    l=[[]]*(teams-1)
    print(l)
    for i in range(len(lst)):
        print(lst[i:][0])
        l[i].append(lst[i:][0])
        print(l)
    return [[lst[i] for i in range(len(lst)) if  eq(lst[i],lst[j])] for j in range(1,len(lst))] 




def main():

   print(build_matches_table(4))

if __name__ == "__main__":
    main()




#
