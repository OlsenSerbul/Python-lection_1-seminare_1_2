# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.(Не совсем 
# понимаю как проверяется истинниость логического выражения, но попыталась)

import random

X = bool(random.choice([True, False]))
Y = bool(random.choice([True, False]))
Z = bool(random.choice([True, False]))
my_list =[X, Y, Z]
not False == True
not True == False
print(my_list)
if (not(X or Y or Z)) == ((not X) and (not Y) and (not Z)):
    print('Истинно')
else:
    print('ложно')