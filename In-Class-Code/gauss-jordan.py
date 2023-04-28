import numpy as np
np.set_printoptions(precision=7, suppress=True, linewidth=100)


def gauss_jordan(A, b):
    n = len(b)
    
    # Combine A and b into augmented matrix
    Ab = np.concatenate((A, b.reshape(n,1)), axis=1)
    
    # Perform elimination
    for i in range(n):
        # Find pivot row
        max_row = i
        for j in range(i+1, n):
            if abs(Ab[j,i]) > abs(Ab[max_row,i]):
                max_row = j
        
        # Swap rows to bring pivot element to diagonal
        Ab[[i,max_row], :] = Ab[[max_row,i], :] # operation 1 of row operations
        
        # Divide pivot row by pivot element
        pivot = Ab[i,i]
        Ab[i,:] = Ab[i,:] / pivot
        
        # Eliminate entries below pivot
        for j in range(i+1, n):
            factor = Ab[j,i]
            Ab[j,:] -= factor * Ab[i,:] # operation 2 of row operations
    
    # Perform back-substitution
    for i in range(n-1, -1, -1):
        for j in range(i-1, -1, -1):
            factor = Ab[j,i]
            Ab[j,:] -= factor * Ab[i,:]
    
    # Extract solution vector x
    x = Ab[:,n]
    
    return x

if __name__ == "__main__":
    A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
    b = np.array([1,2,3])

    x = gauss_jordan(A, b)
    print(x)
