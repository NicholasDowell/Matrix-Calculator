# This will be the fundamental matrix that is used for Matrix Operations
# it stores a 2d grid of values
# 11
# To DO: Restrict the methods so that they will not resize the matrix when they shouldnt


# CONVENTION is [ROW][COLUMN]  BE CAREFUL
class Matrix:
    def __init__(self, rows, columns):
        self._data = [[0 for x in range(columns)] for y in range(rows)]
        self._height = rows
        self._width = columns

    # returns the matrix's height (number of rows)
    def get_height(self):
        return self._height

    def set_height(self, new_height):
        self._height = new_height

    # returns the matrix's width (number of columns)
    def get_width(self):
        return self._width

    # replaces a row in the matrix with the passed new row
    def replace_row(self, row_number, new_row):
        self._data[row_number] = [column for column in new_row]
        return

    # replaces a column in the matrix with the passed new column
    # Column_number represents the index of the column in the matrix that will be replaced.
    # column_index represents the current index in the new column (the value that is being placed into the matrix)
    # the passed column must have the same number of entries as the number of rows in the matrix
    def replace_column(self, column_number, new_column):
        # What do you do to replace a column?
        column_index = 0
        for x in self._data:
            x[column_number] = new_column[column_index]
            column_index += 1
        return

    # adds a new column on the rightmost side of the matrix.
    def add_column(self, new_column):
        self._width += 1
        for x in range(self._height):
            self._data[x].append(new_column[x])

        return

    # adds a new row to the bottom of the matrix
    def add_row(self, new_row):
        self._height += 1
        self._data.append(new_row)

    # replaces a single number in the matrix
    def replace_value(self, new_value, row, column):
        self._data[row][column] = new_value

    def set_row(self, row_index, new_row):
        self._data[row_index] = new_row

    # returns a list containing all elements of one row of the matrix
    def get_row(self, row_index):
        return self._data[row_index]

    # returns a list containing all elements of one column of the matrix
    def get_column(self, column_index):
        column = []
        for x in range(self._height):
            column.append(self._data[x][column_index])
        return column

    # returns the value stored at one coordinate of the matrix
    def get_value(self, row, column):
        return self._data[row][column]

    def get_data(self):
        return self._data

    def set_width(self, new_width):
        self._width = new_width
