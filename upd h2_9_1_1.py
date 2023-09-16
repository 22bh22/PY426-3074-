#Введите последовательно из консоли свое имя, и возраст. Выведите их на экран разделив точкой с запятой.
from sys import argv as sys_argv

if __name__ == '__main__':
	if len(sys_argv) == 1:
		#Вызов без аргументов:
		temp1 = input('Введите последовательно из консоли свое имя и возраст (через пробел):' + chr(10))
		#temp1 = 'Petya Vasechkin 11'
		temp2 = temp1.split(' ')
	else:
		#Вызов с аргументами:
		#Пример вызова: X:\...\h9_2_1_1.py Petya Vasechkin 11
		temp2 = sys_argv[1:]
	temp3 = ' '.join(temp2[:-1]) + ", " + temp2[-1]
	print(temp3)
input('Для завершения нажмите клавишу Enter...')
