# Rail Fence Cipher

## Overview

The Rail Fence Cipher is a classical **transposition cipher**. It rearranges
the positions of the plaintext characters rather than substituting one letter
for another. The characters themselves, including their case and punctuation,
are preserved.

## Algorithm Concept

A **rail** is one row in the zigzag arrangement. The integer key specifies
how many rails to use. Starting at the top rail, write each character while
moving down one rail at a time. At the bottom, reverse direction and move up
until reaching the top; continue this down-and-up pattern for the whole
message.

Encryption reads the completed arrangement one rail at a time, from top to
bottom, to form the ciphertext.

## Worked Example

Use the lecture example:

```text
Key: 3
Plaintext: Information
```

The character positions follow the repeating rail pattern `0, 1, 2, 1`:

```text
Rail 1: I . . . r . . . i . .
Rail 2: . n . o . m . t . o .
Rail 3: . . f . . . a . . . n
```

Dots mark empty positions. Reading each rail from top to bottom gives:

```text
Rail 1: Iri
Rail 2: nomto
Rail 3: fan

Ciphertext: Irinomtofan
```

Independent check by character position (starting at position 0):

```text
0 I -> rail 1    1 n -> rail 2    2 f -> rail 3
3 o -> rail 2    4 r -> rail 1    5 m -> rail 2
6 a -> rail 3    7 t -> rail 2    8 i -> rail 1
9 o -> rail 2   10 n -> rail 3
```

This yields rail contents `Iri`, `nomto`, and `fan`, and confirms the
ciphertext `Irinomtofan`.

## Lecture Code

The original [lecture script](../../Code/Rail-Fence-Cipher/rail_fence_encryption.py)
demonstrates the two-rail case with a fixed plaintext. It places characters
at even positions in `even` and odd positions in `odd`, then concatenates
those groups. This is the two-rail zigzag pattern because a two-rail path
alternates between the top and bottom rails.

The script does not accept a rail-count key or arbitrary input. No original
lecture decryption implementation was found. A separate
[supplementary general encryption/decryption implementation](../../Code/Rail-Fence-Cipher/rail_fence_encryption_supplementary.py)
and [its tests](../../Code/Rail-Fence-Cipher/tests_supplementary.py) are
retained. The broader key-based algorithm described above is the general Rail
Fence method; it should not be confused with features in the lecture script.

Run the hard-coded example from the repository root:

```bash
python Code/Rail-Fence-Cipher/rail_fence_encryption.py
```

There is no current Rail Fence test suite after removing tests that targeted a
separate supplementary implementation.

## Complexity

The general zigzag method assigns each of `n` characters to a rail and reads
the rails in **O(n)** algorithmic time with **O(n + k)** storage for `k`
rails. The lecture script itself visits each character once, but its repeated
string concatenation may take **O(n²)** time in the worst case.

## Limitations

Rail Fence is a classical educational cipher and is not suitable for modern
secure communication. Its simple rearrangement does not provide the
cryptographic security expected of modern encryption.
