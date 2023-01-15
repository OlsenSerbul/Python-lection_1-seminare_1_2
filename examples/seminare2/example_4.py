# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа-определять количество вхождений одной строки в другие.

# #1 вариант с поиском вхождения 1 символ
# text = input('Введите текст: ')
# substring = input('Введите искомый элемент: ')
# #text = text.split() # перевели формат строки в список
# count = 0 # обьявили счетчик
# for char in text: # считаем буквы в каждом элементе
#     if substring == char: # ищем в нем искомый элемент
#         count= count + 1


#print(f'В заданном тексте подстрока "{substring}" встречается {count} раз')

# 2 вариант с поиском вхождения  
# text = input('Введите текст: ')
# substring = input('Введите искомый элемент: ')
# text = text.split(substring)
# print(len(text)-1)

# # 3 способ готовый метод

# text = input('Введите текст: ')
# substring = input('Введите искомый элемент: ')
# text = text.count(substring) 

# 4 способ поиск по срезу
text = input('Введите текст: ')
substring = input('Введите искомый элемент: ')

count = 0
for i in range(len(text)):
    if substring.lower() == text[i: i + len(substring)].lower():
        count +=1

print(f'В заданном тексте подстрока "{substring}" встречается {count} раз')
