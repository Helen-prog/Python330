# name = "User"
# print("Hello,", name)
# age = 20
# print(age)
# print(type(age))
# age = "hello"
# print(age)
# print(type(age))


# a = 4
# print("a =", id(a))
# b = 5
# print("b =", id(b))
# a = b
# print(a)
# print("a =", id(a))

# a = b = c = 1
# print(a, b, c)

# a, b, c = 5, "hello", 9.21
# print(a, b, c)

# PI = 3.14
# print(PI)

# name = "Игорь"
# age = 36
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")

# a = 5
# b = 7
# print("a:", a)
# print("b:", b)
# temp = a
# a = b
# b = temp
# print("a:", a)
# print("b:", b)

# print("\tстрока \nсим \"вол\" ов")
# print("C:\\\\folder\\file.\rtxt")

# print(6 / 2)
# print(6 // 2)

# Функции явного преобразования типов
# int
# str
# float


# s1 = "2"
# s2 = 5
# print(int(s1) + s2)
# print(s1 + str(s2))

# print(564563463546544654465446544654465446534654)
# print(type(5.64563463546544654465446544654465446534654))

# a = 5
# b = 7
# c = 3
# a, b, c = 5, 7, 3
# summ = a + b + c
# pr = a * b * c
# sr = summ / 3
# print('сумма: ', summ, '\nпроизведение: ', pr, '\nсреднее: ', sr)

# a, b, c = 5, 7, 3
# summ = a + b + c
# print('сумма: ', summ, '\nпроизведение: ', a * b * c, '\nсреднее: ', summ / 3)

# number = 6 + 4 * 5 ** 2 + 7
# #              2   1
# print(number)
# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# num = 10
# num += 5  # num = num + 5
# print(num)  # 15
#
# num -= 3  # num = num - 3
# print(num)  # 12

# num = 9753  # 43
# print("Исходное число:", num)
# a = num % 10
# print("a:", a)
# num = num // 10
# # print(num)
# b = num % 10
# print("b:", b)
# num = num // 10
# # print(num)
# c = num % 10
# print("c:", c)
# num = num // 10
# # print(num)
# d = num % 10
# print("d:", d)
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# print("Исходное число:", num)
# res = num % 10 * 1000  # 1000
# num = num // 10
# res += num % 10 * 100  # 200
# num = num // 10
# res += num % 10 * 10  # 30
# num = num // 10
# res += num % 10  # 4
# print(res)

# print(int(3.4789456))
# print(round(3.4789556, 4))

# a = '5.2'
# b = 10
# print(float(a) + b)

# print(float('5.2'))

# a = 1
# b = 2
# print("a:", a, "\nb:", b)

# name = "Виктор"
# age = 21
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут ", name, ". Мне ", age, " лет.", end="\n\n", sep="")
# print("Привет")

# name = input("Введите " + "имя: ")
# print(name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print(type(num))
# print(type(power))
# print(res)

# b1 = True  # 1
# b2 = False  # 0
# print(b1 + 5)
# print(b2 + 5)


# print(bool("python"))
# print(bool(""))  # False
# print(bool(" "))
# print(bool(-0.2))
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(None))  # False

# test = None
# print(test)
# test = 5
# print(test)

# print(2 + 5 == 7 + 3)

# print(2 < 4 < 9)  # True True
# print(2 * 5 > 7 >= 4 + 3)  # True True
# print(3 * 3 <= 7 >= 2)

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10, 5, False


# print(5 - 3 == 2 and 1 + 3 == 4)  # True and True   -> True
# print(5 - 3 == 3 and 1 + 3 == 4)  # False and True  -> False
# print(5 - 3 == 2 and 1 + 3 == 5)  # True and False  -> False
# print(5 - 3 == 3 and 1 + 3 == 5)  # False and False  -> False

# print(5 - 3 == 2 or 1 + 3 == 4)  # True or True   -> True
# print(5 - 3 == 3 or 1 + 3 == 4)  # False or True  -> True
# print(5 - 3 == 2 or 1 + 3 == 5)  # True or False  -> True
# print(5 - 3 == 3 or 1 + 3 == 5)  # False or False  -> False

# print(not 9 - 5)  # not True => False
# print(not 9 - 9)  # not False => True

# cnt = 5
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 35
# b = 25
# # if a > b:
# #     print("a > b")
# # elif a < b:
# #     print("b > a")
# # else:
# #     print("a == b")
# if a > b:
#     print("a > b")
# if a < b:
#     print("b > a")
# if a == b:
#     print("a == b")

# a = int(input("Введите первую сторону: "))
# b = int(input("Введите вторую сторону: "))
# c = int(input("Введите третью сторону: "))
#
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or b == c or a == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели цифрой: "))  # 3
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день -", end=" ")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день -", end=" ")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")
#
# num = int(input("Введите номер месяца: "))
# if 1 <= num <= 12:
#     if num == 1 or num == 2 or num == 12:
#         print("Зима")
#     if 3 <= num <= 5:
#         print("Весна")
#     if 6 <= num <= 8:
#         print("Лето")
#     if 9 <= num <= 11:
#         print("Осень")
# else:
#     print("Неверный номер")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", n, end=" ")
#     if n == 1:
#         print("ворона")
#     elif 2 <= n <= 4:
#         print("вороны")
#     else:
#         print("ворон")
# else:
#     print("Ошибка ввода данных")


# day = 'понедельник'
# time = 16
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")

# a, b = 30, 20
# minim = a if a < b else b
# print(minim)

# a, b = 40, 50
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a, b = 20, 0
# print("На ноль делить нельзя" if b == 0 else a / b)

# a = int(input("Введите число от 1 до 99: "))
# kop = a
# if 1 <= a <= 99:
#     if 11 <= kop <= 14:
#         print(a, "копеек")
#     else:
#         kop = kop % 10
#         if kop == 1:
#             print(a, "копейка")
#         elif 2 <= kop <= 4:
#             print(a, "копейки")
#         else:
#             print(a, "копеек")
# else:
#     print("Некорректное значение")


# a = 5
# b = 0
# print(a / b)

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:  # попытаться
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):  # исключение
#     print("Нельзя вводить строки или нельзя делить на ноль")
# else:  # когда в блоке try не возникло исключения
#     print("Все нормально. Вы ввели", n, "и", m)
# finally:  # выполнится в любом случае
#     print("Конец программы")

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
#
# try:
#     n = int(n)  # 8
#     m = int(m)  # 'l'
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)  # '8' + 'l'


# Циклы

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1  # i = i + 1

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1  # i = i - 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# i = 1
# while i <= 10:
#     b = i * 2
#     print(b)
#     i += 1

# i = 2
# while i <= 20:
#     print("i =", i)
#     i += 2

# n = int(input("Укажите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Укажите количество символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1

# a = int(input("введите число: "))
# print('*' * a)

# a = int(input("Введите начало диапазона: "))  # 1
# b = int(input("Введите конец диапазона: "))  # 5
# res = 0
# while a <= b:
#     if a % 2 != 0:
#         res += a  # res = res + a => res = 0 + 1
#     a += 1
# print(res)

# n = input("Введите число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите число: ")
#
#
# if n % 2 == 0:
#     print("Четное число")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# res = 1
# while True:
#     numb = int(input('Введите число: '))
#     if numb == 0:
#         print("Результат:", res)
#         break
#     res *= numb


# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i, end=" ")
#     i += 1
# else:
#     print("\nЦикл окончен, i =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# for element in collection:
#     print(element)

# for i in 'Hello':
#     print(i)

# for color in 'red', 'blue', 'green', 20:
# print(color)

# print(range(8))
# range(start, stop, step)
#        0,    8,     1

# for i in range(9, -1, -1):  # for(let i=2; i<8; i++)
#     print(i, end=" ")
#
# print()
# j = 9
# while j >= 0:
#     print(j, end=" ")
#     j -= 1

# for i in range(10, 100):
#     if i % 10 == i // 10:  # 12  77
#         print(i, end=" ")

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")


# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done')


# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("\t--")
#         for k in range(2):
#             print("\t\t***")

# a = int(input('Ширина: '))
# b = int(input('Высота: '))
# for i in range(b):
#     for j in range(a):
#         if i == 0 or i == b - 1 or j == 0 or j == a - 1:
#             print('*', end="")
#         else:
#             print(' ', end="")
#     print()

# a = int(input('Ширина'))
# b = int(input('Высота'))
# for i in range(b):
#     if i == 0 or i == b - 1:
#         print('*' * a)
#     else:
#         print('*' + (' ' * (a - 2)) + '*')

# a = [b * 2 for b in "Banana"]
# print(a)
#
# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Список (list)
# nums = [8, 3, 9, 4, 1]
# #       0  1  2  3  4
# #      -5 -4 -3 -2 -1
# # print(nums)
# # print(type(nums))
# # # print(nums[0])
# # # print(nums[-1])
# # nums[3] = 255
# # nums[1] += 100
# print(nums)
# print(len(nums))

# s = []
# print(s)
# print(type(s))
#
# s1 = list("Hello")
# print(s1)
# print(type(s1))

# n = list(range(10, 2, -2))
# print(n)

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]  # [0 0 0 0 0]
# print(a)
#
# d = [v * 3 for v in "list"]
# print(d)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [input("-> ") for i in range(int(input("n = ")))]
# print(a)

# a = [4, 8, 9, 5, 3]
# for i in range(len(a)):  # 0 1 2 3 4
#     print(a[i], end=" ")  # 4 8 9 5 3
# print()
# for i in a:  # 4 8 9 5 3
#     print(i, end=" ")


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# res = 0
# a = [int(input('-->')) for i in range(int(input('Количество чисел ')))]
# for i in range(len(a)):
#     if a[i] < 0:
#         res += a[i]
# print(res)

# n = list(range(21, 41))
# print(n)
# count = 0
# nechet = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         count += 1
#     else:
#         nechet += n[i]
# print(count, nechet)

# a = [7, 9, 2, 1, 17]
# a[0], a[1] = a[1], a[0]
# print(a)

# Срезы

# s = [5, 9, 3, 7, 1, 8]
# # список[start:stop:step]
# print(s[1:4])
# print(s[2:])
# print(s[:2])
# print(s[::2])
# print(s[::-1])
# print(s[5:1:-1])
#
# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[6:])
# print(s[3:4])
# print(s[4:8])
# print(s[-3:1:-1])
# print(s[2:5])

# s = list(range(1, 8))
# print(s)
# s[1:3] = [0, 0, 0, 0]
# # s[1] = [0, 0, 0, 0]
# s[1:2] = [20]
# s[15:20] = [30]
# print(s)

# Методы списков
# s = [1, 20, 0, 0, 0, 4, 5, 6, 7, 30]
# print(s)
# s.append(99)  # добавляет один элемент в конец списка
# print(s)
# s.extend([5, 4, 3])  # добавляет список элементов в конец списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(0, 100)  # добавляет элемент (второй параметр) списка в заданный индекс (первый параметр)
# print(s)
#
# s.insert(-1, 200)
# print(s)

# res = 0
# count = 0
# a = [int(input('-->')) for i in range(int(input('Количество элементов: ')))]
# for i in range(len(a)):
#     res += a[i]
#     if a[i] != 0:
#         count += 1
# print(res / count)

# size = 5  # int(input("Введите размер поля: "))
# symbol = 3  # int(input("Введите количество символов: "))

# pool = int(input('Введите размер поля: '))
# sim = int(input('Введите количество символов: '))
#
# for i in range(pool):
#     for h in range(sim):
#         for j in range(pool):
#             for k in range(sim):
#                 if (i + j) % 2 == 0:
#                     print('* ', end='')
#                 else:
#                     print('  ', end='')
#         print()

# s = []
# n = int(input("n = "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)
#
# print(s)

# s = []
# n = int(input("n = "))
# for num in range(n):
#     x = int(input("Ведите число: "))
#     if x % 3 == 0:
#         s.insert(0, x)
# print(s)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "не делится на 3 без остатка")
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             break
#         if i == j:
#             c.append(i)
#             break
# print(c)


# a = [1, 2, 3, 4, 5]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):
#     a, b = b, a
#
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
#
# # if len(b) > len(a):
# #     for i in range(len(a)):
# #         c.append(a[i])
# #         c.append(b[i])
# #     for i in range(len(a), len(b)):
# #         c.append(b[i])
# # else:
# #     for i in range(len(b)):
# #         c.append(a[i])
# #         c.append(b[i])
# #     for i in range(len(b), len(a)):
# #         c.append(a[i])
# print(c)

# s = [11, 3, 1, 22, 2, 33, 3, 4, 5]
# # s[3:5] = []
# # del s[:]
# print(s)
# n = 11
# if n in s:
#     s.remove(n)  # удалит элемент из списка по значению
# last = s.pop(-3)  # удаляет элемент по индексу заданному в круглых скобках, ели индекс не передан, то последний
# # элемент из списка
# print(last)
# s.clear()  # очищает список
# print(s)

# a = [int(input('->')) for i in range(int(input('n = ')))]
# k = int(input('Введите индекс для удаления:'))
# a.pop(k)
# print(a)

# s = [11, 3, 1, 22, 3, 2, 33, 3, 4, 5]
# # num = s.count(23)  # подсчет количества заданных значений в списке
# # print(num)
# print(s)
# ind = s.index(3, 5)  # возвращает индекс первого элемента, можно передать параметры start и stop
# print(ind)

# s = [11, 3, 1]
# b = s.copy()
# print("s =", s)
# print("b =", b)
# b.append(120)
# s.append(30)
# print("s =", s)
# print("b =", b)

