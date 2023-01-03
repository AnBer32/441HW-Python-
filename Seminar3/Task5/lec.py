# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))
negofibonacci = [1,-1]
fibonacci = [1,1]

for i in range(2,n):
    list = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(list)
    list2 = negofibonacci[i-2] - negofibonacci[i-1]
    negofibonacci.append(list2)

negofibonacci.reverse()
fibonacci.insert(0, 0)

print(f' Для {n} => {negofibonacci+fibonacci}')
