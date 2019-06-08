class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = self.parseMatrix(matrix_string)

    def row(self, index):
        if index > len(self.matrix):
            raise ValueError('Index Error: {index} is out of bounds')
        return self.matrix[index-1]

    def column(self, index):
        if index > len(self.matrix[index-1]):
            raise ValueError('Index Error: {index} is out of bounds')
        return [m[index-1] for m in self.matrix]

    def parseMatrix(self, str):
        lines = str.split('\n')
        return [[int(i) for i in s.split(' ')] for s in lines]


