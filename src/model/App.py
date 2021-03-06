
from src.model.Character import Character
from src.model.Command import Command
from src.model.Message import Message


class App:

    def __new__(cls, *args, **kwargs):
        return super(App, cls).__new__(cls)

    def __init__(self):
        print('System: Init App')

    def __del__(self):
        print('System: Destroy App')

    def play(self, user, command_num):
        # Temp, require obtain parameters
        command = Command()
        char = user
        if user == 'Me':
            char == 'Victoria'
        if command_num == 1:
            Message(char, command.move_forward())
        elif command_num == 2:
            Message(char, command.run())
        elif command_num == 3:
            Message(char, command.jump())
        elif command_num == 4:
            Message(char, command.say_hello())
        else:
            Message(char, command.do_nothing())