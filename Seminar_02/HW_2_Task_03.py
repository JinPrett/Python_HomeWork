"""
Задача 2.04: 
Задать список из N элементов, заполненных числами из [-N, N]. 
Найти произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число.
"""

import random

def write_file(number):
    with open('file_HW_task_04.txt', 'w') as data:
        for i in range(number):
            data.write(f"{random.randrange(0, 2*number)}\n")


def read_file():
    with open('file_HW_task_04.txt', 'r') as data:
        indexs = list(map(int, data.readlines()))
    return indexs
