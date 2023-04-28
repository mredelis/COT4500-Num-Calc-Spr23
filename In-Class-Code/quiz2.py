import numpy as np

np.set_printoptions(precision=7, suppress=True, linewidth=100)


# 4. Divided difference method, Hermite polynomial approximation
def hermite_interpolation(x_points, y_points, slopes):
    # matrix size changes because of "doubling" up info for hermite
    num_of_points = len(x_points)
    matrix = np.zeros((num_of_points * 2, num_of_points * 2))

    # populate x values (make sure to fill every TWO rows)
    for x in range(0, num_of_points * 2, 2):
        matrix[x][0] = x_points[int(x / 2)]
        matrix[x + 1][0] = x_points[int(x / 2)]
        # break

    # prepopulate y values (make sure to fill every TWO rows)
    for x in range(0, num_of_points * 2, 2):
        matrix[x][1] = y_points[int(x / 2)]
        matrix[x + 1][1] = y_points[int(x / 2)]

    # prepopulate with derivates (make sure to fill every TWO rows. starting row CHANGES.)
    for x in range(1, num_of_points * 2, 2):
        matrix[x][2] = slopes[int(x / 2)]

    filled_matrix = apply_div_dif(matrix)
    print("\nHermite Interpolation Matrix: ")
    print(f"\n{filled_matrix}")
    print("\nf[z1, z2, z3, z4] rounded: ", round(filled_matrix[4][4]))


def apply_div_dif(matrix: np.array):
    size = len(matrix)

    for i in range(2, size):
        for j in range(2, i + 2):
            # skip if value is prefilled (we dont want to accidentally recalculate...)
            if j >= len(matrix[i]) or matrix[i][j] != 0:
                continue

            # get left cell entry
            left: float = matrix[i][j - 1]

            # get diagonal left entry
            diagonal_left: float = matrix[i - 1][j - 1]

            # order of numerator is SPECIFIC.
            numerator: float = left - diagonal_left

            # denominator is current i's x_val minus the starting i's x_val....
            denominator = matrix[i][0] - matrix[i - j + 1][0]

            # something save into matrix
            operation = numerator / denominator
            matrix[i][j] = operation

    return matrix


# 5. Cubic spline interpolation
def create_matrix_A(x_points):
    n: int = len(x_points)

    matrix_main_diagonal = np.identity(n)

    h = []
    for i in range(n - 1):
        h.append(x_points[i + 1] - x_points[i])

    # Fill in diagonal
    for i in range(1, n - 1):
        for j in range(1, n):
            if i == j:
                matrix_main_diagonal[i][j] = 2 * (h[i] + h[i - 1])

    below_diagonal = h.copy()
    above_diagonal = h.copy()

    # Replace last element of below_diagonal with 0
    below_diagonal[-1] = 0

    # Replace first element of above_diagonal with 0
    above_diagonal[0] = 0

    matrix_below = np.diagflat(below_diagonal, -1)
    matrix_above = np.diagflat(above_diagonal, 1)

    matrix = matrix_main_diagonal + matrix_below + matrix_above
    print(f"\n{matrix}")

    return h, matrix


def create_vector_b(y_points, h_list):
    # This not necessary but to keep consistency with textbook variables
    a_list = y_points.copy()

    n = len(y_points)

    alpha = np.zeros(n)
    for i in range(1, n - 1):
        alpha[i] = 3 / h_list[i] * (a_list[i + 1] - a_list[i]) - 3 / h_list[i - 1] * (a_list[i] - a_list[i - 1])

    print(f"\n{alpha}")

    return alpha


def create_x_vector(x_points, h_list, b_vector):
    # Step 3 page 150
    n = len(x_points)
    l = np.zeros(n)
    u = np.zeros(n)
    z = np.zeros(n)
    c = np.zeros(n)

    l[0] = 1
    # Not necessary u and z arrays are 0 on their first element
    # u[0] = 0
    # z[0] = 0

    # Step 4
    for i in range(1, n - 1):
        l[i] = 2 * (x_points[i + 1] - x_points[i - 1]) - (h_list[i - 1] * u[i - 1])
        u[i] = h_list[i] / l[i]
        z[i] = (b_vector[i] - h_list[i - 1] * z[i - 1]) / l[i]

    # Step 5
    l[n - 1] = 1
    z[n - 1] = 0
    c[n - 1] = 0

    for j in range(n - 2, 0, -1):
        c[j] = z[j] - u[j] * c[j + 1]
        print(f"c{j} = {c[j]}\n")

    print("\nX vector with c values: ")
    print(f"\n{c}\n")

    return c


# Q4 setup
xi_points = [2.1, 2.5, 2.6]
yi_points = [5.456, 6.298, 6.427]
slopes = [0.862, 1.489, 1.743]
hermite_interpolation(xi_points, yi_points, slopes)

# Q5 setup
xi_p = [0, 1, 2, 3]
fxi_p = [1, 2.718, 7.387, 20.079]
h_list, matrix_A = create_matrix_A(xi_p)
b_vector = create_vector_b(fxi_p, h_list)
x_vector = create_x_vector(xi_p, h_list, b_vector)
