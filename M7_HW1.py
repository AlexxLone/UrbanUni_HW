# Цель: закрепить знания о работе с файлами (чтение/запись) решив задачу.
# Задача "Учёт товаров":
# Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
# Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables')
# и обладать следующими свойствами:
# Атрибут name - название продукта (строка).
# Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
# Атрибут category - категория товара (строка).
# Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
# Все данные в строке разделены запятой с пробелами.
# Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
# Инкапсулированный атрибут __file_name = 'products.txt'.
# Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его
# и возвращает единую строку со всеми товарами из файла __file_name.
# Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
# Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
# Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'.


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}.\n'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        ret = file.read()
        file.close()
        return ret

    def add(self, *products):
        # преобразуем файл с имеющимся ассортиментом магазина в список:
        __assortment_list = list((Shop.get_products(self)).split('\n'))
        # Из полученного списка извлечем только названия для дальнейшей проверки.
        # Результат поместим в новый список "наименование ассортимента в наличии":
        __assortment_names = list()
        for item in __assortment_list:
            __assortment_names.append(list(item.split(','))[0])
        # проверка наличия переданного продукта (по названию); добавление, если еще нет:
        file = open(self.__file_name, 'a')
        for product in products:
            if product.name in __assortment_names:
                print(f'Продукт {product.name} уже есть в ассортименте данного магазина!')
            else:
                # добавляем продукт в файл и список для дальнейшей проверки
                __assortment_names.append(product.name)
                file.write(product.__str__())
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
