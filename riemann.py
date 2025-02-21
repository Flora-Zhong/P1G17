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
    total = np.sum(width * height)
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
    width = b - a
    height = 0.5 * ((func(a)) + (func(b)))
    return np.sum(width * height)

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




x_vals = np.linspace(0, np.pi, 10000)
func = np.sin

# You don't need to change anything below this line
left_endpoint_sum = left_endpoint(x_vals, func)
trapezoid_sum = trapezoid(x_vals, func)
simpson_sum = simpson(x_vals, func)

print(f"Left Endpoint: {left_endpoint_sum}")
print(f"    Trapezoid: {trapezoid_sum}")
print(f"      Simpson: {simpson_sum}")