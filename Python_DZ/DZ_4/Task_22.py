'''Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов 
второго множества. Затем пользователь вводит сами элементы множеств.'''

from random import randint

n1 = int(input("Введите длинну списка 1: "))
n2 = int(input("Введите длинну списка 2: "))

list_1 = [randint(1, 10) for i in range(1, n1+1)]
set1 = set(list_1)
print(list_1)

list_2 = [randint(1, 10) for j in range(1, n2+1)]
set2 = set(list_2)
print(list_2)

print(sorted(set1.intersection(set2)))