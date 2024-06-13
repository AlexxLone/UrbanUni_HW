immutable_var = 24, 'May', 2024, True
print('immutable_var = ', immutable_var, 'immutable_var type:', type(immutable_var))
# immutable_var[0] = 25
# ошибка. Нельзя изменять значения элементов кортежа.
# Назначение кортежа - хранение неизменяемой информации.
# Исключение только для вложенных в кортеж коллекий - их структуру и содержимое можно менять.
immutable_list = immutable_var + ([4.0, 'списки'],)
# тут я был готов разбить монитор.
# Как объявить кортеж с одним списком?
# Оказалось все просто - поствить запятую после списка...
print('immutable_list = ', immutable_list, 'immutable_list type:', type(immutable_list))
immutable_list[4][0] = 4.1
immutable_list[4][1] = 'Кортежи'
immutable_list[4].append('Done')
print('immutable_list = ', immutable_list)
