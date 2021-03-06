from src.model.Cell import Cell
from src.model.util.Matriz import Matriz


class Stage:

    def __new__(cls, *args, **kwargs):
        print("System: Create stage - new")
        return super(Stage, cls).__new__(cls)

    def __init__(self, new_game):
        print("System: Initialize stage - init")
        rows = 20
        cols = 20

        # New game or load and saved game
        if new_game:
            self.matrix = self.create_matrix(rows, cols)
            self.fill_matrix(self.matrix, rows, cols)

        else:
            # TODO Do something
            print("System: Get matrix from data base of saved game")

    def get_matrix(self):
        return self.matrix

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
                matrix[i][j] = self.create_cell(i, j, 10)

    def __del__(self):
        print("System: Destroy stage")


# For testing
s = Stage(True)
print(s.get_matrix())
