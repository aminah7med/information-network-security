# Playfair Cipher Algorithm

The Lecture 02 source scan is available, but its algorithm details have not yet been transcribed and verified. This file remains a placeholder until the handwritten notes are reviewed.

Related: [Lecture 02 source](../../Lectures/Lec-02/source/Lec-02.pdf), [code](../../Code/Playfair-Cipher/README.md), [problems](../../Problems/Playfair/README.md), and [solutions](../../Solutions/Playfair/README.md).
# Playfair Cipher

## 1. Overview

The **Playfair Cipher** is a classical symmetric encryption algorithm that encrypts plaintext using pairs of letters instead of encrypting each letter individually.

It uses a **5 × 5 matrix** constructed from a keyword and the English alphabet. Since the matrix contains 25 cells, the letters `I` and `J` share the same cell.

The encryption process depends on the positions of the two letters in each pair.

> **Note:** The Playfair Cipher is a classical educational cipher and is not secure enough for modern applications.

---

## 2. Algorithm Objectives

- Understand the basic concept of pair-based encryption.
- Build a 5 × 5 matrix using a keyword.
- Prepare plaintext for encryption.
- Locate characters inside the matrix.
- Apply the three Playfair encryption rules.
- Generate the final ciphertext.

---

## 3. How It Works

The encryption process consists of the following steps:

1. Read the keyword and plaintext.
2. Normalize the keyword and plaintext.
3. Replace `J` with `I`.
4. Construct the 5 × 5 matrix.
5. Prepare the plaintext into pairs of letters.
6. Encrypt each pair using the Playfair rules.
7. Combine the encrypted pairs to produce the ciphertext.

---

## 4. Building the 5 × 5 Matrix

### Example Keyword

```text
LEMON
```

### Step 1: Remove Repeated Letters

The keyword contains no repeated letters, so it remains:

```text
LEMON
```

### Step 2: Add the Remaining Alphabet

Append the letters of the English alphabet that do not appear in the keyword. Exclude `J` because `I` and `J` share one cell.

### Step 3: Construct the Matrix

The resulting matrix is:

```text
L E M O N
A B C D F
G H I K P
Q R S T U
V W X Y Z
```

Each letter appears exactly once, except that `I` represents both `I` and `J`.

---

## 5. Plaintext Preparation

Before encryption, the plaintext must be divided into pairs.

### Example

```text
Plaintext: BALLOON
```

The letters are grouped as follows:

```text
BA | LL | OO | N
```

Repeated letters cannot remain together in the same pair. Insert a filler letter, commonly `X`, to separate them.

After preparation:

```text
BA | LX | LO | ON
```

The prepared plaintext is:

```text
BALXLOON
```

### Preparation Rules

- Convert letters to lowercase or uppercase consistently.
- Replace `J` with `I`.
- Insert a filler letter between repeated letters in a pair.
- If one letter remains at the end, append a filler letter.
- Divide the prepared text into pairs.

**Implementation note:** If the repeated letter is itself `X`, choose a filler strategy that avoids creating another identical pair.

---

## 6. Encryption Rules

For each pair of letters, locate both letters in the matrix and apply exactly one of the following rules.

### Rule 1: Same Row

If both letters are in the same row, replace each letter with the letter immediately to its right.

If a letter is at the end of the row, wrap around to the first column.

Example:

```text
L E M O N
```

```text
L → E
N → L
```

### Rule 2: Same Column

If both letters are in the same column, replace each letter with the letter immediately below it.

If a letter is at the bottom of the column, wrap around to the top.

Example:

```text
L
A
G
Q
V
```

```text
L → A
V → L
```

### Rule 3: Rectangle

If the letters are in different rows and different columns, they form the corners of a rectangle.

Replace each letter with the letter in the same row but in the other letter's column.

Example:

```text
L E M O N
A B C D F
G H I K P
Q R S T U
V W X Y Z
```

For the pair `LP`:

- `L` is at row 1, column 1.
- `P` is at row 3, column 5.

Swap their columns while keeping their rows unchanged:

```text
LP → NG
```

---

## 7. Complete Encryption Example

Use the keyword `LEMON` and plaintext `HELP`.

### Step 1: Prepare the Plaintext

```text
HELP → HE | LP
```

No filler letters are needed.

### Step 2: Encrypt Each Pair

| Pair | Rule | Result |
|---|---|---|
| `HE` | Same column | `RB` |
| `LP` | Rectangle | `NG` |

### Step 3: Combine the Results

