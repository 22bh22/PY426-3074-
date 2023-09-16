'''
1. В примере с рачетом зарплаты измените функцию так, чтобы параметр отработанных часов был опциональным, если он не передан то считалось что работник отработал 8 часов.
'''
from copy import deepcopy
def x_uprise()
def x_uprise(user_list):
	print('user_list =', user_list)
	user_list2 = deepcopy(user_list)
	for elem in user_list2:
		if elem['job'] == 'developer':
			elem['salary'] *= 1.1
	print('-' * 72)
	print('user_list =', user_list)
	print('-' * 72)
	print('user_list2 =', user_list2)
	return user_list2

employee = [
  dict(name='John', job='developer', salary=2000),
  dict(name='Mike', job='manager', salary=1900),
  dict(name='Peter', job='developer', salary=2100),
  dict(name='Rayan', job='guard', salary=1000),
]

x_uprise(employee)
'''
2.Реализуйте функцию которая принимает первым аргументом строку символов, а какой-либо символ. Функция должна вернуть число вхождений этого символа в строку. Например:
def get_repeats(string, char):
    ...

get_repeats('abbbcdr', 'b')  # 3
'''

'''
3. Реализуйте функцию make_multiplicator которая в зависимости от аргумента возвращает функцию удваивания, утраивания и т.д. Например:
double = make_multiplicator(2)
double(2)  # 4
double(3)  # 6
triple = make_multiplicator(3)
triple(2)  # 6
triple(3)  # 9
'''
def make_multiplicator(i):
	if i == 2:
		def double(x):
			return x * 2
		return double()
	elif i == 3:
		def triple(x):
			return x * 2
		return triple()
'''
3.1 В примере с рачетом зарплаты я все равно применил копипаст, а как можно преписать программу если хранить информацию об окладе, и выработке в словарях? 3.2 Рассмотрим пример программы которая строит дом:
'''

'''
# Импортируем модуль стандартной библиотеки
# Мы поговорим про импорты чуть позже
# Прочитайте про фунции из модуля random `https://docs.python.org/3/library/random.html`
'''
import random


def make_walls():
    """
    Эта функция возвращает размеры дома.
    Возвращает кортеж из (ширина, длина, глубина)
    """
    return random.randint(), random.randint(), random.randint()


def color_walls():
    """
    Эта функция возвращает цвет стен.
    """
    colors = ['red', 'blue', 'green']
    return random.choice(colors)


def make_roof(width, length):
    """
    Эта функция возвращает крышу, если площадь крыши меньше 10 м кв. то она будет соломенной.
    Иначе деревянной.
    """
    square = width * length
    if square < 10:
        return 'соломенная'
    return 'деревянная'


def build(size, color, roof):
    print(f"Построен дом площадью {size[0] * size[1]}, высота потолков {size[2]}, цвет стен {color}, крыша в доме {roof}.")

room_size = make_walls()
walls_color = color_walls()
roof = make_roof(room_size[0], room_size[1])

build(room_size, walls_color, roof)
'''
Напишите по примеру программу, которая выпекает пиццу, при этом разбив процесс выпекания логически по функциям.
'''