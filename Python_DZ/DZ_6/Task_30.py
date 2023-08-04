"""Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена
 прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""

from random import randint

first_element = randint(1,10)
print(f'Первый элемент прогрессии: {first_element}')
progression_difference = randint(1,20)
print(f'Разность прогрессии: {progression_difference}')
count_elements = randint(1,20)
print(f'Количество элементов прогрессии: {count_elements}')

# Создание и заполнение списка элементами арифметической прогрессии
progression = [first_element + (i-1) * progression_difference for i in range(1, count_elements+1)]

# Вывод списка на экран
print("Массив элементов арифметической прогрессии:")
for num in progression:
    print(num, end=", ")