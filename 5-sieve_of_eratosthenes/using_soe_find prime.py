''' Question 1: Finding primes in Range [1:n] using Sieve of Eratosthenes.

        Logic: Basciaally we mark all the multiple of elements in the given range. We start marking elements from the square of that number
               and the unmarked elements are prime.'''

# def prime_sieve(n):
#     prime = [True for i in range(n + 1)]
#     i =2
#     while i*i <= n:
#         if (prime[i] == True):           # If it remain unchanged then it is prime
#             for j in range(i*2, n+1, i):
#                 prime[j] = False
#         i += 1
#
#     prime[0] = False
#     prime[1] = False
#
#     for i in range(n+1):
#         if prime[i]:
#             print(i, end=" ")
#
#
# n = int(input("Enter the range: "))
# prime_sieve(n)




''' Question 2:  Finding smallest primes factorization in Range [1:n] using Sieve of Eratosthenes.  '''

def spf(n):
    spf = [0 for i in range(n)]
    for i in range(2, n+1):
        spf[i] == i

    for i in range(2, n+1):
        if spf[i] == i:
            for j in range(i**2, n+1, i):
                if spf[j]==j:
                    spf[j] = i


    while n!=1:
        print(spf[n], end=" ")
        n = n/2

n = int(input("Enter the size: "))
spf(n)