# Information and Network Security

> A personal initiative to organize course materials and make them easier to access, study, and review.

## About This Repository

This repository organizes my **Information and Network Security** coursework,
including lecture materials, classical cipher explanations and
implementations, practice exercises, reference resources, and learning
progress.

All materials are for educational purposes. They may contain mistakes or
incomplete information, so refer to official course materials and your
instructor's guidance whenever clarification is needed.

**Course under the supervision of Dr. Asmaa Ahmoud.**

## Repository Structure

Theory and algorithm explanations are in `Algorithms/`; executable examples
and tests are in `Code/`.

```text
Algorithms/
├── Caesar/notes.md
├── Hill/README.md
├── Playfair/notes.md
└── Vigenere/{notes.md, study-guide.md}
Code/
├── Caesar-Cipher/{README.md, caesar_encryption.py, caesar_decryption.py, tests.py}
├── Hill-Cipher/{README.md, hill_encryption.py, hill_decryption.py, tests.py}
├── Playfair-Cipher/{README.md, Playfair-Cipher.py}
└── Vigenere-Cipher/{README.md, vigenere_section.py, vigenere_encryption.py,
                     vigenere_decryption.py, tests.py}
Lectures/
├── Lec-01/ (notes, study guide, source scan, images guide)
├── Lec-02/ (notes, study guide, source scan, images guide)
└── Lec-03/ (notes, study guide, images)
Problems/
├── Caesar/
├── Encryption/
├── Playfair/
└── Vigenere/
Resources/ (README.md and course reference PDF)
Solutions/
├── Caesar/
├── Playfair/
└── Vigenere/
Progress.md
```

The tree lists the repository's current cipher folders. Problem sets and
worked solutions are present for Caesar, Vigenere, and Playfair; there is not
currently a Hill problem or solution folder.

## Algorithms and Implementations

| Algorithm | Documentation | Implementation | Tests |
|---|---|---|---|
| Caesar Cipher | [Algorithm notes](Algorithms/Caesar/notes.md) | [Encryption](Code/Caesar-Cipher/caesar_encryption.py) · [Decryption](Code/Caesar-Cipher/caesar_decryption.py) | [Console checks](Code/Caesar-Cipher/tests.py) |
| Vigenère Cipher | [Algorithm notes](Algorithms/Vigenere/notes.md) · [Study guide](Algorithms/Vigenere/study-guide.md) | [Interactive example](Code/Vigenere-Cipher/vigenere_section.py) · [Encryption function](Code/Vigenere-Cipher/vigenere_encryption.py) · [Decryption function](Code/Vigenere-Cipher/vigenere_decryption.py) | [Console checks](Code/Vigenere-Cipher/tests.py) |
| Playfair Cipher | [Algorithm notes](Algorithms/Playfair/notes.md) | [Encryption script](Code/Playfair-Cipher/Playfair-Cipher.py) | No test file is currently provided |
| Hill Cipher | [Algorithm guide and worked example](Algorithms/Hill/README.md) | [Encryption](Code/Hill-Cipher/hill_encryption.py) · [Decryption](Code/Hill-Cipher/hill_decryption.py) | [Unit tests](Code/Hill-Cipher/tests.py) |

For additional code details, see the [Caesar](Code/Caesar-Cipher/README.md),
[Vigenère](Code/Vigenere-Cipher/README.md), [Playfair](Code/Playfair-Cipher/README.md),
and [Hill](Code/Hill-Cipher/README.md) code guides. Vigenère's separate
encryption and decryption files define functions; the interactive example is
`vigenere_section.py`. Playfair currently provides encryption only.

## Getting Started

Clone the repository and move into its directory:

```bash
git clone https://github.com/aminah7med/information-network-security.git
cd information-network-security
```

Browse the folders above, or open the repository in VS Code or a Markdown
editor. Python examples require Python 3 and prompt for input when run. From
the repository root, for example:

```bash
python Code/Caesar-Cipher/caesar_encryption.py
python Code/Caesar-Cipher/caesar_decryption.py
python Code/Vigenere-Cipher/vigenere_section.py
python Code/Playfair-Cipher/Playfair-Cipher.py
python Code/Hill-Cipher/hill_encryption.py
python Code/Hill-Cipher/hill_decryption.py
```

Vigenère's function-based scripts can be imported from Python; they do not
start an interactive session when run directly. On some systems, use
`python3` instead of `python`.

## Testing

Run the available test/check scripts from the repository root:

```bash
python Code/Caesar-Cipher/tests.py
python Code/Vigenere-Cipher/tests.py
python -m unittest discover -s Code/Hill-Cipher -p tests.py
```

The Caesar and Vigenère scripts print expected and actual values for manual
checks. Hill uses Python's built-in `unittest`. The Playfair folder does not
currently include a test file.

## Lectures and Learning Resources

- [Lecture materials index](Lectures/README.md)
- [Lecture 01 notes](Lectures/Lec-01/notes.md) · [Study guide](Lectures/Lec-01/study-guide.md) · [Source scan](Lectures/Lec-01/source/Lec-01.pdf)
- [Lecture 02 notes](Lectures/Lec-02/notes.md) · [Study guide](Lectures/Lec-02/study-guide.md) · [Source scan](Lectures/Lec-02/source/Lec-02.pdf)
- [Lecture 03 notes](Lectures/Lec-03/notes.md) · [Study guide](Lectures/Lec-03/study-guide.md)
- [Problems index](Problems/README.md): [Encryption](Problems/Encryption/README.md), [Caesar](Problems/Caesar/README.md), [Vigenere](Problems/Vigenere/README.md), and [Playfair](Problems/Playfair/README.md)
- [Solutions index](Solutions/README.md): [Caesar](Solutions/Caesar/README.md), [Vigenere](Solutions/Vigenere/README.md), and [Playfair](Solutions/Playfair/README.md)
- [Course resources index](Resources/README.md) · [William Stallings reference PDF](<Resources/William Stallings-Cryptography and Network Security_ Principles and Practice (6th Edition).pdf>)
- [Course progress checklist](Progress.md)

## Contributions and Feedback

This repository is an independent educational effort, and I would be grateful
for any help that makes it more accurate, useful, and organized.

If you notice an error, have a suggestion, want to improve an explanation, or
would like to contribute additional educational material, please feel free
to get in touch.

**Contributions and collaboration are welcome!** I would sincerely appreciate
corrections, suggestions, useful resources, and contributions from fellow
students and anyone interested in improving these materials.

[📧 Contact Me](mailto:a.ahmed2585@su.edu.eg?subject=Information%20and%20Network%20Security%20Repository)

Thank you for helping make these materials better for everyone.
