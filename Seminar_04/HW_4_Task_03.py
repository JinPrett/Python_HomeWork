"""
Задача 4.03: 
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
"""

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")