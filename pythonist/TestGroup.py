



def testgroup(alst):

  
    test_dict={}
    for i in range(len(alst)):
        key,value=i,[alst[i].index(j)+1  for j in alst[i] if j=='*']#[i for i in range(alst[i][i]) if alst[i][i]=='*']
      
        test_dict[key]=value
        

                   
    return test_dict#[[(i+1,j+1) for j in range(len(alst[i])) if alst[i][j]=='*'] for i in range(len(alst))]


def main():
    print(testgroup([['-','-','*','-','-','-','-','-'],
                    ['-','-','-','*','-','-','-','-'],
                    ['*','-','-','-','-','-','-','*'],
                    ['-','*','-','-','-','*','-','-'],
                    ['-','-','-','-','-','-','-','-'],
                    ['-','-','-','*','-','-','-','-'],
                    ['-','-','-','-','-','-','-','*'],
                    ['-','-','*','-','-','-','*','-']]))
   

if __name__ == "__main__":
    main()


