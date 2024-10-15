from math import gcd, sqrt

primes=[2,3,5,7,11,13,17,19,23,29,31]

def is_prime(n):
    limit=int(n**.5)+1
    for div in primes:
        if div>limit: break
        if n%div==0: return False
    return True

def expand_primes(n):
    global primes
    for i in range(primes[-1]/6*6,n+6,6):
        if is_prime(i-1) and (i-1)>primes[-1]: primes+=[i-1]
        if is_prime(i+1) and (i+1)>primes[-1]: primes+=[i+1]

def divisors(n):
    res,orig=[],n
    for prime in primes:
        if prime**2>n: break
        if n%prime==0:
            res+=[prime]
            while n%prime==0: n/=prime
        if prime==primes[-1] and n>prime**2: expand_primes(int(n**.5)+1)
    return res if n==1 else res+[n]

def proper_fractions(n):
    if n<2: return 0
    for div in divisors(n):
        n=n/div*(div-1)
    return n



def main():
    print(proper_fractions(35))
   
  
  
  
 
if __name__ == "__main__":
    main()


###

# def proper_fractions(n):
#     if n < 10000000000000:
#         return len([a for a in range(1, n) if gcd(a, n) == 1])
#     return 0#[a for a in range(1,n,3) if gcd(a,n)==1]
# def proper_fractions(n):
#     phi = n > 1 and n
#     for p in range(2, int(n ** .5) + 1):
#         if not n % p:
#             print('notp',p,phi // p)
#             phi -= phi // p
#             print(phi)
#             while not n % p:
#                 print('p',p)
#                 n //= p
#     if n > 1: phi -= phi // n
#     return phi
