# Hill Cipher Code

[`hill_encryption.py`](hill_encryption.py) contains the original lecture
script. It reads a lowercase plaintext, the matrix dimension, and each key
matrix entry interactively, then encrypts blocks using NumPy matrix
multiplication modulo 26.

NumPy is required to run the original lecture script:

```bash
python -m pip install numpy
python Code/Hill-Cipher/hill_encryption.py
```

The lecture file contains encryption only. The earlier modular-matrix
implementation has been retained separately as
`hill_encryption_supplementary.py`, `hill_decryption_supplementary.py`, and
`tests_supplementary.py`. Those files form a separate, function-based
implementation, not a lecture variant. They can be checked with:

```bash
python -m unittest discover -s Code/Hill-Cipher -p tests_supplementary.py
```

See the [Hill Cipher guide](../../Algorithms/Hill/README.md) for the
mathematical overview and limitations.
