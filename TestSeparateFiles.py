"""
This file will test to make sure the methods contained in the MATRIXOPERATIONS class work on the Matrix Object
"""
from Matrix import Matrix
import MatrixOperations

myMatrix = Matrix(5, 5)

print(myMatrix.get_data())

MatrixOperations.print(myMatrix)
