from collections import Counter
   
def max_r(alst,blst):
        s=[]
        return max([max([abs(len(a)-len(b)) for b in blst]) for a in alst])
        
           
def main():
 
    print(max_r(['rere','errwet','wtwwtwtt3tw'],['wettweer23','rwttyyrrrwer','fttt','wetwetwe','tqwtwtwtw']))
   

      
if __name__ == "__main__":
    main()


