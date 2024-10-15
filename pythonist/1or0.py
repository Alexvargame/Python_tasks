

def oneOrzero(astr):

    adict={}
    alst=[]
    ai=[]
    aii=[]
    for k, v in enumerate([i for i in astr]):
        adict[k]=v
    
    alst=[int(k) for k,v in adict.items() if v=='?']
    ai=[i if i!='?' else '0' for i in astr ]
    print(ai)
    aii.append(ai)
    for i in range(min(alst),len(ai)):
        if i in alst:
            ai[i]='1'
            aii.append(ai)
            
  
    return adict, alst,ai, aii








def main():
    
     print(oneOrzero('1?1?'))
    


if __name__ == "__main__":
    main()


