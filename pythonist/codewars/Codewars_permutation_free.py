mem={0:0,1:1}

def fact(n):
    if n not in mem:
        mem[n]=fact(n-1)*n
    return mem[n]
def permutation_free(n, l):
    print(pow(n,l))
    print(fact(l))
    return pow(n,l)-fact(l)
        
def main():
    #gen('RGB')
      

    print(permutation_free(4, 10))


    
    
  
    
if __name__ == "__main__":
    main()

