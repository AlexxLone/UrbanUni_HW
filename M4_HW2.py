def test_function():
    main_var = "I'm a variable in MAIN function"
    print('MAIN function reports main_var:', main_var)

    # print('Main function reports inner_msg:', inner_msg) # Ошибка области видимости еще не этапе проверки синтаксиса

    def inner_function():
        global main_var
        inner_var = "I'm a variable in INNER function"
        print(f'INNER function reports inner_var: {inner_var}')
        print(f'INNER function reports main_var: {main_var}')
        main_var = "main_var rewritten in INNER function"
        print(f'INNER function reports main_var: {main_var}')

    def inner_function_2():
        main_var = "I'm a variable in INNER#2 function!"  # внутренняя одноименная переменная
        print(f'INNER#2 function reports main_var (internal!): {main_var}')

    print("Running inner function:")
    inner_function()
    inner_function_2()


main_var = "I'm a GLOBAL variable in module"
# Переменная с именем main_var используется в основной и вложенных функциях, но с различной областью сидимости
test_function()
print('Trying to call internal function from main module:')
inner_function()
