"""
Задача 6.01:
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
"""

from cmath import sqrt
import math
Xa = float(input('Введите начальную координату первой точки: '))
Ya = float(input('Введите конечную координату первой точки: '))
Xb = float(input('Введите начальную координату второй точки: '))
Yb = float(input('Введите конечную координату второй точки: '))
distance = math.sqrt((Xb - Xa)**2 + (Yb-Ya)**2)
print(distance)