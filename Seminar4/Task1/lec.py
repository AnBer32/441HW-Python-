# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

import random, os

def create_my_dict():
    my_dict = {}
    n = int(input('Введите максимальную степень: '))
    for i in range(n, -1, -1):
        if i == n:
            while True:
                koef = random.randint(0, 100)
                if koef != 0:
                    break
            my_dict[i] = koef
        else:
            my_dict[i] = random.randint(0, 100)    
    print(str(my_dict))
    return my_dict

def get_equation(my_dict):
    equation =''
    for item in my_dict:
        value = ''
        if(my_dict[item] == 0):
            continue    
        if(my_dict[item] == 1):
            value = ''
        else:
            value = str(my_dict[item])

        x = ''
        if(item == 0 and my_dict[item] == 1):
            x = '1'
        elif(item == 0):
            x = ''
        elif(item == 1 and my_dict[item] != 1):
            x = '*x'
        elif(item == 1):
            x = 'x'
        elif(my_dict[item] == 1):
             x = 'x**' + str(item)
        else:
            x = '*x**' + str(item)
        
        if(equation != ''):
            equation = equation + ' + ' + value + x
        else: 
            equation = value + x
    equation = equation + ' = 0'    
    print(equation)    
    return equation

def write_file(filename, value):
    f = open(os.path.join(os.path.dirname(__file__), filename), "w")
    f.write(value)
    f.close()

#equation1
my_dict = create_my_dict()
equation = get_equation(my_dict)
write_file("equation1", equation)

#equation2
my_dict = create_my_dict()
equation = get_equation(my_dict)
write_file("equation2", equation)
