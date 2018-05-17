#MatrixExceptions holds a set of exceptions that will make working on the MatrixOperations easier


class RowSizeException(Exception):
    def __init__(self, message):
        print(message)

