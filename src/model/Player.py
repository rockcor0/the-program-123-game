from src.model.Character import Character


class Player:

    def __new__(cls, *args, **kwargs):
        print("New Player")
        return super(Player, cls).__new__(cls)

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.character
        print('Init Player')

    def load_characters(self):
        pass

    def create_new_character(self, sex):
        character = Character()
        character.live(sex)

    def __del__(self):
        pass


#TODO Only for testing
jugador = Player('Ricardo', 'a@b.com', 37)
print(jugador.name)
