# Hill Cipher Code

This educational implementation uses uppercase English letters, with
`A = 0` through `Z = 25`, and square integer key matrices modulo 26. Plaintext
is padded with `X` to a complete block when necessary. Decryption retains that
padding; remove only the padding that was added during preparation.

## Files

| File | Purpose |
|------|---------|
| `hill_encryption.py` | Encryption function and interactive encryption script |
| `hill_decryption.py` | Decryption function, modular inverse, and interactive decryption script |
| `tests.py` | Unit tests for known outputs, round trips, and invalid input |

The functions are `encrypt(plaintext, key_matrix)` and
`decrypt(ciphertext, key_matrix)`. For example:

```python
from hill_encryption import encrypt
from hill_decryption import decrypt

key = [[3, 3], [2, 5]]
ciphertext = encrypt("HELP", key)  # HIAT
plaintext = decrypt(ciphertext, key)  # HELP
```

Run commands from the repository root:

```bash
python Code/Hill-Cipher/hill_encryption.py
python Code/Hill-Cipher/hill_decryption.py
python -m unittest discover -s Code/Hill-Cipher -p tests.py
```

When prompted, enter matrix rows separated by semicolons and values within a
row separated by commas, such as `3,3;2,5`. Keys must be square and contain
integers from 0 to 25. For decryption, the determinant must be coprime to 26.

See the [Hill Cipher guide](../../Algorithms/Hill/README.md) for the
mathematical explanation, worked example, and limitations.
