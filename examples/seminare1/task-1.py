# Введите два числа и проверьте является ли одно число квадратом второго. 
number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))

if number1 == number2**2 or number2 == number1**2:
    print('yes')
else:
    print('no')
    
