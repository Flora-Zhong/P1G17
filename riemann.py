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
    a = x_vals[:-1]
    b = x_vals[1:]
    height = func(a)
    width = b - a
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
    a = x_vals[:-1]
    b = x_vals[1:]
    height = 0.5 * ((func(a)) + (func(b)))
    width = b - a
    total = np.sum(height * width)
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
    a = x_vals[:-1]
    b = x_vals[1:]
    total = np.sum(((b - a) / 6) * (func(a) + 4 * (func((a + b) / 2)) + func(b)))
    return total