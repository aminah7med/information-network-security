# Vigenere Cipher Solutions

No solution set has been added yet.

Related: [algorithm](../../Algorithms/Vigenere/notes.md), [code](../../Code/Vigenere-Cipher/README.md), and [problems](../../Problems/Vigenere/README.md).
# Vigenère Cipher — Solutions

> **Supplementary solutions** to the practice problems in [Problems/Vigenere](../../Problems/Vigenere/README.md). They are not instructor-provided solutions.
> Convention: `a = 0` ... `z = 25`. Results were checked by running the code in [Code/Vigenere-Cipher](../../Code/Vigenere-Cipher/README.md).

## Beginner

**B1.** `r = 17`, `z = 25`, `m = 12`.

**B2.** `8 = i`, `19 = t`, `0 = a`.

**B3.**

1. `(23 + 8) mod 26 = 31 mod 26 = 5`
2. `(19 + 24) mod 26 = 43 mod 26 = 17`
3. `(3 - 5) mod 26 = -2 mod 26 = 24` (`-2 + 26 = 24`)

## Intermediate: Encryption

**E1.** `bad` with `abc`. Repeated key: `abc`.

| Plain | p | Key | k | (p + k) mod 26 | Cipher |
|-------|---|-----|---|----------------|--------|
| b | 1 | a | 0 | 1 | b |
| a | 0 | b | 1 | 1 | b |
| d | 3 | c | 2 | 5 | f |

Ciphertext: **`bbf`**

**E2.** `secure` with `ab`. Repeated key: `ababab`.

| Plain | p | Key | k | (p + k) mod 26 | Cipher |
|-------|---|-----|---|----------------|--------|
| s | 18 | a | 0 | 18 | s |
| e | 4 | b | 1 | 5 | f |
| c | 2 | a | 0 | 2 | c |
| u | 20 | b | 1 | 21 | v |
| r | 17 | a | 0 | 17 | r |
| e | 4 | b | 1 | 5 | f |

Ciphertext: **`sfcvrf`**

**E3.** `data` with `zy`. Repeated key: `zyzy`.

| Plain | p | Key | k | (p + k) mod 26 | Cipher |
|-------|---|-----|---|----------------|--------|
| d | 3 | z | 25 | 28 mod 26 = 2 | c |
| a | 0 | y | 24 | 24 | y |
| t | 19 | z | 25 | 44 mod 26 = 18 | s |
| a | 0 | y | 24 | 24 | y |

Ciphertext: **`cysy`**

**E4.** `attack` with `key`. Repeated key: `keykey`.

| Plain | p | Key | k | (p + k) mod 26 | Cipher |
|-------|---|-----|---|----------------|--------|
| a | 0 | k | 10 | 10 | k |
| t | 19 | e | 4 | 23 | x |
| t | 19 | y | 24 | 43 mod 26 = 17 | r |
| a | 0 | k | 10 | 10 | k |
| c | 2 | e | 4 | 6 | g |
| k | 10 | y | 24 | 34 mod 26 = 8 | i |

Ciphertext: **`kxrkgi`**

## Intermediate: Tracing the Loop

**T1.** `plain = "network"`, `key = "net"` (`len(key) = 3`).

| `i` | `i % 3` | `new_plain` after | `p` | `k` | `c` | Ciphertext so far |
|-----|---------|-------------------|-----|-----|-----|-------------------|
| 0 | 0 | `n` | 13 | 13 | (26 % 26) + 97 = 97 (`a`) | `a` |
| 1 | 1 | `ne` | 4 | 4 | (8 % 26) + 97 = 105 (`i`) | `ai` |
| 2 | 2 | `net` | 19 | 19 | (38 % 26) + 97 = 109 (`m`) | `aim` |
| 3 | 0 | `netn` | 22 | 13 | (35 % 26) + 97 = 106 (`j`) | `aimj` |
| 4 | 1 | `netne` | 14 | 4 | (18 % 26) + 97 = 115 (`s`) | `aimjs` |
| 5 | 2 | `netnet` | 17 | 19 | (36 % 26) + 97 = 107 (`k`) | `aimjsk` |
| 6 | 0 | `netnetn` | 10 | 13 | (23 % 26) + 97 = 120 (`x`) | `aimjskx` |

Printed output: `Ciphertext: aimjskx`

**T2.** For `len(key) = 4`:

| `i` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|-----|---|---|---|---|---|---|---|---|---|---|
| `i % 4` | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3 | 0 | 1 |

## Intermediate: Decryption

**D1.** `rijvs` with `key`. Repeated key: `keyke`.

| Cipher | C | Key | K | (C - K) mod 26 | Plain |
|--------|---|-----|---|----------------|-------|
| r | 17 | k | 10 | 7 | h |
| i | 8 | e | 4 | 4 | e |
| j | 9 | y | 24 | -15 mod 26 = 11 | l |
| v | 21 | k | 10 | 11 | l |
| s | 18 | e | 4 | 14 | o |

Plaintext: **`hello`**

## Advanced for This Course Level

**A1.** `key[i]` only works while `i < len(key)`. When the plaintext is longer than the key, Python raises an `IndexError`. `i % len(key)` always gives a number between `0` and `len(key) - 1`, so the key repeats cyclically.

**A2.** The first `l` (position 2) meets the key letter `y` (value 24), giving `(11 + 24) mod 26 = 9 = j`. The second `l` (position 3) meets `k` (value 10), giving `(11 + 10) mod 26 = 21 = v`. The same plaintext letter is shifted by different amounts, so the ciphertext letters differ.

**A3.** The code prints `lijvs`, which is not correct (the correct encryption of `hello` is `rijvs`, and `Hello` is not valid lowercase input). `ord('H')` is `72`, so `p = 72 - 97 = -25`. With `k = 10`, `(-25 + 10) % 26 = (-15) % 26 = 11` in Python, and `11 + 97 = 108 = 'l'`. The code assumes lowercase letters and does not check its input.

**A4.** `i % len(key)` becomes `i % 0`, which raises `ZeroDivisionError` on the line `new_plain += key[i % len(key)]` (when the plaintext is not empty).

**A5.** The key letter `a` has value `0`, so every shift is `0` and `(p + 0) % 26 = p`. The ciphertext equals the plaintext. For example, `hello` with key `a` gives `hello`.