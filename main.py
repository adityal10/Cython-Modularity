# main.py

import time
import matrix_operations
import cython_matrix


def func_python(matrix):
    start_time = time.time()
    print("Using Python: ")
    inv_matrix = matrix_operations.inverse(matrix)
    # print("\nOriginal Matrix:")
    # for row in matrix:
    #     print(row)
    print("\nInverse Matrix:")
    for row in inv_matrix:
        print(row)
    print("Total Running time = {:.3f} seconds\n".format(time.time() - start_time))

def func_cython(matrix):
    start_time = time.time()
    print("Using Cython: ")
    inv_matrix = cython_matrix.inverse(matrix)
    # print("\nOriginal Matrix:")
    # for row in matrix:
    #     print(row)
    print("\nInverse Matrix:")
    for row in inv_matrix:
        print(row)
    print("Total Running time = {:.3f} seconds".format(time.time() - start_time))

def main():

    matrix = [
        [12311, 13212, 12315, 1234234216, 21212, 32131, 31231], [5, 110002, 1255, 13166, 312312, 3123, 32131], 
        [44231, 42342, 4324, 613, 6321312,2131, 31231], [1312312, 31231, 55, 426, 123122, 1231, 213123], 
        [111, 242342, 542342, 4126, 211, 31231, 123123], [3123,12313,32131,1231,1231231, 31231, 2131],
        [31231, 23123, 31231, 123132, 123123, 3213, 123]]


    func_python(matrix)
    func_cython(matrix)

if __name__ == "__main__":
    main()