# s = [11, 3, 1, 22, 3, 2, 33, 3, 4, 5]
# # s.reverse()  # перестраивает элементы в обратном порядке
# # s.sort(reverse=True)  # сортировка по возрастанию, reverse=True - по убыванию
# # print(s)
# n = sorted(s, reverse=True)
# print(s)
# print(n)

# s = ['Виталий', 'Сергей', 'Александр', 'Анна']
# s.sort(key=len, reverse=True)
# print(s)

# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(1, 9))
# print(random.randrange(2, 9, 2))

# from random import randint, randrange
#
# print(randint(1, 9))
# print(randrange(2, 9, 2))

# from random import *
#
# print(randint(1, 9))
# print(randrange(2, 9, 2))

# print(r.randint(1, 9))
# print(r.randrange(2, 9, 2))
# print(r.uniform(10.5, 25.5))
# print(round(r.uniform(10.5, 25.5), 2))
#
# city = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(r.choice(city))
# print(r.choices(city, k=2))
# r.shuffle(city)
# print(city)

# s = [8, 7, 9, 6, 2, 1, 4, 5, 3, 11, 46, 78, 94, 25]
# print(r.choice(s))
# print(r.choices(s, k=4))

# from random import randint
#
# print([randint(1, 50) for i in range(5)])

# s = [8, 7, 9, 6, 2, 1, 4, 5, 3, 11, 46, 78, 94, 25]
# print(sum(s))
# print(len(s))
# print(min(s))
# print(max(s))

# from random import randint
#
# s = [randint(1, 100) for i in range(10)]
# print(s)
# max_el = max(s)
# print(max_el)
# s.remove(max_el)
# s.insert(0, max_el)
# print(s)


# lst = []
# if not lst:  # len(lst) == 0
#     print("Список пустой")
#
# print(bool(lst))

# from random import randint
#
# n1 = int(input("Размер первого списка: "))
# n2 = int(input("Размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
# c = [min(a), min(b), max(a), max(b)]

# c = a + b
# print("Третий список:", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
#
# print("Элементы обоих списков без повторений:", c)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
#
# print(m)
# print(m[1][2])

# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
# for i in m:
#     for j in i:
#         print(j, end='\t')
#     print()


# for i in m:
#     for j in i:
#         print(j, end='\t')
#     print()
# print()
# for i in m:
#     for j in i:
#         print(j*j, end='\t')
#     print()

# w, h = 5, 3
# m = [[x*y for x in range(w)] for y in range(h)]
# # m = []
# # for y in range(h):
# #     new_row = []
# #     for x in range(w):
# #         new_row.append(0)
# #     m.append(new_row)
# print(m)
# for i in m:
#     for j in i:
#         print(j*j, end='\t')
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

# from random import randint
#
# # w, h = 5, 4
# #
# # m = [[randint(10, 30) for x in range(w)] for y in range(h)]
# # for i in m:
# #     for j in i:
# #         print(j, end='\t\t')
# #     print()
#
# w, h = 3, 4
# m = [[randint(-20, 10) for i in range(w)] for y in range(h)]
# res = 0
# for i in m:
#     for j in i:
#         if j < 0:
#             res += 1
#         print(j, end='\t')
#     print()
# print(res)

# import geometry
#
# num1 = geometry.sqrt(4)
# # num2 = round(5.925654, 2)
# num2 = geometry.ceil(3.2)
# num3 = geometry.floor(3.9)
# print(num1)
# print(num2)
# print(num3)
# print(geometry.pi)

# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")


# sec = time.time()
# print(sec)
#
# local = time.ctime(465467967)
# print(local)
#
# res = time.localtime()
# print(res)
# print(res.tm_year)
#
# print(time.strftime("Сегодня: %B %d, %Y"))
# print(time.strftime("%m/%d/%Y, %H:%M:%S"))
#
# pause = 5
# print("Программа запущена")
# time.sleep(pause)
# print(pause, "sec")


# text = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)


# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res)
#
#
# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)


# Функции

# def hello(name):  # аргументы
#     print("Hello", name)
#
#
# hello("Irina")  # параметры
# hello("Ivan")


# def get_sum(a, b):
#     print(a + b)
#
#
# a1 = 2
# b1 = 5
# get_sum(a1, b1)
# n = 10
# m = 20
# get_sum(n, m)


# def x(sym1, sym2, numb):
#     for i in range(numb):
#         if i % 2 == 0:
#             print(sym1, end='')
#         else:
#             print(sym2, end='')
#     print()
#
#
# x('+', '-', 9)
# x('0', 'X', 7)


# def get_sum(a, b):
#     print("Hello")
#     return a + b
#
#
# a1 = 2
# b1 = 5
# res = get_sum(a1, b1)
# print(res)


# def maximun(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximun(9, 16))

# def coil(x, y):
#     if x > y:
#         return x - y
#     else:
#         return x + y
#
#
# first = int(input("a = "))
# second = int(input("b = "))
# res = coil(first, second)
# print("Результат:", res)


# def cub(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cub(i))

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# if func(10, 5):
#     print("Первое число больше")
# else:
#     print("Второе число больше")

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")  # 'jhkhYIUYIY45464563'
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# num = 2
# print(get_sum(1, 5, d=num))


# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр: ")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("Сумма нечетных цифр: ")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")

# a = 2
# b = 2
# # print(a == b)
# print(a, id(a))
# print(b, id(b))
# a = 3
# b = 3
# print(a, id(a))
# print(b, id(b))
# print(a is b)
#
# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1, id(lt1))
# print(lt2, id(lt2))
# # print(lt1 == lt2)
# print(lt1 is lt2)

# lt1 = [1, 2, 3]
# print(lt1, id(lt1))
# lt1.append(4)
# print(lt1, id(lt1))
# print(lt1[0], id(lt1[0]))


# Кортеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst)
# print(tpl)
#
# print(lst[0])
# print(tpl[0])
#
# lst[0] = 25
# print(lst)
# tpl[0] = 25
# print(tpl)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
#
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = 1, 2, 3, 4, 5, 6
# a = tuple("Hello")
# a = tuple([1, 2, 3, 4, 5, 6])
# print(a)
# print(type(a))

# from random import randint

# s = tuple(randint(0, 100) for i in range(5))
# print(s)
#
# t1 = tuple('hello')
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# # t4 = t1 * 3
# # print(t4)
#
# # print(t3.count('l'))
# # print(t3.index('l', 4))
#
# for i in t3:
#     print(i, end=' ')

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)  # 1
#             second = tpl.index(el, first + 1)  # 4
#             return tpl[first:second + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# from random import randint

# def rnd_tpl(a, b):
#     s = tuple(randint(a, b) for i in range(10))
#     return s
#
#
# n = rnd_tpl(0, 5)
# m = rnd_tpl(-5, 0)
# print(n)
# print(m)
# x = n + m
# print(x)
# print(x.count(0))

# t = (10, 11, [1, 2, 3], [4, 3, 6], ["hello", "world"])
#
# print(t[4][0])
# t[4][0] = "new"
# t[4].append("hi")
# print(t)


# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# first_name, year, married = get_user()
# # user = get_user()
# # print(user)
# # print(user[0])
# # print(user[1])
# # print(user[2])
# # first_name, year, married = user
# print(first_name, year, married)

# t = (1, 2, 3)
# del t
# print(t)

# lst = [1, 2, 3, 4, 5, 6]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lt = list(tpl)
# print(lt)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ", население: ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население: ", city_population, sep="")


# Множества (set)

# s = {"banana", "apple", "orange", "banana", "apple"}
# print(s)
# print(type(s))

# a = set("Hello")
# print(a)
# print(type(a))

# s = ("banana", "apple", "orange", "banana", "apple")
# print(s)
# s1 = set(s)
# print(s1)
# s2 = tuple(s1)
# print(s2)

# s = {x * x for x in range(10)}
# print(len(s))

# def to_set(lst):
#     x = set(lst)
#     return x, len(x)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))


# t = {"red", "green", "blue"}
# # print("green" in t)
# for i in t:
#     print(i)


# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# print(r)
# # a = {i for i in r if 'a' in i}
# # a = {"A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in r}
# a = {"A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in r if i[1] == 'c'}
# print(a)
#
#
# for i in r:
#     if i[1] == 'c':
#         if i[0] == "a":
#             print("A" + i[1:])
#         else:
#             print("B" + i[1:])

# r1 = {'ab_1', 'ac_2'}
# r2 = {'bc_1', 'bc_2'}
# print(r1 * 2)

# user = {"Tom", "Bob", "Alice"}
# print(user)
# # user.remove("Tom1")
# # user.discard("Tom")
# # user.pop()
# # user.clear()
# user.add("Ann")
# print(user)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # print(c)
# # a |= b
# # print(a)
# # c = a & b
# # print(c)
# # a &= b
# # print(a)
# # c = a - b
# # print(c)
# # a -= b
# # print(a)
# c = a ^ b
# print(c)
# a ^= b
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))


# str1 = "Hello"
# str2 = "How are you"
# str3 = set(str1) & set(str2)
# print(str3)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a <= b)

# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
#
# only_one = drawing ^ music
# print(only_one)
# both = drawing & music
# print(both)
# drawing = drawing - both
# print(drawing)

# s = frozenset([1, 2, 3, 4, 5, 6])
# print(s)
# a = frozenset({'hello', "world"})
# print(a)

# Словарь (dict)

# s = ['a', 'b', 'c']
# d = {'one': 'a', 'two': 'b', 'tree': 'c'}
# print(s)
# print(d)
# print(s[0])
# print(d['one'])

# d = {}
# users = (
#     ('one', 'a'),
#     ('two', 'b'),
#     ('tree', 'c')
# )
# print(users)
# d = dict(users)
# print(d)
# print(type(d))


# d = {i: i ** 2 for i in range(7)}
# print(d)
# print(d[0])
# d[0] = 15 * 2
# print(d)
# d[1] += 100
# print(d)


# d = {False: 0, 0: 'text', 'one': 45, (1, 2.3): 'кортеж', 42: [2, 3, 6, 7], True: 1, 'one': 'hello', 12: 'hello'}
# print(d)
# print(d[42][1])
# print(d[(1, 2.3)][2])
# del d[(1, 2.3)]
# print(d)
# print(42 in d)

# d = {'one': 'a', 'two': 'b', 'tree': 'c'}
# for i in d:
#     print(i, "->", d[i])
# key = 'one'
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + key + " нет в словаре")
# print(d)

# x = {1: 3, 2: 7, 3: 5, 4: -1}
# res = 1
# for i in x:
#     res *= x[i]
# print(res)

# d = dict()  # []
# d[1] = input("=> ")
# d[2] = input("=> ")
# d[3] = input("=> ")
# d[4] = input("=> ")
# d = {i: input('-> ') for i in range(1, 5)}
# print(d)
# disl = int(input("Какой элемент исключить: "))
# del d[disl]
# print(d)

# x = {1: 3, 2: 7, 3: 5, 4: -1}
# print(len(x))

# x = {
#     1: ['Core-i3-4330', 9, '4500'],
#     2: ['Core-i5-4670K', 3, '8500'],
#     3: ['AMD FX-6300', 6, '3700'],
#     4: ['Pentium G3220', 8, '2100'],
#     5: ['Core-i5-3450', 5, '6400']
# }
#
#
# def port():
#     for i in x:
#         print(f'{i}) {x[i][0]} - {x[i][1]} шт. по {x[i][2]}руб')
#
#
# port()
#
# while True:
#     j = int(input('№: '))
#     if j == 0 or j > len(x):
#         break
#     else:
#         x[j][1] += int(input('Количество: '))
#
# port()

# Методы словарей
# d = {'one': 'a', 'two': 'b', 'tree': 'c'}
# # print(d.keys())
# # print(d.values())
# # print(d.items())
# # # for i, j in d.items():
# # #     print(i, "->", j)
# # s = list(d.items())
# # print(s)
# # value = d['one']
# # value = d.get('one1', 'Такого ключа нет')
# # print(value)
# # d2 = d.copy()
# # print("D =", d)
# # print("D2 =", d2)
# #
# # d2['four'] = 'd'
# # print("D =", d)
# # print("D2 =", d2)
# # item = d.pop('two2', 'Такого ключа не существует')
# # print(item)
# # print(d)
# # item = d.popitem()
# # print(item)
# # print(d)
# # d.clear()
# # print(d)
# # a = {'four': 'd', 'two': 'last'}
# d.update([('four', 'd'), ('two', 'last')])
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = x.copy()
# # z.update(y)
# z = x | y
# print(z)

# x = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# # d = dict()
# # d['name'] = x.pop('name')
# # d['salary'] = x.pop('salary')
# # print(x)
# # print(d)
# x['location'] = x.pop('city')
# print(x)

# d = {'три': 3, 'один': 1, 'два': 2, 'четыре': 4}
# d2 = {k: v for k, v in d.items() if v <= 2}
# print(d2)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ": ", a[x][y], sep="")

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []  # d = {"one": [1, 2, 3], "two": []}
#         s = i  # "two"
#     else:
#         d[s].append(i)  # d = {"one": [1, 2, 3], "two": [10, 20]}
# print(d)

# sale = {
#     'Join': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'B': 1859},
#     'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
# }
#
# for x in sale:
#     print(x)
#     for y in sale[x]:
#         print('\t', y, ": ", sale[x][y], sep="")
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sale[person][region])
# new_data = int(input("Новое значение: "))
# sale[person][region] = new_data
# print(sale[person])

# a = [1, 2, 3, 4, 5]
# b = ['one', 'two', 'three']
# # # c = [4.0, 5.5, 6.2]
# d = list(zip(a, b))  # , c
# print(d)

