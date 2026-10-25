# Vigenère Cipher Code

[`vigenere_encryption.py`](vigenere_encryption.py) is the original lecture
encryption script. It reads the plaintext and key, converts both to uppercase,
repeats the key to match the message length, and prints the ciphertext.

The lecture script expects alphabetic input and a non-empty key; it does not
validate unsupported characters. No corresponding original lecture
decryption code or test file was found. Earlier supplementary encryption,
decryption, and test scripts have been removed rather than presented as
lecture implementations.

Run the script from the repository root:

```bash
python Code/Vigenere-Cipher/vigenere_encryption.py
```

Related: [algorithm notes](../../Algorithms/Vigenere/notes.md),
[study guide](../../Algorithms/Vigenere/study-guide.md),
[problems](../../Problems/Vigenere/README.md), and
[solutions](../../Solutions/Vigenere/README.md).
