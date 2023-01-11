# напишите программу которая на вход принимает 5 
# чисел и находит максимальное из них.

# number1 = int(input('Введите 1 число: '))
# number2 = int(input('Введите 2 число: '))
# number3 = int(input('Введите 3 число: '))
# number4 = int(input('Введите 4 число: '))
# number5 = int(input('Введите 5 число: '))
# max = number1
# if max < number2:
#     max = number2
# if max < number3:
#     max = number3
# if max < number4:
#     max = number4
# if max < number5:
#     max = number5

# print(max)

# Второй способ решения

# number1 = int(input('Введите 1 число: '))
# number2 = int(input('Введите 2 число: '))
# number3 = int(input('Введите 3 число: '))
# number4 = int(input('Введите 4 число: '))
# number5 = int(input('Введите 5 число: '))

# my_list = [number1, number2, number3, number4, number5]
# max = number1
# for i in my_list:
#     if i > max:
#         max = i

# print(max)

# третий способ решения
my_list =[]
for i in range(5):
    my_list.append(int(input('Введите {i+1} число: ')))

maxX = my_list[0]
for item in my_list:
    if item > maxX:
      maxX = item
print(maxX)  

 



