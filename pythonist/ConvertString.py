

def ConvertString(astr):
  

   return ' '.join([astr.split('-')[0]]+[astr.split('-')[i][0].upper()+astr.split('-')[i][1:] for i in range(1,len(astr.split('-')))]) if '-' in astr else ' '.join([astr.split('_')[0]]+[astr.split('_')[i][0].upper()+astr.split('_')[i][1:] for i in range(1,len(astr.split('_')))]) 





def main():
    
     print(ConvertString('the-stealth-warrior'))
     print(ConvertString('the_stealth_warrior'))
     
    
    

if __name__ == "__main__":
    main()


