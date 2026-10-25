# Hill Cipher Code

[`hill_encryption.py`](hill_encryption.py) contains the original lecture
script. It reads a lowercase plaintext, the matrix dimension, and each key
matrix entry interactively, then encrypts blocks using NumPy matrix
multiplication modulo 26.

NumPy is required to run this script:

```bash
python -m pip install numpy
python Code/Hill-Cipher/hill_encryption.py
```

The lecture file contains encryption only. No original lecture decryption
script or compatible test suite was found. The previous supplementary
decryption and function-based tests have been removed.

See the [Hill Cipher guide](../../Algorithms/Hill/README.md) for the
mathematical overview and limitations.
