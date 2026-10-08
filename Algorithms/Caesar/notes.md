# Caesar Cipher Algorithm

The source-based Caesar Cipher material is documented in [Lecture 01 notes](../../Lectures/Lec-01/notes.md). This file is reserved for a standalone algorithm description and examples; no lecture-derived details have been copied here yet.

Related: [Lecture 01 source](../../Lectures/Lec-01/source/Lec-01.pdf), [code](../../Code/Caesar-Cipher/README.md), [problems](../../Problems/Caesar/README.md), and [solutions](../../Solutions/Caesar/README.md).
 
 
> **Source rule used in this file**
> - 📘 **Lecture** = taken from *Information & Network Security — Lecture 01* (the primary source).
> - ➕ **Additional** = extra explanation, examples, code, or exercises added for study. These were **not** presented by the instructor.

---

## Introduction

The **Caesar Cipher** is a simple classical encryption algorithm. It encrypts a message **character by character** by shifting each letter forward by a fixed number of positions in the alphabet. That fixed number is the **Key**.

| Question | Answer |
|----------|--------|
| What is it? | 📘 A simple classical encryption algorithm that shifts every character by a fixed key. |
| Why is it a classical algorithm? | ➕ It works on letters, uses only simple arithmetic, and needs no computer. It belongs to the "Classical Encryption" family from the lecture. |
| Why is it a substitution cipher? | 📘 Substitution means characters are **replaced** by other characters. In Caesar, each letter is replaced by the letter `K` positions later. Positions in the message do not change. |
| What does the key represent? | 📘 The key is a **number**. It says how many positions to shift. |
| How are characters transformed? | 📘 Convert the letter to an index (`A = 0 … Z = 25`), apply `C = (P + K) % 26`, then convert the index back to a letter. |
| Symmetric? | 📘 One key is used for the encryption/decryption process (symmetric idea). |

---

## Table of Contents

