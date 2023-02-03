import time

# Ошибки
ERROR_NULL_DIVISION = 'На ноль делить нельзя'
ERROR_NUMBER = 'Это не число'
ERROR_OPERATION = 'Нет такой операции'
ERROR_REPEAT = "Напишита 'Да' или 'Нет'"

# Выбор 1-го числа


def choise_x():
    """Выбор первого числа"""
    while True:
        x = str(input('\nВведите 1-ое число: '))
        try:
            return float(x)
        except:
            get_error(ERROR_NUMBER)

# Выбор операции


def choise_operation():
    """Выбор операции"""
    while True:
        operation = str(input('\nВыберите операцию (+, -, *, /): '))

        if operation != '+' and operation != '-' and operation != '*' and operation != '/':
            get_error(ERROR_OPERATION)
        else:
            return operation

# Выбор 2-го числа


def choise_y():
    """Выбор второго числа"""
    while True:
        y = str(input('\nВведите 2-ое число: '))
        try:
            float(y)
            return float(y)
        except:
            get_error(ERROR_NUMBER)


# Сложение


def operation_addition(x, y):
    '''
    Возвращает произведение двух чисел. После проверки в функции check_result.
        Параметры:
            x (float): первое десятичное число
            y (float): второе десятичное число
        Возвращаемое значение:
            check_result(result) (int | float): преобразованное в int, если десятичная часть равна нулю
    '''
    result = x + y
    get_result(check_result(result))

# Вычитание


def operation_subtraction(x, y):
    '''
    Возвращает разницу двух чисел. После проверки в функции check_result.
        Параметры:
            x (float): первое десятичное число
            y (float): второе десятичное число
        Возвращаемое значение:
            check_result(result) (int | float): преобразованное в int, если десятичная часть равна нулю
    '''
    result = x - y
    get_result(check_result(result))

# Умножение


def operation_multiplication(x, y):
    result = x * y
    get_result(check_result(result))

# Деление


def operation_division(x, y):
    try:
        result = x / y
        get_result(check_result(result))
    except ZeroDivisionError:
        get_error(ERROR_NULL_DIVISION)

# Проверка результата на тип int or float


def check_result(result):
    if result - int(result) == 0:
        return int(result)
    else:
        return float(result)

# Вывод результата


def get_result(num):
    first_num = check_result(x)
    second_num = check_result(y)
    expression = str(first_num) + ' ' + str(operation) + ' ' + str(second_num)
    print('\n' + '+-----------+' + '-' *
          (LEN_TITLE * 2 + (len(TITLE))-12) + '+')
    print('| Выражение | ' + str(expression) + ' ' *
          ((LEN_TITLE * 2)-len(str(expression))-2) + '|')
    print('+-----------+' + '-' *
          (LEN_TITLE * 2 + (len(TITLE))-12) + '+')
    print('| Результат | ' + str(num) + ' ' *
          ((LEN_TITLE * 2)-len(str(num))-2) + '|')
    print('+-----------+' + '-' * (LEN_TITLE * 2 + (len(TITLE))-12) + '+')

# Проверка повторного запуска


def check_repeat():
    while True:
        repeat = str(input('\nЖелаете еще?\n(Да/Нет): '))
        repeat = repeat.replace(" ", "")
        repeat = repeat.lower()

        if repeat == 'нет' or repeat == 'н':
            return False
        elif repeat == 'да' or repeat == 'д':
            return True
        else:
            get_error(ERROR_REPEAT)

# Вывод ошибки


def get_error(error):
    print('\n' +
          '+--------+' + '-' * (LEN_TITLE * 2 + (len(TITLE))-9) + '+')
    print('| Ошибка | ' + error + ' ' *
          (LEN_TITLE * 2 + (len(TITLE)) - (len(error)) - 10) + '|')
    print('+--------+' + '-' * (LEN_TITLE * 2 + (len(TITLE))-9) + '+')


# Закрытие программы

def exit():

    expression = ' Программа закроется через 5 секунд'
    print('\n' + '+' + '-' * (LEN_TITLE * 2 + (len(TITLE))) + '+')

    print('|' + expression + ' ' *
          ((LEN_TITLE * 2)-len(str(expression))+12) + '|')

    print('+' + '-' * (LEN_TITLE * 2 + (len(TITLE))) + '+')
    print('|', end='', flush=True)
    for i in range(5, -1, -1):
        print(' ', end='', flush=True)
        print(i, end='', flush=True)
        print(' ', end='', flush=True)
        if not i == 0:
            for i in range(0, 8):
                print('=', end='', flush=True)
                time.sleep(1/9)
    print('|', end='', flush=True)
    print('\n' + '+' + '-' * (LEN_TITLE * 2 + (len(TITLE))) + '+')
    time.sleep(2)


# Заголовок и длина строки заголовка
TITLE = 'КАЛЬКУЛЯТОР '
LEN_TITLE = 23

# Вывод главного заголовка
print('\n' + '+' + '-' * (LEN_TITLE * 2 + (len(TITLE))) + '+')
print('|' + (LEN_TITLE * ' ') + TITLE + (' ' * LEN_TITLE) + '|')
print('+' + '-' * (LEN_TITLE * 2 + (len(TITLE))) + '+')

# Главный цикл
while True:
    # 1-ое число
    x = choise_x()
    # Операция
    operation = choise_operation()
    # 2-ое число
    y = choise_y()

    # Вызов операции
    if operation == '+':
        operation_addition(x, y)
    elif operation == '-':
        operation_subtraction(x, y)
    elif operation == '*':
        operation_multiplication(x, y)
    elif operation == '/':
        operation_division(x, y)

    # Проверка на повторный запуск
    again = check_repeat()
    if not again:
        exit()
        break
