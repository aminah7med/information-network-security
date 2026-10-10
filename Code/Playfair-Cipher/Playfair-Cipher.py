keyword = input("Enter your keyword: ").lower()
alphabet = "abcdefghiklmnopqrstuvwxyz"

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
            
matrix_letters = ""

# Add keyword letters first
for char in keyword:
    if char not in matrix_letters:
        matrix_letters += char

# Add the remaining alphabet letters
for char in alphabet:
    if char not in matrix_letters:
        matrix_letters += char

# Build the 5x5 matrix
matrix = []

for i in range(0, 25, 5):
    row = matrix_letters[i:i+5]
    matrix.append(row)
    
print(matrix)