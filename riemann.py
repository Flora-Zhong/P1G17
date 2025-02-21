import numpy as np

def left_endpoint(x_vals: np.ndarray, func: np.ufunc) -> float:
    """

    Returns the approximate Riemann integrals with the left endpoint function.

    Parameters
    ----------
    x_vals : np.ndarray
        The x values used in approximating the integral.
    func : np.ufunc
        The universal function to approximate the integral.

    Returns
    -------
    float, The approximate Riemann integrals with the left endpoint function.

    """
    height = func(x_vals[:-1])
    width = np.diff(x_vals)
    total = np.sum(height * width)
    return total

def trapezoid(x_vals: np.ndarray, func: np.ufunc) -> float:
    """

    Returns the approximate Riemann integrals with the trapezoid function.

    Parameters
    ----------
    x_vals : np.ndarray
        The x values used in approximating the integral.
    func : np.ufunc
        The universal function to approximate the integral.

    Returns
    -------
    float, The approximate Riemann integrals with the trapezoid function.

    """
    length = len(x_vals)
    x_index = 0
    total = 0
    for i in range(length - 1):
        total += (func(x_vals[x_index]) + func(x_vals[x_index + 1])) * (x_vals[x_index + 1] - x_vals[x_index]) / 2
        x_index += 1
    return total

def simpson(x_vals: np.ndarray, func: np.ufunc) -> float:
    """

    Returns the approximate Riemann integrals with the simpson function.

    Parameters
    ----------
    x_vals : np.ndarray
        The x values used in approximating the integral.
    func : np.ufunc
        The universal function to approximate the integral.

    Returns
    -------
    float, The approximate Riemann integrals with the simpson function.

    """
    length = len(x_vals)
    x_index = 0
    total = 0
    for i in range(length - 1):
        mid = (x_vals[x_index] + x_vals[x_index + 1]) / 2
        total += (x_vals[x_index + 1] - x_vals[x_index]) / 6 * (func(x_vals[x_index]) + 4 * func(mid) + func(x_vals)[x_index + 1])
        x_index += 1
    return total