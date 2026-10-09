# Vigenere Cipher Algorithm

No Vigenere algorithm material has been transcribed or verified from the lecture sources yet. This file remains a placeholder until supporting course material is reviewed.

Related: [code](../../Code/Vigenere-Cipher/README.md), [problems](../../Problems/Vigenere/README.md), and [solutions](../../Solutions/Vigenere/README.md).
# Vigenère Cipher

The Vigenère Cipher is a classical **polyalphabetic substitution cipher**. It encrypts a message with a **keyword** instead of a single number. Each plaintext letter is shifted by an amount that depends on the corresponding letter of the keyword, so the same plaintext letter can produce different ciphertext letters.

This page is a short entry point. The details are in the linked files.

## Key Terms

| Term | Meaning |
|------|---------|
| Plaintext | The original readable message |
| Keyword (key) | A word whose letters decide the shift for each position |
| Key repetition | The keyword is repeated, or indexed cyclically, until it covers the whole message |
| Ciphertext | The encrypted message |

## Letter-to-Number Convention

The reference code uses lowercase letters with `a = 0` through `z = 25` (`ord(character) - 97`).

| a | b | c | d | e | f | g | h | i | j | k | l | m |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |

| n | o | p | q | r | s | t | u | v | w | x | y | z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |

## Formulas

Encryption (written on the whiteboard as `C = (P + K) % 26`):

```text
C_i = (P_i + K_i) mod 26
```

Decryption (supplementary, the inverse operation):

```text
P_i = (C_i - K_i) mod 26
```

- `P_i`, `K_i`, `C_i`: values of the plaintext, key, and ciphertext letters at position `i`.
- `K_i` is the key letter at position `i % len(key)`.

## Modulo

`x mod 26` is the remainder after dividing `x` by 26. It keeps every result between `0` and `25` and wraps the alphabet around after `z`.

```text
(19 + 24) mod 26 = 43 mod 26 = 17
(3 - 5)  mod 26 = -2 mod 26 = 24   (decryption: negative values wrap around)
```

## Encryption Workflow

```text
plaintext + keyword
        ↓
repeat the keyword over the plaintext length
        ↓
convert each letter to a number (a = 0 ... z = 25)
        ↓
C = (P + K) mod 26
        ↓
convert each number back to a letter
        ↓
ciphertext
```

## Contents

| Resource | Purpose |
|----------|---------|
| [notes.md](notes.md) | Lecture notes: formula and the instructor's code workflow |
| [study-guide.md](study-guide.md) | Supplementary line-by-line explanation of the lecture code |
| [Code documentation](../../Code/Vigenere-Cipher/README.md) | How to read, run, and test the code |
| [Instructor's section code](../../Code/Vigenere-Cipher/vigenere_section.py) | Reference implementation |
| [Problems](../../Problems/Vigenere/README.md) | Supplementary practice problems |
| [Solutions](../../Solutions/Vigenere/README.md) | Worked solutions to the practice problems |

## Lecture Content vs. Supplementary Content

| Content | Source |
|---------|--------|
| Encryption formula `C = (P + K) % 26` | Lecture |
| Reference Python code and its workflow | Lecture |
| Decryption formula and decryption code | Supplementary |
| Study guide, dry run, tests, problems, solutions | Supplementary |

## Note on Security

The Vigenère Cipher is a historical cipher used for learning. It is not secure for protecting real data.