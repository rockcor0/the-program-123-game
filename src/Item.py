from random import randint

from src.Statistic import Statistic


# An item is an object in the floor
# Character can get this object and put in the bag or consume
# Consume an object can help or maybe not
class Item:

    def __new__(cls, *args, **kwargs):
        return super(Item, cls).__new__(cls)

    def __init__(self):
        self._item_id = 0
        self._name = 'none'
        self._is_consumible = False
        self._is_equipable = False
        self._action_when_consume = 0
        self._feature = 'Este objeto está pegado al piso. Que vergüenza'
        self._statistics_affected = 'nil'

        self.define_item()

    # Create a random item
    def define_item(self, max_item_value=100, max_item_with_object=21):
        self._item_id = randint(1, max_item_value)

        if self._item_id < max_item_with_object:
            # Require search for item_id in data base
            self.looking_for_item()
            return True
        else:
            return False

    # Look for an item
    def looking_for_item(self):
        # Search in data base for item
        # Sample emulating data base response
        self._item_id = 1
        self._name = 'Cerveza'
        self._is_consumible = True
        self._is_equipable = False
        self._action_when_consume = 20
        self._feature = 'Me siento un poco mareado, pero ya no tengo miedo'

        # return self._item_id, self._name, self._is_consumible, self._is_equipable, self._action_when_consume,
        # self.feature

    # Get the items from data base
    def get_items(self):
        temp_items = []
        item1 = (1, 'Cerveza', True, False, 10, 'Me siento un poco mareado, pero creo que puedo continuar',
                 ['valor++', 'lucidez--'])

    def __del__(self):
        print('Kill Item')


# Only for test
i = Item()
print(i._name)