# main.py

import time
import matrix_operations
import cython_matrix

def main():

    matrix = [
        [12311, 13212, 12315, 12316, 21212], [5, 110002, 1255, 13166, 312312], 
        [44231, 42342, 4324, 613, 6321312], [1312312, 31231, 55, 426, 123122], [111, 242342, 542342, 4126, 211]]

    def func_python(matrix):
        start_time = time.time()
        print("Using Python: ")
        inv_matrix = matrix_operations.inverse(matrix)
        print("Original Matrix:")
        print(matrix)
        print("Inverse Matrix:")
        print(inv_matrix)
        print("Total Running time = {:.3f} seconds\n".format(time.time() - start_time))

    def func_cython(matrix):
        start_time = time.time()
        print("Using Cython: ")
        inv_matrix = cython_matrix.inverse(matrix)
        print("Original Matrix:")
        print(matrix)
        print("Inverse Matrix:")
        print(inv_matrix)
        print("Total Running time = {:.3f} seconds".format(time.time() - start_time))


    func_python(matrix)
    func_cython(matrix)

if __name__ == "__main__":
    main()