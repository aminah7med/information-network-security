# Vigenère Cipher Code

[`vigenere_encryption.py`](vigenere_encryption.py) is the original lecture
script. It reads plaintext and key, uppercases both, repeats the key, and
prints the ciphertext. It expects alphabetic input and a non-empty key; the
lecture script does not validate input.

The folder also retains supplementary variants from the previous code
organization:

| File | Purpose |
|------|---------|
| `vigenere_section.py` | Lowercase reference script |
| `vigenere_decryption.py` | Lowercase supplementary decryption script |
| `tests_supplementary.py` | Print-based checks for the lowercase example |

These supplementary files are not the original root lecture script. Run the
lecture encryption script from the repository root:

```bash
python Code/Vigenere-Cipher/vigenere_encryption.py
```

Run the lowercase demonstration or checks with:

```bash
python Code/Vigenere-Cipher/vigenere_section.py
python Code/Vigenere-Cipher/tests_supplementary.py
```

Related: [algorithm notes](../../Algorithms/Vigenere/notes.md),
[study guide](../../Algorithms/Vigenere/study-guide.md),
[problems](../../Problems/Vigenere/README.md), and
[solutions](../../Solutions/Vigenere/README.md).
