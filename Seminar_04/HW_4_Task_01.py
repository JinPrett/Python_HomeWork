"""
Задача 4.01
Вычислить число c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""

from math import pi

def get_count(d_round):
    s = str(d_round)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0

d_orig = input("Введите число для заданной точности числа Пи:\n")
d_round = d_orig
s = str(d_round)
d_round = (abs(s.find('.') - len(s)) - 1)

print(f'число Пи с заданной точностью {d_orig} равно {round(pi, d_round)}')