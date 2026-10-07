# Information & Network Security — Lecture 01

**Classical Encryption — Caesar Cipher**

> **How to read this document**
> - 📘 **Lecture** = content taken from the instructor's notes (terminology kept as is).
> - ➕ **Additional Explanation / Additional Example / Practice** = extra material added to help you study. It is *not* claimed to be from the lecture.

---

## 📌 Lecture Overview

📘 **Lecture:** Introduction to Information Security & Classical Encryption — Caesar Cipher.

| Part | Topic |
|------|-------|
| 1 | Basic encryption concepts (Plaintext, Encryption, Ciphertext, Decryption) |
| 2 | Encryption techniques (Symmetric, Asymmetric) |
| 3 | Classical encryption (Substitution, Transposition) |
| 4 | Caesar Cipher (main topic) |
| 5–6 | Encryption and decryption formulas |
| 7+ | Worked examples, practice, implementation |

---

## 🎯 Learning Objectives

After studying this file you should be able to:

1. Define **Plaintext, Encryption, Ciphertext, Decryption**.
2. Explain the difference between **Symmetric** and **Asymmetric** encryption.
3. Explain the difference between **Substitution** and **Transposition**.
4. Explain how the **Caesar Cipher** works and what the **Key** does.
5. Convert letters to indexes (`A = 0 … Z = 25`) and back.
6. Encrypt with `C = (P + K) % 26` and decrypt with `P = (C - K) % 26`.
7. Handle **wrap-around** (for example `X → A`).
8. Solve any Caesar problem step by step, and turn the algorithm into code.

---

## 🔐 1. Basic Security & Encryption Concepts

### Plaintext

📘 **Lecture:** The original readable message before encryption.

➕ **Additional Explanation:** This is what you *want to protect*. Example: `HELLO`.

### Encryption

📘 **Lecture:** The process of transforming the **Plaintext** into an unreadable form.

➕ **Additional Explanation:** Encryption uses an algorithm (for example Caesar Cipher) and a **key**. Without the key, the result should look meaningless.

### Ciphertext

📘 **Lecture:** The encrypted message produced after encryption.

➕ **Additional Explanation:** This is what you can send or store. Example: `KHOOR`.

### Decryption

📘 **Lecture:** The process of transforming the **Ciphertext** back into the original **Plaintext**.

➕ **Additional Explanation:** Decryption is the reverse of encryption. The receiver uses the key to get the readable message back.

### Encryption/Decryption Flow

```text
Plaintext
   ↓
Encryption + Key
   ↓
Ciphertext
   ↓
Decryption + Key
   ↓
Plaintext
```

| Component | Simple meaning | Example |
|-----------|----------------|---------|
| Plaintext | Message you can read | `HELLO` |
| Encryption + Key | Scramble the message using the key | shift by `3` |
| Ciphertext | Message you cannot read | `KHOOR` |
| Decryption + Key | Unscramble using the key | shift back by `3` |
| Plaintext | Original message again | `HELLO` |

> ➕ **Additional Explanation:** The key is used in *both* steps. If someone does not know the key, decryption is hard.

---

## 🔑 2. Encryption Techniques

### Symmetric Encryption

📘 **Lecture:**
- Uses **one key**.
- The same key is used for the encryption/decryption process.
- The lecture introduces two classical techniques under this idea: **Substitution** and **Transposition**.

➕ **Additional Explanation:** Both sides (sender and receiver) must know the **same secret key**. If the receiver has a different key, decryption gives wrong text. Caesar Cipher is a symmetric cipher: the key `K` (a number) is used to add and later to subtract.

```text
        Same Key (K)
       ┌────────────┐
       ↓            ↓
Plaintext → [Encrypt] → Ciphertext → [Decrypt] → Plaintext
```

### Asymmetric Encryption

📘 **Lecture:**
- Uses **two keys**: **Public Key** and **Private Key**.
- **RSA** is mentioned as an example.

➕ **Additional Explanation:** The two keys are related but different. In general, one key is shared publicly and the other is kept secret. (The RSA mathematics is not the focus of this lecture, so we skip it.)

