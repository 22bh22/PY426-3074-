#задание:
#создать переменную и сохранить в неё
#любое числовое значение
#скопировать это значение в другую переменную
#удалить первую переменную
a = 123
b = 123
c = a
print('a = {}, b = {}, c = {}'.format(a, b, c))
del(a)
print('b = {}, c = {}'.format(b, c))
#print(a)
input('Для завершения нажмите клавишу Enter...')
