#!/usr/bin/env python3


@profile
def sieve(n):
    primes = [2]
    test = list(range(3, n + 1, 2))
    while test[0] ** 2 <= n:
        p = test.pop(0)
        primes.append(p)
        test = [n for n in test if n % p]  # Overwrite test each loop
    return primes + test


primes = sieve(5000)
print(len(primes))
