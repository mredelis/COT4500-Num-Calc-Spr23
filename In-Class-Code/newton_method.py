# import calculus


## optional (replaces eval statement)
# def function(value):
#     return (value ** 3) - (value**2) + 2


def custom_derivative(value):
    return (3 * value* value) - (2 * value)


def newton_raphson(initial_approximation: float, tolerance: float, sequence: str):
    # remember this is an iteration based approach...
    iteration_counter = 0

    # finds f
    x = initial_approximation
    f = eval(sequence)

    # finds f' 
    f_prime = custom_derivative(initial_approximation)
    
    approximation: float = f / f_prime
    while(abs(approximation) >= tolerance):
        # finds f
        x = initial_approximation
        f = eval(sequence)

        # finds f' 
        f_prime = custom_derivative(initial_approximation)

        # division operation
        approximation = f / f_prime

        # subtraction property
        initial_approximation -= approximation
        iteration_counter += 1


if __name__ == "__main__":
    # newton_raphson method
    initial_approximation: float = -5
    tolerance: float = .000004
    sequence: str = "(x**3) - (x**2) + 2"

    newton_raphson(initial_approximation, tolerance, sequence)