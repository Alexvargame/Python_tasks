

def TicTacToeChecker(alst):

   
   res_dict={'-1':'не заполнена', '1': 'выиграл Х', '2':'выиграл О', '0': 'ничья'}
   if len([a for a in alst if len(a)<len(alst)])>0:
      return res_dict['-1']
   
   else:
      res=[a for a in alst]
      res.extend([list(z) for z in list(zip(*alst))])
      
      res.append([alst[i][i] for i in range(len(alst))])
      res.append([alst[i][len(alst)-1-i] for i in range(len(alst))] )
      #return res_dict[str((len[sum(set(r)) for r in res if len(set(r))<2]))]
      if not ([r[0] for r in res if len(set(r))<2  and r[0]>0]):
         return res_dict['0']
      return res[0][0]
   #res_dict[[str(r[0]) for r in res if len(set(r))<2][0]]


def main():
    
     print(TicTacToeChecker([[0,0,1],[0,1,2],[2,1,0]]))
     print(TicTacToeChecker([[1,1,1],[0,1,2],[2,1,0]]))
     print(TicTacToeChecker([[0,0,1],[2,2,2],[2,1,0]]))
     print(TicTacToeChecker([[0,0,],[2,2,2],[2,1,0]]))
     print(TicTacToeChecker([[0,1,1],[2,0,2],[2,1,0]]))
    
    

if __name__ == "__main__":
    main()


