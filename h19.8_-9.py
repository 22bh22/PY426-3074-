#задание:
#на основе 2 списков
#создать 2 словаря с несколькими одинаковыми ключами
#распечатать значения, ключи которых есть в обоих словарях
dict1 = {'Name': 'John', 'Age': 33}
dict2 = {'Name': 'John', 'Weight': 83}
list = list(dict1.keys() & dict2.keys()) 
print(list)

input('Для завершения нажмите клавишу Enter...')