# one = {'name': 'Igor', 'surname': 'Doe', 'job': 'Consultant'}
# two = {'name': 'Irina', 'surname': 'Smith', 'job': 'Manager'}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)


# pairs = [(4, 'three'), (2, 'one'), (6, 'two')]
# a, b = zip(*pairs)
# print(a)
# print(b)
#
# data = list(zip(b, a))
# print(data)
#
# data.sort()
# print(data)
#
# # data.reverse()
# # print(data)
#
# data = dict(data)
# print(data)
#
# f = {v: k for k, v in data.items()}
# print(f)
# f = list(f.items())
# print(f)

# one = {'apple': 0.45, 'orange': 0.35, 'pepper': 0.35}
# two = {'pepper': 0.25, 'onion': 0.55}
# print({**one, **two})  # {'apple': 0.45, 'orange': 0.35, 'pepper': 0.25, 'onion': 0.55}
#
# for k, v in {**one, **two}.items():
#     print(k, '->', v)

# colors = ['red', 'blue', 'green']
# for i in range(len(colors)):
#     print(i + 1, ") ", colors[i], sep="")
# print()
# j = 1
# for color in colors:
#     print(j, ") ", color, sep="")
#     j += 1
# print()
# for v, color in enumerate(colors, 1):
#     print(v, ") ", color, sep="")

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     return args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(5, 9, 4))

# def to_dict(a, b, c, d):
#     i = (a, b, c, d)
#     return dict(zip(i, i))

# def to_dict(*args):
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4, 5))
# print(to_dict('grey', (2, 17), 3.11, -4))


# def ch(*args):
#     sr = sum(args) / len(args)
#     print(sr)
#     res = []
#     for num in args:
#         if num < sr:
#             res.append(num)
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print(func(2))
# print(func(2, 5, 9, 7))

# def print_scores(stud, *scores):
#     print("Students Name:", stud)
#     for score in scores:
#         print(score)
#
#
# print_scores("Jonathan", 100, 95, 88, 92, 99, 65)
# print_scores("Rick", 96, 20, 30, 56)

# def func(**kwargs):
#     print(kwargs)
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a="python"))

# def info(**data):
#     for k, v in data.items():
#         print(k, '->', v)
#
#
# info(surname="Sharma", name="Irina", age=22, phone=1234567890)
# info(surname="Wood", name="Igor", email="igor@mail.ru", country="Russia", age=25, phone=6789012345)


# my_dict = {'one': 'first'}
#
#
# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='grey')
# print(my_dict)

# def hi():
#     global name
#     name = "Sam"
#     surname = "Johnson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# name = "Tom"
# print(name)
# hi()
# bye()

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5
# x = 3


# def add(a):
#     x = 2
#
#     def add_some():
#         # x = 5
#         print("x =", x)
#         return a + x
#
#     print("XXX", x)
#     return add_some()
#
#
# print(add(3))
#

# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)


# sum = 5
# print(sum)
#
# lst = [5, 9, 7, 1, 6, 4, 8]
# print(sum(lst))

# print = 5
# s = 2
# print(s)

# def outer(who):
#     def inner():
#         print("Hello", who)
#
#     inner()
#
#
# outer("World!")


# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("Сумма:", a + b)
#
#     print("a:", a)
#     fun2(4)
#
#
# fun1()


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30  # 35
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("a:", a)
#
#     inner()
#     t = a
#
#
# fn()
#
# c = x + t  # 25 + 30 = 55
# print(c)

# x = 5
#
#
# def fn1():
#     x = 25  # 55
#
#     def fn2():
#         # x = 33  # 55
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x =', x)  # 33
#
#     fn2()
#     print("fn1.x =", x)  # 25
#
#
# fn1()
# print("x =", x)


# def outer(a1, b1, a2, b2):
#     a = 0  # 1
#     b = 0  # 7
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))  # [1, 7]


# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# a = outer(5)
# print(a(10))
#
# b = outer(6)
# print(b(10))
#
# print(outer(5)(10))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#     # print("c = 1", id(c))
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         # print("c = 2", id(c))
#         b = b + "_!!!"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     c = 0
#
#     def inner():
#         nonlocal c
#         c += 1
#         print(city, c)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res2()
# res2()
# res1()

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def outer(lower, upper):
#     def inner(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return inner
#
#
# b_A = outer(80, 100)
# b_B = outer(70, 80)
# b_C = outer(50, 70)
# b_D = outer(0, 50)
# print("A: ", b_A(students))
# print("B: ", b_B(students))
# print("C: ", b_C(students))
# print("D: ", b_D(students))

# def outer(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj = outer(5, 2)
# print(obj.add())
# print(obj.sub())
# print(obj.mul())


# lambda-выражения (анонимные функции)

# func = lambda x, y: x + y
# print(func(1, 2))

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))


# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())
# print((lambda *args: sum(args))(10, 20, 30))

# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for t in c:
#     print(t('abc__'))

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# f = outer(10)
# print(f(5))
#
#
# def outer1(n):
#     return lambda x: n + x
#
#
# f1 = outer1(10)
# print(f1(5))
#
# outer2 = lambda n: lambda x: n + x
# f2 = outer2(10)
# print(f2(5))
#
# print((lambda n: lambda x: n + x)(10)(5))

# print((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))

# d = {'b': 25, 'a': 15, 'c': 24}
# # lst = list(d.items())
# # print(lst)
# # lst.sort(key=lambda i: i[1])
# # print(lst)
# # print(dict(lst))
# new_d = sorted(d.items(), key=lambda i: i[1])
# print(new_d)
# print(dict(new_d))


# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6},
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# res1 = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res1)
# # res2 = sorted(players, key=lambda item: item['rating'], reverse=True)
# res2 = min(players, key=lambda item: item['name'])
#
# print(res2)

# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# print(a[-1](12, 2))

# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
# }
#
# d[4]()

# area = {
#     'circle': lambda r: 3.14 * r ** 2,
#     'triangle': lambda a, b: a * b,
#     'trapezoid': (lambda a, b, h: (a + b) * h / 2)
# }
#
# print("Площадь окружности", area['circle'](2))
# print("Площадь прямоугольника", area['triangle'](10, 13))
# print("Площадь трапеции", area['trapezoid'](7, 5, 3))

# print((lambda a, b: a if a > b else b)(15, 23))
# print((lambda a, b, c: a if (a <= b) and (a <= c) else b if (b <= a) and (b <= c) else c)(19, 18, 15))


# print((lambda a, b, c: a if b > a < c else b if c > b < a else c)(14, 12, 13))


# map(func, *iter), filter(func, *iter)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(mult, lst)))
# #
# print(list(map(lambda t: t * 2, lst)))

# t = (2.28, 6.44, 100.4)

# print(tuple(map((lambda x: int(x)), t)))
# t = ['1', '2', '3', '4', '5']
# print(list(map(int, t)))

# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))

# s = 0
#
#
# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     global s
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#
#
# outer(2, 4, 6)
# print(s)
# outer(5, 8, 2)
# print(s)
# outer(1, 6, 8)
# print(s)


# def outer(a, b, c):
#     s = 0
#
#     def inner(i, j):
#         nonlocal s
#         s += i * j
#
#     inner(a, b)
#     inner(a, c)
#     inner(b, c)
#     return 2 * s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x, y: (x, y), st, num)))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))

# filter(func, *iter)

# t = ('abcd', 'abc', 'casdf', 'def', 'ghj')
# # t2 = tuple(filter(lambda s: len(s) == 3, t))
# t2 = tuple(filter(lambda s: s, t))
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# from random import randint
#
# b = [randint(1, 40) for i in range(10)]
# print(b)
# res = list(filter(lambda s: 10 <= s <= 20, b))
# print(res)

# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# # print(id(test))
# # print(id(hello))
# print(test())


# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#     return wrap
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая функция
#     def wrap():
#         print('*' * 50)
#         func()
#         print('=' * 50)
#     return wrap
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# @my_decorator
# def hello():
#     print("Hello, I am func 'hello'")
#
#
# func_test()
# hello()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())


# def bold(fn):
#     def wrap():
#         return "(" + fn() + ")"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<" + fn() + ">"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "5 + 2"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def args_decor(fn):
#     def wrap(args1, args2):
#         print(args1, args2)
#         fn(args1, args2)
#
#     return wrap
#
#
# @args_decor
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Лазарева")

# def args_decor(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decor
# def print_full_name(*names, study="Python"):
#     print(*names, "изучают", study, "\n")
#
#
# print_full_name("Борис", 'Елизавета', 'Светлана', study="JavaScript")
# print_full_name("Владимир", 'Екатерина', 'Виктор', 'Виктория', 'Игорь')

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(15, 2)

# def multiply(arg1):
#     def second_func(fn):
#         def three_func(arg3):
#             fn(arg1)
#             print(arg1 * arg3)
#         return three_func
#     return second_func
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))


# def fist_func(arg1):
#     def second_func(func):
#         def three_func(arg3):
#             print(arg1, "=", func(arg3) * arg1)  # 5 * 3
#
#         return three_func
#
#     return second_func
#
#
# @fist_func(3)
# def fn(r):
#     print("Результат:", r, "*", end=" ")
#     return r
#
#
# fn(5)

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:  # type(x) != int
#                     raise TypeError("Некорректный тип данных", f_args[i])
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорректный тип данных")
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# # @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello! "):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Doge"))
# # print(typed_fn(3.6, 4.5, 7.8))
# print(typed_fn2("Hello, ", "World", "!"))
# # print(typed_fn2(3, 4, 5))
# print(typed_fn3("Hello, ", "World", z=5))
# # print(typed_fn3("Hello, ", "World", z="abc"))

#
# print("Новый код")
# print("Еще код")

# print("Производим изменения на другом компьютере")

# print(int('18'))
# # print(int('18.5'))
# print(int(18.5))

# print(int("100", 2))
# print(int("100", 10))
# print(int("100", 8))
# print(int("100", 16))


# print(bin(18))  # 0b10010  - двоичная
# print(oct(18))  # 0o22  - восьмиричная
# print(hex(18))  # 0x12  - шестнадцатеричная
#
#
# print(0b10010 + 0xFF)
# print(0o22)
# print(0xFF)


# def decor(args1):
#     def args_decor(func):
#         def wrap(x, y, z, d):
#             print(args1, x, y, z, d, '=', end=" ")
#             func(x, y, z, d)
#
#         return wrap
#
#     return args_decor
#
#
# @decor("Сумма чисел")
# def summa(a, b, c, r):
#     print(a + b + c + r)
#
#
# @decor("Среднее арифметическое чисел")
# def aref(a, b, c, r):
#     num = [a, b, c, r]
#     summ = 0
#     for i in num:
#         summ += i
#     avg = summ / len(num)
#     print(avg)
#
#
# summa(2, 3, 3, 4)
# aref(2, 3, 3, 4)


# def summa(a, b, c, r):
#     print(a + b + c + r)
#
#
# summa(2, 3, 3, 4)


# def sr_a(fn):
#     def wrap(*f_args):
#         # x = fn(*f_args)
#         # print('Среднее арифметическое чисел', end=' ')
#         # print(*f_args, sep=', ', end=' ')
#         # print('=', x / len(f_args))
#         a = ", ".join(list(map(str, f_args)))
#         print('Среднее арифметическое чисел:', a, "=", fn(*f_args) / len(f_args))
#
#     return wrap
#
#
# @sr_a
# def summa(*args):
#     # res = 0
#     # for i in args:
#     #     res += i
#     # print('Сумма чисел', end=' ')
#     # print(*args, sep=', ', end=' ')
#     # print('=', res)
#     # return res
#     # a = ""
#     # for i in args:
#     #     a += str(i) + ", "
#     # print('Сумма чисел:', a[:-2], "=", sum(args))
#     a = ", ".join(list(map(str, args)))  # ", ".join(['2', '3', '3', '4']) => 2, 3, 3, 4
#     print('Сумма чисел:', a, "=", sum(args))
#     return sum(args)
#
#
# summa(2, 3, 3, 4)

# print(", ".join(['2', '3', '3', '4']))  # 2, 3, 3, 4


# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# # print(e * 3)
# # print(q in e)  # 'Pyt' in 'Python'
# # print(e[1:-1])
# # print(e[::2])
# e = e[:3] + 't' + e[4:]  # Pytton
# print(e)  # Python => Pytton


# def changeCharToStr(s, c_old, c_new):
#     s2 = ""
#
#     for i in s:
#         if i == c_old:
#             s2 += c_new
#         #     continue
#         # s2 += i
#         else:
#             s2 += i
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = changeCharToStr(str1, "N", "P")
# print("str1 =", str1)
# print("str2 =", str2)

# print("Привет")
# print(u"Привет")


# print("C:\\folder\\file.txt")
# print(r"C:\folder\file.txt")
#
# print(r"C:\folder\\"[:-1])
# print(r"C:\folder" + "\\")
# print("C:\\folder\\")


# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")
#
# print(f"{round(3.1564789, 2)}")
# print(f"{3.1564789:.3f}")


# x = 10
# y = 5
# # print("x =", x)
# # print(f"{x = }, {y = }")
# print(f"{x} x {y} / 2 = {x * y / 2}")

# num = 74
# print(f"{{{{{num}}}}}")

# dir_name = "folder"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home" + "\\" + dir_name + "\\" + file_name)


# s = """<div>
# <a href="#">        content             </a>
# </div>"""
# print(s)
#
# s = '''<div>
# <a href="#">content</a>
# </div>'''
# print(s)

# def square(n):
#     """Принимает число n, возвращает квадрат число n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
#
#
# import geometry
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * geometry.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))
# print(ord('А'))
# print(ord('Я'))
# print(ord('а'))


