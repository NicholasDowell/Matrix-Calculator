
#This file will be nick's practice for creating a Matrix
#First steps are to :
#   1: Create a 2 dimensional array
#   2: Create methods to change the numbers stored in the Matrix
#   3: Create methods to Print the Matrix

from Matrix import Matrix
n = Matrix(3, 5)

n.set_value(1, 0, 0)
n.set_value(2, 0, 1)
n.set_value(3, 0, 2)
n.set_value(4, 0, 3)
n.print()
print("W")
n.add_column([7, 7, 3])
n.print()
print("W")

print(n.get_column(2))
print(n.get_row(2))

for x in range(6):
    n.replace_column(x, [x*x*20 % 3, (x*271) % 12, (x*403) % 11])

n.print()

n.replace_row(2, [0, 0, 0, 0, 0, 0])
n.print()

n.row_interchange(0,2)
n.print()

print(n.row_is_all_zero(0))
