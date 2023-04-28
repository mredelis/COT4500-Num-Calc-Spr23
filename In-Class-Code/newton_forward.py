import numpy as np

def divided_difference_table(x_points, y_points):
    # set up the matrix
    size: int = ____
    matrix: np.array = np.zeros(____)

    # fill the matrix
    for index, row in enumerate(matrix):
        row[0] = ____

    # populate the matrix (end points are based on matrix size and max operations we're using)
    for i in range(1, ____):
        for j in range(1, ____):
            # the numerator are the immediate left and diagonal left indices...
            numerator = ___ - ____

            # the denominator is the X-SPAN...
            denominator = ___ - ___

            operation = numerator / denominator

            # cut it off to view it more simpler
            matrix[i][j] = '{0:.7g}'.format(operation)


    print(matrix)
    return matrix


def get_approximate_result(matrix, x_points, value):
    # p0 is always y0 and we use a reoccuring x to avoid having to recalculate x 
    reoccuring_x_span = 1
    reoccuring_px_result = _____
    
    # we only need the diagonals...and that starts at the first row...
    for index in range(____, ____):
        polynomial_coefficient = matrix[index][index]

        # we use the previous index for x_points....
        reoccuring_x_span *= (value - x_points[___])
        
        # get a_of_x * the x_span
        mult_operation = polynomial_coefficient * reoccuring_x_span

        # add the reoccuring px result
        reoccuring_px_result += mult_operation

    
    # final result
    return reoccuring_px_result


if __name__ == "__main__":
    # point setup
    x_points = [1.0, 1.3, 1.6, 1.9, 2.2]
    y_points = [.7651977, .6200860, .4554022, .2818186, .1103623]
    divided_table = divided_difference_table(x_points, y_points)

    # find approximation
    approximating_x = 1.5
    final_approximation = get_approximate_result(divided_table, x_points, approximating_x)

    # second example
    x_points = [8.1, 8.3, 8.6, 8.7]
    y_points = [16.94410, 17.56492, 18.50515, 18.82091]
    divided_table = divided_difference_table(x_points, y_points)
    
    # find approximation
    approximating_x = 8.4
    final_approximation = get_approximate_result(divided_table, x_points, approximating_x)

