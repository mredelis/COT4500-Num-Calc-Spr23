import numpy as np
np.set_printoptions(precision=7, suppress=True, linewidth=100)

def partial_pivot(matrix: np.array, b_vector: np.array) -> None: 
    # you can also use the b_vectors because number of equations is directly 
    # associated with number of rows
    num_rows: int = len(matrix)

    for inital_row in range(0, num_rows):
        # for now, assume max_row is current_row because we have yet to check the rest
        max_row = inital_row

        for other_row in range(inital_row+1, num_rows):
            # be careful here, make sure you get the correct cell from 
            # max row AND current row
            current_cell: float = matrix[other_row][inital_row]
            max_cell: float = matrix[inital_row][inital_row]

            if abs(current_cell) > abs(max_cell):
                max_row = other_row

        # apply swapping
        # if you wanted to switch x and y, you can simply do x,y = y,x 
        matrix[[inital_row, max_row]] = matrix[[max_row, inital_row]]
        b_vector[[inital_row, max_row]] = b_vector[[max_row, inital_row]]

    # print(matrix)
    # print(b_vector)

    return None


def scaled_partial_pivoting(matrix: np.array, b_vector: np.array) -> None: 
    num_rows: int = len(matrix)

    # extract scaled versions of each row
    scaled_factors: np.array = np.zeros(num_rows)
    for row in range(num_rows):
        scaled_factors[row] = max(abs(matrix[row]))

    for inital_row in range(0, num_rows):
        max_row = inital_row
        max_ratio: int = 0

        for other_row in range(inital_row+1, num_rows):
            current_cell: float = matrix[other_row][inital_row]

            # instead of looking at the max row value, we will be using the scaled
            # version to our benefit
            scaled_factor: float = scaled_factors[other_row]
            scaled_value: float = current_cell / scaled_factor

            if abs(scaled_value) > abs(max_ratio):
                max_row = other_row
                max_ratio = scaled_factor

        # apply swapping
        matrix[[inital_row, max_row]] = matrix[[max_row, inital_row]]
        b_vector[[inital_row, max_row]] = b_vector[[max_row, inital_row]]
        scaled_factors[[inital_row, max_row]] = scaled_factors[[max_row, inital_row]]

    print(matrix)
    print(b_vector)

    return None


if __name__ == "__main__":
    matrix = np.array([[.0030, 59.14], 
                       [5.291, -6.130]])
    b_vector = np.array([59.17, 46.78])

    partial_pivot(matrix, b_vector)

    matrix = np.array([[30, 591400], 
                       [5.291, -6.130]])
    b_vector = np.array([591700, 46.78])

    scaled_partial_pivoting(matrix, b_vector)