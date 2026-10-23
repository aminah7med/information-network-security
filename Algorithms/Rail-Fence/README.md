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

## Encryption

The [encryption implementation](../../Code/Rail-Fence-Cipher/rail_fence_encryption.py)
performs these steps:

1. Validate that the key is a positive integer.
2. Create one character list for each rail.
3. Visit each plaintext character in order, changing direction at the top
   and bottom rails.
4. Join the rails from top to bottom to create the ciphertext.

With one rail, or when the key is greater than or equal to the plaintext
length, the characters remain in their original order and the text is returned
unchanged. Empty plaintext also produces empty ciphertext.

## Decryption

The [decryption implementation](../../Code/Rail-Fence-Cipher/rail_fence_decryption.py)
does not encrypt the ciphertext again. It rebuilds the original zigzag path:

1. Walk the path for the ciphertext length and count how many positions belong
   to each rail.
2. Use those counts to split the ciphertext into its rail segments.
3. Walk the saved zigzag path again, taking the next character from its rail.

The one-rail and key-at-least-text-length cases are unchanged by encryption,
so decryption returns them as-is. An empty ciphertext decrypts to an empty
plaintext.

## Python Implementation

Both functions accept a string and a positive integer key:
`encrypt(plaintext, key)` and `decrypt(ciphertext, key)`.

- `rails` stores each rail's characters during encryption.
- `row` tracks the current rail.
- `direction` is `1` while moving down and `-1` while moving up.
- `rail_counts` and `rail_pattern` record the path for decryption.
- `rail_positions` tracks the next unread character on each rail.

The implementation preserves all input characters and their case; it does
not normalize text or remove spaces and punctuation.

## Complexity Analysis

Let `n` be the text length and `k` the number of rails. For the general case
(`1 < k < n`), encryption visits each character once and joins the rail
contents; decryption visits each character a constant number of times while
building counts, splitting rails, and restoring the order. Both therefore
take **O(n + k)** time and **O(n + k)** auxiliary space. The implementation
returns immediately for empty text, one rail, or `k >= n`, avoiding allocation
of a large rail list in those cases.

## Running the Code

Run these commands from the repository root. Each script prompts for the text
and number of rails:

```bash
python Code/Rail-Fence-Cipher/rail_fence_encryption.py
python Code/Rail-Fence-Cipher/rail_fence_decryption.py
```

For the example, enter `Information` and `3` in the encryption script. To
decrypt, enter `Irinomtofan` and `3`.

## Testing

Run the standard-library unit tests from the repository root:

```bash
python -m unittest discover -s Code/Rail-Fence-Cipher -p tests.py
```

The tests cover the lecture example in both directions, round-trip recovery,
one rail, keys equal to or greater than the text length, short and empty text,
invalid keys, and non-string input.

## Limitations

Rail Fence is a classical educational cipher and is not suitable for modern
secure communication. Its simple rearrangement does not provide the
cryptographic security expected of modern encryption.
