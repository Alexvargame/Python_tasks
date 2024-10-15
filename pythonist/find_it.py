from collections import Counter
   
def find_it(alst):
        counter=Counter(alst)
        return [i for i in alst if counter[i]%2!=0]
   
def main():
 
    print(find_it([0]))
    print(find_it([1,2,2,3,3,1,5]))
if __name__ == "__main__":
    main()


