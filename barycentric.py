import numpy as np

def get_barycentric_coordinates(triangle_coordinates: np.ndarray, point_coordinates: np.ndarray) -> np.ndarray:
    """

    Returns the determinant of a matrix.

    Parameters
    ----------
    triangle_coordinates : np.ndarray
        The coordinates of the triangle.
    point_coordinates : np.ndarray
        The coordinates of the point.

    Returns
    -------
    np.ndarray, The barycentric coordinates of the triangle.

    """
    x1, x2, x3 = triangle_coordinates[0]
    y1, y2, y3 = triangle_coordinates[1]
    x, y = point_coordinates
    left_side = np.array([[x1 - x3, x2 - x3], [y1 - y3, y2 - y3]])
    right_side = np.array([[x - x3], [y - y3]])
    lam1, lam2 = np.linalg.solve(left_side, right_side)
    lam3 = 1 - lam1 - lam2
    return np.array([lam1, lam2, lam3])

