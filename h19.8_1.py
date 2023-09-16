from platform import python_version as ver
#вставить в for большую переменную и проверку try ... except
#предусмотреть вариант выражения вида print('111')
#оптимизировать проверку равно тоже через try ... except

#задание:
#дано 2 уравнения:
#	(2.5 x + 50 / 2) = 200
#	y / 2 - 100 = 500
#вычислить x и y
#сравнить x и y любым оператором сравнения
#сохранить результат в переменную result
#определить тип переменной result

print('Python v', ver(), sep ='')
D = 'Description'
R = 'Run'
S1 = 'Даны два уравнения:\n(2,5 x + 50 / 2) = 200 \ny / 2 - 100 = 500'
S2 = 'Упрощаем их:\n2,5 x + 25 = 200 \ny - 200 = 1000'
S2 = 'Находим x и y:\nx = (200 - 25) / 2,5\ny = 1000 + 200'

print(S1)

Description0 = 'Создаём переменую x'
Run0 = "x = (200 - 25) / 2.5"
#12345678901234567890123456789012345678901234567890123456789012345678901
#11111111112222222222333333333344444444445555555555666666666677777777771
Description1 = 'Создаём переменую y'
Run1 = "y = 1000 + 200"

Description2 = 'Выводим значение x'
Run2 = "x"

Description3 = 'Выводим значение y'
Run3 = "y"

Description4 = 'Создаём переменную result, \
в которую сохраняем\nрезультат сравнения x и y'
Run4 = "result = (x < y)"

Description5 = 'Выводим значение result'
Run5 = "result"

Description6 = 'Определяем тип переменной result)'
Run6 = "type(result)"

for i in range(0, 6 + 1):
	X1 = R + str(i)
	exec(eval(X1))
	X2 = str(i + 1) + '. '
	X2 += str(eval(D + str(i))) + ': ' + str(eval(X1))
	X3 = eval(X1)
	if ('=' in X3) == False:
		X2 += ' = ' + str(eval(X3))
	print(X2)
print(chr(10))

#print(f'{x=} > {y=}')#в 3.4.3 выдаёт ошибку SyntaxError: invalid syntax

if result == True:
	print('x = {} < y = {}'.format(x, y))
else:
	if x > y:
		print('x = {} > y = {}'.format(x, y))

input('Для завершения нажмите клавишу Enter...')
