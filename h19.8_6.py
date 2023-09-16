#задание
#дана информация о пользователях в виде списка, где первые 2 позиции
#это имя и фамилия, а остальные - его интересы
#распечатать информацию вида
#Hello, my name is John Anderson, I like computer games, ...
#желательно использовать срезы
list = ['John', 'Anderson', 'computer games', 'books', 'fishing', 'serials']
print('Hello, my name is ', ' '.join(list[0:2]), ', I like ', ', '.join(list[2:]), '.', sep = "")
input('Для завершения нажмите клавишу Enter...')
