# task2.py

import random
from scipy.integrate import quad


def f(x):
    return x ** 2


def monte_carlo_integral(func, a, b, n=100000):
    s = 0.0
    for _ in range(n):
        x = random.uniform(a, b)
        s += func(x)
    return (b - a) * (s / n)


def task2():
    a = 0
    b = 2
    n = 100000

    mc = monte_carlo_integral(f, a, b, n)

    analytic = (b ** 3 - a ** 3) / 3

    q, err = quad(f, a, b)

    print("Monte Carlo:", mc)
    print("Analytic:   ", analytic)
    print("quad:       ", q)
    print("Abs error (MC vs analytic):", abs(mc - analytic))
    print("Abs error (MC vs quad):    ", abs(mc - q))


if __name__ == "__main__":
    task2()
