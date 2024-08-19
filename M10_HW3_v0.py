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
            self.lock.acquire()
            new_balance = self.balance + amount
            if False:  # new_balance > 500:
                print('На счете и так достаточно средств')
            else:
                self.balance = new_balance
                print(f"Пополнение: {amount}. Баланс: {self.balance}.")
            self.lock.release()
            sleep(0.001)

    def taking(self):
        for i in range(100):
            amount = randint(50, 500)
            self.lock.acquire()
            new_balance = self.balance - amount
            if new_balance < 0:
                print(f'Запрос на снятие {amount} отклонён, недостаточно средств на счете: {self.balance}')
            else:
                self.balance = new_balance
                print(f"Снятие: {amount}. Баланс: {self.balance}.")
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
