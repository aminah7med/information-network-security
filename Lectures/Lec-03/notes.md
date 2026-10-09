# Playfair Cipher — Complete Study Guide

> **Course:** Information and Network Security  
> **Topic:** Classical Encryption Algorithms  
> **Algorithm:** Playfair Cipher  
> **Status:** Study Notes and Practice

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [How Playfair Works](#2-how-playfair-works)
3. [Building the 5×5 Matrix](#3-building-the-5x5-matrix)
4. [Preparing the Plaintext](#4-preparing-the-plaintext)
5. [The Three Encryption Rules](#5-the-three-encryption-rules)
6. [Example 1: Encrypt BALLOON](#6-example-1-encrypt-balloon)
7. [Example 2: Encrypt HELP](#7-example-2-encrypt-help)
8. [Example 3: Encrypt MEET](#8-example-3-encrypt-meet)
9. [Decryption Rules](#9-decryption-rules)
10. [Decryption Example](#10-decryption-example)
11. [How to Solve Playfair Problems](#11-how-to-solve-playfair-problems)
12. [Common Mistakes](#12-common-mistakes)
13. [Practice Questions](#13-practice-questions)
14. [Solutions](#14-solutions)
15. [Quick Revision](#15-quick-revision)

---

## 1. Introduction

The **Playfair Cipher** is a classical encryption algorithm that encrypts letters in pairs instead of encrypting each letter individually.

For example, instead of processing each character separately, the algorithm divides the plaintext into pairs:

```text
Plaintext: BALLOON

Pairs: BA | LX | LO | ON
```

Each pair is encrypted using a 5×5 matrix containing the English alphabet.

The encryption result depends on the positions of the two letters in the matrix.

### Main Concepts

- **Plaintext:** The original message before encryption.
- **Keyword:** The word used to construct the matrix.
- **Matrix:** A 5×5 table containing the letters.
- **Ciphertext:** The encrypted message.
- **Digraph:** A pair of letters processed together.

### Why Is It Different from Caesar and Vigenère?

Playfair processes two letters together and uses their positions in a matrix.

It does not simply shift every character by a fixed number.

---

## 2. How Playfair Works

The algorithm follows these steps:

1. Choose a keyword.
2. Build a 5×5 matrix using the keyword.
3. Fill the remaining cells with unused alphabet letters.
4. Prepare the plaintext by dividing it into pairs.
5. Handle repeated letters within a pair.
6. Encrypt each pair using one of three rules.
7. Join the encrypted pairs to obtain the ciphertext.

The process can be summarized as:

```text
Keyword
   |
   v
Build 5x5 Matrix
   |
   v
Prepare Plaintext
   |
   v
Split into Letter Pairs
   |
   v
Apply Encryption Rules
   |
   v
Ciphertext
```

---

## 3. Building the 5×5 Matrix

A standard English alphabet contains 26 letters, but a 5×5 matrix has only 25 cells.

Therefore, the standard Playfair convention combines **I and J into one cell**.

For this guide, both I and J use the same matrix position.

### Step 1: Choose the Keyword

We will use the keyword:

```text
LEMON
```

### Step 2: Write the Keyword Without Repeated Letters

The keyword is:

```text
L E M O N
```

All five letters are unique, so we can write them directly into the first row.

If a keyword contains repeated letters, keep only the first occurrence of each letter.

For example:

```text
Keyword: BALLOON

Unique letters: BALON
```

### Step 3: Add the Remaining Alphabet Letters

Continue with the English alphabet in order.

Skip:

- Letters already present in the keyword.
- The letter J, because I and J share one cell.

The remaining letters are:

```text
A B C D F G H I K P Q R S T U V W X Y Z
```

### Step 4: Complete the Matrix

The final matrix is:

| Row | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |
|---|---|---|---|---|---|
| 1 | L | E | M | O | N |
| 2 | A | B | C | D | F |
| 3 | G | H | I/J | K | P |
| 4 | Q | R | S | T | U |
| 5 | V | W | X | Y | Z |

This matrix will be used in all encryption examples in this guide.

### Important Notes

- The matrix always has 5 rows and 5 columns.
- Each letter appears only once.
- The keyword is written first.
- The remaining letters are added alphabetically.
- I and J share a cell.
- The matrix must remain the same throughout a single encryption or decryption operation.

---

## 4. Preparing the Plaintext

Before encryption, the plaintext must be divided into pairs.

There are two important rules.

### Rule 1: Repeated Letters in the Same Pair

If both letters in a pair are identical, insert X after the first letter and start a new pair.

Example:

```text
Plaintext: BALLOON
```

Start dividing the text:

```text
BA | LL | OO | N
```

The pair `LL` contains two identical letters.

Insert X after the first L:

```text
BA | LX
```

Continue from the second L.

The remaining text becomes:

```text
LO | ON
```

The complete prepared plaintext is:

```text
BA | LX | LO | ON
```

Therefore:

```text
Original: BALLOON
Prepared: BALXLOON
```

Notice that the inserted X separates the repeated L letters.

### Rule 2: An Odd Number of Letters

If one letter remains at the end without a partner, add X to complete the final pair.

Example:

```text
Plaintext: CAT
```

Divide the text:

```text
CA | T
```

The last letter has no partner, so add X:

```text
CA | TX
```

Prepared plaintext:

```text
CATX
```

### Example: Another Repeated-Letter Case

Consider:

```text
Plaintext: HELLO
```

Start with the first pair:

```text
HE
```

The next two letters are `LL`, so insert X after the first L:

```text
LX
```

Continue from the second L:

```text
LO
```

The prepared pairs are:

```text
HE | LX | LO
```

Prepared plaintext:

```text
HELXLO
```

**Important:** After inserting X between repeated letters, continue processing from the second repeated letter. Do not skip it.

---

## 5. The Three Encryption Rules

For every pair, locate both letters in the matrix.

There are three possible cases:

1. Both letters are in the same row.
2. Both letters are in the same column.
3. The letters form the corners of a rectangle.

Only one of these rules applies to a given pair.

### Rule 1: Same Row

If both letters are in the same row, replace each letter with the letter immediately to its right.

If a letter is in the last column, wrap around to the first column of the same row.

Example:

```text
Matrix row:

L E M O N
```

Encrypt the pair:

```text
LO
```

Both letters are in the first row.

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

Why?

- O moves right to N.
- N is already in the last column, so it wraps around to L.

### Rule 2: Same Column

If both letters are in the same column, replace each letter with the letter immediately below it.

If a letter is in the last row, wrap around to the first row of the same column.

Example:

```text
Column 2:

E
B
H
R
W
```

Encrypt the pair:

```text
ER
```

Both letters are in column 2.

- E moves down to B.
- R moves down to W.

Result:

```text
ER → BW
```

Another example:

```text
EW → EB
```

Why?

- E moves down to B.
- W is in the last row, so it wraps around to E.

### Rule 3: Rectangle

If the letters are in different rows and different columns, they form two opposite corners of a rectangle.

Replace each letter with the letter in the same row but in the other letter's column.

Example:

```text
Pair: BA
```

Locate both letters:

- B is in row 2, column 2.
- A is in row 2, column 1.

They are actually in the same row, so Rule 1 applies.

Now consider:

```text
Pair: LX
```

Positions:

- L is in row 1, column 1.
- X is in row 5, column 3.

They are in different rows and different columns, so Rule 3 applies.

The rectangle looks like this:

```text
L  E  M  O  N
         |
         |
V  W  X  Y  Z
```

Swap the columns while keeping each letter in its original row:

- L becomes M.
- X becomes V.

Result:

```text
LX → MV
```

**Remember:** In the rectangle rule, each letter stays in its own row but takes the column of the other letter.

---

## 6. Example 1: Encrypt BALLOON

This is the main example from the lecture notes.

### Given

```text
Keyword: LEMON
Plaintext: BALLOON
```

### Step 1: Build the Matrix

| L | E | M | O | N |
|---|---|---|---|---|
| A | B | C | D | F |
| G | H | I/J | K | P |
| Q | R | S | T | U |
| V | W | X | Y | Z |

### Step 2: Prepare the Plaintext

The original text is:

```text
BALLOON
```

Split it into pairs:

```text
BA | LL | OO | N
```

The repeated L letters require inserting X.

After preparation:

```text
BA | LX | LO | ON
```

The prepared plaintext is:

```text
BALXLOON
```

### Step 3: Encrypt the Pair BA

Positions:

- B: row 2, column 2.
- A: row 2, column 1.

They share the same row.

Apply Rule 1:

- B becomes C.
- A becomes B.

Result:

```text
BA → CB
```

### Step 4: Encrypt the Pair LX

Positions:

- L: row 1, column 1.
- X: row 5, column 3.

They form a rectangle.

Apply Rule 3:

- L becomes M.
- X becomes V.

Result:

```text
LX → MV
```

### Step 5: Encrypt the Pair LO

Positions:

- L: row 1, column 1.
- O: row 1, column 4.

They share the same row.

Apply Rule 1:

- L becomes E.
- O becomes N.

Result:

```text
LO → EN
```

### Step 6: Encrypt the Pair ON

Positions:

- O: row 1, column 4.
- N: row 1, column 5.

They share the same row.

Apply Rule 1:

- O becomes N.
- N wraps around to L.

Result:

```text
ON → NL
```

### Step 7: Combine the Results

| Plaintext Pair | Rule | Ciphertext Pair |
|---|---|---|
| BA | Same row | CB |
| LX | Rectangle | MV |
| LO | Same row | EN |
| ON | Same row | NL |

Final ciphertext:

```text
CBMVENNL
```

Therefore:

```text
BALLOON → CBMVENNL
```

---

## 7. Example 2: Encrypt HELP

We will use the same keyword and matrix.

### Given

```text
Keyword: LEMON
Plaintext: HELP
```

### Step 1: Prepare the Plaintext

Divide the text into pairs:

```text
HE | LP
```

There are no repeated letters within a pair, and the text has an even length.

No additional X is required.

### Step 2: Encrypt HE

Locate the letters:

- H: row 3, column 2.
- E: row 1, column 2.

They share the same column.

Apply Rule 2:

- H moves down to R.
- E moves down to B.

Result:

```text
HE → RB
```

### Step 3: Encrypt LP

Locate the letters:

- L: row 1, column 1.
- P: row 3, column 5.

They are in different rows and columns.

Apply Rule 3:

- L becomes N.
- P becomes G.

Result:

```text
LP → NG
```

### Step 4: Combine the Results

| Plaintext Pair | Rule | Ciphertext Pair |
|---|---|---|
| HE | Same column | RB |
| LP | Rectangle | NG |

Final ciphertext:

```text
RBNG
```

Therefore:

```text
HELP → RBNG
```

---

## 8. Example 3: Encrypt MEET

This example demonstrates the same-row rule and alphabet wraparound.

### Given

```text
Keyword: LEMON
Plaintext: MEET
```

### Step 1: Prepare the Plaintext

Divide the text:

```text
ME | ET
```

Neither pair contains identical letters.

### Step 2: Encrypt ME

Both M and E are in the first row.

- M moves right to O.
- E moves right to M.

Result:

```text
ME → OM
```

### Step 3: Encrypt ET

Locate the letters:

- E: row 1, column 2.
- T: row 4, column 4.

They form a rectangle.

- E becomes O.
- T becomes R.

Result:

```text
ET → OR
```

### Step 4: Combine the Results

```text
ME → OM
ET → OR
```

Final ciphertext:

```text
OMOR
```

Therefore:

```text
MEET → OMOR
```

---

## 9. Decryption Rules

Decryption reverses the direction used by encryption.

The same matrix is used, but the replacement directions change.

### Rule 1: Same Row

During encryption, each letter moves right.

During decryption, each letter moves left.

If a letter is in the first column, wrap around to the last column.

Example:

```text
Ciphertext pair: CB
```

C and B are in the same row.

- C moves left to B.
- B moves left to A.

Result:

```text
CB → BA
```

### Rule 2: Same Column

During encryption, each letter moves down.

During decryption, each letter moves up.

If a letter is in the first row, wrap around to the last row.

Example:

```text
Ciphertext pair: RB
```

Both letters are in column 2.

- R moves up to H.
- B moves up to E.

Result:

```text
RB → HE
```

### Rule 3: Rectangle

The rectangle rule works the same way for encryption and decryption.

Each letter is replaced by the letter in the same row and the other letter's column.

Example:

```text
MV → LX
```

- M is in row 1, column 3.
- V is in row 5, column 1.

Applying the rectangle rule gives:

- M becomes L.
- V becomes X.

Result:

```text
MV → LX
```

---

## 10. Decryption Example

Let's decrypt the ciphertext from Example 1.

### Given

```text
Keyword: LEMON
Ciphertext: CBMVENNL
```

Split the ciphertext into pairs:

```text
CB | MV | EN | NL
```

Use the same matrix created with `LEMON`.

### Pair 1: CB

Same row. Move left.

```text
CB → BA
```

### Pair 2: MV

Rectangle rule.

```text
MV → LX
```

### Pair 3: EN

Same row. Move left.

```text
EN → LO
```

### Pair 4: NL

Same row. Move left.

```text
NL → ON
```

Combine the results:

```text
BALXLOON
```

The original plaintext was:

```text
BALLOON
```

The extra X was inserted during plaintext preparation to separate the repeated L letters.

Therefore, when interpreting the decrypted result, remove padding characters that were inserted during preparation when appropriate.

Recovered message:

```text
BALLOON
```

**Important:** Do not automatically remove every X from decrypted text. X may be a genuine character in the original message.

---

## 11. How to Solve Playfair Problems

When solving a Playfair question in an exam, follow this order.

### Step 1: Identify the Keyword

Example:

```text
LEMON
```

### Step 2: Build the Matrix

- Write unique keyword letters first.
- Add the unused alphabet letters.
- Combine I and J.
- Check that the matrix contains 25 cells.

### Step 3: Prepare the Plaintext

- Divide it into pairs.
- Separate identical letters in the same pair using X.
- Add X if the final pair has only one letter.

### Step 4: Find Each Pair's Positions

For each pair, identify:

- Row of the first letter.
- Column of the first letter.
- Row of the second letter.
- Column of the second letter.

### Step 5: Choose the Correct Rule

| Condition | Encryption | Decryption |
|---|---|---|
| Same row | Move right | Move left |
| Same column | Move down | Move up |
| Different rows and columns | Rectangle rule | Rectangle rule |

### Step 6: Encrypt or Decrypt Each Pair

Work on one pair at a time.

Do not try to encrypt the entire word at once.

### Step 7: Join the Results

Write the resulting pairs in the same order.

### Step 8: Check Your Work

Verify that:

- The matrix was built correctly.
- No keyword letters were repeated.
- The plaintext was prepared correctly.
- The correct rule was used for every pair.
- Wraparound was handled correctly.

---

## 12. Common Mistakes

### Mistake 1: Forgetting to Remove Duplicate Keyword Letters

Incorrect approach:

```text
Keyword: BALLOON
```

Writing every letter directly into the matrix would repeat L and O.

Correct approach:

```text
BALON
```

Keep the first occurrence of each letter.

### Mistake 2: Forgetting That I and J Share a Cell

The matrix has only 25 cells.

Under the convention used in these notes, I and J are treated as one letter position.

### Mistake 3: Encrypting Repeated Letters Together

Incorrect:

```text
LL
```

Correct preparation:

```text
LX
```

Then continue from the second L.

### Mistake 4: Using the Wrong Direction

Remember:

- Encryption: right and down.
- Decryption: left and up.
- Rectangle: swap columns.

### Mistake 5: Applying the Rectangle Rule to Letters in the Same Row

If both letters are in the same row, use the same-row rule.

If both are in the same column, use the same-column rule.

Use the rectangle rule only when both rows and columns differ.

### Mistake 6: Forgetting Wraparound

For encryption:

- Right from the last column returns to the first column.
- Down from the last row returns to the first row.

For decryption, the directions are reversed.

### Mistake 7: Removing Every X After Decryption

An X can be inserted as padding, but it can also be a real letter.

Use the preparation history and context to decide whether it should be removed.

---

## 13. Practice Questions

Use the `LEMON` matrix from this guide for all questions unless stated otherwise.

### Beginner

**Q1.** How many rows and columns does the Playfair matrix contain?

**Q2.** Why are I and J combined in the standard 5×5 matrix?

**Q3.** Build the matrix using the keyword `LEMON`.

**Q4.** Prepare the plaintext `BALLOON` for encryption.

### Intermediate

**Q5.** Encrypt the pair `LO`.

**Q6.** Encrypt the pair `LX`.

**Q7.** Encrypt the plaintext `HELP`.

**Q8.** Encrypt the plaintext `MEET`.

**Q9.** Decrypt the pair `CB`.

**Q10.** Decrypt the pair `MV`.

### Understanding the Algorithm

**Q11.** Explain the difference between the same-row rule and the same-column rule.

**Q12.** Why is X sometimes inserted into the plaintext before encryption?

**Q13.** What happens when a letter is in the last column and the same-row encryption rule is applied?

**Q14.** Explain the rectangle rule in your own words.

**Q15.** Decrypt `CBMVENNL` using the `LEMON` matrix and explain why the decrypted result may contain an extra X.

---

## 14. Solutions

### Q1

The matrix has 5 rows and 5 columns, for a total of 25 cells.

### Q2

The English alphabet contains 26 letters, but the matrix has only 25 cells. The standard convention combines I and J.

### Q3

| L | E | M | O | N |
|---|---|---|---|---|
| A | B | C | D | F |
| G | H | I/J | K | P |
| Q | R | S | T | U |
| V | W | X | Y | Z |

### Q4

Original:

```text
BALLOON
```

Prepared pairs:

```text
BA | LX | LO | ON
```

Prepared plaintext:

```text
BALXLOON
```

### Q5

`LO` uses the same-row rule:

```text
L → E
O → N
```

Answer:

```text
EN
```

### Q6

`LX` uses the rectangle rule:

```text
L → M
X → V
```

Answer:

```text
MV
```

### Q7

```text
HE → RB
LP → NG
```

Answer:

```text
RBNG
```

### Q8

```text
ME → OM
ET → OR
```

Answer:

```text
OMOR
```

### Q9

`CB` uses the same-row decryption rule:

```text
C → B
B → A
```

Answer:

```text
BA
```

### Q10

`MV` uses the rectangle rule:

```text
M → L
V → X
```

Answer:

```text
LX
```

### Q11

The same-row rule changes letters horizontally. The same-column rule changes letters vertically.

### Q12

X separates identical letters in the same pair or completes a final pair containing only one letter.

### Q13

The letter wraps around to the first column of the same row.

### Q14

Each letter is replaced by the letter in the same row but in the other letter's column.

### Q15

Split the ciphertext:

```text
CB | MV | EN | NL
```

Decrypt the pairs:

```text
CB → BA
MV → LX
EN → LO
NL → ON
```

Result:

```text
BALXLOON
```

The X was inserted to separate the repeated L letters in the original word BALLOON.

---

## 15. Quick Revision

### Matrix Construction

1. Write unique keyword letters.
2. Add the unused alphabet letters.
3. Combine I and J.
4. Fill the 5×5 matrix.

### Plaintext Preparation

1. Split the plaintext into pairs.
2. Insert X between repeated letters within a pair.
3. Add X if the final pair is incomplete.

### Encryption

- Same row: move right.
- Same column: move down.
- Rectangle: swap columns.

### Decryption

- Same row: move left.
- Same column: move up.
- Rectangle: swap columns.

### Final Reminder

Playfair is easiest when you solve each pair independently. Always build the matrix first, prepare the plaintext carefully, identify the positions of both letters, and then apply the correct rule.

---

**Document note:** This guide expands the Playfair concepts shown in the lecture notes using additional worked examples and practice questions. The worked examples use the keyword `LEMON` and the I/J combined convention consistently. Follow your instructor's exact conventions if they differ.
