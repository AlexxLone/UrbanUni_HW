# Цель: Применить очереди в работе с потоками, используя класс Queue.
#
# Задача "Потоки гостей в кафе":
# Необходимо имитировать ситуацию с посещением гостями кафе.
# Создайте 3 класса: Table, Guest и Cafe.
# Класс Table:
# Объекты этого класса должны создаваться следующим способом - Table(1)
# Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)
# Класс Guest:
# Должен наследоваться от класса Thread (быть потоком).
# Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
# Обладать атрибутом name - имя гостя.
# Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.
# Класс Cafe:
# Объекты этого класса должны создаваться следующим способом - Guest(Table(1), Table(2),....)
# Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
# Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
# Метод guest_arrival(self, *guests):
# Должен принимать неограниченное кол-во гостей (объектов класса Guest).
# Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest), запускать поток гостя и выводить
# на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
# Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue и выводить сообщение
# "<имя гостя> в очереди".
# Метод discuss_guests(self):
# Этот метод имитирует процесс обслуживания гостей.
# Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
# Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive),
# то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен".
# Так же текущий стол освобождается (table.guest = None).
# Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу присваивается
# гость взятый из очереди (queue.get()). Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди
# и сел(-а) за стол номер <номер стола>"
# Далее запустить поток этого гостя (start)
# Таким образом мы получаем 3 класса на основе которых имитируется работа кафе:
# Table - стол, хранит информацию о находящемся за ним гостем (Guest).
# Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
# Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival)
# и их обслуживания (discuss_guests).

from threading import Thread
import queue
from time import sleep
from random import randint


class Table:
    def __init__(self, number):
        self.number, self.guest = number, None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, tables_):
        self.tables = tables_
        self.awaiting_guests = queue.Queue()

    def available_tables(self):
        return {t for t in self.tables if t.guest is None}

    def guest_arrival(self, guests_):
        # Рассаживание гостей за столы. Здесь очередь гостей представляется в привычном для человеческого понимания
        # очереди: первый в списке - первый в очереди (first in, first out)
        for table in self.available_tables():
            if len(guests_) != 0:
                print(f'{guests_[0].name} сел(а) за стол №{table.number}')
                table.guest = guests_.pop(0)
                table.guest.start()
            else:
                break
        # далее помещаем в очередь оставшихся гостей:
        for guest_ in guests_:
            self.awaiting_guests.put(guest_)
            print(f'{guest_.name} в очереди')

    # дабы далее не вызывать при каждой необходимости циклическую функцию проверки столов в основном цикле serve_guests,
    # учитываю текущее состояние столов как 2-а множества available_tables | occupied_tables = self.tables
    def serve_guests(self):
        available_tables = self.available_tables()  # свободные столы
        occupied_tables = self.tables - available_tables  # занятые столы
        while True:
            released_tables = set()  # освободившиеся (в процессе) столы
            taken_table = set() # занимаемые (в процессе) столы
            if self.awaiting_guests.empty() and len(occupied_tables) == 0:
                print('Посетителей больше нет. Обслуживание завершено.')
                break
            for tb in occupied_tables:  # проверяем занятые столы на наличие посетителя
                if not (tb.guest.is_alive()):
                    print(f'Гость {tb.guest.name} покушал(а) и ушел(ушла).')
                    tb.guest = None
                    print(f'Стол №{tb.number} свободен')
                    available_tables.add(tb)
                    released_tables.add(tb)
            occupied_tables -= released_tables
            for tb in available_tables:  # проверяем свободные столы
                if not (self.awaiting_guests.empty()):  # распределяем посетителей из очереди за свободные столы
                    tb.guest = self.awaiting_guests.get()
                    tb.guest.start()
                    print(f"{tb.guest.name} вышел(-ла) из очереди и сел(-а) за стол №{tb.number}")
                    occupied_tables.add(tb)
                    taken_table.add(tb)
                else:
                    break
            available_tables -= taken_table


# Проверочный код по условию задачи:
tables = {Table(number) for number in range(1, 6)}
cafe = Cafe(tables)
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel',
                'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe.guest_arrival(guests)
cafe.serve_guests()
