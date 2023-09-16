## -*- coding: utf-8 -*-
"""
Хотим добавлять упраженения с помощью команды
python traning_diary add_day приседания 100 10 3
python traning_diary show
python3 traning_diary add_day power приседания 100 10 3
python3 traning_diary add_day cardio велосипед '1 км' '5 мин.'
и смотреть при помощи
python3 traning_diary show
"""
from cli import CommandLineInterface
from diary import Diary
from day import Day
from exercises import PowerExercise, CardioExercise


cli = CommandLineInterface()


traning_diary = Diary()

exercise_type_list = [
'power', 'cardio', 'crossfit'
]

@cli.add_command('add_day')
def add_day(*args):
  if args[0] in exercise_type_list:
    traning_day = Day()
    if args[0] == 'power':
      exercise = PowerExercise(
        type=args[0],
        name=args[1],
        weight=float(args[2]),
        sets=int(args[3]),
        reps=int(args[4]),
      )
    elif args[0] == 'cardio':
        exercise = CardioExercise(
        type=args[0],
        name=args[1],
        x_distance=args[2],
        x_time=args[3]
      )
    elif args[0] == 'crossfit':
          pass
    traning_day.add_exercise(exercise)
    traning_diary.add_day(traning_day)
  else:
    print('''На первом месте должен \
быть один из аргументов:''', exercise_type_list,
'а указан ', args[0])


@cli.add_command('show')
def show():
  """Вызов команды python tarining_diary show"""
  traning_diary.print_days()



def main():
  cli.run()
