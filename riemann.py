import numpy as np

def left_endpoint(x_vals: np.ndarray, func: np.ufunc) -> float:
    length = len(x_vals)
    x_index = 0
    total = 0
    for i in range(length - 1):
        total += func(x_vals[x_index] * (x_vals[x_index + 1] - x_vals[x_index]))
        x_index += 1
    return total