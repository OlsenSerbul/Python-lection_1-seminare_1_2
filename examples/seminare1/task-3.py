# Напишите программу которая на входит будет принимать
# число N и выводить числа от -N  до N

number = int(input('Введите число: '))
# 1 способ через строку
# my_str = ''
# for i in range(-number, number+1):
#     if i <number:
#         my_str += str(i) + ', '
#     else:
#         my_str += str(i)

# print(my_str)


# 2 способ через строку
# my_str = ''
# for i in range(-number, number+1):
#     my_str += str(i) + ', '

# print(my_str[: -2]) # отрезали два последних символа из строки


# 3 способ через список
my_list = []
for i in range(-number, number + 1):
    my_list.append(i)

print(*my_list, sep= ', ')

