import numpy as np
import matplotlib.pyplot as plt


def fracformat(x, pos):
    frac = Fraction(x / np.pi)
    if frac.numerator == 0:
        return 0
    elif frac.numerator == frac.denominator:
        return r"$\pi$"
    elif frac.numerator == 1:
        return r"$\frac{{ \pi }}{{ {:2d} }}$".format(frac.denominator)
    elif frac.denominator == 1:
        return r"${:2d} \pi$".format(frac.numerator)
    else:
        return r"$\frac{{ {:2d} \pi }}{{ {:2d} }}$".format(
            frac.numerator, frac.denominator
        )


def cart2polar(arr):
    arr = np.array((np.linalg.norm(arr, axis=1), np.arctan2(arr[:, 1], arr[:, 0]))).T
    return arr


def cart2spherical(arr):
    R = np.linalg.norm(arr, axis=1)
    theta = np.arctan2(np.linalg.norm(arr[:, :2], axis=1), arr[:, 2])
    phi = np.arctan2(arr[:, 1], arr[:, 0])
    arr = np.array((R, theta, phi)).T
    return arr


def polynomial_xy(npoints):
    x = np.linspace(-5, 5, npoints)
    y = (2 * x**2 - 2 * x + 40) + (10 * np.random.normal(size=x.shape))
    return x, y


def plot_polynomial(x, y, a=None, b=None, c=None):
    plt.figure(figsize=(4, 2))
    plt.plot(x, y, color="b", marker="o", linewidth=0, alpha=0.5)

    if all([args != None for args in (a, b, c)]):
        plt.plot(x, a * x**2 + b * x + c, "r")

    plt.ylabel("$y$", fontsize=14)
    plt.xlabel("$x$", fontsize=14)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.plot()
    return
