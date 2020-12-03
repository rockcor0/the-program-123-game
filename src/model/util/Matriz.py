from random import randint


class Matriz:
    def __new__(cls, *args, **kwargs):
        return super(Matriz, cls).__new__(cls)

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def create_matriz(self):

        matriz = []

        for i in range(self.rows):
            matriz_col = []
            for j in range(self.cols):
                # Fill the matrix with 0's
                matriz_col.append(0)
            matriz.append(matriz_col)

        print(matriz)

        return matriz

test = Matriz(10,10)
test.create_matriz()
