import matplotlib.pyplot as plt
import numpy as np


def cart2polar(arr):
    return np.array((np.linalg.norm(arr, axis=1), np.arctan2(arr[:, 1], arr[:, 0]))).T


def cart2spherical(arr):
    r = np.linalg.norm(arr, axis=1)
    theta = np.arctan2(np.linalg.norm(arr[:, :2], axis=1), arr[:, 2])
    phi = np.arctan2(arr[:, 1], arr[:, 0])
    return np.array((r, theta, phi)).T


def polynomial_xy(npoints):
    rng = np.random.default_rng()
    x = np.linspace(-5, 5, npoints)
    y = (2 * x**2 - 2 * x + 40) + (10 * rng.normal(size=x.shape))
    return x, y


def plot_polynomial(x, y, a=None, b=None, c=None):
    plt.figure(figsize=(4, 2))
    plt.plot(x, y, color="b", marker="o", linewidth=0, alpha=0.5)

    if all(args is not None for args in (a, b, c)):
        plt.plot(x, a * x**2 + b * x + c, "r")

    plt.ylabel("$y$", fontsize=14)
    plt.xlabel("$x$", fontsize=14)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.plot()
