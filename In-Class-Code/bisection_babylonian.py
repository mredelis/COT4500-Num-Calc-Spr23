def func(x):
    return x * x * x - x * x + 2


def babylonian_method(first_number):
    error_tolerance: float = 0.003

    iteration_counter: int = 0
    difference: int = 1
    operation = first_number
    while difference >= error_tolerance:
        cur_variable = operation
        operation = (cur_variable / 2) + (1 / cur_variable)

        difference: float = cur_variable - operation

        iteration_counter += 1
        print(cur_variable)

    print("\n")
    print(iteration_counter)


def bisection_method(left: float, right: float, given_function: str):
    # pre requisites
    # 1. we must have the two ranges be on opposite ends of the function (such that
    # function(left) and function(right) changes signs )
    x = left
    intial_left = eval(given_function)

    x = right
    intial_right = eval(given_function)

    if intial_left * intial_right >= 0:
        print("Invalid inputs. Not on opposite sides of the function")
        return

    tolerance: float = 0.0001
    diff: float = right - left

    # we can only specify a max iteration counter (this is ideal when we dont have all
    # the time in the world to find an exact solution. after 10 iterations, lets say, we
    # can approximate the root to be ###)
    max_iterations = 20
    iteration_counter = 0
    while diff >= tolerance and iteration_counter <= 20:
        iteration_counter += 1

        # find function(midpoint)
        mid_point = (left + right) / 2
        x = mid_point
        evaluated_midpoint = eval(given_function)

        if evaluated_midpoint == 0.0:
            break

        # find function(left)
        x = left
        evaluated_left_point = eval(given_function)

        # this section basically checks if we have crossed the origin point (another way
        # to describe this is if f(midpoint) * f(left_point) changed signs)
        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint > 0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0

        if first_conditional or second_conditional:
            right = mid_point
        else:
            left = mid_point

        diff = abs(right - left)

        # OPTIONAL: you can see how the root finding for bisection works per iteration
        print("Iteration number: ", iteration_counter)
        print(mid_point)


if __name__ == "__main__":
    # caveat with this method is it only finds sqrt(2)...how can we find a zero of any function?
    # babylonian_method(10)

    # bisection gives us the first zero of any function to a certain error threshold
    # left = -2
    # right = 5
    # function_string = "x**3 - (4*(x**2)) - 10"
    # bisection_method(left, right, function_string)

    left = 1
    right = 2
    function_string = "x**3 - (4*(x**2)) + 5*x - 2"
    bisection_method(left, right, function_string)
