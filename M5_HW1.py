# Реализуйте класс House, объекты которого будут создаваться следующим образом:
# House('ЖК Эльбрус', 30)
# Объект этого класса должен обладать следующими атрибутами:
# self.name - имя, self.number_of_floors - кол-во этажей
# Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
# Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
# Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".
class House:
    _reg = []
    # мне захотелось в цикле вывести все экземпляры класса (ниже, в основном теле модуля), но экземпляры класса
    # не являются итерируемыми объектами, поэтому ввел в класс список указателей,
    # заполняемый указателем экземпляра на самого себя для каждого экземпляра
    # (извините за тавтологию. принцип подсмотрел в интернете)
    def __init__(self, name, number_of_floors):
        self._reg.append(self)
        self.name = name
        self.number_of_floors = number_of_floors

    # учитывая неудачные попытки использования пакета termcolor в практике по 4-му модулю
    # захотелось найти альтернативный простой вариант раскраски текста
    # самый простой вариант - коды ASCII (на Win10 сработало):
    # плюс попрактиковлся в форматировании вывода
    def go_to(self, new_floor):
        if new_floor in range(1, self.number_of_floors + 1):
            for i in range(1, new_floor + 1):
                print(f'\033[1m\033[33m\033[40m->{i}\033[0m', end='')
            print()  # перевод строки.
        else:
            print("\033[1m\033[4m\033[30m\033[41m{}\033[0m".format("Такого этажа не существует в этом здании."))


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

for item in House._reg:  # pycharm ругается, но код отрабатывает.
    print(f'\033[34mЗдание: {item.name}, этажность: {item.number_of_floors}\033[0m')

h1.go_to(5)
h2.go_to(10)
