def divider(dividend, divisor):
    quotient = None
    if divisor == 0:
        quotient = "Ошибка. Деление на 0."
    else:
        quotient = dividend / divisor
    return quotient
