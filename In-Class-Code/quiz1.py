MAX_ITERATIONS = 100

# Newton Raphson method finds a solution to f (x) = 0 given an initial approximation p0
def newton_raphson_method(initial_approximation: float, tolerance: float, given_function: str):

    i = 1
    function_derivative: str = "3*x**2 - 2*x"

    while i <= MAX_ITERATIONS:
        x = initial_approximation

        if eval(function_derivative) != 0:
            next_approximation = initial_approximation - eval(given_function) / eval(function_derivative)

            if abs(next_approximation - initial_approximation) < tolerance:
                print("Newton Raphson method -> # of iterations: ", i)
                print()
                return  # procedure was successfull

            i += 1
            initial_approximation = next_approximation
        else:
            print("Error derivative is zero")
            return

    print(f"The method failed after {MAX_ITERATIONS} number of iterations")


initial_approximation: float = 1
error_tolerance: float = 10 ** (-3)
print("Tolerance: ", error_tolerance)
function_string = "x**3 - (x**2) + 4"

newton_raphson_method(initial_approximation, error_tolerance, function_string)
