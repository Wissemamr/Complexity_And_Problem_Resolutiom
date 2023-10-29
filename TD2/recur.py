# Calculer le carre d'un nomdre en utilisant la recursivite
# On sait que (N+ 1)^2 = N^2 + 2N + 1
# Pour n-1
# N^2 = (N-1)^2 + 2N - 1


def recursive_square(n: int) -> int:
    """Calculates the square of n in a recursive way"""
    if n == 0 or n == 1:
        return n
    else:
        return recursive_square(n - 1) + 2 * n - 1


# la somme des n premiers entiers
def recursive_sum(m: int) -> int:
    if m == 0:
        return m
    else:
        return recursive_sum(m - 1) + m


# (n-1)! = (n-1)*n!
def recursive_factorial(a: int) -> int:
    if a < 0:
        raise ValueError(f"the value {a} has to be positive")

    elif a == 0 or a == 1:
        return 1
    else:
        return a * recursive_factorial(a - 1)

    # NOTE : Le type de recursite est : simple


def recursive_fibonacci(t: int) -> int:
    if t == 0 or t == 1:
        return t
    else:
        return recursive_fibonacci(t - 1) + recursive_fibonacci(t - 2)


def iterative_fibonacci(p: int) -> int:
    fib_sum = 0
    if p == 0 or p == 1:
        fib_sum = p
    else:  # i >=2
        curr_el = 0
        prev_el = 1
        for i in range(2, p+2):
            next_el = curr_el + prev_el
            prev_el , curr_el = curr_el , next_el
        return curr_el
            



# ==============================================================================


if __name__ == "__main__":
    n = 13
    sq = recursive_square(n)
    print(f"The square of {n} is : ", sq)
    # -----------------------------------------------------------
    m = 7
    s = recursive_sum(m)
    print(f"The sum of the first {m} integers  is : ", s)
    # -----------------------------------------------------------
    a = 13
    fact = recursive_factorial(a)
    print(f"The factorial of {a} is : {fact} ")
    # -----------------------------------------------------------
    t = 10
    fib = recursive_fibonacci(t)
    print(f"Recursively, the fibonacci serie of {t} is:  F[{t-1}] : {fib}")
    # -----------------------------------------------------------
    p = 10
    fib_iter = iterative_fibonacci(p)
    print(f"Iteratively, the fibonacci serie of {p} is:  F[{p-1}] : {fib_iter}")
