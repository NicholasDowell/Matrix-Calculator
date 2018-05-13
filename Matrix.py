"""""
#This will be the fundamental matrix that is used for Matrix Operations
# it stores a 2d grid of values
#To DO: Restrict the methods so that they will not resize the matrix when they shouldnt
#CONVENTION is [ROW][COLUMN]  BE CAREFUL
"""


class Matrix:
    def __init__(self, rows, columns):
        self._data = [[0 for x in range(columns)] for y in range(rows)]
        self._height = rows
        self._width = columns

    def set_width(self, new_width):
        self._width = new_width

    def set_height(self, new_height):
        self._height = new_height

    # returns the matrix's height (number of rows)
    def get_height(self):
        return self._height

    # returns the matrix's width (number of columns)
    def get_width(self):
        return self._width

    # replaces a single number in the matrix
    def set_value(self, new_value, row, column):
        self._data[row][column] = new_value

    # returns a list containing all elements of one row of the matrix
    def get_row(self, row_index):
        return self._data[row_index]

    def set_row(self, row_index, new_row):
        self._data[row_index] = new_row

    # returns a list containing all elements of one column of the matrix
    def get_column(self, column_index):
        column = []
        for row in range(self._height):
            column.append(self._data[row][column_index])
        return column

    def set_column(self, column_index, new_column):
        new_column_index = 0
        for row in self._data:
            row[column_index] = new_column[new_column_index]
            new_column_index += 1

    # returns the value stored at one coordinate of the matrix
    def get_value(self, row, column):
        return self._data[row][column]

    # returns the data stored in the matrix
    def get_data(self):
        return self._data
