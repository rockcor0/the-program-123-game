class Message:
    actionId = 0
    messageId = ''
    language = 0
    messageText = ''

    def __new__(cls, *args, **kwargs):
        return super(Message, cls).__new__(cls)

    def __init__(self, who, say):
        self.who = who
        self.say = say
        print('Init Message')
        self.say_message(self.who, self.say)

    def __del__(self):
        print('Destroy Message')

    @staticmethod
    def say_message(who, say):
        message = who + ': ' + say
        print(message)



