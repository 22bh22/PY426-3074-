from datetime import date, datetime

from exercises import PowerExercise, CardioExercise


class Day:

  def __init__(self, date_at=None, exercises=[]):
    self.date_at = date_at or date.today() # Текущий день
    self.exercises = exercises

  def __str__(self):
    return self.date_at.isoformat()

  def print_day(self):
    """Распечатать день."""
    print(f'Распечатать день и упражнения, {self.date_at}')
    for exercise in self.exercises:
      # exercise.print_ex()
      print(exercise)

  def as_print_str(self):
    exercises_str = [str(exercise) for exercise in self.exercises]
    border = '-' * max([len(ex) for ex in exercises_str])
    return f'\n'.join(exercises_str) + f'\n{border}'
      
  def add_exercise(self, exercise):
    """Добавление упражнения для конкретного дня."""
    print(f'Добавить упраженение {exercise}')
    self.exercises.append(exercise)

  def as_json(self):
    return {
      'date_at': self.date_at.isoformat(),
      'exercises': [ex.as_json() for ex in self.exercises]
    }
  
  @classmethod
  def from_json(cls, json_dict):
    """Фабричный метод который на основе данных из json-файла,
    а для записи в сам файл быи использован метод as_json,
    создаст экземпляр объекта день.
    Здесь cls - это класс Day"""
    # if PowerExercise.x_type == 'PowerExercise':
    #   pass
    # elif CardioExercise.x_type == 'CardioExercise':
    #   pass
    date_at_isostr = json_dict['date_at']
    date_at = datetime.fromisoformat(date_at_isostr).date()
    exercises = [PowerExercise.from_json(ex_json) for ex_json in json_dict['exercises']]
    return cls(date_at=date_at, exercises=exercises)
  