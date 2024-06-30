# Задача "История строительства":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
# Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно образаться
# к атрибутам класса используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
# Название объекта добавлялось в список cls. houses_history.
# Название строения можно взять из args по индексу.
# Также переопределите метод __del__(self) в котором будет выводится строка:
# "<название> снесён, но он останется в истории"
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.

class Building:
    _reg = []  # список указателей. использую для обхода экземпляров класса в цикле
    houses_history = []  # исторический журнал по ДЗ
    # перечень основных параметров строения:
    # "ЖК"/квартал/микрорайон, номер дома (может быть с литерой), номер строения, этажность, назначение
    b_main_param_key = ["community", 'house_number', 'building_number', 'storeys', 'function']

    def __new__(cls, *args, **kwargs):
        # формируем строку основных параметров для записи в исторический журнал
        # ("ЖК"/квартал/микрорайон, номер дома, номер строения).
        # Передаваямая запись может содержать только 2-а первых параметра.
        # Пришлось ввести доп. проверки на наличие строения, как такового, и на его наличие в адресе.
        if len(args) < 3:  # если поступила упрощенная форма записи, только квартал и номер дома
            cls.houses_history.append(f'{args[0]}, дом №{args[1]}.')
        else:
            cls.houses_history.append(
                f'{args[0]}, дом №{args[1]}{f", строение {args[2]}." if args[2] is not None else "."}')
        # obj = object.__new__(cls)  # так в ДЗ. прямое обращение к ролительскому базовому классу obj
        obj = super().__new__(cls)  # так было в лекции. обращение к прокси-объекту. более верный вариант
        cls._reg.append(obj)
        return obj

    def __init__(self, *args, **kwargs):
        # ввод основных и дополнительных параметров строения в экземпляр класса:
        #  temp_dict = dict(zip(Building.b_main_param_key, args))
        #  temp_dict.update(kwargs)
        temp_dict = {**dict(zip(Building.b_main_param_key, args)), **kwargs}  # синтаксис 3.5.
        for key, values in temp_dict.items():
            setattr(self, key, values)

    def __del__(self):
        numb = Building._reg.index(self) # получаем индекс удаляемого объекта (они совпадают в _reg и houses_history)
        record = f'{Building.houses_history[numb]} Снесен. Но навсегда останется в нашей памяти!'
        print(record)
        Building.houses_history.append(record)
        Building._reg.remove(self) # удаляем ссылку в списке указателей


    def _print_all(cls):
        # вывод полного перечня созданых объектов класса и его аттрибутов:
        for instance in cls._reg:
            print(f'\n\033[31m{instance}:')
            # print(f'\n\033[31m{instance.__mro__}:\033[34m')
            for key, value in vars(instance).items():
                print(f'\t\033[34m{key}: \033[39m{value}')
        print('\033[0m')

# функция сравнения 2-х объектов и форматированного вывода результата в консоль
# def b_comparation(first, second):
#     c_res = first == second
#     equal_str = f'\033[32m эквивалентно \033[0m'
#     not_equal_str = f'\033[31m не эквивалентно \033[0m'
#     print(f'Строение \033[34m{first.name}\033[0m {equal_str if c_res else not_equal_str} \033[34m{second.name}\033[0m:')
#     # print(f'Строение \033[34m{first.name}\033[0m эквивалентно \033[34m{second.name}\033[0m: \033{"[32m" if c_res else "[31m"}{c_res}\033[0m')

# скучное наполнение параметрами для проверки:
# сначала по условиям ДЗ:
# h1 = Building('ЖК Эльбрус', 10)
# print(Building.houses_history)
# print(vars(h1))
# # print(dir(h1))
# h2 = Building('ЖК Акация', 20)
# print(Building.houses_history)
# h3 = Building('ЖК Матрёшки', 20)
# print(Building.houses_history)

# далее - наполнение данными для проверки передачи *args b **kwargs
# формат основных параметров строения: "ЖК", номер дома (может быть с литерой), номер строения, этажность, назначение
h1_param = ('ЖК "Парус"', "1", None, 24, "многоквартирный жилой дом")
# формат дополнительных параметров произволен
h1_add_param = {"подъездов": 5, "квартир": 460, "пассажирских лифтов на подьезд": 2, "грузовых лифтов на подьезд": 1}

h2_param = ('ЖК "Адмирал"', "2a", 1, 16, "многоквартирный жилой дом")
h2_add_param = {"подъездов": 2, "квартир": 64, "пассажирских лифтов на подьезд": 2, "грузовых лифтов на подьезд": 2,
                "спорт-залов": 2, "бассейнов": 1, "назначение верхнего этажа": "открытая веранда"}

h1 = Building(*h1_param, **h1_add_param)
print(Building.houses_history)
print(Building.__mro__)

h2 = Building(*h2_param, **h2_add_param)
print(Building.houses_history)

Building._print_all(Building)
input()
# h2 = Building('ЖК "Парус", д2')
# h2.numberOfFloors = 24
# h2.buildingType = "многоквартирный жилой дом"
#
# h3 = Building('ЖК "Парус", д3')
# h3.numberOfFloors = 4
# h3.buildingType = "школа"
#
# h4 = Building('ЖК "Парус", д4')
# h4.numberOfFloors = 4
# h4.buildingType = "торговый центр"
#
# h5 = Building('ЖК "Южный", д20')
# h5.numberOfFloors = 4
# h5.buildingType = "торговый центр"
