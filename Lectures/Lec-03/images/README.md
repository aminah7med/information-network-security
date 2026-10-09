# Playfair Cipher — Complete Guide

A practical guide to understanding the Playfair encryption algorithm, building its matrix, preparing plaintext, encrypting and decrypting messages, and implementing the algorithm in Python.

## Table of Contents

- [1. Introduction](#1-introduction)
- [2. How Playfair Works](#2-how-playfair-works)
- [3. Building the Matrix](#3-building-the-matrix)
- [4. Preparing the Plaintext](#4-preparing-the-plaintext)
- [5. Encryption Rules](#5-encryption-rules)
- [6. Complete Encryption Examples](#6-complete-encryption-examples)
- [7. Decryption](#7-decryption)
- [8. Complete Python Implementation](#8-complete-python-implementation)
- [9. Understanding the Code](#9-understanding-the-code)
- [10. How to Run the Program](#10-how-to-run-the-program)
- [11. Common Mistakes](#11-common-mistakes)
- [12. Summary](#12-summary)

---

## 1. Introduction

The **Playfair Cipher** is a classical encryption algorithm that encrypts pairs of letters instead of processing each letter individually.

For example, the plaintext:

```text
HELLO
```

is divided into pairs:

```text
HE | LX | LO
```

The algorithm uses a 5×5 matrix containing the English alphabet. The positions of each pair's letters determine how the pair is encrypted.

Unlike the Caesar Cipher, Playfair does not use one fixed shift for every character. Instead, it applies different rules depending on the positions of the two letters.

### Important Terms

| Term | Meaning |
|---|---|
| Plaintext | The original message |
| Keyword | The word used to construct the matrix |
| Matrix | A 5×5 table containing the letters |
| Digraph | A pair of letters |
| Ciphertext | The encrypted message |
| Encryption | Converting plaintext into ciphertext |
| Decryption | Recovering the prepared plaintext from ciphertext |

## 2. How Playfair Works

The algorithm follows these steps:

1. Choose a keyword.
2. Build a 5×5 matrix using the keyword.
3. Fill the remaining cells with unused alphabet letters.
4. Prepare the plaintext and divide it into pairs.
5. Encrypt each pair using one of three rules.
6. Combine the encrypted pairs to produce the ciphertext.

Decryption uses the same matrix but reverses the row and column movements.

---

## 3. Building the Matrix

A 5×5 matrix contains 25 cells, while the English alphabet contains 26 letters.

The standard Playfair convention used in this guide combines **I and J into one cell**.

### Step 1: Choose a Keyword

We will use:

```text
LEMON
```

### Step 2: Write the Keyword Without Repetition

The keyword letters are:

```text
L E M O N
```

If a letter appears more than once in the keyword, keep only its first occurrence.

For example:

```text
BALLOON → BALON
```

### Step 3: Add the Remaining Letters

Continue with the alphabet in order, skipping letters already used in the keyword and skipping J because I and J share one cell.

### Step 4: Complete the Matrix

The resulting matrix is:

| | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |
|---|---|---|---|---|---|
| Row 1 | L | E | M | O | N |
| Row 2 | A | B | C | D | F |
| Row 3 | G | H | I/J | K | P |
| Row 4 | Q | R | S | T | U |
| Row 5 | V | W | X | Y | Z |

**Important rules:**

- The keyword comes first.
- Duplicate keyword letters are removed.
- The remaining letters are added alphabetically.
- I and J share a position.
- Every matrix cell must contain a unique letter position.

The same matrix is used throughout an encryption or decryption operation.

---

## 4. Preparing the Plaintext

Before encryption, divide the message into pairs of letters.

Two important rules apply.

### Rule 1: Repeated Letters in the Same Pair

If both letters in a pair are identical, insert X after the first letter and begin the next pair with the second letter.

Example:

```text
Plaintext: BALLOON
```

Start dividing the message:

```text
BA | LL | OO | N
```

The pair `LL` contains repeated letters, so insert X:

```text
BA | LX
```

Continue from the second L:

```text
LO | ON
```

The prepared plaintext becomes:

```text
BALXLOON
```

Its pairs are:

```text
BA | LX | LO | ON
```

### Rule 2: An Odd Number of Letters

If one letter remains without a partner, append X.

Example:

```text
Plaintext: CAT
```

Initial division:

```text
CA | T
```

After padding:

```text
CA | TX
```

Prepared plaintext:

```text
CATX
```

### Another Example: HELLO

Original plaintext:

```text
HELLO
```

Divide and prepare:

```text
HE | LL | O
HE | LX | LO
```

Prepared plaintext:

```text
HELXLO
```

**Remember:** After inserting X between repeated letters, continue from the second repeated letter. Do not skip it.

---

## 5. Encryption Rules

After preparing the plaintext, encrypt each pair separately.

There are three possible cases.

### Rule 1: Same Row

If both letters are in the same row, replace each letter with the letter immediately to its right.

If a letter is in the last column, wrap around to the first column.

Example using the first row:

```text
L E M O N
```

Encrypt `LO`:

- L moves right to E.
- O moves right to N.

Result:

```text
LO → EN
```

Another example:

```text
ON → NL
```

O moves to N, while N wraps around to L.

### Rule 2: Same Column

If both letters are in the same column, replace each letter with the letter immediately below it.

If a letter is in the last row, wrap around to the first row.

Consider column 2:

```text
E
B
H
R
W
```

Encrypt `ER`:

- E moves down to B.
- R moves down to W.

Result:

```text
ER → BW
```

### Rule 3: Rectangle

If the letters are in different rows and different columns, they form two opposite corners of a rectangle.

Replace each letter with the letter in the same row but in the other letter's column.

Example:

```text
LX
```

Using the matrix:

- L is in row 1, column 1.
- X is in row 5, column 3.

The rectangle rule gives:

- L becomes M.
- X becomes V.

Result:

```text
LX → MV
```

**The key idea:** Each letter stays in its original row but takes the column of the other letter.

### Encryption Rules Summary

| Condition | Rule |
|---|---|
| Same row | Move right |
| Same column | Move down |
| Different rows and columns | Swap columns |

---

## 6. Complete Encryption Examples

All examples in this section use the keyword `LEMON` and the matrix shown earlier.

### Example 1: Encrypt BALLOON

**Given:**

```text
Keyword: LEMON
Plaintext: BALLOON
```

Prepare the plaintext:

```text
BA | LX | LO | ON
```

Encrypt each pair:

| Pair | Rule | Transformation | Result |
|---|---|---|---|
| BA | Same row | B → C, A → B | CB |
| LX | Rectangle | L → M, X → V | MV |
| LO | Same row | L → E, O → N | EN |
| ON | Same row | O → N, N → L | NL |

Combine the results:

```text
CB + MV + EN + NL
```

**Final ciphertext:**

```text
CBMVENNL
```

Therefore:

```text
BALLOON → CBMVENNL
```

### Example 2: Encrypt HELP

**Given:**

```text
Keyword: LEMON
Plaintext: HELP
```

Divide the plaintext:

```text
HE | LP
```

Encrypt `HE`:

- H and E share column 2.
- H moves down to R.
- E moves down to B.

```text
HE → RB
```

Encrypt `LP`:

- L is at row 1, column 1.
- P is at row 3, column 5.
- They form a rectangle.
- L becomes N.
- P becomes G.

```text
LP → NG
```

Final ciphertext:

```text
RBNG
```

### Example 3: Encrypt MEET

**Given:**

```text
Keyword: LEMON
Plaintext: MEET
```

Divide the plaintext:

```text
ME | ET
```

Encrypt `ME`:

- M and E share the first row.
- M moves right to O.
- E moves right to M.

```text
ME → OM
```

Encrypt `ET`:

- E is at row 1, column 2.
- T is at row 4, column 4.
- They form a rectangle.
- E becomes O.
- T becomes R.

```text
ET → OR
```

Final ciphertext:

```text
OMOR
```

### Example 4: Encrypt CAT

**Given:**

```text
Keyword: LEMON
Plaintext: CAT
```

Prepare the plaintext:

```text
CA | TX
```

Encrypt `CA`:

- C and A share the second row.
- C moves right to D.
- A moves right to B.

```text
CA → DB
```

Encrypt `TX`:

- T is at row 4, column 4.
- X is at row 5, column 3.
- They form a rectangle.
- T becomes S.
- X becomes Y.

```text
TX → SY
```

Final ciphertext:

```text
DBSY
```

The extra X was added because the original plaintext contained an odd number of letters.

### Example 5: Encrypt BALON

This example demonstrates that a keyword containing repeated letters is normalized before building the matrix.

**Given:**

```text
Keyword: BALLOON
Plaintext: CAT
```

The keyword is normalized:

```text
BALLOON → BALON
```

The matrix begins:

| | | | | |
|---|---|---|---|---|
| B | A | L | O | N |
| C | D | E | F | G |
| H | I/J | K | M | P |
| Q | R | S | T | U |
| V | W | X | Y | Z |

Prepare the plaintext:

```text
CA | TX
```

Encrypting with this matrix:

- `CA` is in the same row, so C → D and A → L.
- `TX` forms a rectangle, so T → S and X → Y.

Final ciphertext:

```text
DLSY
```

This demonstrates why the keyword matters: changing the keyword changes the matrix and therefore changes the ciphertext.

---

## 7. Decryption

Decryption uses the same matrix, but reverses the row and column movements.

### Rule 1: Same Row

During encryption, letters move right.

During decryption, letters move left.

Example:

```text
CB → BA
```

- C moves left to B.
- B moves left to A.

### Rule 2: Same Column

During encryption, letters move down.

During decryption, letters move up.

Example:

```text
RB → HE
```

- R moves up to H.
- B moves up to E.

### Rule 3: Rectangle

The rectangle rule is the same for encryption and decryption: swap the columns while keeping each letter in its original row.

Example:

```text
MV → LX
```

### Complete Decryption Example

Decrypt:

```text
Ciphertext: CBMVENNL
Keyword: LEMON
```

Divide into pairs:

```text
CB | MV | EN | NL
```

Decrypt each pair:

| Pair | Rule | Result |
|---|---|---|
| CB | Same row, move left | BA |
| MV | Rectangle | LX |
| EN | Same row, move left | LO |
| NL | Same row, move left | ON |

Combine the results:

```text
BALXLOON
```

The original word was:

```text
BALLOON
```

The X was inserted during plaintext preparation to separate the repeated L letters.

**Important:** Decryption recovers the prepared plaintext. It cannot always determine which X characters were inserted or whether I/J originally appeared as I or J. Recovering the exact original message may require context.

---

## 8. Complete Python Implementation

The following implementation includes matrix construction, plaintext preparation, encryption, decryption, and a simple interactive interface.

It uses lowercase letters internally, combines I and J, and preserves spaces and punctuation in the output. These non-letter characters are not encrypted.

Create a file named `playfair.py` and copy this code into it.

```python
# Playfair Cipher
# Educational implementation using a 5x5 matrix.
# I and J share one cell.

ALPHABET = "abcdefghiklmnopqrstuvwxyz"
FILLER = "x"


def build_matrix(keyword):
    keyword = keyword.lower().replace("j", "i")
    matrix_letters = ""

    for char in keyword:
        if char.isalpha() and char in ALPHABET:
            if char not in matrix_letters:
                matrix_letters += char

    for char in ALPHABET:
        if char not in matrix_letters:
            matrix_letters += char

    matrix = []

    for i in range(0, 25, 5):
        matrix.append(list(matrix_letters[i:i + 5]))

    return matrix


def find_position(matrix, char):
    if char == "j":
        char = "i"

    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col

    return None


def prepare_text(text):
    text = "".join(
        char.lower()
        for char in text
        if char.isalpha() and char.lower() in "abcdefghijklmnopqrstuvwxyz"
    )

    text = text.replace("j", "i")
    prepared = ""
    i = 0

    while i < len(text):
        first = text[i]

        if i + 1 >= len(text):
            second = FILLER
            i += 1

        elif text[i] == text[i + 1]:
            second = FILLER
            i += 1

        else:
            second = text[i + 1]
            i += 2

        prepared += first + second

    return prepared


def transform_pair(matrix, first, second, decrypt=False):
    row1, col1 = find_position(matrix, first)
    row2, col2 = find_position(matrix, second)

    if row1 == row2:
        if decrypt:
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        else:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5

    elif col1 == col2:
        if decrypt:
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        else:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5

    else:
        col1, col2 = col2, col1

    return matrix[row1][col1] + matrix[row2][col2]


def encrypt(plaintext, keyword):
    matrix = build_matrix(keyword)
    prepared = prepare_text(plaintext)
    ciphertext = ""

    for i in range(0, len(prepared), 2):
        pair = transform_pair(
            matrix,
            prepared[i],
            prepared[i + 1]
        )
        ciphertext += pair

    return ciphertext


def decrypt(ciphertext, keyword):
    matrix = build_matrix(keyword)

    text = "".join(
        char.lower()
        for char in ciphertext
        if char.isalpha() and char.lower() in "abcdefghijklmnopqrstuvwxyz"
    ).replace("j", "i")

    if len(text) % 2 != 0:
        raise ValueError(
            "Ciphertext must contain an even number of letters."
        )

    plaintext = ""

    for i in range(0, len(text), 2):
        pair = transform_pair(
            matrix,
            text[i],
            text[i + 1],
            decrypt=True
        )
        plaintext += pair

    return plaintext


if __name__ == "__main__":
    keyword = input("Enter the keyword: ")
    plaintext = input("Enter the plaintext: ")

    ciphertext = encrypt(plaintext, keyword)

    print("Ciphertext:", ciphertext)

    decrypted = decrypt(ciphertext, keyword)

    print("Decrypted prepared text:", decrypted)
```

---

## 9. Understanding the Code

### 9.1 Building the Matrix

The function `build_matrix()` creates the 5×5 table.

```python
if char not in matrix_letters:
    matrix_letters += char
```

This prevents repeated keyword letters from occupying multiple cells.

After processing the keyword, the function adds the remaining alphabet letters.

### 9.2 Finding a Letter's Position

The function `find_position()` searches the matrix and returns the row and column.

For example, using the `LEMON` matrix:

```text
L → (0, 0)
B → (1, 1)
X → (4, 2)
```

The coordinates use zero-based indexing, meaning the first row and column are numbered `0`.

### 9.3 Preparing the Plaintext

The function `prepare_text()` creates valid letter pairs.

For example:

```text
BALLOON → BALXLOON
```

It checks whether the next character repeats the current character.

If the letters repeat, it inserts X and processes the second repeated letter again during the next iteration.

### 9.4 Transforming a Pair

The function `transform_pair()` applies the three Playfair rules.

For encryption:

- Same row: increase each column by one.
- Same column: increase each row by one.
- Rectangle: swap the columns.

For decryption, row and column movements are reversed.

The modulo operation `% 5` handles wraparound.

For example:

```python
(col1 + 1) % 5
```

If the current column is `4`, the result becomes `0`, returning to the first column.

### 9.5 Encrypting the Entire Message

The loop:

```python
for i in range(0, len(prepared), 2):
```

moves through the prepared plaintext two characters at a time.

Each pair is passed to `transform_pair()`, and the result is appended to the ciphertext.

### 9.6 Decrypting the Message

The `decrypt()` function processes ciphertext pairs using the reverse transformation rules.

The returned plaintext is the **prepared plaintext**, so it may contain filler X characters and may use I where the original message used J.

---

## 10. How to Run the Program

Save the code as:

```text
playfair.py
```

Open a terminal in the folder containing the file and run:

```bash
python playfair.py
```

Example input:

```text
Enter the keyword: LEMON
Enter the plaintext: BALLOON
```

Expected output:

```text
Ciphertext: cbmvennl
Decrypted prepared text: balxloon
```

The ciphertext is displayed in lowercase because the implementation normalizes the input to lowercase.

The decrypted prepared text contains X because X was inserted to separate repeated letters.

### Test Another Example

Input:

```text
Enter the keyword: LEMON
Enter the plaintext: HELP
```

Expected output:

```text
Ciphertext: rbng
Decrypted prepared text: help
```

---

## 11. Common Mistakes

### Mistake 1: Repeating Keyword Letters

Incorrect: writing every occurrence of a keyword letter into the matrix.

Correct: keep only the first occurrence.

### Mistake 2: Forgetting I/J Combination

The standard matrix has 25 positions, so I and J share one position.

### Mistake 3: Incorrectly Preparing Repeated Letters

`BALLOON` must be prepared as:

```text
BA | LX | LO | ON
```

Not:

```text
BA | LL | OO | NX
```

### Mistake 4: Using the Wrong Direction

| Operation | Same Row | Same Column |
|---|---|---|
| Encryption | Right | Down |
| Decryption | Left | Up |

The rectangle rule swaps columns in both operations.

### Mistake 5: Forgetting Wraparound

The matrix is circular for row and column movements. Moving right from the last column returns to the first column; moving down from the last row returns to the first row.

### Mistake 6: Removing Every X After Decryption

Some X characters are inserted as fillers, but others might be genuine plaintext characters. Do not automatically remove every X without considering the original message.

---

## 12. Summary

Playfair encryption becomes much easier when each stage is handled separately.

1. Build the matrix using the keyword.
2. Remove repeated keyword letters.
3. Combine I and J.
4. Prepare the plaintext into pairs.
5. Insert fillers when necessary.
6. Identify the positions of each pair.
7. Apply the correct encryption rule.
8. Combine the results.
9. Decrypt using the reverse row and column movements.

### Final Rule Table

| Situation | Encryption | Decryption |
|---|---|---|
| Same row | Move right | Move left |
| Same column | Move down | Move up |
| Rectangle | Swap columns | Swap columns |

Playfair is a historical classical cipher intended for educational study. It is not suitable for protecting modern sensitive information.

---

**Document note:** The `LEMON` matrix and `BALLOON` example are based on the lecture material. The additional examples and Python implementation are supplementary educational material.
