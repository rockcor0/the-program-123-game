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
        if new_game:
            for i in range(rows):
                for j in range(cols):
                    cells.append(self.create_cell(i, j, 0))

        print(len(cells))
        print(cells)

    def __del__(self):
        print("Destroy stage")

    @staticmethod
    def create_cell(x_coord, y_coord, z_coord):
        # return Cell(x_coord, y_coord, z_coord)
        return 1


# For testing
s = Stage(True)
