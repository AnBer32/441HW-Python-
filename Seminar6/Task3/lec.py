# Задайте список из n чисел последовательности (1 + 1/n)**n, 
# выведите его на экран, а так же сумму элементов списка.


num = int(input('Введите число: '))
my_list = [(round(((1 + 1/(i+1))**(i+1)),2)) for i in range(num)]

print(f'Для n={num} -> {my_list}')
print(f'Сумма элементов: {sum(my_list)}')