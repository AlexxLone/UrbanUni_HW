# Задание: Декораторы в Python
# Цель задания:
# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
# Задание:
# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом
# и "Составное" в противном случае.
def is_prime(func):
    def wrapper(*args):
        digit = func(*args)
        if digit % 2 == 0:
            prime = (digit == 2)
        n = 3
        while n ** 2 < digit and digit % n != 0:
            n += 2
        prime = (n ** 2 > digit)
        print("Простое" if prime else "Cоставное")
        return digit

    return wrapper


# sum_three = is_prime(sum_three)
@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
