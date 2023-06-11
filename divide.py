def divide_numbers(dividend, divisor):
    """
    Divides the dividend by the divisor and returns the result.
    
    Arguments:
    - dividend: The number to be divided (numerator).
    - divisor: The number to divide by (denominator).
    
    Returns:
    The result of the division.
    """
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    
    quotient = dividend / divisor
    return quotient