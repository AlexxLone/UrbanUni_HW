# Создайте новый класс Building
# Создайте инициализатор для класса Building, который будет задавать целочисленный атрибут этажности
# self.numberOfFloors и строковый атрибут self.buildingType
# Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
# Полученный код напишите в ответ к домашнему заданию

class Building:
    def __init__(self, name):
        self.name = name  # в задании не было, но я добавил название стороения
        self.numberOfFloors = 0
        self.buildingType = ''

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


# функция сравнения 2-х объектов и форматированного вывода результата в консоль
def b_comparation(first, second):
    c_res = first == second
    print(f'Строение \033[34m{first.name}\033[0m эквивалентно \033[34m{second.name}\033[0m: \033{"[32m" if c_res else "[31m"}{c_res}\033[0m')


h1 = Building('ЖК "Парус", д1')
h1.numberOfFloors = 24
h1.buildingType = "многоквартирный жилой дом"

h2 = Building('ЖК "Парус", д2')
h2.numberOfFloors = 24
h2.buildingType = "многоквартирный жилой дом"

h3 = Building('ЖК "Парус", д3')
h3.numberOfFloors = 4
h3.buildingType = "школа"

h4 = Building('ЖК "Парус", д4')
h4.numberOfFloors = 4
h4.buildingType = "торговый центр"

b_comparation(h1, h2)
b_comparation(h3, h4)
b_comparation(h2, h3)
