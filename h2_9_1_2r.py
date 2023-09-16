#Сохраните в файл fruits.txt список фруктов ['apple', 'banana', 'lime', 'orange'],
#в каком виде он сохраниться?
#Прочитайте сохраненный список - какой тип данных вы получили?
list1 = ['apple', 'banana', 'lime', 'orange']
x_sep = chr(32)
with open('fruits.txt', 'w') as x_file:
	x_file.write(' '.join(list1[:-1]) + x_sep + list1[-1])

with open('fruits.txt', 'r') as x_file:
	temp = x_file.readlines()

print(temp, type(temp))

input('Для завершения нажмите клавишу Enter...')
