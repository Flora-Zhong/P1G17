import numpy as np

def left_endpoint(x_vals: np.ndarray, func: np.ufunc):
    a = x_vals[0]
    b = x_vals[-1]
    total = func(a) * (b - a)
    return total

def trapezoid(x_vals: np.ndarray, func: np.ufunc):
    length = len(x_vals)
    x_index = 0
    total = 0
    for i in range(length - 1):
        total += (func(x_vals[x_index]) + func(x_vals[x_index + 1])) * (x_vals[x_index + 1] - x_vals[x_index]) / 2
        x_index += 1
    return total

def simpson(x_vals: np.ndarray, func: np.ufunc):
    length = len(x_vals)
    x_index = 0
    total = 0
    for i in range(length - 1):
        mid = (x_vals[x_index] + x_vals[x_index + 1]) / 2
        total += (x_vals[x_index + 1] - x_vals[x_index]) / 6 * (func(x_vals[x_index]) + 4 * func(mid) + func(x_vals)[x_index + 1])
        x_index += 1
    return total