import switch as switch

from src.model.App import App
from src.model.Message import Message


class Controller(App):

    def __new__(cls, *args, **kwargs):
        return super(Controller, cls).__new__(cls)

    def __init__(self):

        # Temp Command list
        self.commands = [('caminar', 'walk', 1),
                         ('correr', 'run', 2),
                         ('saltar', 'jump', 3),
                         ('saludar', 'hello', 4),
                         ('', '', 5),
                         ('', '', 6),
                         ('', '', 7)
                         ]

        self.users = ['0', 'System', 'Scenary']

        print('Init de controller')

    def validate_command(self, command):
        # Search in local data base for command
        found = False
        the_commands = self.commands

        for i in the_commands:
            if i[0] == command.lower() or i[1] == command.lower():
                found = True
                break

        return found

    def get_commands(self):
        pass

    def do_something(self, user, command):

        for item in self.commands:
            if item[0] == command.lower or item[1] == command.lower:
                return super().do_something(user, item[2])

        return Message(command)

    def get_commands(self):
        return self.commands


# Test
c = Controller()
c.validate_command('caminar')
