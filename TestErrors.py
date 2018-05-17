# The TestErrors file will be a runnable file
# that demonstrates that the errors written in MatrixExceptions are functioning correctly

from Matrix import Matrix
import MatrixOperations

# creates a Matrix of size 3x3 and initializes it with some basic integers
m = Matrix(3, 3)
MatrixOperations.printout(m)
new_row = [3, 3, 2]
MatrixOperations.replace_row(m, 0, new_row)

MatrixOperations.printout(m)
too_big_row = [1, 2, 3, 4]
MatrixOperations.replace_row(m, 2, too_big_row)

MatrixOperations.printout(m)

