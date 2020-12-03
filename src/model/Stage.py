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
        self.z_coord_default = 10

        # New game or load and saved game
        if new_game:
            self.matriz = self.create_matrix(rows, cols)
            self.fill_matrix(self.matriz, rows, cols)

        else:
            # TODO Do something
            print("Get matrix from data base of saved game")

    def get_matrix(self):
        return self.matriz

    @staticmethod
    def create_cell(x_coord, y_coord, z_coord):
        return Cell(x_coord, y_coord, z_coord)

    @staticmethod
    def create_matrix(rows, cells):
        temp_matrix = Matriz(rows, cells)
        return temp_matrix.create_matriz()

    def fill_matrix(self, matrix, rows, cells):
        for i in range(rows):
            for j in range(cells):
                matrix[i][j] = self.create_cell(i, j, self.z_coord_default)

    def __del__(self):
        print("Destroy stage")


# For testing
s = Stage(True)
print(s.get_matrix())
