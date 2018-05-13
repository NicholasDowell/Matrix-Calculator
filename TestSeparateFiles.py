"""
This file will test to make sure the methods contained in the MATRIXOPERATIONS class work on the Matrix Object
"""
from Matrix import Matrix
import MatrixOperations

myMatrix = Matrix(5, 5)

MatrixOperations.printout(myMatrix)

print("Setting all rows to numbers 1 through 5")

for integer in range(5):
    myMatrix.set_row(integer, [1, 2, 3, 4, 5])

MatrixOperations.printout(myMatrix)

print("SEtting row 2 to new numbes")
MatrixOperations.replace_row(myMatrix, 2, [7, 5, 1, 0, 0])
MatrixOperations.printout(myMatrix)

print("Replacing Column 4 with 2^x")
MatrixOperations.replace_column(myMatrix, 4, [2 ** number for number in range(5)])
MatrixOperations.printout(myMatrix)

print("Adding a sixth column to the matrix")
MatrixOperations.add_column(myMatrix, [0, 0, 1, 1, 2])
MatrixOperations.printout(myMatrix)

print("Adding a sixth row to the matrix")
MatrixOperations.add_row(myMatrix, [0, 0, 0, 0, 0, 0])
MatrixOperations.printout(myMatrix)

print("Row interchanging row 1 with row 5")
MatrixOperations.row_interchange(myMatrix, 1, 5)
MatrixOperations.printout(myMatrix)

print("Putting all rows of all zeros on the bottom!")
MatrixOperations.put_all_zero_rows_on_bottom(myMatrix)
MatrixOperations.printout(myMatrix)

print("Adding lots more zero rows")
for x in range(10):
    MatrixOperations.add_row(myMatrix, [0, 0, 0, 0, 0, 0])
    MatrixOperations.row_interchange(myMatrix, myMatrix.get_height()-1, x)

MatrixOperations.printout(myMatrix)

print("Putting all zeros on bottom")
MatrixOperations.put_all_zero_rows_on_bottom(myMatrix)
MatrixOperations.printout(myMatrix)




