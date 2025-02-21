import numpy as np

def simpson(x_vals: np.ndarray, func):
    length = len(x_vals)
    x_index = 0
    total = 0
    for i in range(length - 1):
        mid = (x_vals[x_index] + x_vals[x_index + 1]) / 2
        total += (x_vals[x_index + 1] - x_vals[x_index]) / 6 * (func(x_vals[x_index]) + 4 * func(mid) + func(x_vals)[x_index + 1])
        x_index += 1
    return total
