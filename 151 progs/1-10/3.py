#WAP TO PRINT STAR PATTERN

# n = int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#     print("*" * i)

'''
# 76. LONGEST LINE IN THE FILE

with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("Python is awesome!\n")
    file.write("Writing to files is easy.\n")

print("File written successfully!")


try:
    # Replace the path below with the actual path to your C++ file
    with open("example.txt", "r") as file:
        lines = file.readlines()  # Read all lines into a list
        if lines:  # Check if the list is not empty
            longest_line = max(lines, key=len).strip()  # Find the longest line
            print("Longest line:", longest_line)
        else:
            print("The file is empty.")
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

'''


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
    # Result will store the element-wise multiplication results
    result = []

    # Iterate through each element and multiply corresponding elements
    for i in range(len(A)):  # Rows of A
        row_result = []
        for j in range(len(A[0])):  # Columns of A
            # Ensure we do the element-wise multiplication for corresponding elements
            row_result.append(A[i][j] * B[i][j])   #modified formula
        result.append(row_result)

    return result


# Input dimensions for matrix A
rows_A = int(input("Enter the number of rows in Matrix A: "))
cols_A = int(input("Enter the number of columns in Matrix A: "))

# Input dimensions for matrix B
rows_B = int(input("Enter the number of rows in Matrix B: "))
cols_B = int(input("Enter the number of columns in Matrix B: "))

# Check if the dimensions of A and B are the same for element-wise multiplication
if rows_A != rows_B or cols_A != cols_B:
    print("Matrix multiplication not possible. The matrices must have the same dimensions.")
else:
    # Input matrices
    A = input_matrix(rows_A, cols_A)
    B = input_matrix(rows_B, cols_B)

    # Multiply matrices element-wise
    result = multiply_matrices(A, B)

    # Display result
    print("\nResult of element-wise multiplication:")
    for row in result:
        print(row)