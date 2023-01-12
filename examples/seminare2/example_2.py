# Напишите программу которая принимает на вход число N и выдает последовательность из N членов

# Пример
#Для N= 5: 1; -3; 9; -27; 81

N = int(input('Введите N: '))
result = []

for i in range(N):
    result.append((-3)**i)
print(f'Для N = {N}:', end=' ')
print(*result, sep=', ')