```text
Plaintext → [Encrypt with Key 1] → Ciphertext → [Decrypt with Key 2] → Plaintext
```

### ➕ Additional Explanation: Symmetric vs Asymmetric

| | Symmetric | Asymmetric |
|---|-----------|------------|
| Number of keys | 1 | 2 (Public + Private) |
| Same key for both steps? | Yes | No |
| Example in lecture | Substitution / Transposition, Caesar | RSA |

---

## 🔄 3. Classical Encryption Techniques

### Substitution

📘 **Lecture:** The characters are **replaced** by other characters.

```text
Example idea:
AMIN → ROMA
```

➕ **Additional Explanation:**
- **What changes:** every letter is replaced by a different letter.
- **What stays the same (conceptually):** the message still has the same length, and each position still holds one character.
- Note: `AMIN → ROMA` only shows the *idea* of replacement. It is not a Caesar shift, because Caesar uses one fixed shift for all letters.

### Transposition

📘 **Lecture:** The characters themselves remain the same, but their **order is changed**.

```text
Example idea:
ROMA → ORMA
```

➕ **Additional Explanation:** Look at `ROMA → ORMA`: the letters `R, O, M, A` are all still there. Only the first two swapped places. No new letters appear.

### Comparison

| Technique | What changes? |
|-----------|---------------|
| Substitution | Characters are replaced |
| Transposition | Character positions are rearranged |

➕ **Additional Explanation – quick test:** Compare the *set of letters* in plaintext and ciphertext.
- Same letters, different order → **Transposition**.
- Different letters → **Substitution**.

---

# 🔥 4. Caesar Cipher

### What is it?

📘 **Lecture:** The Caesar Cipher is a simple classical encryption algorithm. Each character is **shifted by a fixed number of positions** in the alphabet. The fixed number is the **Key**.

```text
Key = 5
```

### Why is it a substitution technique?

➕ **Additional Explanation:** Each plaintext letter is **replaced** by another letter (for example `O` becomes `T`). The positions do not change. Replacing letters = substitution.

### Why is it "simple" and "classical"?

➕ **Additional Explanation:** It uses only one small number (the key) and one simple operation (addition). It was used long ago, before computers, and it is mainly taught to explain the basic ideas.

### Character-by-character processing

📘 **Lecture:** Caesar Cipher works **character by character**. Each letter is processed alone, using the same key.

```text
H   E   L   L   O
↓   ↓   ↓   ↓   ↓      (same key for every letter)
K   H   O   O   R
```

### The role of the key

📘 **Lecture:** The key is a **number**. It tells you how many positions to shift.

➕ **Additional Explanation:** `K = 3` means: move 3 letters forward. `A → D`, `B → E`, `C → F`.

### Alphabet indexing

📘 **Lecture:** The lecture uses:

```text
A = 0
B = 1
C = 2
...
Z = 25
```

So we work with **26 letters**. ⚠️ **Counting starts at 0, not 1.**

| Letter | A | B | C | D | E | F | G | H | I | J | K | L | M |
|--------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Index  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |

| Letter | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|--------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Index  | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |

➕ **Additional Explanation – shifting on a line:**

```text
Key = 3
A  B  C  D  E  F  G ... X  Y  Z
0  1  2  3  4  5  6 ... 23 24 25
└──────→ +3 ──────→
A → D     X → A (wrap-around)
```

---

# 🧮 5. Caesar Encryption Formula

```text
C = (P + K) % 26
```

| Symbol | Meaning |
|--------|---------|
| `P` | Plaintext character **index** |
| `K` | **Key** (the shift number) |
| `C` | Ciphertext character **index** |
| `26` | Number of letters in the English alphabet |
| `%` | **Modulo**: the remainder after division |

### What is modulo?

➕ **Additional Explanation:** `a % 26` is the remainder when you divide `a` by 26.

```text
 5 % 26 = 5      (26 does not fit in 5, remainder 5)
26 % 26 = 0      (26 fits exactly once, remainder 0)
27 % 26 = 1
30 % 26 = 4
```

