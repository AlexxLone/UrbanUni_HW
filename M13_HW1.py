# Необходимо сделать имитацию соревнований по поднятию шаров Атласа.
# Напишите асинхронную функцию start_strongman(name, power), где name - имя силача, power - его подъёмная мощность.
# Реализуйте следующую логику в функции:
# В начале работы должна выводиться строка - 'Силач <имя силача> начал соревнования.'
# После должна выводиться строка - 'Силач <имя силача> поднял <номер шара>' с задержкой обратно пропорциональной его
# силе power. Для каждого участника количество шаров одинаковое - 5.
# В конце поднятия всех шаров должна выводится строка 'Силач <имя силача> закончил соревнования.'
# Также напишите асинхронную функцию start_tournament, в которой создаются 3 задачи для функций start_strongman.
# Имена(name) и силу(power) для вызовов функции start_strongman можете выбрать самостоятельно.
# После поставьте каждую задачу в ожидание (await).
# Запустите асинхронную функцию start_tournament методом run.

import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял шар {i}.")
    print(f"Силач {name} закончил соревнования.")


async def start_tournament(contestants):
    # решил передать в качестве аргументов на вход словарь с перечнем параметров для запуска отдельных асинхронных
    # функций и столкнулся с проблемой - нехватки знаний из лекций по синтаксису asincio для такого случая.
    # Google  мне в помощь!
    # for name, power in contestants.items():
    #     task = asyncio.create_task(start_strongman(name, power))
    #     await task # тут, собственно, "косяк". Пока не выполнится текущая итерация цикла, другая асинхронная функция не запуститься.
    await asyncio.gather(*[start_strongman(name, power) for name, power in contestants.items()])


contestants = {'Pasha': 3, 'Denis': 4, 'Apollon': 5}
asyncio.run(start_tournament(contestants))
