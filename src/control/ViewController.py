from src.control.Controller import Controller


class ViewController(Controller):

    def __new__(cls, *args, **kwargs):
        return super(ViewController, cls).__new__(cls)

    def __init__(self):
        super(ViewController, self).__init__()
        print('System: Init view controller')

