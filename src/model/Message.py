class Message:

    def __new__(cls, *args, **kwargs):
        return super(Message, cls).__new__(cls)

    def __init__(self, who, say):
        self._who = who
        self._say = say
        print('Init Message')
        self.say_message(self._who, self._say)

    def __del__(self):
        print('Destroy Message')

    @staticmethod
    def say_message(who, say):
        message = str(who) + ': ' + say
        print(message)



