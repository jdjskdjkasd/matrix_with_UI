import numpy as np
import glfw
import math
from OpenGL.GL import *
import matplotlib.pyplot as plt

class Vectors:
    def __init__(self):
        #Инициализация координат векторов в виде массива
        self.userInput = int(input("Сколько элементов будет в нашем векторе?\n"))
        self.vectorA = np.zeros(self.userInput, dtype=int)
        self.vectorB = np.zeros(self.userInput, dtype=int)

    def Plot(self):
        plt.plot(self.vectorA, self.vectorB)
        plt.show()


    def grafic(self, pr=str):
        if pr.lower() == "gr":
            if not glfw.init():
                return

            window = glfw.create_window(640, 480, "Векторы", None, None)

            if not window:
                glfw.terminate()
                return

            glfw.make_context_current(window)

            glColor3f(1.0, 0.0, 0.0)

            while not glfw.window_should_close(window):
                glClear(GL_COLOR_BUFFER_BIT)  # Очистка буфера перед каждым кадром

                glBegin(GL_LINES)
                for i in range(self.userInput):
                    x = self.vectorA[i]
                    y = self.vectorB[i]
                    length = math.sqrt(x * x + y * y)
                    if length > 0:
                        angle = math.atan2(y, x)
                        arrow_size = 0.1

                        glVertex2f(0, 0)
                        glVertex2f(x, y)

                        glVertex2f(x, y)
                        glVertex2f(x - arrow_size * math.cos(angle - math.pi / 6),
                                   y - arrow_size * math.sin(angle - math.pi / 6))
                        glVertex2f(x, y)
                        glVertex2f(x - arrow_size * math.cos(angle + math.pi / 6),
                                   y - arrow_size * math.sin(angle + math.pi / 6))
                glEnd()

                glfw.swap_buffers(window)  # Обмен буферами для отображения изменений
                glfw.poll_events()  # Обработка событий GLFW (клавиатура, мышь, окно)

            glfw.terminate()

    def InputVectors(self):
        #Инициализация координат в векторе
        for i in range(self.userInput):
            try:
                print(f"Введите значение {i + 1} элемента:")
                self.vectorA[i] = int(input())
            except ValueError:
                print("Error! Введите целое число.")

        for j in range(self.userInput):
            try:
                print(f"Введите значение второго вектора {j + 1}-го элемента:")
                self.vectorB[j] = int(input())
            except ValueError:
                print("Error! Введите целое число.")

    def VectorOperation(self, operationChoice):
        #Выбор операции над векторами, принимает в себя ссылку на пременную
        match operationChoice:
            case 1:
                print(f"----Что вы хотите сделать с векторами?----"
                      f"\n+ Сложение"
                      f"\n- Вычитание"
                      f"\n* Умножение на скаляр")
                plusOrMinus = input()
                match plusOrMinus:
                    case '+':
                        sum_result = self.vectorA + self.vectorB
                        print(f"Сумма векторов A и B: {sum_result}"
                              f"\nЕсли хотите нарисовать график, то напишите /gr"
                              f"\nНу а если хотите продолдить то напишите /ex")
                        vc_pr = input()
                        self.grafic(vc_pr)
                    case '-':
                        minus_result = self.vectorA - self.vectorB
                        print(f"Результат вычитания вектора B из вектора A: {minus_result}")
                    case '*':
                        scalar = float(input("На какое число вы хотите умножить векторы? "))
                        multiplicationA = scalar * self.vectorA
                        multiplicationB = scalar * self.vectorB
                        print(f"Произведение умножения вектора А на {scalar}: {multiplicationA}"
                                 f"\nПроизведение умножения вектора B на {scalar}: {multiplicationB}")
            case 2:
                #Модуль вектора
                magnitudeA = np.linalg.norm(self.vectorA)
                magnitudeB = np.linalg.norm(self.vectorB)
                print(f"Модуль вектора А = {magnitudeA}. Модуль вектора Б = {magnitudeB}")
            case 3:
                #Скалярное произведение векторов
                multiplication = np.dot(self.vectorA,self.vectorB)
                print(f"Скалярное произведение векторов А и В: {multiplication}")
            case 4:
                #Нормализация вектора А и Б
                normalizedA = self.vectorA / np.linalg.norm(self.vectorA)
                normalizedB = self.vectorB / np.linalg.norm(self.vectorB)
                print(f"Нормализированный вектор А: {normalizedA}"
                      f"\nНормализированный вектор B: {normalizedB}")
            case 5:
                #График вектора
                #print("Напишите gr чтобы отрисовать график")
                #vc_pr=input()
                #self.grafic(vc_pr)
                self.Plot()

