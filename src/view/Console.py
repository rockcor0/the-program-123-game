from src.control.ViewController import ViewController


class Console(ViewController):

    def __new__(cls, *args, **kwargs):
        return super(Console, cls).__new__(cls)

    def __init__(self):
        print('Hello, init the console')

    def __del__(self):
        print('Destructor console')

    def write_command(self):
        command = input('Please write something: ')

        if self.exit_from_console(command):
            print('Bye')

        else:
            if self.is_valid_command(command):
                print(super().do_something('Character', command))
            else:
                print('Que vergüenza, estoy algo confundido')
            self.write_command()

    def is_valid_command(self, command):
        # Check if command is valid
        return super().validate_command(command)

    @staticmethod
    def exit_from_console(command):
        if command == 'exit':
            return True
        else:
            return False


# For testing
c = Console()
c.write_command()
