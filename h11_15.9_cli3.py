#Реализовать алгоритм сортировки пузырьком либо слиянием
#Сравнить их быстродействие
#сортировка от меньшего к большему

import random
from datetime import datetime


def timeit(func):
     def wrapper(*args, **kwargs):
         start = datetime.now()
         result = func(*args, **kwargs)
         end = datetime.now()
         delta = end - start
         print(f"Выполнено за {delta.seconds} сек.")
         return result
     return wrapper


# @timeit # тоже самое что sort_bubble = timeit(sort_bubble)
# def multi(*args):

class NotSortedListError(Exception):
    """Cписок не отсортирован по возрастанию"""
    def __init__(self, *args):
        super().__init__(*args)
        self.args = args

class EmptyListError(Exception):
    """Пустой список"""
    def __init__(self, *args):
        super().__init__(*args)
        self.args = args

def sort_bubble(lst):
	if len(lst) == 0:
		raise EmptyListError("Список пуст!")
	for x_num1, x_elem1 in enumerate(lst):
		x_min_idx = x_num1
		x_min_elem = x_elem1	#lst[x_min_idx]
		#print(f'{x_min_elem=}, {x_num1=}, {x_elem1=}')
		for x_num2, x_elem2 in enumerate(lst[x_num1:]):
			x_num3 = x_num2 + x_num1
			if x_min_elem > lst[x_num3]:
				#print(f'{x_min_elem=}, {x_num2=}, {x_elem2=}')
				lst[x_min_idx], lst[x_num3] = lst[x_num3], lst[x_min_idx]
				x_min_elem = lst[x_min_idx]
				x_min_idx = x_min_idx
				#print(f'{x_min_elem=}')
		elem1 = random.randint(0, len(lst))
		elem2 = random.randint(0, elem1)
		if elem2 > elem1:
			raise NotSortedListError(f'''Cписок {lst}
			не отсортирован по возрастанию''')
	return lst

def sort_plus(lst):
	#lst1 = [i for i in range(11)]
	if len(lst) == 0:
		raise EmptyListError("Список пуст!")
	lst1 = lst[:]
	#print(lst1)
	x_not_odd = (len(lst1) % 2 == 1)
	lst2 = []
	if x_not_odd == True:
		lst2 = [[lst1[0]]]

	for i in lst1[int(x_not_odd)::2]:
		if lst1[i] < lst1[i + 1]:
			lst2.append([lst1[i], lst1[i + 1]])
		else:
			lst2.append(lst1[i + 1], [lst1[i]])

	#print(lst2)

	return lst2


#X = random.randint(50,100)
sort_time = 0

x_diap = 1000
x_try = 100
x_elements = 100
#list_len = [i for i in range(X)]
for i in range(x_try):
	x_start = datetime.now()
	lst1 = [random.randint(-x_diap, x_diap) for i in range(x_elements)]
	#print(lst1)
	lst2 = sort_bubble(lst1)
	x_end = datetime.now()
	delta = x_end - x_start
	sort_time += delta.microseconds
	#print(lst2)
print("Время сортировки списка из ", x_elements," элементов составляет ", sort_time / x_try, """ мс
(взято среднее на основе """, x_try,
" попыток)\nСреднее время сортировки 1 элемента: ", sort_time / x_try / x_elements, ' ms', sep = "")
#print(sort_time, ' ms', encoding='utf-8')
