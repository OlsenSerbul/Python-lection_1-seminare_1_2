# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int
import random


num = int(input('Введите количество элементов списка: '))
my_list = []
for el in range(num):
    my_list.append(random.randint(0, 100))

print(f'Список до перемешивания:' , my_list)
temp = 0
for i in range(len(my_list)):
    for j in range(len(my_list) - 1):
        temp = my_list[i]
        my_list[i] = my_list[j]
        my_list[j] = temp
print(f'Список после перемешивания:' ,my_list)
