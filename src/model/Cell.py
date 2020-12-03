from src.model.Item import Item


class Cell:

    def __new__(cls, *args, **kwargs):
        print('Creating cell - new')
        return super(Cell, cls).__new__(cls)

    def __init__(self, x_coord, y_coord, z_coord):
        print('Initialize cell - init')
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._z_coord = z_coord
        self._item = self.create_random_item()

    @staticmethod
    def create_random_item():
        item = Item()
        print(item.get_name())
        print(item.get_feature())
        return item


#Sample for testing
cell = Cell(1,1,10)
print(cell._z_coord)


