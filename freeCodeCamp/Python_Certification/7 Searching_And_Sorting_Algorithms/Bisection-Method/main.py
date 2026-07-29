def square_root_bisection(number, tolerance = 0.01, iterations = 10):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif number in [0, 1]:
        print(f"The square root of {number} is {number}")
        return number
    else:
        if number > 1:
            lower = 1
            upper = number  
        else:
            lower = number
            upper = 1
        
        root = None  
        i = 0

        while (upper - lower) > tolerance and iterations > i:
            mid = (lower + upper) / 2
            
            if mid ** 2 > number:
                upper = mid
            else:
                lower = mid
            
            if (upper - lower) < tolerance:
                root = mid

            i += 1

        if not root:
            print(f"Failed to converge within {iterations} iterations")
        else:
            print(f"The square root of {number} is approximately {root}")

        return root

square_root_bisection(0)
square_root_bisection(0.001, 1e-7, 50)
square_root_bisection(225, 1e-7, 10)