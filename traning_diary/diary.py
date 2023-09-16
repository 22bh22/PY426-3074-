import os
import json

from day import Day
from utils import get_map_from_list


class Diary:
  user = 'Roman'
  # file_path = os.path.join(os.path.abspath(__file__), 'files', 'exersices.json')
  file_path = 'exercises.json'

  def __init__(self):
    days = []
    json_days = self.load_days_from_json()
    for json_day in json_days:
      day = Day.from_json(json_day)
      days.append(day)
    self.days = days

  def print_days(self, x_type):
    """Задать отображение самого дневника, 
    а отображение отдельных дней делегировать им самим."""
    # Распечатать информацию о дневнике, например заголовок с именем юзера
    title_str = f"Дневник тренировок для {self.user}"
    border = '-' * len(title_str)
    print(border)
    print(title_str)
    print(border)
    days_by_date = get_map_from_list(
      self.days, 
      lambda day: day.date_at
    )
    days_str = []
    for date_at, days in days_by_date.items():
      date_at_str = date_at.isoformat()
      for num, day in enumerate(days):
        if num == 0:
            days_str.append(f"{date_at_str}: {day.as_print_str()}")
        else:
          days_str.append(f"{' '*len(date_at_str)}: {day.as_print_str()}")
    print('\n'.join(days_str))

  def add_day(self, day : Day):     #43
    """Добавить день в дневник, возможно понадобится более сложная логика, 
    но пока просто добавим в список.
    Здесь day - это экземпляр объекта Day"""
    print(f'Добавлен день: {day}')
    self.days.append(day)
    self.dump_days_to_json()

  def dump_days_to_json(self):
    json_days = [tr_day.as_json() for tr_day in self.days]
    with open(self.file_path, 'w', encoding='windows-1252') as fp:
      json.dump(json_days, fp, ensure_ascii=True, indent=4)

  def load_days_from_json(self):
    """Загрузить дни из файла."""
    print(f"{self.file_path=}")
    try:
      with open(self.file_path, 'r', encoding='windows-1252') as fp:
        days = json.load(fp)
    except FileNotFoundError:
      return []
    return days