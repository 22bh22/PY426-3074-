#задание:
#заданы переменные a = '1' b = 2 c = '11'
#найти сумму чисел и вывести в консоли

#вставить в for большую переменную и проверку try ... except
#предусмотреть вариант выражения вида print('111')
#оптимизировать проверку равно тоже через try ... except

D = 'Description'
R = 'Run'

#12345678901234567890123456789012345678901234567890123456789012345678901
#11111111112222222222333333333344444444445555555555666666666677777777771
Description0 = 'Создаём переменую a'
Run0 = "a = '1'"

Description1 = 'Создаём переменую b'
Run1 = "b = 2"

Description2 = 'Создаём переменую c'
Run2 = "c = '11'"

Description3 = 'Создаём переменную d, \
в которую сохраняемсумму a, b и c'
Run3 = "d = int(a) + b + (c)"

Description4 = 'Выводим значение d'
Run4 = "d"

for i in range(0, 4 + 1):
	X1 = R + str(i)
	exec(eval(X1))
	X2 = str(i + 1) + '. '
	X2 += str(eval(D + str(i))) + ': ' + str(eval(X1))
	X3 = eval(X1)
	if ('=' in X3) == False:
		X2 += ' = ' + str(eval(X3))
	print(X2)
print(chr(10))

#print(f'{a=} + {b=} + {c=} = {d=}')
#в 3.4.3 выдаёт ошибку SyntaxError: invalid syntax


input('Для завершения нажмите клавишу Enter...')
