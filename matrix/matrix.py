class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[int(i) for i in line.split(' ')] for line in matrix_string.splitlines()]

    def row(self, index):
        if index > len(self.matrix):
            raise IndexError()
        return self.matrix[index-1]

    def column(self, index):
        if index > len(self.matrix[index-1]):
            raise IndexError()
        return [m[index-1] for m in self.matrix]