### Why do we need modulo 26?

📘 **Lecture:** `% 26` keeps the result inside the range `0–25` and handles the wrap-around from `Z` back to `A`.

➕ **Additional Explanation:** Indexes only exist from 0 to 25. Without `% 26`, `X + 3` gives `26`, and there is no letter with index 26. Modulo turns the alphabet into a **circle**: after `Z` you go back to `A`.

```text
          A(0)
     Z(25)    B(1)
   Y(24)         C(2)
  X(23)           D(3)
   ...  alphabet as a circle ...
```

### Wrap-around example (from the lecture, X with K = 3)

```text
X = 23
K = 3

C = (23 + 3) % 26
C = 26 % 26
C = 0
0 = A
```

Therefore:

```text
X → A
```

---

# 🔓 6. Caesar Decryption Formula

```text
P = (C - K) % 26
```

📘 **Lecture:** This moves the character **backward** by the same key.

### Why subtraction?

➕ **Additional Explanation:** Encryption moved forward by `K`. To go back to the start, move backward by `K`. Adding `K` and then subtracting `K` gives the original number.

```text
P = 14, K = 5
Encrypt: 14 + 5 = 19
Decrypt: 19 - 5 = 14   ← back to P
```

### Encryption and decryption are inverse operations

```text
Encryption:
P → C
C = (P + K) % 26

Decryption:
C → P
P = (C - K) % 26
```

---

# 🧠 7. VERY DETAILED WORKED EXAMPLES

Formula: `C = (P + K) % 26`

---

### Example 1 — Single Character 📘

| Item | Value |
|------|-------|
| Plaintext | `O` |
| Key | `5` |
| Character | `O` |
| Character index | `14` |
| Formula | `C = (P + K) % 26` |
| Calculation | `(14 + 5) % 26 = 19 % 26 = 19` |
| Resulting index | `19` |
| Resulting character | `T` |
| Final ciphertext | `T` |

```text
O → T
```

---

### Example 2 — OMAR, Key = 5 📘

| Plaintext | Index | Key | Calculation | Cipher Index | Ciphertext |
|-----------|-------|-----|-------------|--------------|------------|
| O | 14 | 5 | (14 + 5) % 26 = 19 | 19 | T |
| M | 12 | 5 | (12 + 5) % 26 = 17 | 17 | R |
| A | 0 | 5 | (0 + 5) % 26 = 5 | 5 | F |
| R | 17 | 5 | (17 + 5) % 26 = 22 | 22 | W |

Final:

```text
OMAR → TRFW
```

---

### Example 3 — ABC, Key = 3 📘

| Plaintext | Index | Key | Calculation | Cipher Index | Ciphertext |
|-----------|-------|-----|-------------|--------------|------------|
| A | 0 | 3 | (0 + 3) % 26 = 3 | 3 | D |
| B | 1 | 3 | (1 + 3) % 26 = 4 | 4 | E |
| C | 2 | 3 | (2 + 3) % 26 = 5 | 5 | F |

```text
ABC → DEF
```

---

### Example 4 — XYZ, Key = 3 (wrap-around) 📘

| Plaintext | Index | Key | Calculation | Cipher Index | Ciphertext |
|-----------|-------|-----|-------------|--------------|------------|
| X | 23 | 3 | (23 + 3) % 26 = 26 % 26 = 0 | 0 | A |
| Y | 24 | 3 | (24 + 3) % 26 = 27 % 26 = 1 | 1 | B |
| Z | 25 | 3 | (25 + 3) % 26 = 28 % 26 = 2 | 2 | C |

```text
XYZ → ABC
```

The `% 26` operation makes the alphabet **wrap around** after `Z`.

---

### Example 5 — HELLO, Key = 3 ➕ *Additional Example*

