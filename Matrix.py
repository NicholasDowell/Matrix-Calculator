#THIS IS A TEST COMMENT THAT I AM MAKING TO TEST GIT

#This will be the fundamental matrix that is used for Matrix Operations
# it stores a 2d grid of values

#To DO: Restrict the methods so that they will not resize the matrix when they shouldnt

#CONVENTION is [ROW][COLUMN]  BE CAREFUL
class Matrix:
    def __init__(self, rows, columns):
        self.v = [[0 for x in range(columns)] for y in range(rows)]
        self.height = rows
        self. width = columns

    #returns the matrix's height (number of rows)
    def get_height(self):
        return self.height

    #returns the matrix's width (number of columns)
    def get_width(self):
        return self.width


    #prints out all values stored in the matrix to the console
    def print(self):
        row_string = ""
        for y in range(len(self.v)):
            #print("Printing row number" + str(y+1))
            for x in range(len(self.v[y])):
                row_string += str(self.v[y][x]) + " "
            print(row_string)
            row_string = ""

    # replaces a row in the matrix with the passed new row
    def replace_row(self, row_number, new_row):
        self.v[row_number] = [x for x in new_row]
        return

    #replaces a column in the matrix with the passed new column
    #Column_number represents the index of the column in the matrix that will be replaced.
    #column_index represents the current index in the new column (the value that is being placed into the matrix)
    # the passed column must have the same number of entries as the number of rows in the matrix
    def replace_column(self, column_number, new_column):

        #What do you do to replace a column?
        column_index = 0
        for x in self.v:
            x[column_number] = new_column[column_index]
            column_index += 1
        return

    #adds a new column on the rightmost side of the matrix.
    def add_column(self, new_column):
        self.width += 1
        for x in range(self.height):
            self.v[x].append(new_column[x])

        return

    # adds a new row to the bottom of the matrix
    def add_row(self, new_row):
        self.height += 1
        self.v.append(new_row)

    #replaces a single number in the matrix
    def replace_value(self, new_value, row, column):
        self.v[row][column] = new_value

    #returns a list containing all elements of one row of the matrix
    def get_row(self, row_index):
        row = []
        for x in range(self.width):
            row.append(self.v[row_index][x])
        return row

    #returns a list containing all elements of one column of the matrix
    def get_column(self, column_index):
        column = []
        for x in range(self.height):
            column.append(self.v[x][column_index])

        return column

    #returns the value stored at one coordinate of the matrix
    def get_value(self, row, column):
        return self.v[row][column]


    #changes the stored matrix into a row reduced echelon form
    def rref(self):
        print(1)
        #does the thing

        ## Step 1: regular echelon form
            #all numbers below pivot are zero
            #all pivots to the right of above pivots
            #all nonzero rows are above all rows of zeros
        #ECHELON LOOP
        #Find the first nonzero column.
        #pick a number to be the pivot in that column
        #interchange rows to put that number in the first row
        #create all zeros below the pivot
        #That column is done for now. "Ignore" that column and the row its in for now.
        #If there are more columns to echelonize, repeat loop.

        ##now RREF LOOP
        # now starting with the rightmost pivot, zero the positions above all pivots


        #when all columns have zeros above and below pivots, its done! the matrix is in RREF


    # looks through each row,
    # if it contains all zeroes, interchange it with the lowest nonzero row
    def put_all_zero_rows_on_bottom(self):
        number_of_zero_rows = 0
        row_index = 0
        for x in self.v:
            #check if its zero
            #if its zero, switch it
            #then check to make sure the new one isnt zero
            if self.row_is_all_zero(x):
                self.row_interchange(self.height-number_of_zero_rows, self.v[row_index])
                number_of_zero_rows += 1

            if self.row_is_all_zero(x):
                self.row_interchange(self.height-number_of_zero_rows, self.v[row_index])
            row_index += 1



    def row_interchange(self, row1, row2):
        #pass in two row numbers (INTEGERS)  those two rows of te matrix will be interchanged with each other
        temp = self.v[row1]
        self.v[row1] = self.v[row2]
        self.v[row2] = temp

        #PAss in a row number! (integer index of the row you are checking to see if its zero)
    def row_is_all_zero(self, row):
        for x in self.v[row]:
            if x != 0:
                return False

        return True
