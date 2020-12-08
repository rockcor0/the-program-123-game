class Controller:

    def __new__(cls, *args, **kwargs):
        return super(Controller, cls).__new__(cls)

    def __init__(self):
        print('Init de controller')

    def validate_command(self, command):
        # Search in local data base for command
        pass

    def get_commands(self):
        pass
