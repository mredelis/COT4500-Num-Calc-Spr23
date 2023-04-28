import numpy as np
np.set_printoptions(precision=7, suppress=True, linewidth=100)

def original_ode_function(t: float, y: float):
    return y - (t**2) + 1


def first_prime_ode_function(t: float, y: float):
    return original_ode_function(t, y) - (2 * t) 


def get_result_from_taylor_series(t: float, w: float, h: float):
    # the terms are based on the order specified
    # because it is order 2, we only do two equations (or two results)

    # first result
    first_term = original_ode_function(t, w)

    # second result
    multiplication_value = h / 2
    second_term = multiplication_value * first_prime_ode_function(t, w)

    return first_term + second_term


def higher_order_taylor_series():
    # this comes from straight from the lecture
    start, end = (0, 2)
    x, y = (0, .5)

    # optional inputs
    iterations: int = 10

    # the order determines HOW MANY FUNCTIONS WE WILL BE USING.
    # since it is order 2, how many functions does that mean?
    # we would the derivate of the ODE from above

    # so the next step is iterating through all of i, where i is the iteration

    # w0 = .5
    # w1 = w0 + (h * taylor_series)
    # wi = w(i-1) + (h * taylor series)

    # because w starts of at the y point
    cur_w = y 

    # intial value of t is simply the start of the boundary
    cur_t = start

    # h will refer to step size here 
    h: float = (end - start) / iterations 


    for i in range(0, iterations):
        # do the math inside, we need the taylor series summation
        taylor_sum = get_result_from_taylor_series(cur_t, cur_w, h)

        # then we can get the next w
        next_w = cur_w + (h * taylor_sum)

        # we save for future iterations
        cur_t += h
        cur_w = next_w


    print(next_w)
    return next_w


if __name__ == "__main__":
    higher_order_taylor_series()