class Cell:

    def __new__(cls, *args, **kwargs):
        print('Creating cell - new')
        return super(Cell, cls).__new__(cls)

    def __init__(self, x_coord, y_coord, z_coord):
        print('Initialize cell - init')
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.z_coord = z_coord

#Sample for testing
cell = Cell(1,1,10)
print(cell.z_coord)


