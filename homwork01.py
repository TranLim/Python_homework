# Задание 1. Встроенные типы данных, операторы, функции и генераторы
#
# Напишите реализации объявленных ниже функций. Для проверки
# корректности реализации ваших функций, запустите тесты:
#
# pytest test_homework01.py
#
# Если написанный вами код не содержит синтаксических ошибок,
# вы увидите результаты тестов ваших решений.


def fac(n):
    suma = 1
    while n >= 1:
        suma = suma * n
        n = n - 1
    return suma

    # if n == 1:
    #     return n
    # else:
    #     return n * fac(n - 1)
    # """
    # Факториал
    #
    # Факториал числа N - произведение всех целых чисел от 1 до N
    # включительно. Например, факториал числа 5 - произведение
    # чисел 1, 2, 3, 4, 5.
    #
    # Функция должна вернуть факториал аргумента, числа n.
    # """



def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    # """
    # Наибольший общий делитель (НОД) для двух целых чисел.
    #
    # Предполагаем, что оба аргумента - положительные числа
    # Один из самых простых способов вычесления НОД - метод Эвклида,
    # согласно которому
    #
    # 1. НОД(a, 0) = a
    # 2. НОД(a, b) = НОД(b, a mod b)
    #
    # (mod - операция взятия остатка от деления, в python - оператор '%')
    # """


def fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a
    # """
    # Генератор для ряда Фибоначчи
    #
    # Вам необходимо сгенерировать бесконечный ряд чисел Фибоначчи,
    # в котором каждый последующий элемент ряда является суммой двух
    # предыдущих. Начало последовательности: 1, 1, 2, 3, 5, 8, 13, ..
    #
    # Подсказка по реализации: для бесконечного цикла используйте идиому
    #
    # while True:
    #   ..
    #
    # """


def flatten(seq):
    # """
    # Функция, преобразующая вложенные последовательности любого уровня
    # вложенности в плоские, одноуровневые.
    #
    # >>> flatten([])
    # []
    # >>> flatten([1, 2])
    # [1, 2]
    # >>> flatten([1, [2, [3]]])
    # [1, 2, 3]
    # >>> flatten([(1, 2), (3, 4)])
    # [1, 2, 3, 4]
    # """
    num = []
    for x in seq:
        if type(x) != list and type(x) != tuple:
            num.append(x)
        else:
            num.extend(flatten(x))
    return num