```text
Plaintext:  HELP
Ciphertext: RBNG
```

Therefore, the ciphertext is:

```text
RBNG
```

---

## 8. Python Implementation

The following implementation builds the matrix automatically, prepares the plaintext, and encrypts the letter pairs.

```python
# Playfair Cipher - Encryption

# Step 1: Get the keyword and plaintext
keyword = input("Enter your keyword: ").lower().replace("j", "i")
plaintext = input("Enter your plaintext: ").lower()

# Step 2: Define the alphabet without J
alphabet = "abcdefghiklmnopqrstuvwxyz"

# Step 3: Build the matrix letters
matrix_letters = ""

# Add unique keyword letters first
for char in keyword:
    if char in alphabet and char not in matrix_letters:
        matrix_letters += char

# Add the remaining alphabet letters
for char in alphabet:
    if char not in matrix_letters:
        matrix_letters += char

# Step 4: Build the 5x5 matrix
matrix = []

for i in range(0, 25, 5):
    row = matrix_letters[i:i + 5]
    matrix.append(row)

# Display the matrix
print("\nPlayfair Matrix:")
for row in matrix:
    print(" ".join(row))


# Step 5: Find the position of a character
def find_position(matrix, char):
    if char == "j":
        char = "i"

    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col


# Step 6: Prepare the plaintext
plaintext = "".join(
    char for char in plaintext
    if char in "abcdefghijklmnopqrstuvwxyz"
).replace("j", "i")

prepared_text = ""
i = 0

while i < len(plaintext):
    first = plaintext[i]

    if i + 1 >= len(plaintext):
        second = "x"
        i += 1
    elif plaintext[i] == plaintext[i + 1]:
        second = "x"
        i += 1
    else:
        second = plaintext[i + 1]
        i += 2

    prepared_text += first + second


# Step 7: Encrypt one pair
def encrypt_pair(matrix, first, second):
    row1, col1 = find_position(matrix, first)
    row2, col2 = find_position(matrix, second)

    # Rule 1: Same row - move right
    if row1 == row2:
        col1 = (col1 + 1) % 5
        col2 = (col2 + 1) % 5

    # Rule 2: Same column - move down
    elif col1 == col2:
        row1 = (row1 + 1) % 5
        row2 = (row2 + 1) % 5

    # Rule 3: Rectangle - swap columns
    else:
        col1, col2 = col2, col1

    return matrix[row1][col1] + matrix[row2][col2]


# Step 8: Encrypt the complete plaintext
ciphertext = ""

for i in range(0, len(prepared_text), 2):
    first = prepared_text[i]
    second = prepared_text[i + 1]

    ciphertext += encrypt_pair(matrix, first, second)


# Step 9: Display the results
print("\nOriginal plaintext:", plaintext)
print("Prepared plaintext:", prepared_text)
print("Ciphertext:", ciphertext)
```

---

## 9. How to Run

Save the code in a file named `playfair_encryption.py`.

Run it from your terminal:

```bash
python playfair_encryption.py
```

Example input:

```text
Enter your keyword: LEMON
Enter your plaintext: HELP
```

Expected ciphertext:

```text
rbng
```

---

## 10. Time and Space Complexity

Let \(n\) be the length of the plaintext.

| Operation | Complexity |
|---|---|
| Building the matrix | \(O(1)\) for the fixed 25-letter alphabet |
| Finding a character's position | \(O(1)\) for the fixed 5 × 5 matrix |
| Preparing the plaintext | \(O(n)\) |
| Encrypting all pairs | \(O(n)\) |
| Total time | \(O(n)\) |
| Auxiliary space | \(O(n)\) for the prepared text and ciphertext |

These complexities assume the standard fixed-size Playfair matrix and account for the text-processing operations.

---

## 11. Limitations

- The `I` and `J` distinction is lost during normalization.
- Filler letters can make the original plaintext ambiguous during decryption.
- The cipher preserves patterns and is vulnerable to classical cryptanalysis.
- It should be used for learning classical cryptography, not for protecting sensitive information.

---

## 12. Key Takeaways

- Playfair encrypts **pairs of letters** rather than individual letters.
- The keyword determines the matrix layout.
- The matrix contains 25 cells, with `I` and `J` sharing one cell.
- Encryption uses three rules: **Same Row, Same Column, and Rectangle**.
- Python `for` loops, string indexing, lists, and conditional statements are sufficient to implement the core algorithm.
- Playfair is useful for understanding classical cryptography, but it is not suitable for modern security.