| Plaintext | Index | Key | Calculation | Cipher Index | Ciphertext |
|-----------|-------|-----|-------------|--------------|------------|
| H | 7 | 3 | (7 + 3) % 26 = 10 | 10 | K |
| E | 4 | 3 | (4 + 3) % 26 = 7 | 7 | H |
| L | 11 | 3 | (11 + 3) % 26 = 14 | 14 | O |
| L | 11 | 3 | (11 + 3) % 26 = 14 | 14 | O |
| O | 14 | 3 | (14 + 3) % 26 = 17 | 17 | R |

```text
HELLO → KHOOR
```

💡 Notice: both `L` letters became `O`. The same plaintext letter always gives the same ciphertext letter (same key).

---

### Example 6 — SECURITY, Key = 5 ➕ *Additional Example*

| Plaintext | Index | Key | Calculation | Cipher Index | Ciphertext |
|-----------|-------|-----|-------------|--------------|------------|
| S | 18 | 5 | (18 + 5) % 26 = 23 | 23 | X |
| E | 4 | 5 | (4 + 5) % 26 = 9 | 9 | J |
| C | 2 | 5 | (2 + 5) % 26 = 7 | 7 | H |
| U | 20 | 5 | (20 + 5) % 26 = 25 | 25 | Z |
| R | 17 | 5 | (17 + 5) % 26 = 22 | 22 | W |
| I | 8 | 5 | (8 + 5) % 26 = 13 | 13 | N |
| T | 19 | 5 | (19 + 5) % 26 = 24 | 24 | Y |
| Y | 24 | 5 | (24 + 5) % 26 = 29 % 26 = 3 | 3 | D |

```text
SECURITY → XJHZWNYD
```

(`Y` wraps around to `D`.)

---

### Example 7 — DATA, Key = 7 ➕ *Additional Example*

| Plaintext | Index | Key | Calculation | Cipher Index | Ciphertext |
|-----------|-------|-----|-------------|--------------|------------|
| D | 3 | 7 | (3 + 7) % 26 = 10 | 10 | K |
| A | 0 | 7 | (0 + 7) % 26 = 7 | 7 | H |
| T | 19 | 7 | (19 + 7) % 26 = 26 % 26 = 0 | 0 | A |
| A | 0 | 7 | (0 + 7) % 26 = 7 | 7 | H |

```text
DATA → KHAH
```

(`T` wraps around to `A`.)

---

### Example 8 — Longer sentence ➕ *Additional Example*

Plaintext = `MEET ME AT NOON`, Key = 3

> ➕ **Additional implementation note:** spaces can be preserved depending on the implementation. The lecture notes only show letters, so this guide does not claim a lecture rule for spaces. Here we **keep the spaces** unchanged and encrypt only the letters.

| Word | Letter calculations | Result |
|------|--------------------|--------|
| MEET | M(12)→15=P, E(4)→7=H, E(4)→7=H, T(19)→22=W | PHHW |
| ME | M(12)→15=P, E(4)→7=H | PH |
| AT | A(0)→3=D, T(19)→22=W | DW |
| NOON | N(13)→16=Q, O(14)→17=R, O(14)→17=R, N(13)→16=Q | QRRQ |

```text
MEET ME AT NOON → PHHW PH DW QRRQ
```

---

# 🔓 8. DETAILED DECRYPTION EXAMPLES

Formula: `P = (C - K) % 26`

---

### Example 1 — TRFW, Key = 5 📘

| Ciphertext | Index | Key | Calculation | Plain Index | Plaintext |
|------------|-------|-----|-------------|-------------|-----------|
| T | 19 | 5 | (19 - 5) % 26 = 14 | 14 | O |
| R | 17 | 5 | (17 - 5) % 26 = 12 | 12 | M |
| F | 5 | 5 | (5 - 5) % 26 = 0 | 0 | A |
| W | 22 | 5 | (22 - 5) % 26 = 17 | 17 | R |

```text
TRFW → OMAR
```

---

### Example 2 — DEF, Key = 3 ➕ *Additional Example*

