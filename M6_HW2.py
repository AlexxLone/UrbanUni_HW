# Задача "Изменять нельзя получать":
# В этой задаче мы реализуем классы транспорта, в которых нельзя будет просто так поменять цвет, мощность двигателя
# и прочие свойства, т.к. в реальной жизни это чаще всего делается не владельцем, а в специальных сервисах.
# Да, узнать значения этих свойств мы сможем, но вот изменить - нет.
#
# Вам необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это любой транспорт, а Sedan(седан) -
# наследник класса Vehicle.
#
# I. Каждый объект Vehicle должен содержать следующие атрибуты объекта:
# Атрибут owner(str) - владелец транспорта. (владелец может меняться)
# Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
# Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
# Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)
# А так же атрибут класса:
# Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания. (Цвета написать свои)
# Каждый объект Vehicle должен содержать следующий методы:
# Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
# Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
# Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
# Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color;
# а так же владельца в конце в формате "Владелец: <имя>"
# Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в списке
# __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
# Взаимосвязь методов и скрытых атрибутов:
# Методы get_model, get_horsepower, get_color находятся в одном классе с соответствующими им атрибутами:
# __model, __engine_power, __color. Поэтому атрибуты будут доступны для методов.
# Атрибут класса __COLOR_VARIANTS можно получить обращаясь к нему через объект(self).
# Проверка в __COLOR_VARIANTS происходит не учитывая регистр ('BLACK' ~ 'black').
# II. Класс Sedan наследуется от класса Vehicle, а так же содержит следующие атрибуты:
# Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров)


class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, model: str, color: str, power: int):
        # порядок в соответствии с поверочными данными (не совпадает с условиями)
        self.owner = owner
        self.__model = model
        self.__engine_power = power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: {self.owner}')

    def set_color(self, new_color: str):
        for check_color in self.__COLOR_VARIANTS:
            if check_color.lower() == new_color.lower():  # а кто его знает, как будут написаны оба цвета
                self.__color = new_color
                break
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    def __init__(self, owner, model, color, power):
        super().__init__(owner, model, color, power)
        self.__PASSENGERS_LIMIT = 5


# Проверка строго по условию задачи:
# Исходный код:
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
