from src.control.Controller import Controller


class ViewController(Controller):

    def __new__(cls, *args, **kwargs):
        return super(ViewController, cls).__new__(cls)

    def __init__(self):
        print('Init view controller')

    def validate_command(self, command):
        # Validate if a command exist and what it do
        super().validate_command(command)