import numpy as np
np.set_printoptions(precision=7, suppress=True, linewidth=100)

def apply_div_dif(matrix: np.array):
    size = len(matrix)
    for i in range(2, size):
        for j in range(2, i+2):
            # skip if value is prefilled (we dont want to accidentally recalculate...)
            if j >= len(matrix[i]) or matrix[i][j] != 0:
                continue
            
            # get left cell entry
            left: float = ___

            # get diagonal left entry
            diagonal_left: float = ___

            # order of numerator is SPECIFIC.
            numerator: float = ___ - ___

            # denominator is current i's x_val minus the starting i's x_val....
            denominator = ___

            # something save into matrix
            operation = numerator / denominator
            matrix[i][j] = operation
    
    return matrix


def hermite_interpolation():
    x_points = [1.3, 1.6, 1.9]
    y_points = [.6200, .4554, .2818]
    slopes = [-.522, -.569, -.581]

    # matrix size changes because of "doubling" up info for hermite 
    num_of_points = len(x_points)
    matrix = np.zeros((___, ____))

    # populate x values (make sure to fill every TWO rows)
    for x in range(___):
        break
    
    # prepopulate y values (make sure to fill every TWO rows)
    for x in range(___):
        break

    # prepopulate with derivates (make sure to fill every TWO rows. starting row CHANGES.)
    for x in range(___):
        break

    filled_matrix = apply_div_dif(matrix)
    print(filled_matrix)



if __name__ == "__main__":
    hermite_interpolation()