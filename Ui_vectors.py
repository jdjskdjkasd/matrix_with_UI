import numpy as np
import matplotlib.pyplot as plt

class Vectors():
    def __init__(self, vector_a, vector_b):
        self.vectorA = np.array(vector_a)
        self.vectorB = np.array(vector_b)


    def plot(self):
        plt.plot(self.vectorA, self.vectorB)
        plt.show()


    def add(self):
        return self.vectorA + self.vectorB


    def subtract(self):
        return self.vectorA - self.vectorB


    def dot_product(self):
        return np.dot(self.vectorA, self.vectorB)


    def scalar_multiply(self, scalar):
        return self.vectorA * scalar, self.vectorB * scalar


    def scalar(self):
        mp_s = np.dot(self.vectorA, self.vectorB)
        return mp_s