import numpy as np

def left_endpoint(x_vals: np.ndarray, func):
    a = x_vals[0]
    b = x_vals[-1]
    total = func(a) * (b - a)
    return total

def trapezoid(x_vals: np.ndarray, func):
    return

def simpson(x_vals: np.ndarray, func):
    return