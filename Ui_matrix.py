import numpy as np

class Matrix():
    def __init__(self, matrix_a, matrix_b):
        self.matrixA = np.array(matrix_a)
        self.matrixB = np.array(matrix_b)


    def transpose(self, matrix):
        return np.transpose(matrix)


    def add(self):
        return self.matrixA + self.matrixB


    def subtract(self):
        return self.matrixA - self.matrixB


    def determinant(self):
        det_a = np.linalg.det(self.matrixA)
        det_b = np.linalg.det(self.matrixB)
        return det_a, det_b


    def multiply(self):
        return np.dot(self.matrixA, self.matrixB)


    def scalar_multiply(self, scalar):
        return self.matrixA * scalar, self.matrixB * scalar