1. [Core Idea](#1-core-idea)
2. [Terminology](#2-terminology)
3. [Alphabet Indexing](#3-alphabet-indexing)
4. [The Key](#4-the-key)
5. [Encryption](#5-encryption)
6. [Decryption](#6-decryption)
7. [Wrap-Around and Modulo](#7-wrap-around-and-modulo)
8. [Step-by-Step Algorithm](#8-step-by-step-algorithm)
9. [Worked Examples](#9-worked-examples)
10. [Implementation](#10-implementation)
11. [Edge Cases and Implementation Notes](#11-edge-cases-and-implementation-notes)
12. [Complexity](#12-complexity)
13. [Security Analysis](#13-security-analysis)
14. [Common Mistakes](#14-common-mistakes)
15. [Quick Reference](#15-quick-reference)
16. [Practice Exercises](#16-practice-exercises)
17. [Practice Answers](#17-practice-answers)
18. [Interview Questions](#18-interview-questions)

---

# 1. Core Idea

```text
Plaintext
   ↓
Shift each character by K
   ↓
Ciphertext
```

And in reverse:

```text
Ciphertext
   ↓
Shift each character back by K
   ↓
Plaintext
```

➕ **Additional — picture:** with `K = 3`, the alphabet is "slid" three places.

```text
Plain  : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Cipher : D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
```

---

# 2. Terminology

| Term | Meaning | Source |
|------|---------|--------|
| Plaintext | The original readable message | 📘 |
| Ciphertext | The encrypted message | 📘 |
| Encryption | Transforming plaintext into an unreadable form | 📘 |
| Decryption | Transforming ciphertext back into plaintext | 📘 |
| Key (`K`) | The number of positions to shift | 📘 |
| `P` | Plaintext character index | 📘 |
| `C` | Ciphertext character index | 📘 |
| Substitution | Characters are replaced | 📘 |
| Symmetric | One key for encryption and decryption | 📘 |

---

# 3. Alphabet Indexing

📘 **Lecture:** The alphabet uses indexes from `0` to `25`. There are **26 letters**.

```text
A = 0
B = 1
C = 2
...
Z = 25
```

| Letter | A | B | C | D | E | F | G | H | I | J | K | L | M |
|--------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Index  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |

| Letter | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|--------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Index  | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |

⚠️ ➕ **Additional:** Indexing starts at **0**, not 1. Most beginner mistakes come from this.

---

# 4. The Key

📘 **Lecture:** The key is a **number**. Example: `Key = 5`.

➕ **Additional — what the key means:**

| Key | Effect |
|-----|--------|
| `K = 0` | No change (ciphertext = plaintext) |
| `K = 1` | `A → B`, `B → C`, … `Z → A` |
| `K = 3` | `A → D`, `B → E`, … `Z → C` |
| `K = 26` | Full circle, same as `K = 0` |
| `K > 26` | Same as `K % 26` (for example `K = 29` behaves like `K = 3`) |

➕ **Additional — decryption key:** decrypting with `K` is the same as encrypting with `26 - K`.
Example: `TRFW` decrypted with `K = 5` gives `OMAR`. Encrypting `TRFW` with `K = 21` (`26 - 5`) also gives `OMAR`.

---

# 5. Encryption

📘 **Lecture:**

```text
C = (P + K) % 26
```

| Symbol | Meaning |
|--------|---------|
| `P` | Plaintext character index |
| `K` | Key |
| `C` | Ciphertext character index |
| `% 26` | Keeps the result inside `0–25` |

### Procedure

```text
letter → index (P) → add K → % 26 → index (C) → letter
```

### 📘 Example — single character

```text
Plaintext = O
Key = 5

O = 14
C = (14 + 5) % 26 = 19
19 = T

O → T
```

---

# 6. Decryption

📘 **Lecture:**

```text
P = (C - K) % 26
```

It moves the character **backward** by the same key.

### Procedure

```text
letter → index (C) → subtract K → % 26 → index (P) → letter
```

### 📘 Inverse operations

```text
Encryption:   P → C    C = (P + K) % 26
Decryption:   C → P    P = (C - K) % 26
```

➕ **Additional — why they cancel out:** adding `K` then subtracting `K` returns the original index.

```text
P = 14, K = 5
Encrypt: (14 + 5) % 26 = 19
Decrypt: (19 - 5) % 26 = 14   ← original P
```

---

# 7. Wrap-Around and Modulo

📘 **Lecture:** `% 26` handles the wrap-around from `Z` back to `A`.

### Why it is needed

Indexes only go from `0` to `25`. If `P + K` is `26` or more, there is no matching letter. Modulo brings the number back into range.

```text
% means "remainder after dividing by 26"

 5 % 26 = 5
26 % 26 = 0
27 % 26 = 1
28 % 26 = 2
```

### 📘 Example — XYZ with Key = 3

```text
X = 23 → (23 + 3) % 26 = 26 % 26 = 0 → A
Y = 24 → (24 + 3) % 26 = 27 % 26 = 1 → B
Z = 25 → (25 + 3) % 26 = 28 % 26 = 2 → C

XYZ → ABC
```

### ➕ Additional — wrap-around in decryption (negative numbers)

```text
Ciphertext = A, Key = 3
A = 0
0 - 3 = -3        ← negative
-3 mod 26 = 23    ← mathematically correct
23 = X

A → X
```

Some programming languages return `-3` for `-3 % 26`. A safe version of the **same formula** is:

```text
P = ((C - K) % 26 + 26) % 26
```

---

# 8. Step-by-Step Algorithm

### Encryption

1. Write the alphabet with indexes `0–25`.
2. Identify the plaintext and the key.
3. Convert each character to its index `P`.
4. Apply `C = (P + K) % 26`.
5. Convert each index `C` back to a letter.
6. Repeat for every character.
7. Write the final ciphertext.

### Decryption

1. Convert each ciphertext letter to its index `C`.
2. Identify the key.
3. Apply `P = (C - K) % 26`.
4. Convert each index `P` back to a letter.
5. Repeat for every character.
6. Recover the plaintext.

### ➕ Additional — pseudocode

```text
function encrypt(plaintext, K):
    result = ""
    for each character ch in plaintext:
        if ch is a letter:
            P = index of ch                  // A=0 ... Z=25
            C = (P + K) % 26
            result = result + letter at index C
        else:
            result = result + ch             // implementation choice
    return result

function decrypt(ciphertext, K):
    result = ""
    for each character ch in ciphertext:
        if ch is a letter:
            C = index of ch
            P = ((C - K) % 26 + 26) % 26     // safe for negative values
            result = result + letter at index P
        else:
            result = result + ch
    return result
```

### ➕ Additional — flowchart

```text
Start
  ↓
Read text and key K
  ↓
Take next character ──→ (no more characters) ──→ Output result
  ↓
Is it a letter? ── No ──→ Copy it unchanged ──┐
  ↓ Yes                                        │
Convert to index                               │
  ↓                                            │
Apply formula (+K or -K) % 26                  │
  ↓                                            │
Convert index to letter                        │
  ↓                                            │
Append to result ←─────────────────────────────┘
  ↓
(repeat)
```

---

# 9. Worked Examples

### 📘 Example 1 — OMAR, Key = 5

| Plaintext | Index | Key | Calculation | Cipher Index | Ciphertext |
|-----------|-------|-----|-------------|--------------|------------|
| O | 14 | 5 | (14 + 5) % 26 = 19 | 19 | T |
| M | 12 | 5 | (12 + 5) % 26 = 17 | 17 | R |
| A | 0 | 5 | (0 + 5) % 26 = 5 | 5 | F |
| R | 17 | 5 | (17 + 5) % 26 = 22 | 22 | W |

```text
OMAR → TRFW
```

### 📘 Example 2 — Decrypting TRFW, Key = 5

| Ciphertext | Index | Key | Calculation | Plain Index | Plaintext |
|------------|-------|-----|-------------|-------------|-----------|
| T | 19 | 5 | (19 - 5) % 26 = 14 | 14 | O |
| R | 17 | 5 | (17 - 5) % 26 = 12 | 12 | M |
| F | 5 | 5 | (5 - 5) % 26 = 0 | 0 | A |
| W | 22 | 5 | (22 - 5) % 26 = 17 | 17 | R |

```text
TRFW → OMAR
```

### 📘 Example 3 — ABC, Key = 3

```text
A = 0 → (0 + 3) % 26 = 3 → D
B = 1 → (1 + 3) % 26 = 4 → E
C = 2 → (2 + 3) % 26 = 5 → F

ABC → DEF
```

### 📘 Example 4 — XYZ, Key = 3 (wrap-around)

See [Section 7](#7-wrap-around-and-modulo): `XYZ → ABC`.

### ➕ Additional Example 5 — HELLO, Key = 3

| Plaintext | Index | Calculation | Cipher Index | Ciphertext |
|-----------|-------|-------------|--------------|------------|
| H | 7 | (7 + 3) % 26 = 10 | 10 | K |
| E | 4 | (4 + 3) % 26 = 7 | 7 | H |
| L | 11 | (11 + 3) % 26 = 14 | 14 | O |
| L | 11 | (11 + 3) % 26 = 14 | 14 | O |
| O | 14 | (14 + 3) % 26 = 17 | 17 | R |

```text
HELLO → KHOOR
```

### ➕ Additional Example 6 — SECURITY, Key = 5

| Plaintext | Index | Calculation | Cipher Index | Ciphertext |
|-----------|-------|-------------|--------------|------------|
| S | 18 | (18 + 5) % 26 = 23 | 23 | X |
| E | 4 | (4 + 5) % 26 = 9 | 9 | J |
| C | 2 | (2 + 5) % 26 = 7 | 7 | H |
| U | 20 | (20 + 5) % 26 = 25 | 25 | Z |
| R | 17 | (17 + 5) % 26 = 22 | 22 | W |
| I | 8 | (8 + 5) % 26 = 13 | 13 | N |
| T | 19 | (19 + 5) % 26 = 24 | 24 | Y |
| Y | 24 | (24 + 5) % 26 = 29 % 26 = 3 | 3 | D |

```text
SECURITY → XJHZWNYD
```

### ➕ Additional Example 7 — Sentence with spaces, Key = 3

> **Additional implementation note:** spaces can be preserved depending on the implementation. The lecture does not specify a rule for spaces. Here, spaces are kept and only letters are shifted.

```text
THIS IS FUN → WKLV LV IXQ
```

| Word | Calculation | Result |
|------|-------------|--------|
| THIS | T19→22 W, H7→10 K, I8→11 L, S18→21 V | WKLV |
| IS | I8→11 L, S18→21 V | LV |
| FUN | F5→8 I, U20→23 X, N13→16 Q | IXQ |

### ➕ Additional Example 8 — Decryption with wrap-around

```text
Ciphertext = BQQ, Key = 2

B = 1  → (1 - 2) = -1  → -1 + 26 = 25 → Z
Q = 16 → (16 - 2) = 14 → O
Q = 16 → (16 - 2) = 14 → O

BQQ → ZOO
```

---

# 10. Implementation

➕ **Additional:** The lecture presents only the mathematical algorithm. The code below is an example of how to implement it. These examples **process letters A–Z only** and keep other characters unchanged.

## Python

```python
def caesar_encrypt(text: str, key: int) -> str:
    result = []
    for ch in text.upper():
        if "A" <= ch <= "Z":
            p = ord(ch) - ord("A")
            c = (p + key) % 26
            result.append(chr(c + ord("A")))
        else:
            result.append(ch)
    return "".join(result)


def caesar_decrypt(text: str, key: int) -> str:
    result = []
    for ch in text.upper():
        if "A" <= ch <= "Z":
            c = ord(ch) - ord("A")
            p = ((c - key) % 26 + 26) % 26   # safe for negative values
            result.append(chr(p + ord("A")))
        else:
            result.append(ch)
    return "".join(result)


if __name__ == "__main__":
    assert caesar_encrypt("O", 5) == "T"
    assert caesar_encrypt("OMAR", 5) == "TRFW"
    assert caesar_encrypt("ABC", 3) == "DEF"
    assert caesar_encrypt("XYZ", 3) == "ABC"
    assert caesar_decrypt("TRFW", 5) == "OMAR"
    assert caesar_decrypt("A", 3) == "X"
    print("All tests passed")
```

## JavaScript

```javascript
function caesarEncrypt(text, key) {
  let result = "";
  for (const ch of text.toUpperCase()) {
    if (ch >= "A" && ch <= "Z") {
      const p = ch.charCodeAt(0) - 65;
      const c = (p + key) % 26;
      result += String.fromCharCode(c + 65);
    } else {
      result += ch;
    }
  }
  return result;
}

function caesarDecrypt(text, key) {
  let result = "";
  for (const ch of text.toUpperCase()) {
    if (ch >= "A" && ch <= "Z") {
      const c = ch.charCodeAt(0) - 65;
      const p = (((c - key) % 26) + 26) % 26; // JS can return negative values
      result += String.fromCharCode(p + 65);
    } else {
      result += ch;
    }
  }
  return result;
}

console.log(caesarEncrypt("OMAR", 5)); // TRFW
console.log(caesarDecrypt("TRFW", 5)); // OMAR
```

## C#

```csharp
using System.Text;

static string CaesarEncrypt(string text, int key)
{
    var result = new StringBuilder();
    foreach (char ch in text.ToUpper())
    {
        if (ch >= 'A' && ch <= 'Z')
        {
            int p = ch - 'A';
            int c = (p + key) % 26;
            result.Append((char)(c + 'A'));
        }
        else result.Append(ch);
    }
    return result.ToString();
}

static string CaesarDecrypt(string text, int key)
{
    var result = new StringBuilder();
    foreach (char ch in text.ToUpper())
    {
        if (ch >= 'A' && ch <= 'Z')
        {
            int c = ch - 'A';
            int p = ((c - key) % 26 + 26) % 26;   // C# can return negative values
            result.Append((char)(p + 'A'));
        }
        else result.Append(ch);
    }
    return result.ToString();
}
```

## Test cases

| Mode | Input | Key | Expected |
|------|-------|-----|----------|
| Encrypt | `O` | 5 | `T` |
| Encrypt | `OMAR` | 5 | `TRFW` |
| Encrypt | `ABC` | 3 | `DEF` |
| Encrypt | `XYZ` | 3 | `ABC` |
| Encrypt | `HELLO` | 3 | `KHOOR` |
| Decrypt | `TRFW` | 5 | `OMAR` |
| Decrypt | `A` | 3 | `X` |
| Encrypt | `HELLO` | 29 | `KHOOR` (29 ≡ 3) |
| Encrypt | `HELLO` | 0 | `HELLO` |

---

# 11. Edge Cases and Implementation Notes

➕ **Additional**

| Case | Recommended handling |
|------|----------------------|
| Spaces, digits, punctuation | Can be preserved unchanged depending on the implementation (not specified in the lecture). |
| Lowercase letters | Convert to uppercase first, or use a separate base (`'a'`) to keep the case. |
| `K ≥ 26` | Reduce with `K % 26`; the result is identical. |
| `K < 0` | Use the safe modulo form `((x % 26) + 26) % 26`. |
| `K = 0` or `K = 26` | Output equals input. |
| Empty string | Return an empty string. |
| Non-English letters | Not covered by the 26-letter formula. |

---

# 12. Complexity

➕ **Additional**

| Measure | Value | Reason |
|---------|-------|--------|
| Time | `O(n)` | Each of the `n` characters is processed once |
| Space | `O(n)` | A new output string of length `n` is built |
| Key space | 26 values (`0–25`) | Keys above 25 repeat the same shifts |

---

# 13. Security Analysis

➕ **Additional — this section is general background, not lecture content.**

Caesar Cipher is excellent for **learning**, but it is **not secure** for real use.

- **Tiny key space:** only 26 possible keys (one of them, `0`, does nothing). An attacker can try them all (**brute force**).
- **Letter patterns remain:** the same plaintext letter always becomes the same ciphertext letter. For example, the two `L` letters in `HELLO` both become `O` in `KHOOR`.
- **Frequency analysis:** common letters in a language (like `E`) stay common in the ciphertext, so the shift can be guessed.

### Brute-force example

Ciphertext `KHOOR`, trying each key by decryption:

| Key tried | Result |
|-----------|--------|
| 1 | JGNNQ |
| 2 | IFMMP |
| **3** | **HELLO** ← readable |

```python
def brute_force(ciphertext: str) -> None:
    for k in range(26):
        print(k, caesar_decrypt(ciphertext, k))
```

### Relation to other ideas

| Idea | Note |
|------|------|
| Substitution cipher | Caesar is the simplest case, with one fixed shift for all letters |
| ROT13 | Caesar with `K = 13`. Encrypting twice returns the original (`HELLO → URYYB → HELLO`) |
| Transposition | Different idea: keeps letters and changes order (`ROMA → ORMA` in the lecture) |

---

# 14. Common Mistakes

➕ **Additional**

| # | Mistake | Tiny example (wrong → right) |
|---|---------|------------------------------|
| 1 | Starting `A` at 1 | `A + 3`: wrong `1 + 3 = 4 → E`; right `0 + 3 = 3 → D` |
| 2 | Forgetting `% 26` | `X + 3`: wrong `26`; right `26 % 26 = 0 → A` |
| 3 | Wrong key | `HELLO` with `K = 4` gives `LIPPS`, not `KHOOR` |
| 4 | Adding the key when decrypting | Decrypt `D`, `K = 3`: wrong `6 → G`; right `0 → A` |
| 5 | Subtracting the key when encrypting | Encrypt `D`, `K = 3`: wrong `0 → A`; right `6 → G` |
| 6 | Mixing plaintext and ciphertext | In `TRFW → OMAR`, `TRFW` is the ciphertext |
| 7 | Forgetting negative values in decryption | `A`, `K = 3`: `-3` must become `23 → X` |
| 8 | Wrong index from memory | `O = 14`, not 15 |
| 9 | Confusing substitution with transposition | Caesar replaces letters; transposition reorders them |

---

# 15. Quick Reference

```text
Alphabet : A=0  B=1  C=2  ...  Z=25
Encrypt  : C = (P + K) % 26
Decrypt  : P = (C - K) % 26
Safe decrypt (code): P = ((C - K) % 26 + 26) % 26
```

| | Encryption | Decryption |
|---|---|---|
| Input | Plaintext | Ciphertext |
| Output | Ciphertext | Plaintext |
| Formula | `C = (P + K) % 26` | `P = (C - K) % 26` |
| Operation | Add key | Subtract key |

**Lecture examples to remember:** `O → T` (K = 5), `OMAR → TRFW` (K = 5), `ABC → DEF` (K = 3), `XYZ → ABC` (K = 3).

---

# 16. Practice Exercises

➕ **Additional** (answers are in the next section)

### Easy

1. Encrypt `A` with `K = 3`.
2. Encrypt `B` with `K = 5`.
3. Encrypt `HELLO` with `K = 3`.
4. Decrypt `DEF` with `K = 3`.
5. Decrypt `TRFW` with `K = 5`.

### Medium

1. Encrypt `CAESAR` with `K = 4`.
2. Encrypt `ZOO` with `K = 2`.
3. Decrypt `GEIWEV` with `K = 4`.
4. Decrypt `BQQ` with `K = 2`.
5. Decrypt `WKLV LV IXQ` with `K = 3` (keep spaces).

### Challenge

1. Encrypt `PYTHON` with `K = 12`.
2. Plaintext is `HELLO` and ciphertext is `KHOOR`. Find the key.
3. Plaintext is `OMAR` and ciphertext is `TRFW`. Find the key.
4. Which value in `0–25` is the same as `K = 30`?
5. `TRFW` was encrypted with `K = 5`. Decrypt it by **encrypting** with another key. Which key?

---

# 17. Practice Answers

### Easy

1. `A` → **D**
2. `B` → **G**
3. `HELLO` → **KHOOR**
4. `DEF` → **ABC**
5. `TRFW` → **OMAR**

### Medium

1. `CAESAR` (C 2→6 G, A 0→4 E, E 4→8 I, S 18→22 W, A→E, R 17→21 V) → **GEIWEV**
2. `ZOO` (Z 25→27%26=1 B, O 14→16 Q, O→Q) → **BQQ**
3. `GEIWEV` → **CAESAR**
4. `BQQ` (B 1−2=−1→25 Z, Q 16→14 O, Q→O) → **ZOO**
5. `WKLV LV IXQ` → **THIS IS FUN**

### Challenge

1. `PYTHON` (P 15→27%26=1 B, Y 24→36%26=10 K, T 19→31%26=5 F, H 7→19 T, O 14→26%26=0 A, N 13→25 Z) → **BKFTAZ**
2. `H (7) → K (10)`, so `K = 10 − 7 = ` **3**
3. `O (14) → T (19)`, so `K = 19 − 14 = ` **5**
4. `30 % 26 =` **4**
5. `26 − 5 =` **21** (e.g. `T`: 19 + 21 = 40, 40 % 26 = 14 → `O`)

---

# 18. Interview Questions

➕ **Additional**

**1. What is the Caesar Cipher?**
A substitution cipher that shifts each letter by a fixed key, using `C = (P + K) % 26`.

**2. Is it symmetric or asymmetric?**
Symmetric: the same key `K` is used for encryption and decryption.

**3. Why do we use modulo 26?**
To wrap around from `Z` back to `A` and keep indexes in `0–25`.

**4. How do you decrypt?**
`P = (C - K) % 26`. In code, use `((C - K) % 26 + 26) % 26` to avoid negative results.

**5. How many keys are possible?**
26 (0–25). Other numbers repeat the same shifts.

**6. Why is it insecure?**
Brute force tries all 26 keys quickly, and letter frequencies stay visible.

**7. What is the time complexity?**
`O(n)` for a message of length `n`.

**8. What is ROT13?**
A Caesar Cipher with `K = 13`. Applying it twice returns the original text.

**9. Substitution vs. transposition?**
Substitution replaces characters (Caesar). Transposition rearranges positions.

**10. What happens with `K = 26`?**
Nothing changes: `26 % 26 = 0`.

---

## References

- 📘 *Information & Network Security — Lecture 01: Classical Encryption — Caesar Cipher* (primary source).
- ➕ All sections marked **Additional** are general educational material added for study.