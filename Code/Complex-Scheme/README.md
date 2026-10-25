# Complex Scheme

[`complex_scheme.py`](complex_scheme.py) is the original lecture script. It
uses a fixed plaintext and numerical key, groups characters into columns, and
concatenates the columns in sorted key order. Its column ordering is a
columnar-transposition operation.

The example is hard-coded in the source; it prints the column dictionary and
then the resulting ciphertext:

```bash
python Code/Complex-Scheme/complex_scheme.py
```

No separate original decryption implementation was found.
