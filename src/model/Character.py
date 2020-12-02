class Character:

    def __new__(cls):
        print('New')
        return super(Character, cls).__new__(cls)

    def __init__(self):
        self.name = ''
        self.sex = ''
        self.age = 0
        print('self')

    def __del__(self):
        pass

    def set_name(self, name):
        self.name = name

    def set_sex(self, sex):
        self.sex = sex

    def set_age(self, age):
        self.age = age

    def walk(self, x, y):
        pass

    def eat(self):
        pass

    def drink(self):
        pass

    def take_object(self):
        pass


c = Character()
c.set_name('Ricardo')
c.set_age(37)
c.set_sex('Hombre')
print(c.age)
