import numpy as np
np.set_printoptions(precision=7, suppress=True, linewidth=100)


def row_operations():
    # Define the matrix
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Print the original matrix
    print("Original matrix:\n", A)

    # Perform row operations
    # a[0] = [1, 2, 3] -> 4a[0] = [4,8,12] -> [4, 5, 6] - [4,8,12]
    # 4 - 4 = 0
    # 5 - 8 = -3
    # 6 - 12 = -6
    A[1] = A[1] - 4 * A[0] 
    A[2] = A[2] - 7 * A[0]
    A[2] = A[2] - 2 * A[1]

    # Print the matrix after row operations
    print("Matrix after row operations:\n", A)
    
if __name__ == "__main__":
    row_operations()
