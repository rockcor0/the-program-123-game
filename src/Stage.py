from src.Cell import Cell


class Stage:

    def __new__(cls, *args, **kwargs):
        print("Create stage - new")
        return super(Stage, cls).__new__(cls)

    def __init__(self, new_game):
        print("Initialize stage - init")

        cells = []
        rows = 20
        cols = 20
        # New game or load and saved game
        # if new_game:
        print('Aqui')
        for i in range(rows):
            for j in range(cols):
                print("agregando")
                cells.append(self.create_cell(i, j, 0))

        print(len(cells))

        for i in cells:
            for j in cells:
                print(j.x_coord)
                print('Recorriendo')

    def __del__(self):
        print("Destroy stage")

    @staticmethod
    def create_cell(x_coord, y_coord, z_coord):
        return Cell(x_coord, y_coord, z_coord)


# For testing
s = Stage(True);
