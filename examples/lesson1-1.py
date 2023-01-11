# print('Введите a ')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a,'+',b,'=',a+b)


# управляющие контрукции if, if-eise
#a = int(input('a = '))
#b = int(input('b = '))

#if a > b:
#    print(a)
#else:
#    print(b)

# управляющие контсрукции if- elif - else

#username = input('Введите Имя пользователя')
#if username == 'Оля':
#    print('Ура! это Оля')
#elif username == 'Марк':
#    print('Привет, Маркуша!')
#elif username == 'Дима':
#    print('Ананас - Димке в глаз,чтоб не обижал он нас! ')
#else:
#    print('Привет,', username)


original = 23
inverted = 0
while original !=0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)