class Matrix():
    def __init__(self):
        #Даем координаты нашей матрице
        while True:
            try:
                print("----ВАШ ВЫБОР ВЛИЯЕТ НА КОЛИЧЕСТВО СТРОК И СТОЛБЦОВ ОБЕИХ МАТРИЦ----")
                self.rowsA = int(input("Количество строк в матрице: "))
                self.colsA = int(input("Количество столбцов в матрице: "))
                self.coordinats = self.rowsA, self.colsA
                self.rowsB = self.rowsA
                self.colsB = self.colsA
                if(self.rowsA != self.rowsB or self.colsA != self.colsB or self.rowsB != self.rowsA or self.colsB != self.colsA):
                    print("Для того чтобы проводить операции над матрицами нужно, чтобы координаты матриц были равны!")
                    exit("Попробуйте заного!")
                if self.rowsA > 0 and self.colsA > 0 and self.rowsB > 0 and self.colsB > 0:
                    break
            except ValueError:
                print("Error! Введите целое число.")

    def matrixInitialize(self):
        #Инициализация матрицы. Даем координаты каждому элементу матрицы
        self.matrixA = np.zeros((self.rowsA, self.colsA), dtype=int)
        self.matrixB = np.zeros((self.rowsB, self.colsB), dtype=int)

        print("----Введите элементы матрицы A----")
        for i in range(self.rowsA):
            for j in range(self.colsA):
                while True:
                    try:
                        self.matrixA[i, j] = int(input(f"Элемент [{i + 1}, {j + 1}]: "))
                        break
                    except ValueError:
                        print("Error! Введите целое число.")

        print("----Введите элементы матрицы B----")
        for i in range(self.rowsB):
            for j in range(self.colsB):
                while True:
                    try:
                        self.matrixB[i, j] = int(input(f"Элемент [{i + 1}, {j + 1}]: "))
                        break
                    except ValueError:
                        print("Error! Введите целое число.")
    def transpose_Matrix(self, matrix:[list])->list[list]:
        #Метод для транспонирования матрицы. Принимает в себя ссылку переменной матрицы
        transposedMatrix = np.zeros_like(matrix)
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                transposedMatrix[j, i] = matrix[i, j]

        return transposedMatrix

    def matrixOperation(self, matrixOperation):
        #Выбор операции над матрицами. Принимает в себя сслыку на переменную
        match(matrixOperation):
            case 1:
                #Сложение/вычитание/умножение на скаляр
                print(f"----Что вы хотите сделать с матрицами?----"
                      f"\n+ Сложение"
                      f"\n- Вычитание"
                      f"\n* Умножение на скаляр")
                operation = input()
                match(operation):
                    case '+':
                        pluss = self.matrixA + self.matrixB
                        print(f"Сумма двух матриц {pluss}")
                    case '-':
                        minus = self.matrixa + self.matrixA
                        print(f"Вычитание двух матриц {minus}")
                    case '*':
                        matrixScalar = int(input())
                        multiplicationA = matrixScalar * self.matrixA
                        multiplicationB = matrixScalar * self.matrixB
                        print(f"Произведение матрицы на число {matrixScalar}"
                              f"\n A = {multiplicationA}"
                              f"\n B = {multiplicationB}")
            case 2:
                #Нахождение детерминанта
                detA = np.linalg.det(self.matrixA)
                detB = np.linalg.det(self.matrixB)
                print(f"Детерминант матрицы A = {detA}"
                      f"\nДетерминант матрицы B = {detB}")
            case 3:
                #Умножение 2х матрицы
                multiplication = np.dot(self.matrixA, self.matrixB)
                print(f"Прозведение матрицы А и В = {multiplication}")
            case 4:
                #Умножение на еденичную матрицу
                multiplicationA = np.dot(np.eye(self.coordinats, dtype=int), self.matrixA)
                multiplicationB = np.dot(np.eye(self.coordinats, dtype=int), self.matrixB)
                print(f"Произведение матрицы А на еденичную матрицу {multiplicationA}"
                      f"\nПроизведение матрицы B на еденичную матрицу {multiplicationB}")
            case 5:
                #Транспонирование матрицы
                transposeA = self.transpose_Matrix(self.matrixA)
                transposeB = self.transpose_Matrix(self.matrixB)
                print(f"Транспонированная матрица А {transposeA}."
                      f"\nТранспонированная матрица B {transposeB}.")

def main():
    #Мэейн программы
    print("----С чем вы хотите работать?----"
          "\n1 - Векторы"   
          "\n2 - Матрицы")
    vectorsOrMatrix = int(input())

    match(vectorsOrMatrix):
        case 1:
            #Работа с векторами
            vectors = Vectors()
            vectors.InputVectors()

            print(f"----Какую операцию вы хотите сделать с векторами?----"
                  f"\n1 - Операции над 2-мя векторами"
                  f"\n2 - Нахождение модуля"
                  f"\n3 - Скалярное произведение"
                  f"\n4 - Нормализация вектора"
                  f"\n5 - Отрисовака графика"
                  f"\nВаш вариант ответа: ")

            vetorOperationChoice = int(input())
            vectors.VectorOperation(vetorOperationChoice)
        case 2:
            #Работа с матрицами
            matrix = Matrix()
            matrix.matrixInitialize()

            print(f"----Какую операцию вы хотите сделать с векторами?----"
                  f"\n1 - Сложение/Вычитание/Умножение на скаляр"
                  f"\n2 - Нахождение детерминанта"
                  f"\n3 - Умножение 2-х матриц"
                  f"\n4 - Умножение матрицы А и В на еденичную матрицу"
                  f"\n5 - Транспонирование матрицы"
                  f"\nВаш вариант ответа: ")
            matrixOperationChoice = int(input())
            matrix.matrixOperation(matrixOperationChoice)

main()