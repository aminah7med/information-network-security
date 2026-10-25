# Columnar Transposition Code

No separately named lecture implementation was found. The original
[Complex Scheme script](../Complex-Scheme/complex_scheme.py) uses a fixed
numerical key to group plaintext characters by column and read columns in
sorted key order. Its source is kept in the folder named for the lecture
program; it is not duplicated here.

The earlier general-purpose function implementation is retained with explicit
supplementary names:
`columnar_encryption_supplementary.py`,
`columnar_decryption_supplementary.py`, and
`tests_supplementary.py`. These are not lecture sources. Run their tests with:

```bash
python -m unittest discover -s Code/Columnar-Transposition -p tests_supplementary.py
```

See the [algorithm guide](../../Algorithms/Columnar-Transposition/README.md)
for the general method and worked examples.
