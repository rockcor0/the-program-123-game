from random import randint


class Matriz:
    def __new__(cls, *args, **kwargs):
        return super(Matriz, cls).__new__(cls)

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def create_matriz(self):

        test_row = []

        for i in range(self.rows):
            test_col = []
            for j in range(self.cols):
                test_col.append(randint(1,10))
            test_row.append(test_col)
            #test_col = []

        '''
        test_col = [1,2,3]
        test_row.append(test_col)

        test_col = [4,5,6]
        test_row.append(test_col)

        test_col = [7,8,9]
        test_row.append(test_col)
        '''
        print(test_row)

        return 0

test = Matriz(10,10)
test.create_matriz()
