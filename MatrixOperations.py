##The MatrixOperations class includes a group of methods that allow the matrix to be used for row reduction operations
# prints out all values stored in the matrix to the console


def print(A):
    row_string = "BAA"
    for row in range(A.get_width()):
        print(row_string)
        for column in range(A.get_height()):
            row_string += str(A.get_value(row, column)) + " "
            print(row_string)
        print(row_string)
        row_string = ""


# replaces a row in the matrix with the passed new row
def replace_row(A, row_number, new_row):
    A.get_data[row_number] = [number for number in new_row]


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


# changes the stored matrix into a row reduced echelon form
def rref(A):
    print(1)
    # does the thing

    ## Step 1: regular echelon form
    # all numbers below pivot are zero
    # all pivots to the right of above pivots
    # all nonzero rows are above all rows of zeros
    # ECHELON LOOP
    # Find the first nonzero column.
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
    row_index = 0
    for row in A.get_data():
        # check if its zero
        # if its zero, switch it
        # then check to make sure the new one isnt zero
        if A.row_is_all_zero(row):
            A.row_interchange(A.get_height() - number_of_zero_rows, A.get_row(row_index))
            number_of_zero_rows += 1

        if A.row_is_all_zero(row):
            A.row_interchange(A.get_height() - number_of_zero_rows, A.get_row(row_index))
        row_index += 1


def row_interchange(A, row1_index, row2_index):
    # pass in two row numbers (INTEGERS)  those two rows of te matrix will be interchanged with each other
    temp = A.get_row(row1_index)
    A.set_row(row1_index, row2_index)
    A.set_row(row2_index, temp)

