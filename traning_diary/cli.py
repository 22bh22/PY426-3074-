import sys


class CommandLineInterface:

  def __init__(self):
    self.commands = {}

  def add_command(self, label):
    def deco(command):
      self.commands[label] = command
      return command
    return deco

  def run(self):
    args = sys.argv
    if len(args) < 2:
      print('''Неверный запуск, используйте например:
            python3 traning_diary power \
            add_day приседания 100 10 3''')
    else:
      command = sys.argv[1]
    command_args = sys.argv[2:]
    if command in self.commands:
      command = self.commands.get(command)
      command(*command_args)
    else:
      all_commands_str = ', '.join(self.commands.keys())
      print(f'Неизвестная команда, \
        используйте одну из: {all_commands_str}, \
        а не {command}')
