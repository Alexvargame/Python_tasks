
from collections import Counter
   

def magic_square(alst):
        res=[]
        res.extend([sum(al) for al in alst])
        res.extend([sum(a) for a in list(zip(alst[0],alst[1],alst[2]))])
        res.append(sum([alst[i][i] for i in range(len(alst))]))
        res.append(sum([alst[i][len(alst)-i-1] for i in range(len(alst))]))
        return all(res)
        
        
def main():
 
    print(magic_square([[8,1,6],[3,5,7], [4,9,2]]))
if __name__ == "__main__":
    main()


