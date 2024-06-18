def divider(dividend, divisor):
    quotient = None
    if divisor == 0:
        if dividend >= 0:
            quotient = float('inf')
        elif dividend < 0:
            quotient = -float('inf')
    else:
        quotient = dividend / divisor
    return quotient
