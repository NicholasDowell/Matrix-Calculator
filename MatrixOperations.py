# The MatrixOperations class includes a group of methods that allow the matrix to be used for row reduction operations
# prints out all values stored in the matrix to the console
import MatrixExceptions
from MatrixExceptions import RowSizeException


# Prints out each value stored in the mateix
def printout(a):
    row_string = ""
    for row in range(a.get_height()):
        for column in range(a.get_width()):
            row_string += str(a.get_value(row, column)) + " "
        print(row_string)
        row_string = ""


# replaces a row in the matrix with the passed new row
def replace_row(A, row_number, new_row):
    matrix_width = A.get_width()
    row_size = len(new_row)
    if row_size > matrix_width:
        raise RowSizeException(
            "Tried to place a row with {0} elements into a Matrix with only {1} Columns"
            .format(row_size, matrix_width))
        return

    print("Setting row {0} to {1}".format(row_number, new_row))
    A.set_row(row_number, new_row)


"""replaces a column in the matrix with the passed new column
#Column_number represents the index of the column in the matrix that will be replaced.
#column_index represents the current index in the new column (the value that is being placed into the matrix)
# the passed column must have the same number of entries as the number of rows in the matrix
"""


def replace_column(A, column_number, new_column):
    new_column_index = 0
    for row in A.get_data():
        row[column_number] = new_column[new_column_index]
        new_column_index += 1
    return


# adds a new column on the rightmost side of the matrix
def add_column(A, new_column):
    A.set_width(A.get_width() + 1)
    for row in range(A.get_height()):
        A.get_row(row).append(new_column[row])

    return


# adds a new row to the bottom of the matrix
def add_row(A, new_row):
    old_height = A.get_height()
    A.set_height(old_height + 1)
    A.get_data().append(new_row)
    A.set_height(old_height + 1)


# changes the stored matrix into a row reduced echelon form
def rref(A):
    print(1)
    # does the thing
    ## Step 1: regular echelon form
    # all numbers below pivot are zero
    # all pivots to the right of above pivots
    # all nonzero rows are above all rows of zeros
    # ECHELON LOOP
    # Find the first nonzero column. (column_is_all_zero())
    # pick a number to be the pivot in that column
    # interchange rows to put that number in the first row
    # create all zeros below the pivot
    # That column is done for now. "Ignore" that column and the row its in for now.
    # If there are more columns to echelonize, repeat loop.

    ##now RREF LOOP
    # now starting with the rightmost pivot, zero the positions above all pivots

    # when all columns have zeros above and below pivots, its done! the matrix is in RREF


# looks through each row,
# if it contains all zeroes, interchange it with the lowest nonzero row
def put_all_zero_rows_on_bottom(A):
    number_of_zero_rows = 0
    height = A.get_height()
    for row_index in range(height):
        # Only runs if the row index hasn't reached the known rows of all zeros
        if row_index < height - number_of_zero_rows:
            # check if its zero
            if row_is_all_zero(A.get_row(row_index)):
                # if its zero, switch it
                print("Row {0} is all zeros".format(row_index))
                row_interchange(A, height - 1 - number_of_zero_rows, row_index)
                number_of_zero_rows += 1
        # Only re-checks if the row index hasn't reached the known rows of all zeros
        if row_index < height - number_of_zero_rows:
            if row_is_all_zero(A.get_row(row_index)):
                print("ITS ALL ZERO AGAIN")
                # then check to make sure the new one isn't zero as well
                row_interchange(A, height - 1 - number_of_zero_rows, row_index)
                number_of_zero_rows += 1


# PAss in a row number! (integer index of the row you are checking to see if its zero)
# returns true if the passed list contains only 0 elements
def row_is_all_zero(row):
    for value in row:
        if value != 0:
            return False

    return True


# Pass in a "column" in the form of a list of integers.
# Returns true only if every integer in the list is zero
def column_is_all_zero(column):
    for number in column:
        if number != 0:
            return False

    return True


# pass in two row numbers (INTEGERS)  those two rows of te matrix will be interchanged with each other
def row_interchange(A, row1_index, row2_index):
    print("Interchanging rows with index {0}, {1} ".format(row1_index, row2_index))
    temp = A.get_row(row1_index)
    A.set_row(row1_index, A.get_row(row2_index))
    A.set_row(row2_index, temp)


# matrix row add operation to add a row into another row
def row_add(A, row_index1, row_index2):
    row1 = A.get_row(row_index1)
    row2 = A.get_row(row_index2)

    if len(row1) != len(row2):  # this should never happen
        print("Error! Attempting to add rows of different lengths")
        return A

    for x in range(len(row1)):  # both rows have the same legth
        row1[x] += row2[x]

    A.set_row(row_index1, row1)


# matrix row scale operation, scales the row at A[row_index] by scale factor
def row_scale(A, row_index, scale_factor):
    row = A.get_row(row_index)
    for x in range(len(row)):
        row[x] *= scale_factor
    A.set_row(row_index, row)


# Scales row 2 and adds it to row 1, but then scales row2 back so that it is unchanged
# row_index1 and row_index 2 are expected to be integer values < the number of rows in A
def row_scaled_add(A, row_index1, row_index2, scale_factor):
    row_scale(A, row_index2, scale_factor)
    row_add(A, row_index1, row_index2)
    inverse_scale_factor = 1 / scale_factor
    row_scale(A, row_index2, inverse_scale_factor)
