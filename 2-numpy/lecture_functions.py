"""
File containing functions that are used in the notebooks.

The function in this file are related to tranforming coordinates
and making and plotting polynomials.
"""
import matplotlib.pyplot as plt
import numpy as np


def cart2polar(arr):
    """
    Convert cartesian coordinates to polar coordinates.

    Parameters
    ----------
    arr : numpy array
    An array of cartesian coordinates.

    Returns
    -------
    numpy array
    An array of polar coordinates.
    """
    return np.array((np.linalg.norm(arr, axis=1), np.arctan2(arr[:, 1], arr[:, 0]))).T


def cart2spherical(arr):
    """
    Convert cartesian coordinates to spherical coordinates.

    Parameters
    ----------
    arr : numpy array
    An array of cartesian coordinates.

    Returns
    -------
    numpy array
    An array of spherical coordinates.
    """
    r = np.linalg.norm(arr, axis=1)
    theta = np.arctan2(np.linalg.norm(arr[:, :2], axis=1), arr[:, 2])
    phi = np.arctan2(arr[:, 1], arr[:, 0])
    return np.array((r, theta, phi)).T


def polynomial_xy(npoints):
    """
    Generate x and y data for a polynomial.

    Parameters
    ----------
    npoints : int
    The number of points to generate.

    Returns
    -------
    tuple
    A tuple containing x and y data, both are nunpy arrays.
    """
    rng = np.random.default_rng()
    x = np.linspace(-5, 5, npoints)
    y = (2 * x**2 - 2 * x + 40) + (10 * rng.normal(size=x.shape))
    return x, y


def plot_polynomial(x, y, a=None, b=None, c=None):
    """
    Plot a polynomial.

    Parameters
    ----------
    x : numpy array
        The x values.

    y : numpy array
        The y values.

    a : Plot a polynomial.

    Parameters
    ----------
    x : numpy array
        The x values.

    y : numpy array
        The y values.

    a : float, optional
        The coefficient of the x^2 term.

    b : float, optional
        The coefficient of the x term.

    c : float, optional
        The coefficient of the constant term.
    """
    plt.figure(figsize=(4, 2))
    plt.plot(x, y, color="b", marker="o", linewidth=0, alpha=0.5)

    if all(args is not None for args in (a, b, c)):
        plt.plot(x, a * x**2 + b * x + c, "r")

    plt.ylabel("$y$", fontsize=14)
    plt.xlabel("$x$", fontsize=14)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.plot()
