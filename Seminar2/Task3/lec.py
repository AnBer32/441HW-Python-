#Реализуйте алгоритм перемешивания списка.
import random
n = input("Введите список:\n")
n = list(n)
a = random.sample(n, len(n))
print(a)
