# Напишите программу, которая на вход принимает дробь 
# и показывает первыю цифру дробной части числа.
#1 способ

#number = float(input('Введите дробь: '))
# newNumber = (number * 10) % 10
# if number - round(number) == 0:
#     print('нет')
# else:
#     print(round(newNumber))

#2 способ со строкой

# my_str = input('введите дробь: ')
#
# for i in range(len(my_str)):
#     if my_str[i] == '.' :
#         print(my_str[i+1])

# 3 способ
# num = float(input('Введите дробь: '))
# if num == int(num):
#     print('Нет дробной части')
# else:
#     print(int(num * 10) % 10)

# 4 способ

number = input('Введите число: ')
number = number.split('.')
if len(number) < 2:
    print('целое')
else:
    print(number[1] [0])
