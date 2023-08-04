"""Задача 32: Определить индексы элементов массива (списка), значения которых 
принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)"""

from random import randint

def find_indexes(arr, min_val, max_val):
    indexes = []
    for i in range(len(arr)):
        if arr[i] >= min_val and arr[i] <= max_val:
            indexes.append(i)
    return indexes

arr = [randint(1,10) for _ in range(10)]
print(f'Изначальный массив (список): {arr}')
min_val = randint(1,5)
max_val = randint(5,10)
result = find_indexes(arr, min_val, max_val)
print(f"Индексы элементов, принадлежащих диапазону [от {min_val} до {max_val}]: {result}")
