# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

# n = int(input('Введите число: '))
# dict = {}
# for i in range(1, n + 1):
#     dict[i] = 3 * i + 1
# print(dict)



# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# start = False
# while start == False:
#     n = int(input('Введите положительное число: '))
#     if n >= 1:
#         start = True
#     else:
#         print('Неправильное число')
# lst = [1]
# for i in range(2, n + 1):
#     lst.append(lst[i - 2] * i)
# print(lst)



# Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.

# start = False
# while start == False:
#     n = int(input('Введите положительное число: '))
#     if n >= 1:
#         start = True
#     else:
#         print('Неправильное число')
# result = 0
# for i in range(1, n + 1):
#     result += (1 + 1 / i) ** i
# print(round(result, 2))



# Задайте число N и создайте список, заполненный числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# n = int(input('Введите число: '))
# if n < 0:
#     n = -n
# lst = []
# for i in range(-n, n + 1):
#     lst.append(i)
# print(lst)
# a = open('file.txt', 'r')
# x = a.readlines()
# a.close()
# result = 1
# for i in range(len(x)):
#     x[i] = int(x[i])
#     print(x[i])
#     result *= lst[x[i]]
# print(x, result)


# Реализуйте алгоритм перемешивания списка

import datetime

n = int(input('Введите число: '))
if n < 0:
    n = -n
lst = []
for i in range(0, n + 1):
    lst.append(i)
print(lst)
shuflle_lst = []
for i in range(len(lst)):
    shuflle_lst.append(lst[(i + datetime.datetime.now().microsecond % len(lst)) % len(lst)])
    del lst[(i + datetime.datetime.now().microsecond % len(lst)) % len(lst)]
print(shuflle_lst)
