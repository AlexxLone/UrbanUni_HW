# Создайте новый класс House
# Создайте инициализатор для класса House, который будет задавать атрибут этажности self.numberOfFloors = 0
# Создайте метод setNewNumberOfFloors(floors), который будет изменять атрибут numberOfFloors на параметр floors
# и выводить в консоль numberOfFloors
class House:
    def __init__(self, name):
        self.name = name  # в задании не было, но я добавил название стороения
        self.number_of_floors = 0

    # в задании не было, но я добавил:
    def __del__(self):
        print(f'{self.name} Снесен!')

    # такжев задании не было, но я добавил:
    def __len__(self):
        return self.number_of_floors

    def setNewNumberOfFloors(self, floors):
        self.number_of_floors = floors
        print(f'{self.name} Этажей теперь: {self.number_of_floors}')


h1 = House("Красная поляна, 1.")
print(f'{h1.name} Пока имеет этажность: {h1.number_of_floors}')  # обращение к аттрибутам объекта
h1.setNewNumberOfFloors(16)
print(f'{h1.name} Текущая этажность: {len(h1)}')  # 2-й параметр - обращение к специальному методу класса
