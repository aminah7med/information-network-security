# Rail Fence Cipher Code

[`rail_fence_encryption.py`](rail_fence_encryption.py) is the original lecture
demonstration. It uses the hard-coded plaintext `meetmeafterthetogaparty`,
separates characters at even and odd positions, and concatenates those two
groups to demonstrate a two-rail transposition.

The script does not prompt for a key or plaintext. The earlier generic
multi-rail encrypt/decrypt functions and tests are retained separately as
`rail_fence_encryption_supplementary.py`,
`rail_fence_decryption_supplementary.py`, and `tests_supplementary.py`. They
are not the lecture implementation.

Run the example from the repository root:

```bash
python Code/Rail-Fence-Cipher/rail_fence_encryption.py
```

The supplementary generic implementation can be checked with:

```bash
python -m unittest discover -s Code/Rail-Fence-Cipher -p tests_supplementary.py
```

See the [Rail Fence guide](../../Algorithms/Rail-Fence/README.md) for the
general algorithm and the distinction from this fixed two-rail example.