# s = "Test string for me "
# arr = [ord(x) for x in s]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(35))
# print(chr(8364))


# a, b = 122, 97
# # if a > b:
# #     arr = [chr(i) for i in range(b, a + 1)]
# #     print(' '.join(arr))
# # else:
# #     arr = [chr(i) for i in range(a, b + 1)]
# #     print(' '.join(arr))
#
# if a < b:
#     a, b = b, a
# arr = [chr(i) for i in range(b, a + 1)]
# print(' '.join(arr))


# print("apple" == "Apple")
# print("apple" > "Apple")  # 97 > 65

# from random import randint
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(SHORTEST, LONGEST)
#     res = ""
#     for i in range(rand_len):
#         rand_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += rand_char
#     return res
#
#
# print("Случайный пароль:", random_password())


# s = "hello, WORLD! I am learning Python."
# # print(s.capitalize())  # Hello, world! i am learning python.
# # print(s.lower())  # hello, world! i am learning python.
# # print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# # print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
# # print(s.title())  # Hello, World! I Am Learning Python.
#
# # print(s.count("h", 1, -4))
# # print(s.find("l", 4, 19))  # '-1' - нет совпадений
# # print(s.index("Python1"))  # ValueError
# # print(s.find("l"))
# # print(s.rfind("l1"))
# # print(s.index("l"))
# # print(s.rindex("l1"))
#
# # text = input("Введите два слова: ")  # 'один два'
# # a = text[:text.find(' ')]  # text[:4] => один
# # b = text[text.find(' ') + 1:]  # text[5:] => два
# # new_text = b + ' ' + a  # два один
# # print(new_text)
#
# print(s.index("I am"))
# print(s.startswith(("I am", "hello")))
# print(s.endswith("Python."))


# print('abc123'.isalnum())  # цифры и буквы
# print('ABCabc'.isalpha())  # буквы
# print('123'.isdigit())  # цифры


# print('abc12%^&'.islower())
# print('ABC45&*b'.isupper())


# print('py'.center(10))
# print('py'.center(10, "-"))
# print('py'.center(100))

# print("                 py".lstrip())
# print("py                 ".rstrip())
# print("       py          ".strip())
#
# print('https://www.python.org'.lstrip("/:pths"))
# print('py.$$$;'.rstrip(';$.'))


# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования. New"
# print(str1.replace("Nython", "Python", 2))

# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(['1', '2']))
#
# print(":".join("Hello"))

# print('Строка разделенная пробелами'.split())
# print('www.python.org.ru'.split('.', 1))
# print('www.python.org.ru'.rsplit('.', 1))
# print('www...python...org'.split("."))

# s = input("-> ").split()
# s = list(map(int, s))
# print(s)
# print(type(s[0]))
# print(f"{s[0]} {s[1][0]}. {s[2][0]}.")

# Регулярные выражения
import csv
import re

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = ' '

# print(re.findall(reg, s))  # список, содержащий все совпадения#
# print(re.search(reg, s))  # месторасположение первого совпадения
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())#
# print(re.match(reg, s))  # поиск по заданному шаблону в начале строки#
# print(re.split(reg, s, 3))  # возвращает список строк, разбитых по шаблону разделителю#
# print(re.sub(reg, "!", s, 3))  # поиск и замена


# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счё-та. 9178 [H^el_lo]"
# reg = '[12][0-9][0-9][0-9]'
# reg = r'[A-Za-z0+.\[\]-]'
# reg = r'\.'
# reg = r'[^0-9]'
# print(re.findall(reg, s))

# print(ord("Ё"))
# print(ord("А"))
# print(ord("Я"))
#
# print(ord("а"))
# print(ord("я"))
# print(ord("ё"))

# t = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:59."
# p = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(p, t))


# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счё-та. [H^el_lo] 9178  2000000"
# # reg = r'\w+'
# reg = r'\d+'
# # reg = r'20*'
# print(re.findall(reg, s))


# s = """Ежевику для ежат
# Принесли два ежа.
# Ежевику еле-еле
# Ежата возле ели съели. """
# print(s)
# up_e = s.count('Е')
# # print(up_e)
# lower_e = s.count(' е')
# # print(lower_e)
# count = up_e + lower_e
# print('Кол-во слов:', count)


# text = 'Ежевику для ежат ' \
#        'Принеси два ежа. ' \
#        'Ежевику еле-еле ' \
#        'Ежата возле ели съели'
#
# print(text)
# text_arr = text.split(' ')
# print(text_arr)
# count = 0
# for i in text_arr:
#     if i[0] == 'е' or i[0] == 'Е':
#         count += 1
#
# print(count)


# d = 'Цифры: 7, +17, -42, 0013, 0.345456654'
# print(re.findall(r'[+-]?\d+\.?\d*', d))

# s = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub("#.+", "", s))
#
# # Дата рождения: 05.03.1987
# # s = "Дата рождения: 09-09-1987"
# print("Дата рождения:", re.sub("-", ".", re.sub("#.+", "", s)))

# s = "12 сентября 2023 года 456"
# reg = r'\d{2,4}'
# print(re.findall(reg, s))

# s = '+7 499 456-45-78 , +74994564578 , 7 (499) 456 45 78 , 74994564578'
# reg = r'\+?7\d{10}'
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счё-та."
# # reg = r'^\w+\s\w+'
# reg = r'\w+\.$'
# print(re.findall(reg, s))

# def validate_login(name):
#     return re.findall('^[A-Za-z_-]{3,16}$', name)
#
#
# print(validate_login('Python_master'))
# print(validate_login('Python'))

# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))
# print(re.findall(r'\w+', '12 + й', re.A))

# text = 'hello world'
# print(re.findall(r'\w\+', text, re.DEBUG))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счё-та."
# reg = r'я'
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.findall(reg, s, re.I))


# text = """
# one
# two
# """

# print(re.findall(r'one.\w+', text))
# print(re.findall(r'one.\w+', text, re.DOTALL))
# print(re.findall(r'one.\w+', text, re.S))
# print(re.findall(r'one$', text))
# print(re.findall(r'one$', text, re.MULTILINE))
# print(re.findall(r'one$', text, re.M))

# print(re.findall("""
# [a-z.-]+   # part 1
# @          # @
# [a-z.-]+   # part 2
# """, 'test@mail.ru', re.VERBOSE))

# text = """Python
# python
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))


# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))   # ['<body>', '</body>']
#
# # *?, +?, ??
# # {m,n}?, {,n}?, {m,}?
#
# s = "12 сентября 2023 года 4561234"
# reg = r'\d{2,4}?'
# print(re.findall(reg, s))

# s = "<p>Изображение <img width='300' src = 'bg.jpg' alt='картинка'> - фон страницы</p>"
# # reg = r'<img.*?>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))  # ['<img src='bg.jpg'>']

# s = "Петр, Ольга и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий|Ирина"
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0, double = 8.0f, int"
# # reg = r'(?:int|double)\s*=\s*\d[.\w]*'
# reg = r'((int|double)\s*=\s*(\d[.\w]*))'
# print(re.findall(reg, s))

# () - сохраняющие круглые скобки
# (?:) - не сохраняющие круглые скобки

# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))


# a = '01-11-2021'
# reg = r'(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])'
# print(re.findall(reg, a))


# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счё-та."
# reg = r'(\d+)\s(\D+)'
# print(re.findall(reg, s))
# print(re.search(reg, s))
# m = re.search(reg, s)
# print(m[1])
# print(m[2])
# print(m[0])
# print(re.search(reg, s).group(1))

# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def repl_find(m):
#     global count
#     count += 1
#     return f'<option value="{count}">{m.group(1)}</option>\n'
#
#
# print("<select>")
# print(re.sub(r"\s*(\w+)\s*", repl_find, text))
# print("</select>")

# s = "<p>Изображение <img width='300' src = \"bg.jpg\"> - фон страницы</p>"
# # reg = r'<img\s+[^>]*src\s*=\s*([\'"])(.+?)\1>'
# reg = r'<img\s+[^>]*src\s*=\s*(?P<q>[\'"])(.+?)(?P=q)>'
# print(re.findall(reg, s))  # ['bg.jpg']


#  (?P<name>)  (?P=name)

# s = "Самолет прилетает 10/23/2023. Будем рады вас видеть после 10/24/2023."  # 23.10.2023  24.10.2023
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))

# s = "yandex.com and yandex.ru"
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r"http://\1", s))


# def func(a):
#     numb = ''
#     while a > 0:
#         numb = str(a % 2) + numb
#         a = a // 2
#     print(numb)
#
#
# while True:
#     x = int(input('-> '))
#     if x == 0:
#         break
#     func(x)

# Файлы

# f = open("test.txt")
# print(f)
# print(*f)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# f.close()
# print(f.closed)


# f = open("D:\\Python330\\330\\test.txt")
# f = open(r"D:\Python330\330\test.txt")
# f = open("test.txt")
# print(f.read(3))
# print(f.read())
# f.close()


# f = open("one.txt", "r")
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()


# f = open("one.txt", "r")
# print(f.readlines(22))
# print(f.readlines())
# print(f.readlines())
# f.close()

# count = 0
# f = open("one.txt", "r")
#
# for line in f:
#     # print(line, end="")
#     count += 1
# # print(f.readlines())
# # print(len(f.readlines()))
# f.close()
# print(count)


# f = open('xyz.txt', 'w')
# print(f.write("Hello \nWorld"))
# f.close()
#
# f = open('xyz.txt', 'a')
# print(f.write("\nNew text."))
# f.close()


# f = open('xyz.txt', 'a')
# line = ['\nThis is line 1', '\nThis is line 2']
# f.writelines(line)
# f.close()

# f = open('xyz.txt', 'w')
# lst = [str(i) for i in range(1, 20)]
# print(lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# # t = "\t".join(map(str, lst))
# # print(t)
# # f.write(t)
# for index in lst:
#     f.write(index + '\t')
# f.close()

# f = open("text2.txt", "w")
# f.write("Замена строки в текстом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# f.close()
#
# f = open("text2.txt", "r")
# read_file = f.readlines()
# print(read_file)
# read_file[1] = "Hello world!\n"
# print(read_file)
# f.close()
#
# f = open("text2.txt", "w")
# f.writelines(read_file)
# f.close()

# f = open("text2.txt", 'w')
# f.write("Замены строки с текстом файле;\nизменить строку в списке;\nзаписать список в фаил")
# f.close()
#
# f = open("text2.txt", 'r')
# in_put = int(input("Числл: "))
# read_file = f.readlines()
# if 0 <= in_put < len(read_file):
#     del read_file[in_put]
# else:
#     print("Индекс введен некорректно!")
# print(read_file)
# f.close()
#
# f = open("text2.txt", 'w')
# f.writelines(read_file)
# f.close()

# f = open("test.txt", "r")
# print(f.read(3))
# print(f.tell())  # позиция условного курсора
# print(f.seek(1))
# print(f.read())
# f.close()

# f = open("test.txt", "r+")
# print(f.write('I am learning Python'))  # 20
# print(f.seek(3))  # 3
# print(f.write("-new string-"))  # 12
# print(f.tell())  # 15
# f.close()

# with open('test.txt', 'w+') as f:
#     print(f.write('01234\n56789'))
#
# with open('test.txt', 'r') as f:
#     for line in f:
#         print(line[:3])


# file = "res_1.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     return " ".join(map(str, lt))  # '4.5 2.8 3.9'
#
#
# with open(file, 'w') as f:
#     f.write(get_line(lst))
#
# print("Done!")
#
# with open(file, 'r') as f:
#     nums = f.read()
#
# print(nums)
#
# nums_list = list(map(float, nums.split()))
# print(nums_list)
# print(sum(nums_list))
# print(len(nums_list))


# def longest_words(file):
#     with open(file, "r") as text:
#         w = text.read().split()
#         print(w)
#         max_length = len(max(w, key=len))  # 11
#         print(max_length)
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_words("test.txt"))


# read_file = "one.txt"
# write_file = "two.txt"
#
#
# # text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
# #
# # with open(read_file, 'w') as f:
# #     f.write(text)
#
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)


# read_file = "one.txt"
# write_file = "two.txt"
# third = "three.txt"
#
# with open(read_file, 'r') as f1, open(write_file, 'r') as f2, open(third, 'w') as f3:
#     file_1 = f1.readlines()
#     file_2 = f2.readlines()
#     f4 = file_1 + file_2
#     f3.writelines(f4)


# Модули OS и OS.PATH

# import os
# import os.path
# print(os.getcwd())  # возвращает путь к текущей директории
# print(os.listdir())  # список файлов и директорий
# print(os.listdir(".."))
# print(os.listdir(r"D:\Python330\JavaScript"))

# os.mkdir("folder_2")  # создание директории
# os.makedirs("nested1/nested2/nested3")  # создаст не только конечную директорию, но и промежуточные

# os.rmdir("folder_2")  # удаляет пустой каталог

# os.rename('xyz.txt', 'x.txt')  # переименование файлов и каталогов
# os.rename('x.txt', 'nested1/x.txt')  # перемещение файла в папку

# os.renames('two.txt', 'text/two.txt')  # перемещение файла в папку (создавая промежуточные директории)

# os.remove('three.txt')  # удаление файла


# for root, dirs, files in os.walk("nested1", topdown=False):
#     print("Root:", root)
#     print("Subdirs:", dirs)
#     print("Files:", files)
#     print()


# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print('-' * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#     print('-' * 50)
#
#
# remove_empty_dirs("nested1")

# import os


