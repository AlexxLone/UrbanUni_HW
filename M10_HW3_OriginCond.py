import threading
from time import sleep
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            amount = randint(50, 500)
            new_balance = self.balance + amount
            if new_balance > 500 and self.lock.locked():
                self.lock.release()
            self.balance = new_balance
            print(f"Пополнение: {amount}. Баланс: {self.balance}.")
            sleep(0.001)

    def taking(self):
        for i in range(100):
            amount = randint(50, 500)
            new_balance = self.balance - amount
            if new_balance < 0:
                self.lock.acquire()
                print(f'Запрос на снятие {amount} отклонён, недостаточно средств на счете: {self.balance}')
            else:
                self.balance = new_balance
                print(f"Снятие: {amount}. Баланс: {self.balance}.")
            sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.taking, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
