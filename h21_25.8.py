from random import random
kkk = 72
#1. типы данных dict.keys, dict.items и dict.items:
dict1 = {1: 2, 3: 4}
print(dict1.keys())			#dict1_keys([1, 3])
print(type(dict1.keys()))	#<class 'dict1_keys'>
print(dict1.items())		#dict1_items([(1, 2), (3, 4)])
print(type(dict1.items()))	#<class 'dict1_items'>

print(dict1.values())		#dict1_values([2, 4])
print(type(dict1.values()))	#<class 'dict1_values'>

#2. создать числовые переменные first и second,
#сравнить и написать, что больше:

print('-' * kkk)

first = int(random() * 100)
second = int(random() * 100)
if first > second:
	#print(f'{first=} больше, чем {second=}')
	print('first ({}) больше, чем second ({})'.format(first, second))
elif first < second:
	#print(f'{first=} меньше, чем {second=}')
	print('first ({}) меньше, чем second ({})'.format(first, second))
else:
	#print(f'{first=} и {second=} равны')
	print('first ({}) и second ({}) равны'.format(first, second))

print('-' * kkk)
	
player_1_score = int(random() * 100)
player_2_score = int(random() * 100)
#ошибка в логике: в однострочнике можно предусмотреть только два варианта - больше у первого или больше у второго, но у них м/б поровну очков
#Вариант 1:
#print("Player 1 (",  player_1_score ,") win!", sep = "") if player_1_score > player_2_score else print("Player 2 (",  player_2_score ,") win!", sep = "")
#Вариант 2:
#print(f"Player 1 ({player_1_score}) win!") if player_1_score > player_2_score else print(f"Player 2 ({player_2_score}) win!")
#Вариант 3:
print("Player 1 ({}) win!".format(player_1_score)) if player_1_score > player_2_score else print("Player 2 ({}) win!".format(player_2_score))
#12345678901234567890123456789012345678901234567890123456789012345678901

print('-' * kkk)

fruits = ['apple', 'peach', 'banana', 'pear', 'watermelon', 'lime']
#распечатать сумму всех символов слов в списке
print('Исходный список фруктов:\n', fruits)
k = 0
for i in fruits:
	k += len(i)
print('Длина всех слов в списке:', k)

print('-' * kkk)

#распечатать все элементы из списка, которые меньше нуля:
list1 = [1, -5, 10, 50, 63, -9, 12]
i = int(random() * 10) + 5
list2 = []
[list2.append(int(random() * 100) - 50) for j in range(i)]
list1 = list2
print('Исходный список-1:', list1)
for i in list1:
	if i < 0:
		print('Отрицательный элемент:', i)
#print(i) for i in list1

print('-' * kkk)

#Максимум и минимум из списка:
#вариант решения с циклами
list1 = [2, 55, 88, 96, 5, 2, 3]
print('Исходный список:', list1)
dict1 = {'max': list1[0], 'min': list1[0]}

for i in list1:
	if i > dict1['max']:
		dict1['max'] = i
	#dict1['max'] = i if i > dict1['max']	#синтаксическая ошибка при попытке использовать однострочник
	if i < dict1['min']:
		dict1['min'] = i
	#dict1['min'] = i if i < dict1['min']	#синтаксическая ошибка при попытке использовать однострочник

print('С использованием цикла: минимум: ', dict1['min'], '; максимум: ', dict1['max'], sep = "")
#вариант решения без циклов
#print('Отсортированный список', list1.sort())
print('Без использования цикла: минимум', sorted(list1)[0], ' максимум', sorted(list1)[-1])

print('-' * kkk)
#использовать range и enumerate

list2 = [chr(i) for i in range(80, 80 + 10)]
print('Список c использованием range', list2)

i = 80
list2 = []
while i < 90:
	list2.append(chr(i))
	i += 1
print('Список с использованием while', list2)

print('-' * kkk)

#print({x ** 2 for x in range(10) if x % 2 == 0})
#print([x ** 2 for x in range(10) if x % 2 == 0])

#print(['FizzBuzz' if i % 3 == 0 and i % 5 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range (1, 20)])

#print('-' * kkk)
print('Использование enumerate:')
for N, i in enumerate(list2, start = 1):
    print(N, i)

k = 0
print('Использование while:')
while(k < len(list2)):
	print(k + 1, list2[k])
	k += 1
input('Для завершения нажмите клавишу Enter...')
#использовать while вместо range и enumerate
