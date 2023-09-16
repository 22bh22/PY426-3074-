#Для списка ['apple', 'banana', 'lime', 'orange'] 
#реализуйте программу которая сохранит список в виде:
#
## fruits.txt
#apple
#banana
#lime
#orange
#После этого восстановите список из файла, должен получиться именно список.
#Подсказка: используйте метод объекта файла f.readlines().
#Сохранение и получение списка из файла разбейте на отдельные функции. 

list1 = ['apple', 'banana', 'lime', 'orange']
with open('fruits.txt', 'w') as x_file:
	#x_file.write(str(list1))
	for i in list1:
		x_file.write(i + chr(10))


		
with open('fruits.txt', 'r') as x_file:
	#вариант 1 (через readlines):
	list2 = x_file.readlines()
	for num, elem in enumerate(list2):
		list2[num] = elem[:-1]
	#вариант 2 (в одну строку):
	#list2 = x_file.read().splitlines()
	
print(list2)

input('Для завершения нажмите клавишу Enter...')
