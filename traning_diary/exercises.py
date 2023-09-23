#exercises.py
class ExerciseInterface:
    
  def print_ex(self):
    raise NotImplementedError
  
  def as_json(self):
    raise NotImplementedError
  
  @classmethod
  def from_json(cls, json_dict):
    return cls(**json_dict)


class PowerExercise(ExerciseInterface):
  x_user_type = 'power'
  def __init__(self, name, weight, sets, reps, type):
    self.name = name
    self.weight = weight
    self.sets = sets
    self.reps = reps
    self.x_user_type = type

  def __str__(self):
    return f"{self.name}: {self.weight} x {self.sets} x {self.reps}"

  def print_ex(self):
    print(f"{self.name}: {self.weight} x {self.sets} x {self.reps}")

  def as_json(self):
    return {
      'type': self.x_user_type,
      'name': self.name,
      'weight': self.weight,
      'sets': self.sets,
      'reps': self.reps
    }
  
class CardioExercise(ExerciseInterface):
  x_user_type = 'cardio'
  def __init__(self, name, distance, time, type):
    self.name = name
    self.x_distance = distance
    self.x_time = time
    self.x_user_type = type

  def __str__(self):
    return f"{self.name}: {self.x_distance} x {self.x_time}"

  def print_ex(self):
    print(f"{self.name}: {self.x_distance} x {self.x_time}")

  def as_json(self):
    return {
      'type': self.x_user_type,
      'name': self.name,
      'distance': self.x_distance,
      'time': self.x_time
    }
  
  class CrossFit(ExerciseInterface):
    """
    Для кроссфита существует также подкласс упражнений:
    'AFAP' - 
    'AMRAP'
    'EMOM'
    'Chipper' - 
    'Tabata' - 8 упражнений в режиме 20 секунд нагрузки, 10 секунд отдыха
    'AMReps' - как можно больше повторений за определённое время
    'Death by reps' - вес не меняется, количество повторений увеличивается
    'Death by weight' - количество повторений не меняется, вес увеличивается
    """
    x_CF_ex_list = [
      'AFAP', 'AMRAP', 'EMOM', 'Chipper', 
      'Tabata', 'AMReps',
      'Death by reps', 'Death by weight'
      ]
