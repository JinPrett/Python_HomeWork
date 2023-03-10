"""
Задача 2.03: 
Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму.
Пример: 
- Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
        Сумма 9.06
"""

n = int(input("Введите число n: "))
s = 0
for i in range(1, n+1):
    s += (1+1/i)**i
print(f"Полученная сумма последовательности (1+1/n)^n равнна {round(s,2)}")