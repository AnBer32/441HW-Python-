# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

my_list = [(round(random.uniform(0,10), 2)) for i in range(5)]
print(my_list)

result = [(int(my_list[i]*100)%100) for i in range(5)]

print((max(result) - min(result))/100)
