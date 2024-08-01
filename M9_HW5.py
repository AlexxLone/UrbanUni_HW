class StepValueError(ValueError):
    pass


class Iterator:
    #  Проверка перед созданием на соответствие шага:
    #  не равен нулю и направление совпадает с направлением указанного диапазона
    def __new__(cls, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        elif (start > stop and step > 0) or (start < stop and step < 0):
            raise StepValueError('Направление счета не соответствует шагу')
        else:
            return super().__new__(cls)

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.stopit = False

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        # введены дополнительные проверки, дабы указатель не вышел за диапазон и для выдачи крайнего значения
        if self.stopit:
            raise StopIteration
        else:
            next_ = self.pointer + self.step
            if (self.step > 0 and (next_ <= self.stop)) or (self.step < 0 and (next_ >= self.stop)):
                pointer = self.pointer
                self.pointer = next_
                return pointer
            else:
                self.stopit = True
                return self.pointer


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
    print()
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()

# в 5-м примере ввел проверку на соответствие направления шага указанному диапазону
try:
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=' ')
    print()
except StepValueError:
    print('Направление шага не соответствует диапазону')
