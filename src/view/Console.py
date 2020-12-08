class Console:

    def __new__(cls, *args, **kwargs):
        return super(Console, cls).__new__(cls)

    def __init__(self):
        print('Hello, init the console')

    def write_command(self):
        command = input('Please write something: ')

        if self.exit_from_console(command):
            print('Bye')

        else:
            print(command)
            self.write_command()

    def check_command(self, command):
        # Check if command is valid
        pass

    @staticmethod
    def exit_from_console(command):
        if command == 'exit':
            return True
        else:
            return False


# For testing
c = Console()
c.write_command()