| Ciphertext | Index | Key | Calculation | Plain Index | Plaintext |
|------------|-------|-----|-------------|-------------|-----------|
| D | 3 | 3 | (3 - 3) % 26 = 0 | 0 | A |
| E | 4 | 3 | (4 - 3) % 26 = 1 | 1 | B |
| F | 5 | 3 | (5 - 3) % 26 = 2 | 2 | C |

```text
DEF → ABC
```

---

### Example 3 — Wrap-around decryption ➕ *Additional Example*

```text
Ciphertext = A
Key = 3
```

`A = 0`, so:

```text
P = (0 - 3) % 26
P = (-3) % 26
```

The result of `0 - 3` is **negative** (`-3`). On the alphabet circle, going back 3 steps from `A` goes to `Z, Y, X`. So the answer must be `X`.

**Safe mathematical approach (same formula, same meaning):**
In mathematics, the modulo result is always between `0` and `25`, so `-3 mod 26 = 23`. You can get this by adding `26` first:

```text
-3 + 26 = 23
23 % 26 = 23
23 = X
```

```text
A → X
```

➕ **Additional implementation note:** some programming languages return a **negative** number for `-3 % 26` (for example C, C++, C#, Java), and some return `23` (for example Python). To avoid problems in any language, write:

```text
P = ((C - K) % 26 + 26) % 26
```

This is the *same* formula as the lecture, just made safe for negative values.

**Check:** `X` encrypted with `K = 3` gives `A` (Example 4 above), so `A → X` is correct.

---

# 📊 9. ENCRYPTION vs DECRYPTION

| | Encryption | Decryption |
|---|---|---|
| Input | Plaintext | Ciphertext |
| Output | Ciphertext | Plaintext |
| Formula | `C = (P + K) % 26` | `P = (C - K) % 26` |
| Operation | Add key | Subtract key |
| Direction | Forward (`A → D`) | Backward (`D → A`) |
| Key | Same `K` | Same `K` |

---

# 🔢 10. ALPHABET INDEX REFERENCE

```text
A → 0     H → 7     O → 14    V → 21
B → 1     I → 8     P → 15    W → 22
C → 2     J → 9     Q → 16    X → 23
D → 3     K → 10    R → 17    Y → 24
E → 4     L → 11    S → 18    Z → 25
F → 5     M → 12    T → 19
G → 6     N → 13    U → 20
```

Compact table for solving problems:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|----|----|----|
| A | B | C | D | E | F | G | H | I | J | K | L | M |

| 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |
|----|----|----|----|----|----|----|----|----|----|----|----|----|
| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |

---

# 🧩 11. HOW TO SOLVE ANY CAESAR PROBLEM

## Encryption

1. Write the alphabet (with indexes `0–25`).
2. Convert letters to indexes.
3. Identify the key.
4. Apply `C = (P + K) % 26`.
5. Convert indexes back to letters.
6. Repeat for all characters.
7. Write the final ciphertext.

## Decryption

1. Convert ciphertext letters to indexes.
2. Identify the key.
3. Apply `P = (C - K) % 26`.
4. Convert indexes back to letters.
5. Repeat for all characters.
6. Recover the plaintext.

➕ **Additional tips**
- If the sum is `26` or more, subtract `26` (this is what `% 26` does).
- If the subtraction is negative, add `26`.
- Always **check** your answer: decrypt the ciphertext and see if you get the original plaintext.

---

# ⚠️ 12. COMMON MISTAKES

| # | Mistake | Tiny example (wrong → right) |
|---|---------|------------------------------|
| 1 | Starting `A` from 1 instead of 0 | `A + 3`: wrong `1 + 3 = 4 → E`; right `0 + 3 = 3 → D` |
| 2 | Forgetting `% 26` | `X + 3`: wrong `26` (no letter); right `26 % 26 = 0 → A` |
| 3 | Using the wrong key | `HELLO` with `K = 4` gives `LIPPS`, not `KHOOR` (`K = 3`) |
| 4 | Adding the key during decryption | Decrypt `D` (`K = 3`): wrong `3 + 3 = 6 → G`; right `3 - 3 = 0 → A` |
| 5 | Subtracting the key during encryption | Encrypt `D` (`K = 3`): wrong `3 - 3 = 0 → A`; right `3 + 3 = 6 → G` |
| 6 | Confusing plaintext and ciphertext | In `TRFW → OMAR` with K = 5, `TRFW` is the *ciphertext*, `OMAR` is the *plaintext* |
| 7 | Forgetting wrap-around | `Y + 3`: wrong "no letter after Z"; right `27 % 26 = 1 → B` |
| 8 | Wrong alphabet indexing | `O` is `14`, not `15`. Use the reference table; do not count by memory |
| 9 | Mixing up substitution and transposition | `ROMA → ORMA` is transposition (same letters). Caesar `O → T` is substitution (new letters) |

---

# 🧪 13. PRACTICE QUESTIONS

➕ **Practice** (answers are in the next section; try first!)

### Easy

1. Encrypt `A` with K = 3
2. Encrypt `B` with K = 5
3. Encrypt `HELLO` with K = 3
4. Encrypt `DATA` with K = 2
5. Decrypt `DEF` with K = 3

### Medium

1. Encrypt `SECURITY` with K = 7
2. Encrypt `INFORMATION` with K = 4
3. Decrypt `TRFW` with K = 5
4. Encrypt `NETWORK` with K = 9
5. Decrypt `ABC` with K = 3

### Challenge

1. Encrypt `ZEBRA` with K = 3
2. Encrypt `WINTER` with K = 10
3. Decrypt `KHOOR ZRUOG` with K = 3 (keep the space)
4. Decrypt `BOB` with K = 5
5. Encrypt `NETWORKSECURITY` with K = 15
6. Decrypt `PHHW PH DW QRRQ` with K = 3 (keep the spaces)

---

## ✅ Practice Answers

### Easy

1. `A` (0 + 3 = 3) → **D**
2. `B` (1 + 5 = 6) → **G**
3. `HELLO` → **KHOOR**
4. `DATA` (D 3→5 F, A 0→2 C, T 19→21 V, A 0→2 C) → **FCVC**
5. `DEF` → **ABC**

### Medium

1. `SECURITY` (S 18→25 Z, E 4→11 L, C 2→9 J, U 20→27%26=1 B, R 17→24 Y, I 8→15 P, T 19→26%26=0 A, Y 24→31%26=5 F) → **ZLJBYPAF**
2. `INFORMATION` (I 8→12 M, N 13→17 R, F 5→9 J, O 14→18 S, R 17→21 V, M 12→16 Q, A 0→4 E, T 19→23 X, I→M, O→S, N→R) → **MRJSVQEXMSR**
3. `TRFW` → **OMAR**
4. `NETWORK` (N 13→22 W, E 4→13 N, T 19→28%26=2 C, W 22→31%26=5 F, O 14→23 X, R 17→26%26=0 A, K 10→19 T) → **WNCFXAT**
5. `ABC` (0−3=−3→23 X, 1−3=−2→24 Y, 2−3=−1→25 Z) → **XYZ**

### Challenge

1. `ZEBRA` (Z 25→28%26=2 C, E 4→7 H, B 1→4 E, R 17→20 U, A 0→3 D) → **CHEUD**
2. `WINTER` (W 22→32%26=6 G, I 8→18 S, N 13→23 X, T 19→29%26=3 D, E 4→14 O, R 17→27%26=1 B) → **GSXDOB**
3. `KHOOR ZRUOG` → **HELLO WORLD** (Z 25−3=22 W, R 17−3=14 O, U 20−3=17 R, O 14−3=11 L, G 6−3=3 D)
4. `BOB` (B 1−5=−4→22 W, O 14−5=9 J, B→W) → **WJW**
5. `NETWORKSECURITY` (N→C, E→T, T→I, W→L, O→D, R→G, K→Z, S→H, E→T, C→R, U→J, R→G, I→X, T→I, Y→N) → **CTILDGZHTRJGXIN**
6. `PHHW PH DW QRRQ` → **MEET ME AT NOON**

---

# 💻 14. IMPLEMENTATION SECTION

➕ **Additional Explanation:** This section shows how the math becomes a program. It is not from the lecture.

## Language-independent pseudocode

```text
for each character:
    convert character to index
    apply Caesar formula
    convert index back to character
```

### Detailed pseudocode — encryption

```text
function encrypt(plaintext, K):
    result = ""
    for each character ch in plaintext:
        if ch is a letter:
            P = index of ch          // A=0 ... Z=25
            C = (P + K) % 26
            result = result + letter at index C
        else:
            result = result + ch     // spaces/symbols kept (implementation choice)
    return result
```

### Detailed pseudocode — decryption

```text
function decrypt(ciphertext, K):
    result = ""
    for each character ch in ciphertext:
        if ch is a letter:
            C = index of ch
            P = ((C - K) % 26 + 26) % 26    // safe for negative values
            result = result + letter at index P
        else:
            result = result + ch
    return result
```

### Mapping letters to indexes

```text
index = (ASCII code of uppercase letter) - (ASCII code of 'A')
letter = character with code (index + ASCII code of 'A')
```

Example: `'O'` has ASCII code 79 and `'A'` has 65, so index = `79 - 65 = 14`. ✔

## Optional example in Python (only an example, not required)

```python
def caesar_encrypt(text, key):
    result = ""
    for ch in text.upper():
        if ch.isalpha():
            p = ord(ch) - ord('A')
            c = (p + key) % 26
            result += chr(c + ord('A'))
        else:
            result += ch
    return result

def caesar_decrypt(text, key):
    result = ""
    for ch in text.upper():
        if ch.isalpha():
            c = ord(ch) - ord('A')
            p = ((c - key) % 26 + 26) % 26
            result += chr(p + ord('A'))
        else:
            result += ch
    return result

print(caesar_encrypt("OMAR", 5))   # TRFW
print(caesar_decrypt("TRFW", 5))   # OMAR
```

## Optional example in C# (only an example, not required)

```csharp
static string CaesarEncrypt(string text, int key)
{
    var result = new System.Text.StringBuilder();
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
    var result = new System.Text.StringBuilder();
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

## Test cases to check your code

| Mode | Input | Key | Expected |
|------|-------|-----|----------|
| Encrypt | `O` | 5 | `T` |
| Encrypt | `OMAR` | 5 | `TRFW` |
| Encrypt | `ABC` | 3 | `DEF` |
| Encrypt | `XYZ` | 3 | `ABC` |
| Decrypt | `TRFW` | 5 | `OMAR` |
| Decrypt | `A` | 3 | `X` |

---

# 🧠 Quick Summary

| Concept | Meaning |
|---------|---------|
| Plaintext | Original readable message |
| Encryption | Converts plaintext to ciphertext |
| Ciphertext | Encrypted message |
| Decryption | Converts ciphertext back to plaintext |
| Symmetric | Uses one key |
| Asymmetric | Uses two keys |
| Public Key | One of the asymmetric keys |
| Private Key | One of the asymmetric keys |
| Substitution | Replaces characters |
| Transposition | Rearranges characters |
| Caesar Cipher | Shifts characters by a fixed key |

## 💡 Important Notes

📘 **Lecture**
- Caesar Cipher works **character by character**.
- The key is a **number**.
- The alphabet is represented using indexes `0–25`.
- `% 26` handles the wrap-around from `Z` back to `A`.
- The lecture presents Caesar as a simple classical encryption algorithm.

➕ **Additional note:** Because there are only 26 possible shifts, a Caesar Cipher is easy to break by trying every key. This is one reason it is only a teaching example and not used for real security.

---

## 📚 Lecture Progress

- [x] Encryption & Decryption
- [x] Plaintext & Ciphertext
- [x] Symmetric Encryption
- [x] Asymmetric Encryption
- [x] Public Key & Private Key
- [x] Substitution
- [x] Transposition
- [x] Caesar Cipher
- [x] Caesar Encryption Formula
- [x] Caesar Decryption Formula
- [x] Practice Examples
- [x] Detailed examples, common mistakes, practice, implementation