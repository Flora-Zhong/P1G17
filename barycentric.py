def is_inside_triangle(triangle_coordinates, point_coordinates):
    barycentric_coord = get_barycentric_coord(triangle_coordinates, point_coordinates)
    return np.all(barycentric_coord >= 0)