# Vigenère Cipher — Study Guide

> **Supplementary material.** This guide explains the instructor's code in more detail. It is not a transcript of the lecture. The lecture content is in [notes.md](notes.md).

## The Reference Code

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

## Line-by-Line Explanation

### `new_plain = ""` and `ciphertext = ""`

Both strings start empty and grow by one character in every loop iteration. `new_plain` holds the repeated key. `ciphertext` holds the result. They must be created before the loop, otherwise `+=` would fail on an undefined name.

### `for i in range(len(plain))`

One ciphertext letter is produced for each plaintext letter. `range(len(plain))` gives the positions `0, 1, ..., len(plain) - 1`, so the loop runs exactly once per plaintext character, and `i` is the current position.

### `new_plain += key[i % len(key)]`

The key is often shorter than the plaintext, so `key[i]` would fail with an `IndexError` as soon as `i` reaches `len(key)`. The expression `i % len(key)` always gives a number from `0` to `len(key) - 1`, and it counts up and then starts again from `0`:

| `i` | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|-----|---|---|---|---|---|---|---|
| `i % 3` (key length 3) | 0 | 1 | 2 | 0 | 1 | 2 | 0 |

This is why the key repeats cyclically. Each iteration appends one key character, so after the loop `new_plain` has the same length as `plain`.

### `p = ord(plain[i]) - 97`

`ord()` returns the ASCII code of a character. For lowercase letters the codes run from `97` (`'a'`) to `122` (`'z'`). Subtracting `97` shifts that range to `0`–`25`, which matches the alphabet numbering `a = 0, ..., z = 25`.

### `k = ord(new_plain[i]) - 97`

The same conversion, applied to the key character that belongs to position `i`.

### `c = ((p + k) % 26) + 97`

This line has two parts:

1. `(p + k) % 26` is the formula `C = (P + K) % 26`. The sum can be as large as `50`, and `% 26` wraps it back into `0`–`25`.
2. `+ 97` turns the number `0`–`25` back into an ASCII code of a lowercase letter, so that `chr()` can use it.

### `ciphertext += chr(c)`

`chr(c)` converts the ASCII code to a character, and `+=` appends it to the end of `ciphertext`.

### `print("Ciphertext:", ciphertext)`

Shows the final result after the loop has processed every character.

## Same Plaintext Letter, Different Ciphertext Letters

Plaintext `hello` with key `key` (repeated key: `keyke`):

| Position | Plain | Key | p | k | (p + k) % 26 | Cipher |
|----------|-------|-----|---|---|--------------|--------|
| 2 | l | y | 11 | 24 | 35 % 26 = 9 | j |
| 3 | l | k | 11 | 10 | 21 % 26 = 21 | v |

Both plaintext letters are `l`, but they meet different key letters (`y` and `k`), so the ciphertext letters are different (`j` and `v`). A Caesar cipher, with one fixed shift, would give the same letter both times.

## Additional Example

Plaintext `cat`, key `dog`:

| Position | Plain | p | Key | k | Calculation | Cipher |
|----------|-------|---|-----|---|-------------|--------|
| 0 | c | 2 | d | 3 | (2 + 3) % 26 = 5 | f |
| 1 | a | 0 | o | 14 | (0 + 14) % 26 = 14 | o |
| 2 | t | 19 | g | 6 | (19 + 6) % 26 = 25 | z |

`cat` → `foz`

## Decryption (Supplementary)

The lecture material supplied for this topic shows encryption only. Decryption reverses it:

```text
P = (C - K) % 26
```

Decrypting `foz` with `dog`: `(5 - 3) = 2 → c`, `(14 - 14) = 0 → a`, `(25 - 6) = 19 → t`.

In Python, `%` returns a non-negative result for a positive modulus, so `(0 - 3) % 26` gives `23`. Many other languages return a negative number; there, use `((x % 26) + 26) % 26`.

## Common Beginner Mistakes

| Mistake | Correct approach |
|---------|------------------|
| Using `a = 1` | The code uses `a = 0` (`ord(ch) - 97`) |
| Using `key[i]` | Use `key[i % len(key)]` so the key repeats |
| Forgetting `% 26` | Results above 25 would not be letters of the alphabet |
| Forgetting `+ 97` | `chr(c)` would return a control character, not a letter |
| Subtracting the key to encrypt | Encryption adds; decryption subtracts |
| Pairing a letter with the wrong key letter | Position `i` always pairs with key position `i % len(key)` |
| Counting spaces in the key position | The code treats a space like any other character (see limitations) |

## Limitations of the Demonstrated Implementation

These are limits of the code, not criticism of the lecture. The lecture code is written for the simple case shown in class.

| Input | What happens |
|-------|--------------|
| Uppercase letters | `ord('H') - 97` is `-25`. The code does not fail, but gives a wrong letter. Example: `Hello` with key `key` gives `lijvs` instead of `rijvs` |
| Spaces and punctuation | They are converted to numbers like letters, so a space becomes a letter in the output. For example, `hi there` with key `key` gives `rmldlcbi`, and the space turned into `l` |
| Empty key | `i % len(key)` raises `ZeroDivisionError` |
| Non-ASCII characters | Not supported by the `97`-offset approach |
| Decryption | Not provided; see the supplementary [decryption file](../../Code/Vigenere-Cipher/vigenere_decryption.py) |

For input validation, see the supplementary [encryption implementation](../../Code/Vigenere-Cipher/vigenere_encryption.py).

## Related Files

- [Overview](README.md)
- [Lecture notes](notes.md)
- [Code documentation](../../Code/Vigenere-Cipher/README.md)
- [Problems](../../Problems/Vigenere/README.md) and [Solutions](../../Solutions/Vigenere/README.md)
