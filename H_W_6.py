# Урок 6. Повторение списков

# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


# first_element = int(input("Введите первый элемент: "))
# increment  = int(input("Введите инкремент: "))
# array_length = int(input("Введите размер массива: "))
# lst = []

# for i in range(array_length):
#     lst.append(first_element + (i)*increment)
# print(lst)


######################################


# first_element = int(input("Введите первый элемент: "))
# increment  = int(input("Введите инкремент: "))
# array_length = int(input("Введите размер массива: "))
# lst = []
# lst= [i for i in range(first_element, first_element+increment*array_length, increment)]
# print(lst)

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


a = int(input('Введите верхнюю границу поиска: '))
b = int(input('Введите нижнюю границу поиска: '))
lst = [i * 2 for i in range(10) if i % 2 == 0]
print(lst)
for i in range(lst[-1],lst[0]-1,-4):
    lst.append(i)
print(lst)

for i in range(len(lst)):
    if b<lst[i]<a:
        print(i)