# /Users/daniilfil/PycharmProjects/pythonProject/nes

# print(os.path.split(r"D:\Python330\330\nested1\nested2\test.txt"))
# # print(os.path.split("/Users/daniilfil/PycharmProjects/pythonProject/nes"))
#
# print(os.path.dirname(r"D:\Python330\330\nested1\nested2\test.txt"))
# print(os.path.basename(r"D:\Python330\330\nested1\nested2\test.txt"))
#
# print(os.path.join("files", r"D:\Python330", "folder", "dir", "two.txt"))
# print(os.path.join("/Users", "daniilfil", "PycharmProjects", "pythonProject", "nes"))

# import os

# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         open(file_path, 'w').close()
#
# files_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
#
# for file in files_with_text:
#     with open(file, 'w') as f:
#         f.write(f"some sample text for {file} file")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, fls in os.walk(root, topdown):
#         print(root)
#         print(dirs)
#         print(fls)
#     print("-" * 50)
#
#
# print_tree("Work", False)
# print_tree("Work", True)

# Work\w.txt
# Work\F1\f11.txt
# Work\F1\f12.txt
# Work\F1\f13.txt
# Work\F2\F21\f211.txt
# Work\F2\F21\f212.txt

import os
import time

# print(os.path.exists(r'D:\Python330\330\Work\F2\F21\f212.txt'))  # возвращается True, если path указывает на
# # существующий путь в файловой системе
# print(os.path.isfile(r'D:\Python330\330\Work\F2\F21\f212.txt'))  # проверка на наличие по заданному пути файла
# print(os.path.isdir(r'D:\Python330\330\Work\F2\F21'))  # проверка на наличие по заданному пути папки

# path = 'main.py'
# print(os.path.getsize(path))  # 76842 - в байтах
# print(os.path.getsize(path) / 1024)
# print(os.path.getatime(path))  # последний доступ к файлу
# print(os.path.getctime(path))  # время создания файла (Windows) или время последнего изменения (Unix)
# print(os.path.getmtime(path))  # время последнего изменения  в секундах
#
# c = os.path.getctime(path)
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getctime(path))))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getatime(path))))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getmtime(path))))

# file_path = 'nested1/nested2/test.txt'
#
# if os.path.exists(file_path):
#     dirs, name = os.path.split(file_path)
#     atime = os.path.getatime(file_path)
#     print(f"{name} ({dirs}) - время последнего доступа к файлу {atime}")
# else:
#     print(f"Файл {file_path} не существует!")


# Рекурсия

# def elevator(n):  # 5 4 3 2 1
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)  # elevator(0)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))  # 5
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res

# def sum_list(lst):  # [9]
#     if len(lst) == 1:
#         return lst[0]  # 9
#     else:
#         return lst[0] + sum_list(lst[1:])   # 1 3 5 7
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25


# import re
#
# s = '+7 499 456-45-78 , +74994564578 , 7 (499) 456 45 78 , 7 (499) 456-45-78'
# reg = r'\+?7\s*\(?\d+\)?\s*\d+[- ]?\d+[- ]?\d+'
# print(re.findall(reg, s))

# def to_str(n, base):  # 15
#     convert = "0123456789ABCDEF"
#     if n < base:  # 15 < 16
#         return convert[n]  # convert[15] => 'F'
#     else:
#         return to_str(n // base, base) + convert[n % base]  # to_str(15, 16)  # convert[254 % 16] => (14) 'E'
#
#
# print(to_str(254, 16))

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names)
#
#
# # print(len(names))
# # print(names[1])
# # print(isinstance(names[1], list))
# # print(names[1][1])
# # print(isinstance(names[1][1], list))
# # print(names[1][1][0])
# # print(isinstance(names[1][1][0], list))
# def count_items(item_list):   # ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex',
#     # ['Bea', 'Bill'], 'Ann']
#     count = 0  # 10
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))


# def remove(text):  # " "
#     if not text:  # ""
#         return ""
#     if text[0] == "\t" or text[0] == " " or text[0] == "!":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])  # 'HelloWorld'
#
#
# print(remove(" Hel!!lo\tWor!!!ld "))

# print(bool(""))


# class Point:
#     x = 1
#     y = 2
#
#
# p1 = Point()
# print(p1.x)
# print(p1.y)
# p1.x = 5
# p1.y = 7
# p1.z = 3
# print(p1.x)
# print(p1.y)
# print(p1.__dict__)
# # print(type(p1))
# p2 = Point()
# print(p2.x)
# print(p2.y)
# print(p2.__dict__)

# print(id(Point.x))  # 2947684560624
# print(id(p1.x))     # 2947685777360
# print(id(p2.x))     # 2947685777264


# class Point:
#     x = 1
#     y = 2
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# # p1.set_coord(5, 10)
# Point.set_coord(p1, 5, 10)
# print(p1.__dict__)
#
# p2 = Point()
# # p2.x = 3
# # p2.y = 7
# p2.set_coord(3, 7)
# print(p2.__dict__)


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = 'street, house'
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\nСтрана: "
#               f"{self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.address = address
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#
#     def set_phone(self, phone):  # устанавливает значение
#         self.phone = phone
#
#     def get_phone(self):  # получает значение
#         return self.phone
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_phone("55-99-33")
# print(h1.get_phone())
# h1.set_name("Валерия")
# print(h1.get_name())


# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print("Инициализатор класса Person")
#
#     def __del__(self):
#         print("Удаление экземпляра класса")
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, "\n")
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# # p1 = 0
# p1.add_skill(3)
# # del p1
#
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)

# import os
#
# dir_name = "nested1"
#
# objs = os.listdir(dir_name)
# print(objs)
#
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     if os.path.isfile(p):
#         print(f"{obj} - file - {os.path.getsize(p)} bytes")
#     elif os.path.isdir(p):
#         print(f"{obj} - dir")


# class Point:
#     count = 0  # 1 2 3
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# p2 = Point(2, 8)
# p3 = Point(7, 12)
# print(p1.count)
# # print(p2.count)
# # print(p3.count)
# print(Point.count)
# print(p1.x)

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f"Инициализация робота: {self.name}")
#         Robot.k += 1
#
#     def __del__(self):
#         print(f"{self.name} выключается!")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(f"{self.name} был последним")
#         else:
#             print(f"Работающих роботов осталось: {Robot.k}")
#
#     def say_hi(self):
#         print(f"Приветствую! Меня зовут {self.name}")
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print(f"Численность роботов: {Robot.k}")
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print(f"Численность роботов: {Robot.k}")
#
# droid3 = Robot("P-PO3")
# droid3.say_hi()
# print(f"Численность роботов: {Robot.k}")
#
# print("\nЗдесь роботы могут проделать какую-то работу\n")
#
# print("Роботы закончили свою работу. Давайте их выключим")
# del droid1  # Здесь __del__ droid1
# del droid2  # Здесь __del__ droid2
# del droid3  # Здесь __del__ droid3
# print(f"Численность роботов: {Robot.k}")


# class Point:
#     __slots__ = ["__x", "__y"]
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x  # _Point__x
#             self.__y = y  # _Point__y
#
#     def __check_value(s):  # _Point__check_value
#         if isinstance(s, int) or isinstance(s, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):  # установили новые координаты
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):  # получили координаты
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def get_x(self):
#         return self.__x
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# # print(p1.__x, p1.__y)
# # p1.x = 100
# # p1.__y = "abc"
# # print(p1.x, p1.__y)
#
# # p1.set_coord(100.2, 200.4)
# # print(p1.__dict__)
# # print(p1.get_coord())
# # # print(Point.__dict__)
# # # p1.__check_value(5)
# # p1.set_x(50)
# # print(p1.get_x())
# # p1.set_y(70)
# # print(p1.get_y())
# # print(p1._Point__x)
# # p1._Point__x = "abc"
# # print(p1.__dict__)
# print(p1.get_coord())


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         if isinstance(x, (int, float)):
#             self.__x = x
#         else:
#             raise ValueError("Неверный формат данных")
#
#     def __get_x(self):
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 3
# print(p1.x)
# del p1.x
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     @x.setter
#     def x(self, x):
#         if isinstance(x, (int, float)):
#             self.__x = x
#         else:
#             raise ValueError("Неверный формат данных")
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 3
# print(p1.x)
# del p1.x
# print(p1.__dict__)

# class KgToPounds:
#     def __init__(self, kg):
#         if isinstance(kg, (int, float)):
#             self.__kg = kg
#         else:
#             self.kg = 0
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(f"{weight.kg} кг => {weight.to_pounds()} фунтов")
# weight.kg = 41
# print(f"{weight.kg} кг => {weight.to_pounds()} фунтов")
# weight.kg = 'десять'
# print(f"{weight.kg} кг => {weight.to_pounds()} фунтов")

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     # get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.get_count())

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))

# class Number:
#     @staticmethod
#     def max(a, b, c, d):
#         mx = a  # 3
#         if b > mx:
#             mx = b  # 5
#         if c > mx:
#             mx = c  # 7
#         if d > mx:
#             mx = d  # 9
#         return mx
#
#     @staticmethod
#     def min(*args):  # (3, 5, 7, 9)
#         mn = args[0]
#         for i in args:
#             if i < mn:
#                 mn = i
#         return mn
#
#     @staticmethod
#     def average(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def factorial(n):  # 5
#         fact = 1
#         for i in range(1, n + 1):  # 1 2 3 4 5
#             fact *= i  # fact = fact * 1
#         return fact
#
#
# print("Максимальное число:", Number.max(3, 5, 7, 9))
# print("Минимальное число:", Number.min(3, 5, 7, 9))
# print("Среднее арифметическое:", Number.average(3, 5, 7, 9))
# print("Факториал числа:", Number.factorial(5))
# # 5! = 1*2*3*4*5

# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, string_data):
#         day, month, year = map(int, string_data.split('.'))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split('.'))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# dates = [
#     '30.12.2023',
#     '30-12-2020',
#     '01.01.2021',
#     '12.31.2023'
# ]
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         date_db = date.string_to_db()
#         print(date_db)
#     else:
#         print(f"Неправильная дата или формат строки с датой")

# date2 = Date.from_string('23.10.2023')
# # date = Date(day, mount, year)
# print(date2.string_to_db())
#
# date3 = Date.from_string('21.12.2023')
# print(date3.string_to_db())

# class Account:
#     rate_usd = 0.013  # 2
#     rate_eur = 0.011  # 3
#     suffix = 'RUB'
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value):
#         self.__num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счет №{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет №{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @property
#     def num(self):
#         return self.__num
#
#     @num.setter
#     def num(self, val):
#         self.__num = val
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print('Информация о счете:')
#         print('-' * 20)
#         print(f"№{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print('-' * 20)
#
#
# acc = Account("Долгих", '12345', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# acc.add_percents()
# print()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# print()

# class Account:
#     rate_usd = 0.013  # 2
#     rate_eur = 0.011  # 3
#     suffix = 'RUB'
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value):
#         self.__num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счет №{self.get_num()} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет №{self.__num} принадлежащий {self.surname} был закрыт.")
#
#     def get_num(self):
#         return self.__num
#
#     def set_num(self, val):
#         self.__num = val
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print('Информация о счете:')
#         print('-' * 20)
#         print(f"№{self.__num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print('-' * 20)
#
#
# acc = Account("Долгих", '12345', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# acc.add_percents()
# print()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# print()


# import geometry

# class Rectangle:
#     def __init__(self, breadth, length):
#         self.__breadth = breadth
#         self.__length = length
#
#     @property
#     def breadth(self):
#         return self.__breadth
#
#     @breadth.setter
#     def breadth(self, val):
#         if Rectangle.check_value(val):
#             self.__breadth = val
#         else:
#             print("Неверный тип данных")
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, val):
#         if Rectangle.check_value(val):
#             self.__length = val
#         else:
#             print("Неверный тип данных")
#
#     @staticmethod
#     def check_value(s):
#         if isinstance(s, (int, float)):
#             return True
#         return False
#
#     def square(self):
#         return self.__breadth * self.__length
#
#     def perimeter(self):
#         return (self.__breadth + self.__length) * 2
#
#     def hypotenuse(self):
#         return geometry.sqrt(self.__breadth ** 2 + self.__length ** 2)
#
#     def print_rectangle(self):
#         # for i in range(self.__length):
#         #     for j in range(self.__breadth):
#         #         print('*', end='')
#         #     print()
#         print(("*" * self.__breadth + "\n") * self.length)
#
#
# a = int(input("Введите длину прямоугольника: "))
# b = int(input("Введите ширину прямоугольника: "))
# # a = 15
# # b = 8
# obj = Rectangle(a, b)
# print("Длина прямоугольника:", obj.length)
# print("Ширина прямоугольника:", obj.breadth)
# obj.length = 3
# obj.breadth = 9
# print("Длина прямоугольника:", obj.length)
# print("Ширина прямоугольника:", obj.breadth)
# print("Площадь прямоугольника:", obj.square())
# print("Периметр прямоугольника:", obj.perimeter())
# print("Гипотенуза прямоугольника:", obj.hypotenuse())
# obj.print_rectangle()


# try:
#
#     class Rectangle:
#         def __init__(self, length, width):
#             self.length = length
#             self.width = width
#
#         def info(self):
#
#             print(f"Длина прямоугольника: {self.length}\nШирина прямоугольника: {self.width}")
#
#         def square(self):
#
#             print(f"Площадь прямоугольника:", self.length * self.width)
#             for i in range(self.length):
#                 for j in range(self.width):
#                     print("*", end=" ")
#                 print()
#
#         def perimeter(self):
#
#             print(f"Периметр прямоугольника:", 2 * (self.length + self.width))
#
#         def hypotenuse(self):
#
#             s = (self.length ** 2 + self.width ** 2) ** 0.5
#
#             print(f"Гипотенуза прямоугольника:", round(s, 2))
#
#
#     p1 = Rectangle('3', '9')
#
#     p1.info()
#
#     p1.square()
#
#     p1.perimeter()
#
#     p1.hypotenuse()
#
#
# except NameError:
#
#     print("Нет такого значения только цифры!")


