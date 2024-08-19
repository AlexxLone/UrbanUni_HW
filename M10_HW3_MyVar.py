import threading
from time import sleep
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.cond500 = threading.Condition(self.lock)

    def deposit(self):
        for i in range(100):
            amount = randint(50, 500)
            self.lock.acquire()
            new_balance = self.balance + amount
            if new_balance >= 500 and self.lock.locked():
                self.cond500.notify()
            self.balance = new_balance
            print(f"Пополнение №{i}: {amount}. Баланс: {self.balance}.")
            self.lock.release()
            sleep(0.001)

    def taking(self):
        for i in range(100):
            amount = randint(50, 500)
            self.lock.acquire()
            new_balance = self.balance - amount
            if new_balance < 0:
                print(f'Запрос №{i} на снятие {amount} отклонён, недостаточно средств на счете: {self.balance}')
                print('Для разблокировки счета Вам необходимо пополнить баланс до минимум 500')
                # проверка на существование потока необходима, поскольку если поток пополнения уже завершен
                # вызов wait приведет к зависанию
                # можно указать таймаут для такого случая (не знаю, что лучше)
                if th1.is_alive():
                    self.cond500.wait()
            else:
                self.balance = new_balance
                print(f"Снятие №{i}: {amount}. Баланс: {self.balance}.")
            self.lock.release()
            sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.taking, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
