# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint as RI 
my_list = [(RI(1,10)) for i in range (int(RI(4,8)))]
print(my_list)

def get_mult_pairs(my_list):
    result = [(my_list[i]*my_list[len(my_list)-i-1]) for i in range (len(my_list))]
    for i in range (len(result)):
        if i > (len(result)/2):        
            del result[-1]        

    if len(my_list) % 2 == 0:
        del result[-1]
    return result

print(get_mult_pairs(my_list))