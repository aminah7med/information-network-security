# Hill Cipher

The Hill Cipher is a classical polygraphic substitution cipher. It encrypts
groups of letters together using matrix multiplication modulo 26. This
supplementary overview explains the mathematics and links to the Python
implementation; it is not presented as instructor-provided material.

## Letter Mapping and Preparation

Convert each uppercase English letter to a number:

```text
A = 0, B = 1, ..., Z = 25
```

The implementation ignores letter case and accepts only ASCII letters
`A` through `Z`. Remove spaces and punctuation before using it. The plaintext
is divided into blocks whose length equals the key matrix dimension. If the
last block is short, append `X` (value 23) until it is full. Decryption keeps
this padding; remove the known padding from the result when appropriate.
Because a real message may also end in `X`, padding cannot always be
unambiguously removed automatically.

## Matrix Encryption

Use an invertible square matrix as the key. For an `n × n` key matrix `K` and
a plaintext block represented as a column vector `P`, calculate:

```text
C = K × P (mod 26)
```

Reduce each resulting number modulo 26 and convert it back to a letter.

### Worked example

Use the key

```text
K = | 3  3 |
    | 2  5 |
```

and plaintext `HELP`. Its blocks and numeric vectors are:

```text
HE -> | 7 |      LP -> | 11 |
      | 4 |            | 15 |
```

For `HE`:

```text
| 3  3 | | 7 |   | 3×7 + 3×4 |   | 33 |   | 7 |   -> HI
| 2  5 | | 4 | = | 2×7 + 5×4 | = | 34 | ≡ | 8 | (mod 26)
```

For `LP`:

```text
| 3  3 | | 11 |   | 3×11 + 3×15 |   | 78 |   | 0 |   -> AT
| 2  5 | | 15 | = | 2×11 + 5×15 | = | 97 | ≡ | 19| (mod 26)
```

Therefore, encrypting `HELP` gives `HIAT`.

## Decryption and Key Invertibility

Decryption uses the modular inverse of the key matrix:

```text
P = K⁻¹ × C (mod 26)
```

The inverse exists only when the determinant of `K` has a multiplicative
inverse modulo 26. Equivalently, the key is invertible exactly when:

```text
gcd(det(K), 26) = 1
```

For the example key, `det(K) = 3×5 - 3×2 = 9`, and `gcd(9, 26) = 1`.
The modular inverse of 9 is 3, since `9×3 ≡ 1 (mod 26)`. The adjugate
formula gives:

```text
K⁻¹ = 9⁻¹ × |  5  -3 | (mod 26)
             | -2   3 |
    = | 15  17 |
      | 20   9 |
```

Applying this inverse to `HI` (`|7, 8|ᵀ`) gives `HE`; applying it to `AT`
(`|0, 19|ᵀ`) gives `LP`. Thus decryption returns `HELP`.

The inverse calculation uses the determinant, its modular inverse, and the
transposed cofactor matrix (the adjugate), with all results reduced modulo 26.
The supplementary implementation rejects non-square keys and keys whose
determinant is not coprime to 26 before decrypting.

## Run the Python Code

The original lecture script uses NumPy, prompts for a lowercase message and a
square matrix dimension, then prompts for each integer matrix entry. Install
NumPy and run it from the repository root:

```bash
python -m pip install numpy
python Code/Hill-Cipher/hill_encryption.py
```

The repository also retains a separate [supplementary function-based
implementation](../../Code/Hill-Cipher/README.md), including decryption and
tests. It is not the lecture source.

## Limitations

The Hill Cipher is a classical cipher, not secure for modern use. It is
vulnerable to known-plaintext attacks, and its linear transformation leaks
patterns when enough plaintext/ciphertext is available. This implementation
is educational: it handles only English letters, uses a fixed `X` padding
convention, and does not preserve spaces or punctuation.
