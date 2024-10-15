
# def isPrime(x):
# 	if x < 2:
# 		return False
# 	elif x == 2:
# 		return True
# 	for n in range(2, x):
# 		if x % n == 0:
# 			return False
# 	return True
#
# def primeGenerator(a, b):
# 	for num in range(a, b):
# 		if isPrime(num):
# 			yield num
#
#

import gmpy2

class Primes:
    @staticmethod
    def stream():
        n = 2
        while True:
            yield n
            n = gmpy2.next_prime(n)
# def sieve_for_primes_to(n):
#     size = n//2
#     sieve = [1]*size
#     limit = int(n**0.5)
#     print('size',size,'sieve',sieve,'limit',limit)
#     for i in range(1,limit):
#         if sieve[i]:
#             print('s[i]',sieve[i],end=' ')
#             val = 2*i+1
#             tmp = ((size-1) - i)//val
#             sieve[i+val::val] = [0]*tmp
#             print('val',val,tmp,sieve[i+val::val],sieve)
#     return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]
#
# #_primes = sieve_for_primes_to(50000000)
#
# class Primes:
#
#     @staticmethod
#     def stream():
#         global _primes
#         primes = iter(_primes)
#         while True:
#             yield next(primes)
#


def main():
    n=2000000000000000
    primes=[2]
    i = 2
    while i<n:
        i = gmpy2.next_prime(i)
        if i<n:
            primes.append(i)
        print(primes,i)


    #print(gmpy2.next_prime(3))

    #print(sieve_for_primes_to(30))
    # p=Primes()
    # p.stream()


 
if __name__ == "__main__":
    main()


# ###
# import gmpy2
# class Primes:
#     @staticmethod
#     def stream():
#         n = 2
#         while True:
#             yield n
#             n = gmpy2.next_prime(n)
#
#
# def sieve_for_primes_to(n):
#     size = n//2
#     sieve = [1]*size
#     limit = int(n**0.5)
#     for i in range(1,limit):
#         if sieve[i]:
#             val = 2*i+1
#             tmp = ((size-1) - i)//val
#             sieve[i+val::val] = [0]*tmp
#     return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]
#
# _primes = sieve_for_primes_to(50000000)
#
# class Primes:
#
#     @staticmethod
#     def stream():
#         global _primes
#         primes = iter(_primes)
#         while True:
#             yield next(primes)
#
#
# import itertools as it
#
#
# class Primes:
# 	@staticmethod
# 	def stream():
# 		D = {9: 3, 25: 5}
# 		yield 2
# 		yield 3
# 		yield 5
# 		MASK = 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
# 		MODULOS = frozenset((1, 7, 11, 13, 17, 19, 23, 29))
#
# 		for q in it.compress(
# 				it.islice(it.count(7), 0, None, 2),
# 				it.cycle(MASK)):
# 			p = D.pop(q, None)
# 			if p is None:
# 				D[q * q] = q
# 				yield q
# 			else:
# 				x = q + 2 * p
# 				while x in D or (x % 30) not in MODULOS:
# 					x += 2 * p
# 				D[x] = p
#
# class Primes:
#     @staticmethod
#     def stream():
#         n = int(1.55e7)
#         prime = [False, False, True] + [True, False] * (n//2-1)
#         for p in range(3, int(n**0.5) + 1, 2):
#             if prime[p]:
#                 prime[p ** 2::p] = [False] * ((n-p**2)//p+1)
#         for i in range(2 * n):
#             if prime[i]:
#                 yield i