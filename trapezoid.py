import numpy as np

def trapezoid(x_vals: np.ndarray, func):
    length = len(x_vals)
    x_index = 0
    total = 0
    for i in range(length - 1):
        total += (func(x_vals[x_index]) + func(x_vals[x_index + 1])) * (x_vals[x_index + 1] - x_vals[x_index]) / 2
        x_index += 1
    return total
