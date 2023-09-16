class ExerciseInterface:
    
  def print_ex(self):
    raise NotImplementedError
  
  def as_json(self):
    raise NotImplementedError
  
  @classmethod
  def from_json(cls, json_dict):
    return cls(**json_dict)


class PowerExercise(ExerciseInterface):
  x_type = 'PowerExercise'
  def __init__(self, name, weight, sets, reps, type):
    self.name = name
    self.weight = weight
    self.sets = sets
    self.reps = reps
    self.x_type = type

  def __str__(self):
    return f"{self.name}: {self.weight} x {self.sets} x {self.reps}"

  def print_ex(self):
    print(f"{self.name}: {self.weight} x {self.sets} x {self.reps}")

  def as_json(self):
    return {
      'type': self.x_type,
      'name': self.name,
      'weight': self.weight,
      'sets': self.sets,
      'reps': self.reps
    }
  
class CardioExercise(ExerciseInterface):
  x_type = 'CardioExercise'
  def __init__(self, name, distance, time, type):
    self.name = name
    self.x_distance = distance
    self.x_time = time
    self.x_type = type

  def __str__(self):
    return f"{self.name}: {self.x_distance} x {self.x_time}"

  def print_ex(self):
    print(f"{self.name}: {self.x_distance} x {self.x_time}")

  def as_json(self):
    return {
      'type': self.x_type,
      'name': self.name,
      'distance': self.x_distance,
      'time': self.x_time
    }