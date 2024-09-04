# ruff: noqa: D100


@profile  # noqa: F821
def sieve(n):
    """Return a list of all primes up to integer n.

    Parameters
    ----------
    n : int
        The upper limit to find primes up to.

    Returns
    -------
    list
        A list of integers up to n.
    """
    primes = [2]
    test = list(range(3, n + 1, 2))
    while test[0] ** 2 <= n:
        p = test.pop(0)
        primes.append(p)
        test = [n for n in test if n % p]  # Overwrite test each loop
    return primes + test


if __name__ == "__main__":
    primes = sieve(5000)
    print(len(primes))  # noqa: T201
