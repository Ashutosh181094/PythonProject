import numpy
import random
import logging
import sys
import numpy as np

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="QuestionThree.log", level=logging.DEBUG, format=LOG_FORMAT)
logger = logging.getLogger()


class EvaluateMatrix:

    def createMatrix(size, values):
        matrix = numpy.zeros(shape=(size, size))
        try:
            for i in range(size):
                for j in range(size):
                    matrix[i][j] = random.choice(values)
        except ValueError:
            print("Invalid Values")
            logger.error("Invalid Values")
            sys.exit(1)
        # ValueError: could not convert string to float: 'A'
        return matrix

    def createProcessMatrix(*values, size=4, DiagonalRight="", DiagonalLeft=""):
        try:
            int(size)
            matrix = EvaluateMatrix.createMatrix(size, values)
            print("nestLst=", matrix)

            if DiagonalLeft == "Multiply" or DiagonalLeft == "multiply":
                print("DiagonalLeft :: Multiply -->", EvaluateMatrix.diagonalLeftMultiply(size, matrix))
            else:
                print("The Operation doesnt Exist.Please Pass Multiply or multiply")

            if DiagonalRight == "Sum" or DiagonalRight == "sum":
                print("DiagonalRight :: Sum --> ", EvaluateMatrix.diagonalRightSum(size, matrix))
            else:
                print("The Operation doesnt Exist.Please Pass Sum or sum")

        except ValueError:
            print("Value specified for size not correct")
            logger.error("size not an integer")

    def diagonalRightSum(size, matrix):

        sumRight = 0
        for i in range(size):
            for j in range(size):
                if j < i:
                    sumRight = sumRight + matrix[i][j]

                    # print("Not a valid Integer")
        return sumRight

    def diagonalLeftMultiply(size, matrix):
        mulLeft = 1
        for i in range(size):
            for j in range(size):
                if j > i:
                    mulLeft = mulLeft * matrix[i][j]
        return mulLeft


if __name__ == '__main__':
    EvaluateMatrix.createProcessMatrix(1, 2, 3, 4, 5, 6, 7, 8, 9, size=5, DiagonalRight="Sum")
    #EvaluateMatrix.createProcessMatrix(1, 2, 3, 4, 5, DiagonalRight="Sum", DiagonalLeft="Multiply")
    #EvaluateMatrix.createProcessMatrix(13, 61, 32, 67, 23, DiagonalLeft="Multiply")


