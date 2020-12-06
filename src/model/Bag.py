class Bag:

    def __new__(cls):
        return super(Bag, cls).__new__(cls)

    def __init__(self):
        self.slots = 8

    def __del__(self):
        pass

    def create_matrix(self):
        pass

    def save_item(self):
        pass

    def drop_item(self):
        pass

    def use_item(self):
        pass

    def calculate_slots(self):
        pass

    def is_available_slot(self):
        pass

    def move_item(self):
        pass
