# Цель: научиться создавать классы наследованные от класса Thread.
#
# Задача "За честь и отвагу!":
# Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
# Атрибут name - имя рыцаря. (str)
# Атрибут power - сила рыцаря. (int)
# А также метод run, в котором рыцарь будет сражаться с врагами:
# При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
# Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
# В процессе сражения количество врагов уменьшается на power текущего рыцаря.
# По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>..., осталось
# <кол-во воинов> воинов."
# После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
# Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.
# Пункты задачи:
# Создайте класс Knight с соответствующими описанию свойствами.
# Создайте и запустите 2 потока на основе класса Knight.
# Выведите на экран строку об окончании битв.


from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power, enemies):
        Thread.__init__(self)
        self.name, self.power, self.enemies = name, power, enemies

    def run(self):
        days_of_battle = 0
        while self.enemies > 0:
            sleep(1)
            days_of_battle += 1
            score = self.enemies - self.power
            # Число оставшихся не может быть отрицательным. Проверяем:
            self.enemies = (score if score >= 0 else 0)
            print(f'\n{self.name} сражается {days_of_battle} дня(дней)..., осталось {self.enemies} враг(а,ов).', end='')
        print(f'\n{self.name} одержал победу спустя {days_of_battle} дней(дня)!', end='')


first_knight = Knight('Sir Lancelot', 11, 100)
second_knight = Knight("Sir Galahad", 23, 100)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('\nВсе битвы закончились!')
