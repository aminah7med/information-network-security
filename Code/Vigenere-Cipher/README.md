# Vigenere Cipher Code

No implementation has been added yet. Add code only after the course requirements and algorithm behavior are verified.

Related: [algorithm](../../Algorithms/Vigenere/notes.md), [problems](../../Problems/Vigenere/README.md), and [solutions](../../Solutions/Vigenere/README.md).
# Vigenère Cipher — Code

This page explains how to read, run, test, and practice the Vigenère code. The theory is in the [algorithm overview](../../Algorithms/Vigenere/README.md).

## A. Directory Guide

| File | Purpose | Source |
|------|---------|--------|
| `vigenere_section.py` | Reference implementation from the section (encryption) | Instructor |
| `vigenere_encryption.py` | Encryption as a function, with input validation | Supplementary |
| `vigenere_decryption.py` | Decryption as a function, with input validation | Supplementary |
| `tests.py` | Basic verification tests | Supplementary |

## B. Instructor's Section Code

File: [`vigenere_section.py`](vigenere_section.py)

```python
plain = input("Enter the plain text: ")
key = input("Enter the key: ")

new_plain = ""      # stores the repeated key (name kept from the lecture code)
ciphertext = ""

for i in range(len(plain)):
    new_plain += key[i % len(key)]

    p = ord(plain[i]) - 97
    k = ord(new_plain[i]) - 97

    c = ((p + k) % 26) + 97
    ciphertext += chr(c)

print("Ciphertext:", ciphertext)
```

The algorithm and the variable names are unchanged from the lecture code. The only additions are two comments. The code already initializes `ciphertext = ""` before the loop. Line-by-line explanations are in the [study guide](../../Algorithms/Vigenere/study-guide.md).

## C. How to Think Through the Problem

| Step | What to do | Why |
|------|-----------|-----|
| 1. Identify the inputs | The plaintext and the keyword | The algorithm needs a message and a key to produce one ciphertext |
| 2. Understand why the keyword repeats | The key is usually shorter than the message | Every plaintext letter needs its own key letter |
| 3. Connect each plaintext character to a key character | Plaintext position `i` uses key position `i % len(key)` | `%` makes the index return to 0 after the last key letter, so the key never runs out |
| 4. Convert both characters to numbers | `ord(character) - 97` | Arithmetic works on numbers, not letters. Subtracting 97 maps `a`–`z` to `0`–`25` |
| 5. Apply the formula | `c = ((p + k) % 26) + 97` | `(p + k) % 26` is the cipher formula. The `+ 97` prepares the number for `chr()` |
| 6. Convert the result to a character | `chr(c)` | The output must be readable letters |
| 7. Build the ciphertext | `ciphertext += chr(c)` | Each loop iteration adds one letter, in the same order as the plaintext |

## D. Dry Run

Additional example (not from the lecture). Plaintext `hello`, key `key`.

Repeated key (`new_plain` after the loop): `keyke`

| `i` | Plain | Key char (`key[i % 3]`) | `p` | `k` | `(p + k) % 26` | `c` (+ 97) | Cipher |
|---|-------|--------------------------|-----|-----|----------------|------------|--------|
| 0 | h | k | 7 | 10 | 17 % 26 = 17 | 114 | r |
| 1 | e | e | 4 | 4 | 8 % 26 = 8 | 105 | i |
| 2 | l | y | 11 | 24 | 35 % 26 = 9 | 106 | j |
| 3 | l | k | 11 | 10 | 21 % 26 = 21 | 118 | v |
| 4 | o | e | 14 | 4 | 18 % 26 = 18 | 115 | s |

Final output:

```text
Ciphertext: rijvs
```

## E. How to Run

Run all commands from the repository root.

Instructor's code (type the inputs when prompted):

```bash
python Code/Vigenere-Cipher/vigenere_section.py
```

Without typing (Linux, macOS, Git Bash):

```bash
printf 'hello\nkey\n' | python Code/Vigenere-Cipher/vigenere_section.py
```

Expected output (the prompts are printed without line breaks):

```text
Enter the plain text: Enter the key: Ciphertext: rijvs
```

Supplementary scripts:

```bash
python Code/Vigenere-Cipher/vigenere_encryption.py
python Code/Vigenere-Cipher/vigenere_decryption.py
```

Tests:

```bash
python Code/Vigenere-Cipher/tests.py
```

On some systems the command is `python3` instead of `python`.

## F. Separate Implementations

| File | Notes |
|------|-------|
| `vigenere_section.py` | Instructor-style script. Reads input, prints the result. No validation |
| `vigenere_encryption.py` | Supplementary. `encrypt(plain, key)` uses the same convention (`a = 0`, lowercase). Raises `ValueError` for an empty key or characters outside `a`–`z` |
| `vigenere_decryption.py` | Supplementary. `decrypt(cipher, key)` uses `P = (C - K) % 26` with the same convention and the same validation |
| `tests.py` | Uses Python's built-in `unittest`. Also runs the instructor's script and compares its output with `encrypt()` |

The supplementary files are practice implementations. They are not the instructor's original code.

## G. Testing and Expected Results

| Plaintext | Key | Ciphertext |
|-----------|-----|------------|
| `cat` | `dog` | `foz` |
| `bad` | `abc` | `bbf` |
| `hello` | `key` | `rijvs` |
| `attackatdawn` | `lemon` | `lxfopvefrnhr` |

What `tests.py` checks:

- The four encryption cases above, and the matching decryption cases.
- Key repetition: `hello` with `key` equals `hello` with `keyke`.
- Round trip: decrypting an encrypted message with the same key gives the original plaintext.
- Wrap-around in decryption: `a` with key `d` gives `x`.
- Input validation of the supplementary functions (empty key, uppercase, space, digit in key).
- The instructor's script gives the same ciphertext as `encrypt()`.

Result of the last run (9 tests): `OK`.

## H. Limitations

The instructor's code assumes:

- Lowercase ASCII letters `a`–`z` only. Uppercase letters, spaces, and punctuation do not raise an error, but they produce wrong output.
- A non-empty key. An empty key causes `ZeroDivisionError`.
- Encryption only. Decryption is provided in the supplementary file.

Examples are in the [study guide](../../Algorithms/Vigenere/study-guide.md#limitations-of-the-demonstrated-implementation). The supplementary functions reject unsupported input instead of handling it; they do not support spaces or uppercase letters.

## I. Further Reading

- [Algorithm overview](../../Algorithms/Vigenere/README.md)
- [Lecture notes](../../Algorithms/Vigenere/notes.md)
- [Study guide](../../Algorithms/Vigenere/study-guide.md)
- [Practice problems](../../Problems/Vigenere/README.md)
- [Solutions](../../Solutions/Vigenere/README.md)