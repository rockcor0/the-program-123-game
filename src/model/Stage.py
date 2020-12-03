from src.model.Cell import Cell
from src.model.util.Matriz import Matriz


class Stage:

    def __new__(cls, *args, **kwargs):
        print("Create stage - new")
        return super(Stage, cls).__new__(cls)

    def __init__(self, new_game):
        print("Initialize stage - init")
        rows = 20
        cols = 20

        # New game or load and saved game
        if new_game:
            self.matriz = self.create_matriz(rows, cols)
            self.fill_matriz(self.matriz, rows, cols)

        print(self.matriz)

    def get_matriz(self):
        return self.matriz

    def __del__(self):
        print("Destroy stage")

    @staticmethod
    def create_cell(x_coord, y_coord, z_coord):
        return Cell(x_coord, y_coord, z_coord)

    @staticmethod
    def create_matriz(rows, cells):
        temp_matriz = Matriz(rows, cells)
        return temp_matriz.create_matriz()

    def fill_matriz(self, matriz, rows, cells):
        for i in range(rows):
            for j in range(cells):
                #print(self.matriz[i][j])
                matriz[i][j] = self.create_cell(i, j, 0)


# For testing
s = Stage(True)
print(s.get_matriz())
