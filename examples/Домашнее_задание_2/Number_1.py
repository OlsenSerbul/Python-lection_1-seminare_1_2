# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = input('Введите вещественное число: ')
sumNum = 0
my_number = []
for i in range(len(number)):
    my_number.append(number[i])

for i in range(len(my_number)):
    if my_number[i] != '.' :
       sumNum  += int(my_number[i]) 

print(f'Сумма цифр вещественного числа {number}  равна {sumNum}')