# class Pound:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, n_kg):
#         try:
#             self.__kg = int(n_kg)
#             print(f"{self.__kg} kg => {round(self.__kg * 2.2, 2)} pounds")
#         except ValueError:
#             print("Введите число")
#
#
# vod = input("=> ")
# p = Pound(0)
# p.kg = vod

# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь!', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         # ['В', 'о', 'л', 'к', 'о', 'в', 'И', 'г', 'о', 'р', 'ь', 'Н', 'и', 'к', 'о', 'л', 'а', 'е', 'в', 'и', 'ч']
#         letters = "".join(re.findall("[a-zа-яё-]", fio, re.IGNORECASE))  # ВолковИгорьНиколаевич
#         for s in f:
#             # print(s.strip(letters))
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()  # ['1234', '567890']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, val):
#         self.verify_old(val)
#         self.__old = val
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# p1.fio = "Рыцарев Игорь Николаевич"
# print(p1.fio)
# print(p1.__dict__)


# class Point:
#     """Точка в двумерном пространстве"""
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# print(issubclass(Point, object))
# print(Point.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         print("Инициализатор базового класса")
#         self._sp = sp  # self._sp = Point(1, 2)
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределенный инициализатор Line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.draw_line()
#
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()


# class Figure:
#     ...
#     # родительский класс
#     # в инициализаторе __color
#
#
# class Rectangle:
#     ...
#     # дочерний класс
#
#     # создать метод нахождения площади фигуры
#
#     # проверка на ввод отрицательных значений

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     def get_color(self):
#         return self.__color
#
#     def set_color(self, color):
#         self.__color = color
#
#
# class Rectangle(Figure):
#
#     def __init__(self, w, h, color):
#         self.verify(w)
#         self.verify(h)
#         self.__w = w
#         self.__h = h
#         super().__init__(color)
#
#     def square(self):
#         return self.__w * self.__h
#
#     @staticmethod
#     def verify(val):
#         if val < 0:
#             raise ValueError('Переменная не должна быть отрицательной')
#
#     def get_info(self):
#         print(f'Высота: {self.__h}'
#               f'\nШирина: {self.__w}'
#               f'\nЦвет: {self.get_color()}'
#               f'\nПлощадь: {self.square()}')
#
#
# first = Rectangle(3, 6, 'red')
# first.set_color('blue')
# first.get_info()
# second = Rectangle(1, -1, 'blue')


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целочисленными")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.draw_line()
# line.set_coord(Point(20, 30), Point(100, 200))
# line.draw_line()


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, w, h, px):
#         super().__init__(w, h)
#         self.border = px
#
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка", self.border)
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px solid red")
# shape2.show_rect()


# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))
#
# a = [5, 6, 7]
# print(type(a))


# Перегрузка методов

# def func(a, b=None, c=None):
#     ...
#
#
# func(1, 2, 3)
# func(1, 2)
# func(1, c=5)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp=None, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print("Координата должны быть целочисленная")
#         elif sp is None:
#             if ep.is_int():
#                 self._ep = ep
#             else:
#                 print("Координата должны быть целочисленная")
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#             else:
#                 print("Координаты должны быть целочисленными")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.draw_line()
# line.set_coord(Point(20, 30), Point(100, 200))
# line.draw_line()
# line.set_coord(Point(-40, -60))
# line.draw_line()
#
# line.set_coord(ep=Point(500, 300))
# line.draw_line()


# Абстрактные методы

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw(self):  # абстрактный метод
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     # def draw(self):
#     #     print(f"Рисование прямоугольник: {self._sp}, {self._ep}, {self._color}, {self._width}")
#     ...
#
#
# figs = list()  # [Line(), Line(), Rect()]
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
#
# for f in figs:
#     f.draw()

# from geometry import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     # def calc_area(self):
#     #     return round(pi * self._radius ** 2, 2)
#     ...
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t2 = SqTable(20)
# print(t2.__dict__)
# print(t2.calc_area())
#
# t3 = RoundTable(radius=20)
# print(t3.__dict__)
# # print(t3.calc_area())


# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):  # Абстрактный класс
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         pass
#
#
# class Queen(Chess):
#     def move(self):
#         print("Ферзь перемещен на e2e4")
#
#
# # q = Chess()
# q = Queen()
# q.move()
# q.draw()


# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(f"{Euro.suffix} = {self.convert_to_rub():.2f} RUB")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
#
# print("*" * 50)
# for elem in d:
#     elem.print_value()
#     print(f"= {elem.convert_to_rub():.2f} RUB")
#
# print("*" * 50)
# for elem in e:
#     elem.print_value()


# Интерфейс

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child Class")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild Class")
#
#
# gc = GrandChild()
# gc.display1()
# gc.display2()

# Вложенные классы

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_method():
#         return "Метод внешнего класса"
#
#     def outer_obj(self):
#         return "Метод экземпляра"
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print(MyOuter.age, MyOuter.outer_method(), self.obj.outer_obj(), self.obj.name)
#
#
# out = MyOuter("внешний")
# inner = out.MyInner("внешний", out)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "LightGreen"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()
# class Intern:
#     def __init__(self):
#         self.name = "Smith"
#
#     def display(self):
#         print("Name:", self.name)
#
#
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = "Alba"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d2 = outer.head
# print()
# d1.display()
# print()
# d2.display()


# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("Outer")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("Inner")
#
#         class InnerClass:
#             def show(self):
#                 print("InnerClass")
#
#
# out = Outer()
# out.show()
# # inner1 = out.inner
# # inner1.show()
# # inner2 = inner1.inner_inner
# inner2 = out.inner.inner_inner
# inner2.show()

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         # self.os = self.OS()
#         # self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
#
# comp = Computer()
# # my_os = comp.os
# # my_cpy = comp.cpu
# my_os = Computer.OS()
# my_cpy = Computer.CPU()
# print(comp.name)
# print(my_os.system())
# print(my_cpy.make())
# print(my_cpy.model())

# class Base:
#     def __init__(self):
#         print("Инициализатор Base")  # отработал
#         # self.db = self.Inner()
#
#     def display(self):
#         print("Base")  # отработал
#
#     class Inner:
#         def display1(self):
#             print("Inner in Base")  # отработал
#
#
# class SubClass(Base):
#     def __init__(self):
#         print("SubClass")  # отработал
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print("Inner in SubClass")
#
#
# a = SubClass()
# a.display()
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = Cat("Пушок")
# print(cat)

# class Point:
#     def __init__(self, *args):
#         self.__coord = args  # ()
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(5, 7)
# print(len(p))
# p2 = Point(2, 4, 9)
# print(len(p2))


# import geometry
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = geometry.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# pt = Point(2, 7)
# print(pt.x)
# print(pt.y)
# pt.length = 10
# print(pt.length)
# pt.z = 5
# print(pt.__dict__)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# pt2 = Point2(1, 2)
# print("pt =", pt.__sizeof__())
# print("pt2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = ('z',)
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt = Point(1, 2)
# pt3 = Point3D(10, 20, 30)
# print(pt3.x)
# # pt3.z = 30
# print(pt3.z)
# print(pt3.__dict__)


# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def __init__(self, name):
#         print("Инициализатор Dog")
#         self.name = name
#
#     def bark(self):
#         print(self.name + " is barking")
#
#
# beast = Dog("Buddy")
# beast.bark()
# beast.sleep()
# beast.play()

#
# class A:
#     def __init__(self):
#         print("Инициализатор класса A")
#
#
# class AA:
#     def __init__(self):
#         print("Инициализатор класса AA")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#
# class C(AA):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#
# class D(B, C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#         print("Инициализатор класса D")
#
#
# d = D()
# print(D.mro())
# print(D.__mro__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Styles:
#     def __init__(self, color, width):
#         print("Инициализатор Styles")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, color="red", width=1):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         super().__init__(color, width)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line1 = Line(Point(10, 10), Point(100, 100))  #, "green", 5
# line1.draw()
#
# print(Line.__mro__)
# from geometry import sqrt
#
#
# class Pair:
#     def __init__(self, a, b):
#         self.A = a
#         self.B = b
#
#     def set_a(self, a):
#         self.A = a
#
#     def set_b(self, b):
#         self.B = b
#
#     def sum(self):
#         return self.A + self.B
#
#     def mult(self):
#         return self.A * self.B
#
#
# class RightTriangle(Pair):
#     def __init__(self, a, b):
#         super().__init__(a, b)
#         self.C = self.hypot()
#
#     def hypot(self):
#         hypot = round(sqrt(self.A ** 2 + self.B ** 2), 2)
#         print(f"Гипотенуза ABC: {hypot}")
#         return hypot
#
#     def print_info(self):
#         print(f"Прямоугольный треугольник ABC ({self.A}, {self.B}, {self.C})")
#
#     def square(self):
#         s = round(0.5 * self.mult(), 2)
#         print(f"Площадь ABC: {s}")
#         return s
#
#
# tr = RightTriangle(5, 8)
# tr.print_info()
# tr.square()
# print()
# print(f"Сумма: {tr.sum()}")
# print(f"Произведение: {tr.mult()}")
# print()
# tr.set_a(10)
# tr.hypot()
# tr.set_b(20)
# tr.hypot()
# print(f"Сумма: {tr.sum()}")
# print(f"Произведение: {tr.mult()}")
# tr.square()


# Миксины

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename="logfile.txt"):  # 'subclass.txt'
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='subclass.txt')
#
#
# subclass = MySubClass()
# subclass.display("Эта строка будет печататься и записываться в файл")


# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()
# n2 = NoteBook("HP", 1.5, 35000)
# n2.save_sell_log()


# Перегрузка операторов

# Число секунд в одном дне 24*60*60 = 86400

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec == other.sec
#         # if self.sec == other.sec:
#         #     return True
#         # return False
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         elif item == "min":
#             return (self.sec // 60) % 60
#         elif item == "sec":
#             return self.sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         elif key == "min":
#             self.sec = s + 60 * value + h * 3600
#         elif key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# c1["hour"] = 9
# c1["min"] = 61
# c1["sec"] = 32
# print(c1["hour"], c1["min"], c1["sec"])
# print(c1.get_format_time())
# c1 = Clock(100)
# c2 = Clock(100)
# # c4 = Clock(300)
# print(c1.get_format_time())
# print(c2.get_format_time())
# # print(c4.get_format_time())
# # c3 = c1 + c2 + c4
# # c1 += c2  # c1 = c1 + c2
# # print(c1.get_format_time())
# # if c1 == c2:
# #     print("Время одинаковое")
# # else:
# #     print("Время разное")
#
# if c1 != c2:
#     print("Время разное")
# else:
#     print("Время одинаковое")


# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good Kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(["M", "F"])) for _ in range(randint(1, 5))]  # 0, 5
#         else:
#             raise TypeError("Types are not supported")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Elsa", 5, "F")
# cat3 = Cat("Murzik", 5, "M")
# print(cat1)
# print(cat2)
# print(cat1 + cat2)


# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)  # [5, 5, 3, 4, 5]
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым неотрицательным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)  # 10 + 1 - 5 = 6
#             self.marks.extend([None] * off)  # [5, 5, 3, 4, 5, None, None, None, None, None, None]
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#
#         del self.marks[key]
#
#
# s1 = Student("Сергей", 5, 5, 3, 4, 5)
# # print(s1.marks[2])
# print(s1[2])
# s1[10] = 4
# del s1[2]
# print(s1.marks)

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.nb = self.NoteBook()
#
#     def display(self):
#         print(f"{self.name}", end=" ")
#         self.nb.display()
#
#     class NoteBook:
#         def __init__(self):
#             self.hp = "HP"
#             self.i7 = "i7"
#             self.memory = "16"
#
#         def display(self):
#             print(f"=> {self.hp}, {self.i7}, {self.memory}")
#
#
# stud = Student("Roman")
# stud.display()
# stud2 = Student("Vladimir")
# stud2.display()


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return self.a * 4
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
#
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
# # print(t1.get_per_tr(), t2.get_per_tr())
#
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_perimetr())

#
# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))  # "Python35"
#
#
# t1 = Number(10)
# t2 = Text("Python")
#
# print(t1.total(35))  # 45
# print(t2.total(35))  # 8

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я кот. меня зовут {self.name}. Мой возвраст {self.age}."
#
#     def sound(self):
#         return f"{self.name} мяукает"
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я собака. меня зовут {self.name}. Мой возвраст {self.age}."
#
#     def sound(self):
#         return f"{self.name} гав."
#
#
# c1 = Cat("Пушок", 2.5)
# # print(c1.info(), c1.sound())
# d2 = Dog("Мухтар", 4)
# # print(d2.info(), d2.sound())
#
# for animal in (c1, d2):
#     print(animal.info())
#     print(animal.sound())


# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for i in group:
#     i.info()

# Функторы

# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()

# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return string.strip(chars)
#
#     return wrap
#
#
# s1 = string_strip("?:!.,; ")
# print(s1(" ?Hello, World! , "))
#
#
# class StringStrip:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):   # string
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return args[0].strip(self.__chars)
#
#
# s2 = StringStrip("?:!.,; ")
# print(s2(" ?Hello, World! , "))


# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self):
#         print('Перед вызовом функции')
#         self.fn()
#         print('После вызова функции')
#
#
# @MyDecorator
# def func():
#     print("text")
#
#
# func()


# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, x, y):
#         res = self.fn(x, y)
#         return f'Перед вызовом функции\n{res}\nПосле вызова функции'
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))

# class Power:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, x, y):
#         return self.fn(x, y) ** 2
#
#
# @Power
# def func(a, b):
#     return a * b
#
#
# print("Результат:", func(2, 3))

# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, *args, **kwargs):
#         res = self.fn(*args, **kwargs)
#         return f'Перед вызовом функции\n{res}\nПосле вызова функции'
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# @MyDecorator
# def func1(a, b, c):
#     return a * b * c
#
#
# @MyDecorator
# def func2(a, b, c):
#     return a + b + c
#
#
# print(func(2, 5))
# print(func1(2, 5, 2))
# print(func2(2, c=5, b=2))


# class MyDecorator:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, fn):
#         def wrap(*args, **kwargs):
#             res = fn(*args, **kwargs)
#             return f'{self.arg} {res}'
#
#         return wrap
#
#
# @MyDecorator("Произведение:")
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))
# print(func(12, 5))


# class Power:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, x, y):
#         return self.fn(x, y) ** 2
#
#
# @Power
# def func(a, b):
#     return a * b
#
#
# print("Результат:", func(2, 3))


# class MyDecorator:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, fn):
#         def wrap(*args, **kwargs):
#             res = fn(*args, **kwargs)
#             return res ** self.arg
#
#         return wrap
#
#
# @MyDecorator(6)
# def func(a, b):
#     return a * b
#
#
# print("Результат:", func(2, 2))

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Красов")
# p1.info()

# def decorator(cls):
#     class Wrapper(cls):
#         def double(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print(f"Инициализатор ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.double(4))


# Дескрипторы
# __get__()
# __set__()
# __delete__()
# __set_name__()

# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise TypeError(f"{value} должно быть строкой")
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)

# @property
# def name(self):
#     return self.__name
#
# @name.setter
# def name(self, value):
#     if not isinstance(value, str):
#         raise TypeError(f"{value} должно быть строкой")
#     self.__name = value
#
# @property
# def surname(self):
#     return self.__surname
#
# @surname.setter
# def surname(self, value):
#     if not isinstance(value, str):
#         raise TypeError(f"{value} должно быть строкой")
#     self.__surname = value


# p = Person("Ivan", "Petrov")
# print(p.name.get())

# Дескрипторы
# __get__()
# __set__()
# __delete__()
# __set_name__()

# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise TypeError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Ivan", "Petrov")
# print(p.name)
# print(p.surname)

# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f"Координата {coord} должна быть числом")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         Integer.verify_coord(value)
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# print(p1.__dict__)
# print(p1.x, p1.y, p1.z)

# Метакласс
# a = 5
# print(type(a))
# print(type(int))

# class MyList(list):
#     def get_length(self):
#         return len(self)

# MyList = type(
#     'MyList',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
#
# lst = MyList()
# lst.append(5)
# lst.append(8)
# lst.append(9)
# print(lst, lst.get_length())

# Создание модулей

# import geometry
# from random import randint


# import geometry.rect
# import geometry.sq
# import geometry.trian

# import geometry  # работать не будет
# from geometry import *
# from geometry import rect, sq, trian
#
#
# def run():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#     for g in shape:
#         print(g.get_perimetr())
#
#
# if __name__ == '__main__':
#     run()


# from car.elecrtocar import ElectroCar
#
#
# if __name__ == '__main__':
#     e_car = ElectroCar("Tesla", "T", 2018, 99000, 100)
#     e_car.show_car()
#     e_car.description_battery()


# Сериализация (упаковка данных) и десириализация (распаковка данных)

# marshal  (*.pyc)
# pickle
# json

# import pickle

# file_name = "basket.txt"
#
# shop_list = {
#     "фрукты": ['яблоки', 'манго'],
#     "овощи": ("морковь", "лук"),
#     "бюджет": 1000
# }
#
# with open(file_name, "wb") as f:
#     pickle.dump(shop_list, f)
#
# with open(file_name, "rb") as f:
#     shop_list_2 = pickle.load(f)
#
# print(shop_list_2)
# print(type(shop_list_2))

# class Text:
#     num = 35
#     string = "Привет"
#     lst = [1, 2, 3]
#     tpl = (22, 23)
#     d = {"first": 1, "second": 2}
#
#     def __str__(self):
#         return f"Число: {Text.num}\nСтрока: {Text.string}\nСписок: {Text.lst}\nКортеж: {Text.tpl}\nСловарь: {Text.d}"
#
#
# obj = Text()
#
# obj1 = pickle.dumps(obj)
# print(obj1)
# obj2 = pickle.loads(obj1)
# print(obj2)
# print(type(obj2))

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)

# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     def __init__(self, name, color, a):
#         self._color = color
#         self._name = name
#         self._a = a
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, name):
#         self._name = name
#
#     def get_color(self):
#         return self._color
#
#     def set_color(self, color):
#         self._color = color
#
#     def get_a(self):
#         return self._a
#
#     def set_a(self, a):
#         self._a = a
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#     @abstractmethod
#     def square(self):
#         pass
#
#     @abstractmethod
#     def print_figure(self):
#         pass
#
#     @abstractmethod
#     def get_info(self):
#         pass
#
#
# class Square(Shape):
#     def perimeter(self):
#         return self._a * 4
#
#     def square(self):
#         return self._a * self._a
#
#     def print_figure(self):
#         return f'{"*" * self._a}\n' * self._a
#
#     def figure(self):
#         print(f'==={self._name}===\n'
#               f'Сторона: {self._a}\n'
#               f'Цвет :{self._color}')
#
#     def get_info(self):
#         self.figure()
#         print(f'Площадь: {self.square()}\n'
#               f'Периметр: {self.perimeter()}\n'
#               f'{self.print_figure()}')
#
#
# class Rectangle(Square):
#     def __init__(self, name, color, a, b):
#         super().__init__(name, color, a)
#         self._b = b
#
#     def get_b(self):
#         return self._b
#
#     def set_b(self, b):
#         self._b = b
#
#     def perimeter(self):
#         return (self._a + self._b) * 2
#
#     def square(self):
#         return self._a * self._b
#
#     def figure(self):
#         print(f'==={self._name}===\n'
#               f'Длина: {self._a}\n'
#               f'Ширина: {self._b}\n'
#               f'Цвет :{self._color}')
#
#     def print_figure(self):
#         a = self._a
#         b = self._b
#         if a < b:
#             a, b = b, a
#         return f'{"*" * a}\n' * b
#
#
# class Triangle(Rectangle):
#     def __init__(self, name, color, a, b, c):
#         super().__init__(name, color, a, b)
#         self.__c = c
#
#     def get_c(self):
#         return self.__c
#
#     def set_c(self, c):
#         self.__c = c
#
#     def perimeter(self):
#         return self._a + self._b + self.__c
#
#     def square(self):
#         p = self.perimeter() / 2
#         return round((p * (p - self._a) * (p - self._b) * (p - self.__c)) ** 0.5, 2)
#
#     def figure(self):
#         print(f'==={self._name}===\n'
#               f'Сторона A: {self._a}\n'
#               f'Сторона B: {self._b}\n'
#               f'Сторона C: {self.__c}\n'
#               f'Цвет :{self._color}')
#
#     def print_figure(self):
#         a = round((self._a + self._b) / 2)
#         c = self.__c
#         if c < a:
#             a, c = c, a
#         step = round(c / a)
#         prnt = ''
#         for i in range(a):
#             prnt += f'{" " * (step * (a - i) // 2)}*{"*" * step * i}\n'
#         return prnt
#
#
# lst = (Square('Квадрат', 'red', 3),
#        Rectangle('Прямоугольник', 'green', 3, 7),
#        Triangle('Треугольник', 'yellow', 6, 6, 11))
#
# for i in lst:
#     i.get_info()


# from math import sqrt
#
#
# class Shape:
#     def __init__(self, color):
#         self.color = color
#
#
# class Square(Shape):
#     def __init__(self, a):
#         super().__init__(color="red")
#         self.a = a
#
#     def squar(self):
#         print("===Квадрат===")
#         print(f"Сторона:{self.a}")
#         print(f"Цвет:{self.color}")
#         print(f"Площадь:{self.a * self.a}")
#         print(f"Периметр:{self.a + self.a + self.a + self.a}")
#         print((" * " * self.a + "\n") * self.a)
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         super().__init__(color="green")
#         self.a = a
#         self.b = b
#
#     def recta(self):
#         print("===Прямоугольник===")
#         print(f"Длина:{self.a}")
#         print(f"Ширина:{self.b}")
#         print(f"Цвет:{self.color}")
#         print(f"Площадь:{self.a * self.b}")
#         print(f"Периметр:{self.a + self.b + self.a + self.b}")
#         print((" * " * self.b + "\n") * self.a)
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         super().__init__(color="yellow")
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def tria(self):
#         print("===Треугольник===")
#         print(f"Сторона a:{self.a}")
#         print(f"Сторона b:{self.b}")
#         print(f"Сторона c:{self.c}")
#         print(f"Цвет:{self.color}")
#         p = (self.a + self.b + self.c) / 2
#         d = round(sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 2)
#         print(f"Площадь:", d)
#         print(f"Периметр:{(self.a + self.b + self.c) / 2}")
#         for i in range(self.a - 4):
#             print(' ' * (self.a - i) + '*' * (2 * i - 1))
#
#
# s = Square(3)
# s.squar()
# r = Rectangle(3, 7)
# r.recta()
# t = Triangle(11, 6, 6)
# t.tria()

# from abc import ABC, abstractmethod
# import math
#
#
# class Shape(ABC):
#     def __init__(self, *args, **kwargs):
#         self.args = args
#         self.kwrgs = kwargs
#
#     @abstractmethod
#     def perimeter(self):
#         print(" ")
#
#     @abstractmethod
#     def area(self):
#         print(" ")
#
#     @abstractmethod
#     def paint_figure(self):
#         print(" ")
#
#
# class Square:
#     def __init__(self, arg, color):
#         self.arg = arg
#         self.color = color
#
#     def area(self):
#         return self.arg * self.arg
#
#     def perimeter(self):
#         return self.arg * 4
#
#     def paint_figure(self):
#         print((f"{self.color * self.arg}\n") * self.arg)
#
#     def print_info(self):
#         print("===Квадрат===")
#         print(f"Сторона: {self.arg}")
#         print(f"Цвет: {self.color}")
#         print(f"Площадь: {self.area()}")
#         print(f"Периметр: {self.perimeter()}")
#         self.paint_figure()
#
#
# class Rectengle:
#     def __init__(self, width, height, color):
#         self.width = width
#         self.height = height
#         self.color = color
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return (self.height + self.width) * 2
#
#     def paint_figure(self):
#         print((f"{self.color * self.width}\n") * self.height)
#
#     def print_info(self):
#         print("===Прямоуголник===")
#         print(f"Длинна : {self.height}")
#         print(f"Ширина: {self.width}")
#         print(f"Цвет: {self.color}")
#         print(f"Площадь: {self.area()}")
#         print(f"Периметр: {self.perimeter()}")
#         self.paint_figure()
#
#
# class Triangle:
#     def __init__(self, arg_a, arg_b, arg_c, color):
#         self.arg_a = arg_a
#         self.arg_b = arg_b
#         self.arg_c = arg_c
#         self.color = color
#
#     def area(self):
#         p = (self.arg_a + self.arg_b + self.arg_c) * 0.5
#         return round((p * (p - self.arg_a) * (p - self.arg_b) * (p - self.arg_c)) ** 0.5, 2)
#
#     def perimeter(self):
#         return self.arg_a + self.arg_b + self.arg_c
#
#     def paint_figure(self):
#         r = 0
#         for i in range(self.arg_b):
#             r += 1
#             print((self.color * (i + r)).center(self.arg_a, " "))
#
#     def print_info(self):
#         print("===Треуголник===")
#         print(f"Сторона 1 : {self.arg_a}")
#         print(f"Сторона 2: {self.arg_b}")
#         print(f"Сторона 3: {self.arg_c}")
#         print(f"Цвет: {self.color}")
#         print(f"Площадь: {self.area()}")
#         print(f"Периметр: {self.perimeter()}")
#         self.paint_figure()
#
#
# ls = [
#     Square(3, " + "),
#     Rectengle(7, 3, " * "),
#     Triangle(11, 6, 6, "#")
# ]
#
# for cl in ls:
#     cl.print_info()

# import json

# data = {
#     'name': 'Olga',
#     "age": 35,
#     '20': None,
#     'True': 1,
#     'hobbies': ('running', 'singing'),
#     'children': [
#         {
#             'first_name': 'Alice',
#             'age': 6
#         }
#     ]
# }
#
# # with open("data_file.json", "w") as fw:
# #     json.dump(data, fw, indent=4)
# #
# # with open("data_file.json", "r") as fw:
# #     data1 = json.load(fw)
# #     print(data1)
#
# json_string = json.dumps(data, sort_keys=True)
# print(json_string)
# print(type(json_string))
# data2 = json.loads(json_string)
# print(data2)
# print(type(data2))

# x = {
#     "name": "Виктор"
# }
# print(json.dumps(x))
# print(json.dumps(x, ensure_ascii=False))

# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open("persons.json"))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())


# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __str__(self):
#         # a = ""
#         # for i in self.marks:
#         #     a += str(i) + ", "
#         # return f"Студент: {self.name}: {a[:-2]}"
#
#         # a = ", ".join(map(str, self.marks))
#         # return f"Студент: {self.name}: {a}"
#
#         return f"Студент: {self.name}: {', '.join(map(str, self.marks))}"
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     def dump_to_json(self, file_name):
#     def dump_to_json(self, file_name):
#         data = {"name": self.name, "marks": self.marks}
#         with open(file_name, "w") as f:
#             json.dump(data, f)
#
#     def load_from_file(self, file_name):
#         with open(file_name, "r") as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, gr):
#         self.students = students
#         self.group = gr
#
#     def __str__(self):
#         # a = ""
#         # for i in self.students:
#         #     a += str(i) + "\n"
#         # return f"{a}"
#
#         return "\nГруппа: " + self.group + "\n" + '\n'.join(map(str, self.students))
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     def dump_group(self, file_name):
#         with open(file_name, 'w') as f:
#             stud_list = []
#             for i in self.students:
#                 stud_list.append([i.name, i.marks])
#             json.dump(stud_list, f)
#
#     def upload_group(self, file_name):
#         with open(file_name, "r") as f:
#             print(json.load(f))
#
#
#
# st1 = Student("Bodnya", 5, 4, 3, 4, 5, 3)
#
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(3)
# # print(st1)
# # st1.edit_mark(2, 4)
# # print(st1)
# # print(st1.average_mark())
#
# # st1.dump_to_json("st1.json")
# # st1.load_from_file("st1.json")
#
# st2 = Student("Nikolaenko", 2, 3, 5, 4, 2)
# st3 = Student("Birukov", 3, 5, 3, 2, 5, 4)
#
# sts = [st1, st2]
# my_group = Group(sts, "ГК Python")
# # print(my_group)
# my_group.add_student(st3)
# # print(my_group)
# my_group.remove_student(1)
# # print(my_group)
#
# group22 = [st2]
# my_group2 = Group(group22, "ГК Web")
# # print(my_group2)
#
# Group.change_group(my_group, my_group2, 0)
#
# # print(my_group)
# # print(my_group2)
# file = "group2.json"
# my_group2.dump_group(file)
# my_group2.upload_group(file)

# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# todos_by_user = {}  # {1: 11, 2: 8, 3: 7, 4: 6, 5: 12, 6: 6, 7: 9, 8: 11, 9: 8, 10: 12}
#
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo["userId"]] += 1  # todos_by_user[2] = todos_by_user[2] + 1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1  # todos_by_user[2] = 1
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)  # [(5, 12), (10, 12), (1, 11), (8, 11), (7, 9), (2, 8), (9, 8), (3, 7), (4, 6), (6, 6)]
#
# max_complete = top_users[0][1]
# print(max_complete)  # 12
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:  # 11 < 12
#         break
#     users.append(str(user))
# print(users)  # ['5', '10']
# # users = ["10"]
#
# max_users = " and ".join(users)
# print(max_users)
#
# s = "s" if len(users) > 1 else ""
# print(f"User{s} {max_users} completed {max_complete} TODOs")
#
#
# def keep(td):
#     is_complete = td["completed"]
#     has_max_count = str(td["userId"]) in users
#     return is_complete and has_max_count
#
#
# with open("filter_max_completed.json", "w") as f:
#     filter_todos = list(filter(keep, todos))
#     json.dump(filter_todos, f, indent=2)

# CSV (Comma Separated Values)

# import csv

# with open("data.csv") as r_file:
#     file_reader = csv.reader(r_file, delimiter=";")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1
#     print(f"Всего в файле {count} строки.")


# with open("data.csv") as r_file:  # , encoding="utf-8"
#     fields = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(r_file, delimiter=";", fieldnames=fields)
#     count = 0
#     for row in file_reader:
#         # print(row)
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#
#         print(f"\t{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году.")
#         count += 1
#     print(f"Всего в файле {count} строки.")


# with open("student.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open("sw_data.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)

#
# with open("sw_data.csv") as f:
#     print(f.read())


# with open("student1.csv", "w") as f:
#     names = ["Имя", "Возраст"]
#     file_writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({"Имя": "Женя", "Возраст": 6})
#     file_writer.writerow({"Имя": "Маша", "Возраст": 15})
#     file_writer.writerow({"Имя": "Вова", "Возраст": 14})


# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dict.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)


# print(list(data[0].keys()))


# import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# # print(response.text)
#
# todos = json.loads(response.text)
# # for i in todos:
# #     print(i)
#
# with open('todos.csv', 'w') as f:
#     writer = csv.DictWriter(f, todos[0].keys(), delimiter=';', lineterminator='\r', )
#     writer.writeheader()
#     for i in todos:
#         writer.writerow(i)

# Парсинг

# from bs4 import BeautifulSoup

# f = open("index.html", encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find("div", class_="name")
# row = soup.find_all("div", class_="name")
# row = soup.find_all("div", {"class": "name"})
# row = soup.find_all("div", class_="row")[1].find("div", class_="links")
# row = soup.find("div", {"data-set": "salary"})
# row = soup.find("div", id="whois")
# row = soup.find("div", string="Alena").parent.parent
# row = soup.find("div", string="Alena").find_parent(class_="row")
# row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
# print(row)

# def get_copyrigter(tag):
#     whois = tag.find("div", class_="whois").text
#     two = tag.find("div", class_="python").text
#     if "Copywriter" == whois and "Copywriter" == two:
#         return tag
#     return None
#
#
# f = open("index.html", encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# copywriter = []
# row = soup.find_all("div", class_="row")
# for i in row:
#     cw = get_copyrigter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)

# import re
#
#
# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open("index.html", encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# salary = soup.find_all("div", {"data-set": "salary"})
#
# for i in salary:
#     get_salary(i.text)

# import requests

# r = requests.get("https://ru.wordpress.org/")
# # print(r.status_code)
# # print(r.headers)
# # print(r.headers['Content-Type'])
# # print(r.headers['content-type'])
# # print(r.content)
# print(type(r.text))
# print(r.text)


# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     return re.sub(r"\D+", "", s)
#
#
# def write_csv(data):
#     with open("plugin.csv", "a") as f:
#         writer = csv.writer(f, lineterminator='\r', delimiter=";")
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     s = soup.find(id="main").find_all("section", class_="plugin-section")[-1]
#     plugins = s.find_all("article", class_="plugin-card")
#
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         # url = plugin.find("h3").find("a").get("href")
#         url = plugin.find("h3").find("a")["href"]
#         rating = plugin.find("span", class_="rating-count").find("a").text
#         r = refined(rating)
#
#         data = {'name': name, "url": url, "rating": r}
#         write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/photos")
# album = json.loads(response.text)
#
# albums = []
# for i in album:
#     if i['albumId'] % 2 == 0:
#         albums.append(i)
#
# # print(albums)
#
# with open("album.json", "w") as f:
#     json.dump(albums, f, indent=2)
#
# import csv
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open("plugin1.csv", "a", encoding="utf-8-sig") as f:
#         writer = csv.writer(f, lineterminator='\r', delimiter=";")
#         writer.writerow((data['name'], data['snippet'], data['active'], data['test_cy']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("article", class_="plugin-card")
#     for el in p1:
#         try:
#             name = el.find("h3").text
#         except AttributeError:
#             name = ''
#
#         try:
#             snippet = el.find("div", class_="entry-excerpt").text.strip()
#         except AttributeError:
#             snippet = ""
#
#         try:
#             active = el.find("span", class_="active-installs").text.strip()
#         except AttributeError:
#             active = ""
#
#         try:
#             test = el.find("span", class_="tested-with").text.strip()
#             test_cy = refine_cy(test)
#         except AttributeError:
#             test_cy = ""
#
#         data = {
#             'name': name,
#             'snippet': snippet,
#             'active': active,
#             'test_cy': test_cy
#         }
#         write_csv(data)
#
#
# def main():
#     for i in range(15, 50):
#         url = f"https://ru.wordpress.org/plugins/browse/popular/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# from parsers import Parser
#
#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/news/", "news.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()


# MVC
# Model (модель)
# View (вид или представление)
# Controller (контроллер)


# Сокет

# import socket
# from view import index, blog
#
#
# URLS = {
#     '/': index,
#     '/blog': blog
# }
#
#
# def parse_request(request):
#     parsed = request.split()
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != 'GET':
#         return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 404 Page Not Found!\n\n', 404
#     return 'HTTP/1.1 200 OK!\n\n', 200
#
#
# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Page Not Found!</h3>'
#     elif code == 405:
#         return '<h1>405</h1><h3>Method Not Allowed!</h3>'
#     return URLS[url]()
#
#
# def generate_response(request):
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     body = generate_content(code, url)
#     return (headers + body).encode()
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))  # 127.0.0.1:5000
#     server_socket.listen()
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#         print(f"Клиент: {addr} => \n{request.decode('utf-8')}\n")
#
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#         client_socket.close()
#
#
# if __name__ == "__main__":
#     run()


# import sqlite3

# con = sqlite3.connect("profile.db")
# cur = con.cursor()
#
# cur.execute("""
# """)
#
# con.close()

# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()
#     # cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # summa REAL,
#     # date TEXT
#     # )""")
#     cur.execute("DROP TABLE users")


# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()
#
#     cur.execute("""
#     DROP TABLE person_table
#     """)

# cur.execute("""
# ALTER TABLE person_table
# RENAME COLUMN address TO home_address;
# """)

# cur.execute("""
# ALTER TABLE person_table
# DROP COLUMN address
# """)

# cur.execute("""
# ALTER TABLE person_table
# ADD COLUMN address TEXT NOT NULL DEFAULT "city, street"
# """)

# cur.execute("""
# ALTER TABLE person
# RENAME TO person_table;
# """)

# cur.execute("""CREATE TABLE IF NOT EXISTS person(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# phone BLOB NOT NULL DEFAULT "+79090000000",
# age INTEGER CHECK(age > 0 AND age < 100),
# email TEXT UNIQUE
# )""")


# with sqlite3.connect("db_3.db") as con:
#     cur = con.cursor()
# cur.execute("""
#     SELECT *
#     FROM T1
#     LIMIT 2, 5;
# """)

# res = cur.fetchone()
# print(res)
# res2 = cur.fetchmany(2)
# print(res2)
# res3 = cur.fetchall()
# print(res3)

# for i in cur:
#     print(i)

# with sqlite3.connect("education.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS student(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         surname TEXT NOT NULL,
#         name TEXT NOT NULL,
#         patronymic TEXT NOT NULL,
#         age INTEGER NOT NULL CHECK(age >= 16 AND age <= 45),
#         [group] TEXT NOT NULL,
#         FOREIGN KEY ([group]) REFERENCES groups (id) ON DELETE RESTRICT
#     )""")
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS groups(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         group_name TEXT NOT NULL
#     )""")
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS lessons(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         lesson_title TEXT NOT NULL
#     )""")
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS association (
#         lesson_id INTEGER NOT NULL,
#         group_id INTEGER NOT NULL,
#         FOREIGN KEY (group_id) REFERENCES groups(id)
#         FOREIGN KEY (lesson_id) REFERENCES lessons(id)
#     )""")


import sqlite3


# cars = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000),
# ]
#
# with sqlite3.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS car(
#          car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#          model TEXT,
#          price INTEGER
#     )
#     """)
#
#     cur.executescript("""
#     DELETE FROM car WHERE model LIKE 'B%';
#     UPDATE car SET price = price + 100;
#     """)

# cur.execute("UPDATE car SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})

# cur.executemany("INSERT INTO car VALUES(NULL, ?, ?)", cars)

# for car in cars:
#     cur.execute("INSERT INTO car VALUES(NULL, ?, ?)", car)

# cur.execute("INSERT INTO car VALUES(1, 'Renault', 22000)")
# cur.execute("INSERT INTO car VALUES(2, 'Volvo', 29000)")
# cur.execute("INSERT INTO car VALUES(3, 'Mercedes', 57000)")
# cur.execute("INSERT INTO car VALUES(4, 'Bentley', 35000)")
# cur.execute("INSERT INTO car VALUES(5, 'Audi', 52000)")

# con.commit()
# con.close()

# con = None
# try:
#     con = sqlite3.connect("cars.db")
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS car(
#          car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#          model TEXT,
#          price INTEGER
#     );
#     BEGIN;
#     INSERT INTO car VALUES(NULL, 'Renault', 22000);
#     UPDATE car2 SET price = price + 100;
#     """)
#     con.commit()
# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса", e)
# finally:
#     if con:
#         con.close()

# with sqlite3.connect("cars.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS car(
#          car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#          model TEXT,
#          price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     )
#     """)

# cur.execute("SELECT model, price FROM car")
# for res in cur:
#     print(res['model'], res['price'])
# row = cur.fetchone()
# print(row)
# row2 = cur.fetchmany(5)
# print(row2)
# row3 = cur.fetchall()
# print(row3)


# cur.execute("INSERT INTO car VALUES(NULL, 'Запорожец', 1000)")
# last_row_id = cur.lastrowid
# buy_car_id = 2
# cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))

# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#     return True
#
#
# with sqlite3.connect("cars.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#        name TEXT,
#        ava BLOB,
#        score INTEGER
#     );
#     """)
#
#     # cur.execute("SELECT ava FROM users")
#     # img = cur.fetchone()['ava']
#     # write_ava("out.png", img)
#
#     img = read_ava(2)
#     if img:
#         binary = sqlite3.Binary(img)
#         cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))


# with sqlite3.connect("cars.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "w") as f:
#         for sql in con.iterdump():
#             f.write(sql)

# with sqlite3.connect("cars.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)

# ORM

# pip install sqlalchemy
