# Lecture 02

Lecture-derived notes have not yet been transcribed or verified against the source scan. No additional lecture topics are inferred here.

Source: [Lecture 02 scan](source/Lec-02.pdf).

Related material: [Playfair algorithm notes](../../Algorithms/Playfair/notes.md), [Playfair code](../../Code/Playfair-Cipher/README.md), [Playfair problems](../../Problems/Playfair/README.md), and [Playfair solutions](../../Solutions/Playfair/README.md).
 # Vigenère Cipher — Lecture Notes

These notes follow the instructor's whiteboard formula and section code. They contain lecture content only. Explanations that go beyond the lecture are in [study-guide.md](study-guide.md).

> **Source limitation:** these notes are based on the formula and the Python code supplied from the section. No whiteboard photo was available when this file was written, so any whiteboard detail beyond the formula and code below is not recorded here.

## Formula on the Board

```text
C = (P + K) % 26
```

| Symbol | Meaning |
|--------|---------|
| `P` | Plaintext letter value |
| `K` | Key letter value |
| `C` | Ciphertext letter value |
| `% 26` | Remainder after dividing by 26 (the alphabet has 26 letters) |

## Code Workflow

```python
plain = input("Enter the plain text: ")
key = input("Enter the key: ")

new_plain = ""
ciphertext = ""

for i in range(len(plain)):
    new_plain += key[i % len(key)]

    p = ord(plain[i]) - 97
    k = ord(new_plain[i]) - 97

    c = ((p + k) % 26) + 97
    ciphertext += chr(c)

print("Ciphertext:", ciphertext)
```

The program follows these steps:

1. Read the plaintext and the key.
2. Start with empty `new_plain` and `ciphertext` strings.
3. For each position `i` of the plaintext, take the key character at position `i % len(key)` and append it to `new_plain`. This repeats the keyword to match the plaintext length.
4. Convert the plaintext character and the repeated key character to numbers with `ord(...) - 97`.
5. Add the two numbers, apply `% 26`, and add `97` to get an ASCII code.
6. Convert the code back to a character with `chr()` and append it to `ciphertext`.
7. Print the ciphertext.

## Variables

| Variable | Role |
|----------|------|
| `plain` | The plaintext entered by the user |
| `key` | The keyword entered by the user |
| `new_plain` | Stores the **repeated key**, built one character per loop iteration (the name is kept as in the lecture code) |
| `ciphertext` | The encrypted message built so far |
| `i` | Current position in the plaintext |
| `p` | Value of the plaintext character (0–25) |
| `k` | Value of the repeated key character (0–25) |
| `c` | ASCII code of the ciphertext character |

## Functions and Operators

| Item | Meaning in this code |
|------|----------------------|
| `ord(ch)` | Returns the ASCII code of a character. `ord('a')` is `97` |
| `chr(n)` | Returns the character for the ASCII code `n`. `chr(97)` is `'a'` |
| `% 26` | Wraps a number into the range 0–25 |
| `97` | ASCII code of `'a'`. Subtracting it maps `a`–`z` to `0`–`25`; adding it maps back |
| `len(x)` | Length of a string |

## Key Index

The plaintext index and the key index are related by:

```text
key index = i % len(key)
```

If the key is `key` (length 3), the key indexes for `i = 0, 1, 2, 3, 4, 5` are `0, 1, 2, 0, 1, 2`. The key repeats cyclically.

## Assumptions of the Lecture Code

- The input uses lowercase letters `a`–`z` (the offset `97` is the code of `'a'`).
- The key is not empty (`i % len(key)` needs `len(key) > 0`).

## Examples

The supplied lecture material contains the formula and the code, but no worked numerical example. A verified example is given as supplementary material in the [code documentation](../../Code/Vigenere-Cipher/README.md#d-dry-run).

## Related Files

- [Overview](README.md)
- [Study guide](study-guide.md)
- [Instructor's code](../../Code/Vigenere-Cipher/vigenere_section.py)