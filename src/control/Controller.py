from src.model.Message import Message


class Controller:

    def __new__(cls, *args, **kwargs):
        return super(Controller, cls).__new__(cls)

    def __init__(self):
        print('Init de controller')

    def validate_command(self, command):
        # Search in local data base for command
        commands = [('caminar', 'walk'),
                    ('correr', 'run'),
                    ('saltar', 'jump'),
                    ('hola', 'hello'),
                    ('', ''),
                    ('', ''),
                    ('', '')
                    ]

        found = False
        for i in commands:
            if i[0] == command or i[1] == command.lower():
                found = True
                break

        return found

    def get_commands(self):
        pass

    def do_something(self, command):
        return Message(command)

# Test
c = Controller()
c.validate_command('caminar')