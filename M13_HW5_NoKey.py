from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton(text='Рассчитать')
btn2 = KeyboardButton(text='Информация')
kb.row(btn1, btn2)


# Формула Миффлина-Сан Жеора для подсчета оптимального уровня калорий при различном уровне активности
# В этом ДЗ переместил сюда весь функционал формирования инфо-строки и строки с расчетом.
def MifflinStJeorEq(**data):
    activity_lvl_sf = {'Sedentary': 1.2, 'Lightly active': 1.375, 'Moderately active': 1.55, 'Active': 1.725,
                       'Very active': 1.9}
    try:
        weight = float(data['weight'])
        height = float(data['height'])
        age = int(data['age'])
    except ValueError:
        return "Неверно переданы параметры! Рост, вес и возраст должны быть числами!"

    fm = data['sex'] in {'w', 'W', 'ж', 'Ж'}  # feminine
    msg = (f"Ваш возраст: {age}. Ваш пол: {'female' if fm else 'male'}. Ваш рост: {height}см. \nВаш вес: {weight}кг."
           f" \nРекомендуемый уровень потребляемых калорий: \n")
    msg += f'Activity level -- Resting Metabolic Rate (kcal/day)\n'
    for scale_factor in activity_lvl_sf.keys():
        #  resting metabolic rate (RMR):
        # Females: (10*weight [kg]) + (6.25*height [cm]) – (5*age [years]) – 161
        # Males: (10*weight [kg]) + (6.25*height [cm]) – (5*age [years]) + 5
        rmr = round(
            ((10 * weight + 6.25 * height - 5 * age) + (fm * -161) + (not fm * 5)) * activity_lvl_sf[scale_factor])
        msg += f'\t{scale_factor} -- {rmr}\n'
    return msg


class UserState(StatesGroup):
    sex = State()
    age = State()
    height = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start_msg(msg):
    #  print("Привет! Я бот помогающий твоему здоровью.")
    await msg.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


@dp.message_handler(text=['Рассчитать'])
async def set_age(msg):
    await msg.answer("Введите ваш пол: ('w', 'W', 'ж', 'Ж' - женский, иначе - мужской.)")
    await UserState.sex.set()


@dp.message_handler(state=UserState.sex)
async def set_sex(msg, state):
    await state.update_data(sex=msg.text)
    await msg.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_height(msg, state):
    await state.update_data(age=msg.text)
    await msg.answer("Введите свой рост В САНТИМЕТРАХ:")
    await UserState.height.set()


@dp.message_handler(state=UserState.height)
async def set_weight(msg, state):
    await state.update_data(height=msg.text)
    await msg.answer("Введите свой вес в килограммах:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def ssend_calories(msg, state):
    await state.update_data(weight=msg.text)
    data = await state.get_data()
    await msg.answer(MifflinStJeorEq(**data))
    await state.finish()


@dp.message_handler(text='Информация')
async def all_massages(msg):
    await msg.answer("Расчет количества рекомендуемых калорий по формуле Миффлина-Сан Жеора в доработанном варианте. "
                     "Выдает необходимое количество килокалорий (ккал) в сутки для каждого конкретного человека с "
                     "учетом уровня его активности.")


@dp.message_handler()
async def all_massages(msg):
    #  print("Введите команду /start, чтобы начать общение.")
    await msg.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
