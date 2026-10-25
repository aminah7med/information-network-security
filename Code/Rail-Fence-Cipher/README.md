# Rail Fence Cipher Code

[`rail_fence_encryption.py`](rail_fence_encryption.py) is the original lecture
demonstration. It uses the hard-coded plaintext `meetmeafterthetogaparty`,
separates characters at even and odd positions, and concatenates those two
groups to demonstrate a two-rail transposition.

The script does not prompt for a key or plaintext, and no original lecture
decryption implementation was found. The earlier generic multi-rail
encryption/decryption functions and their tests have been removed.

Run the example from the repository root:

```bash
python Code/Rail-Fence-Cipher/rail_fence_encryption.py
```

See the [Rail Fence guide](../../Algorithms/Rail-Fence/README.md) for the
general algorithm and the distinction from this fixed two-rail example.
