# Columnar Transposition Cipher

## Overview

The Columnar Transposition Cipher rearranges the positions of message
characters without substituting the characters themselves. The plaintext is
written in rows beneath a numerical key, then read out one column at a time
according to the key.

## Key Concept

Each key value labels the column in its original position. For example, the
key `4 2 3 1 5` labels five columns from left to right. Read the column labeled
`1` first, then `2`, and so on. The key values are ordering labels, not letter
shifts, and must be distinct positive integers.

Write the plaintext from left to right across each row. If the last row is
incomplete, leave its right-hand cells empty; do not add padding. Read each
column from top to bottom in ascending key-value order to form the ciphertext.

The implementation removes whitespace from the input text and preserves the
case and other characters. Decryption therefore returns the normalized
plaintext without its original whitespace.

## Worked Examples

The examples below use row-wise writing and ascending-key column reading, with
no padding added to incomplete rows.

### Example 1

```text
Key: 4 2 3 1 5
Plaintext: Information
Normalized plaintext: Information
```

Write the characters into five columns from left to right. Leave the
incomplete last row unpadded:

```text
Key:    4  2  3  1  5
        ------------
        I  n  f  o  r
        m  a  t  i  o
        n
```

The column values in ascending order point to original columns `4, 2, 3, 1,
5`. Their contents are `oi`, `na`, `ft`, `Imn`, and `ro`:

```text
Ciphertext: oinaftImnro
```

### Example 2

```text
Key: 6 5 4 2 1 3
Plaintext: Meet me after section
Normalized plaintext: Meetmeaftersection
```

The normalized text fills six columns in three complete rows:

```text
Key:    6  5  4  2  1  3
        ----------------
        M  e  e  t  m  e
        a  f  t  e  r  s
        e  c  t  i  o  n
```

Read original columns `5, 4, 6, 3, 2, 1`, corresponding to key values
`1, 2, 3, 4, 5, 6`. The column contents are `mro`, `tei`, `esn`, `ett`,
`efc`, and `Mae`:

```text
Ciphertext: mroteiesnettefcMae
```

Both results are verified against the implementation and covered by tests.

## Encryption

The supplementary [encryption implementation](../../Code/Columnar-Transposition/columnar_encryption_supplementary.py)
follows these steps:

1. Validate that the key is a non-empty sequence of distinct positive
   integers.
2. Remove whitespace from the plaintext.
3. Fill a list of rows from left to right, leaving the last row incomplete
   when needed.
4. Sort the original column positions by their key values.
5. Read existing characters top to bottom from each column in that order.

## Decryption

The supplementary [decryption implementation](../../Code/Columnar-Transposition/columnar_decryption_supplementary.py)
reconstructs the grid without padding:

1. Determine the number of complete rows and the number of cells in the
   incomplete final row using the ciphertext length and key length.
2. Assign each column its length. Every column has the number of complete
   rows; the leftmost columns receive one extra character when the final row
   is incomplete.
3. Split the ciphertext into column segments in ascending key order and put
   each segment back at its original column position.
4. Read the grid row by row to restore the normalized plaintext.

## Python Implementation

The functions are `encrypt(plaintext, key)` and `decrypt(ciphertext, key)`.
The key is a list or tuple of distinct positive integers.

- `grid` stores plaintext rows as character lists.
- `column_order` stores original column positions sorted by their key values.
- During decryption, `full_rows` and `extra_characters` determine the column
  lengths when a row is incomplete.
- `grid_columns` stores each recovered column at its original position before
  the plaintext is read across the rows.

The interactive scripts prompt for text and a key entered as
space-separated numbers, for example `4 2 3 1 5`.

## Complexity Analysis

Let `n` be the normalized text length and `k` the number of key columns.
Sorting the column positions takes **O(k log k)** time; writing or reading the
grid takes **O(n + k)** time. Total time is therefore **O(n + k log k)**.
The grid, column segments, and output require **O(n + k)** auxiliary space.

## Running the Code

Run from the repository root:

```bash
python Code/Columnar-Transposition/columnar_encryption_supplementary.py
python Code/Columnar-Transposition/columnar_decryption_supplementary.py
```

At the prompts, enter the plaintext or ciphertext, then the numeric key with
values separated by spaces.

## Testing

Run the standard-library unit tests from the repository root:

```bash
python -m unittest discover -s Code/Columnar-Transposition -p tests_supplementary.py
```

The supplementary tests cover both examples, complete and incomplete rows, whitespace
normalization, round trips, a one-column key, empty text, and invalid keys
and text values.

## Limitations

Columnar Transposition is a classical educational cipher, not a modern
encryption method. It only permutes character positions and is not suitable
for protecting information in modern secure communication.
