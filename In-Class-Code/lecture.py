
def check_for_alternating(function_we_got: str):
    term_check = check_for_negative_1_exponent_term(function_we_got)

    return term_check

def check_for_decreasing(function_we_got: str, x: int):
    decreasing_check = True
    k = 1
    starting_val = abs(eval(function_we_got))
    for k in range(2, clea):
        result = abs(eval(function_we_got))

        print(result)
        if starting_val <= result:
            decreasing_check = False

    return decreasing_check


def check_for_negative_1_exponent_term(function: str) -> bool:
    if "-1**k" in function:
        return True

    return False

def absolute_error(precise:float, approximate: float):

    sub_operation = precise - approximate

    return abs(sub_operation)

def relative_error(precise:float, approximate: float):

    sub_operation = absolute_error(precise, approximate)
    div_operation = sub_operation / precise

    return div_operation

if __name__ == "__main__":

    # print(absolute_error())
    # print(relative_error())

    x: float = 4/9
    y: float = 1/3
    z: float = 7/3

    precise_val: float = (x - y) * z

    print(absolute_error(precise_val, .259))

    print(relative_error(precise_val, .259))

    ' section 1.3 '

    ' minimum of terms needed to computer f(1) with error 10^-6'

    ' pre reqs'
    function_a: str = "(-1**k) * (x**k) / (k**3)"
    x: int = 1
    check1: bool = check_for_alternating(function_a)
    check2: bool = check_for_decreasing(function_a, x)

    print(check1 and check2)

    if check1 and check2:
        use_minimum_term_function(function_a)



