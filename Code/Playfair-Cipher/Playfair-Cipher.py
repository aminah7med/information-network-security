keyword = input("Enter your keyword: ").lower()
alphabet = "abcdefghiklmnopqrstuvwxyz"
matrix = []

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
            
def encrypt_pair(matrix, first, second):
    row1, col1 = find_position(matrix, first)
    row2, col2 = find_position(matrix, second)

    if row1 == row2:
        col1 = (col1 + 1) % 5
        col2 = (col2 + 1) % 5

        encrypted_first = matrix[row1][col1]
        encrypted_second = matrix[row2][col2]

    elif col1 == col2:
        row1 = (row1 + 1) % 5
        row2 = (row2 + 1) % 5

        encrypted_first = matrix[row1][col1]
        encrypted_second = matrix[row2][col2]

    else:
        encrypted_first = matrix[row1][col2]
        encrypted_second = matrix[row2][col1]

    return encrypted_first + encrypted_second

plaintext = input("Enter your plaintext: ").lower()
plaintext = plaintext.replace("j", "i")

ciphertext = ""

for i in range(0, len(plaintext), 2):
    first = plaintext[i]
    second = plaintext[i + 1]

    ciphertext += encrypt_pair(matrix, first, second)

print("Ciphertext:", ciphertext)

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

for i in range(0, 25, 5):
    row = matrix_letters[i:i+5]
    matrix.append(row)
    
print(matrix)