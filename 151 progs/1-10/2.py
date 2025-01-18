# #WAP TO PRINT MULTIPLES OF INPUT NO
#
# n = int(input("Number: "))
#
# for i in range(1, 11):
#     print(f"{n} x {i} = {n*i} ")
#
#
# # def tower_of_hanoi(n, a, b, c):
# #     if n == 1:
# #         print("Move disk 1 from", a, "to", b)
# #         return
# #
# #     tower_of_hanoi(n - 1, a, c, b)
# #
# #     print("Move disk", n, "from", a, "to", b)
# #
# #     tower_of_hanoi(n - 1, c, b, a)
# #
# #
# # n = int(input("Enter the number of disks: "))
# # tower_of_hanoi(n, 'A', 'C', 'B')

def input_matrix(rows, cols):
    print(f"Enter the elements of a {rows}x{cols} matrix row by row:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        while len(row) != cols:
            print(f"Row {i + 1} must have {cols} elements. Try again.")
            row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix.append(row)
    return matrix


def multiply_matrices(A, B):
    # Dimensions of matrices
    m = len(A)
    n = len(A[0])
    p = len(B[0])

    # Resultant matrix of size m x p
    result = [[0] * p for _ in range(m)]

    # Multiply matrices
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j] #initial statement / formula
    return result


# Input dimensions for matrix A
rows_A = int(input("Enter the number of rows in Matrix A: "))
cols_A = int(input("Enter the number of columns in Matrix A: "))

# Input dimensions for matrix B
rows_B = int(input("Enter the number of rows in Matrix B: "))
cols_B = int(input("Enter the number of columns in Matrix B: "))

# Check compatibility for multiplication
if cols_A != rows_B:
    print(
        "Matrix multiplication not possible. Number of columns in Matrix A must equal the number of rows in Matrix B.")
else:
    # Input matrices
    A = input_matrix(rows_A, cols_A)
    B = input_matrix(rows_B, cols_B)

    # Multiply matrices
    result = multiply_matrices(A, B)

    # Display result
    print("\nResultant Matrix:")
    for row in result:
        print(row)