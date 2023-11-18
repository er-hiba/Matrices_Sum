# This code prompts the user for the size of the matrices, allow them to
# input values for two matrices, display each matrix after it's filled,
# compute the sum of the matrices, and display the resulting matrix.


# Function that prints a matrix row by row
def display(matrix):
    for row in matrix:
        print(row)

# Main program 

# Prompt the user to input the number of rows and columns for the matrices
r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))


a_matrix = [[0 for _ in range(c)] for _ in range(r)]    # First matrix initialized with zeros
b_matrix = [[0 for _ in range(c)] for _ in range(r)]    # Second matrix initialized with zeros
c_matrix = [[0 for _ in range(c)] for _ in range(r)]    # Resultant matrix initialized with zeros


# Fill the first matrix by user-input integers and display it
print(f"\nEnter integer values for the first matrix:")
for i in range(r):
    for j in range(c):
        a_matrix[i][j] = int(input(f"Enter value at position [{i}][{j}]: "))

print("\n- The first matrix:")
display(a_matrix)

# Fill the second matrix by user-input integers and display it
print(f"\nEnter integer values for the second matrix:")
for i in range(r):
    for j in range(c):
        b_matrix[i][j] = int(input(f"Enter value at position [{i}][{j}]: "))

print("\n- The second matrix:")
display(b_matrix)

# Fill the third matrix by the sum of the first and second matrices
for i in range(r):
    for j in range(c):
        c_matrix[i][j] = a_matrix[i][j] + b_matrix[i][j]

# Display the resultant matrix
print("\n- The sum of the matrices is:")
display(c_matrix)
