class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:

    def __new__(cls, model, vin, numbers):
        valid_numb, valid_vin = False, False
        err_msg = (f'\033[31mЭкземпляр не создан! \033[0mМодель: {model}. VIN: {vin}. '
                   f'Гос. номер: {numbers}. ')
        try:
            valid_vin = Car.__is_valid_vin(vin)
        except IncorrectVinNumber as err:
            err_msg += err.message
        try:
            valid_numb = Car.__is_valid_numbers(numbers)
        except IncorrectCarNumbers as err:
            err_msg += err.message
        if valid_numb and valid_vin:
            return super().__new__(cls)
        else:
            print(err_msg)
            return None

    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        print(f'\033[32mЭкземпляр успешно создан: \033[0mМодель: {self.model}. VIN: {self.__vin}. '
              f'Гос. номер: {self.__numbers}')

    @staticmethod
    def __is_valid_vin(vin):
        if not (isinstance(vin, int)):
            raise IncorrectVinNumber(f'\033[31mНекорректный тип vin номера: \033[0m{vin}. ')
        if vin not in range(1000000, (9999999 + 1)):
            raise IncorrectVinNumber(f'\033[31mНеверный диапазон для vin номера: \033[0m{vin}. ')
        else:
            return True

    @staticmethod
    def __is_valid_numbers(numbers):
        if not (isinstance(numbers, str)):
            raise IncorrectCarNumbers(f'\033[31mНекорректный тип данных для номеров: \033[0m{numbers}. ')
        if len(numbers) != 6:
            raise IncorrectCarNumbers(f'\033[31mНеверная длина номера: \033[0m"{numbers}". ')
        else:
            return True


first = Car('Model1', 1000000, 'f123dj')
second = Car('Model2', 300, 'т001тр')
third = Car('Model3', 20202020, 'нет номера')
fourth = Car('Model4', 'abcdefg', 123456)
