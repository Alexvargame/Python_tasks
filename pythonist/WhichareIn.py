

def WhichareIn(alst, blst):

   

   return [a for a in alst if any([a in b for b in blst])]







def main():
    
     print(WhichareIn(['a','arp', 'live','strong','oiuo'],['lively','alive',
                                                'harp','sharp','armstrong']))
    

if __name__ == "__main__":
    main()


