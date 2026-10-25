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
├── README.md
├── Caesar/
│   └── notes.md
├── Columnar-Transposition/
│   └── README.md
├── Hill/
│   └── README.md
├── Playfair/
│   └── notes.md
├── Rail-Fence/
│   └── README.md
└── Vigenere/
    ├── notes.md
    └── study-guide.md
Code/
├── README.md
├── Caesar-Cipher/
│   ├── README.md
│   ├── caesar_encryption.py
│   ├── caesar_decryption.py
│   └── tests.py
├── Columnar-Transposition/
│   ├── README.md
│   ├── columnar_encryption_supplementary.py
│   ├── columnar_decryption_supplementary.py
│   └── tests_supplementary.py
├── Complex-Scheme/
│   ├── README.md
│   └── complex_scheme.py
├── Hill-Cipher/
│   ├── README.md
│   ├── hill_encryption.py
│   ├── hill_encryption_supplementary.py
│   ├── hill_decryption_supplementary.py
│   └── tests_supplementary.py
├── Playfair-Cipher/
│   ├── README.md
│   ├── Playfair-Cipher.py
│   └── Playfair-Cipher-supplementary.py
├── Rail-Fence-Cipher/
│   ├── README.md
│   ├── rail_fence_encryption.py
│   ├── rail_fence_encryption_supplementary.py
│   ├── rail_fence_decryption_supplementary.py
│   └── tests_supplementary.py
└── Vigenere-Cipher/
    ├── README.md
    ├── vigenere_encryption.py
    ├── vigenere_section.py
    ├── vigenere_decryption.py
    └── tests_supplementary.py
Lectures/
├── README.md
├── Lec-01/ (notes.md, study-guide.md, images/README.md, source/Lec-01.pdf)
├── Lec-02/ (notes.md, study-guide.md, images/README.md, source/Lec-02.pdf)
└── Lec-03/ (notes.md, study-guide.md, images/README.md, images/1.png, images/2.png, images/3.png)
Problems/
├── README.md
├── Caesar/README.md
├── Encryption/README.md
├── Playfair/README.md
└── Vigenere/README.md
Resources/
├── README.md
└── William Stallings-Cryptography and Network Security_ Principles and Practice (6th Edition).pdf
Solutions/
├── README.md
├── Caesar/README.md
├── Playfair/README.md
└── Vigenere/README.md
Progress.md
```

The tree lists the repository's current cipher folders. Problem sets and
worked solutions are present for Caesar, Vigenere, and Playfair; there is not
currently a Hill problem or solution folder.

## Algorithms and Implementations

| Algorithm | Documentation | Implementation | Tests |
|---|---|---|---|
| Caesar Cipher | [Algorithm notes](Algorithms/Caesar/notes.md) | [Lecture encryption](Code/Caesar-Cipher/caesar_encryption.py) · [Supplementary decryption](Code/Caesar-Cipher/caesar_decryption.py) | [Console checks](Code/Caesar-Cipher/tests.py) |
| Vigenère Cipher | [Algorithm notes](Algorithms/Vigenere/notes.md) · [Study guide](Algorithms/Vigenere/study-guide.md) | [Lecture encryption](Code/Vigenere-Cipher/vigenere_encryption.py) · [Supplementary lowercase version](Code/Vigenere-Cipher/vigenere_section.py) · [Supplementary decryption](Code/Vigenere-Cipher/vigenere_decryption.py) | [Supplementary checks](Code/Vigenere-Cipher/tests_supplementary.py) |
| Playfair Cipher | [Algorithm notes](Algorithms/Playfair/notes.md) | [Lecture script](Code/Playfair-Cipher/Playfair-Cipher.py) | No test file is currently provided |
| Hill Cipher | [Algorithm guide](Algorithms/Hill/README.md) | [Lecture encryption](Code/Hill-Cipher/hill_encryption.py) · [Supplementary encryption/decryption](Code/Hill-Cipher/hill_encryption_supplementary.py) | [Supplementary tests](Code/Hill-Cipher/tests_supplementary.py) |
| Rail Fence Cipher | [Algorithm guide](Algorithms/Rail-Fence/README.md) | [Lecture two-rail example](Code/Rail-Fence-Cipher/rail_fence_encryption.py) · [Supplementary general encryption/decryption](Code/Rail-Fence-Cipher/rail_fence_encryption_supplementary.py) | [Supplementary tests](Code/Rail-Fence-Cipher/tests_supplementary.py) |
| Columnar Transposition | [Algorithm guide](Algorithms/Columnar-Transposition/README.md) | [Complex Scheme lecture script](Code/Complex-Scheme/complex_scheme.py) · [Supplementary general encryption/decryption](Code/Columnar-Transposition/columnar_encryption_supplementary.py) | [Supplementary tests](Code/Columnar-Transposition/tests_supplementary.py) |
| Complex Scheme | — | [Lecture script](Code/Complex-Scheme/complex_scheme.py) | No test file is currently provided |

For additional code details, see the [Caesar](Code/Caesar-Cipher/README.md),
[Vigenère](Code/Vigenere-Cipher/README.md), [Playfair](Code/Playfair-Cipher/README.md),
and [Hill](Code/Hill-Cipher/README.md) code guides, plus the [Rail Fence](Code/Rail-Fence-Cipher/README.md),
[Columnar Transposition](Code/Columnar-Transposition/README.md), and
[Complex Scheme](Code/Complex-Scheme/README.md) guides. Lecture scripts are
kept distinct from supplementary implementations; no original lecture
decryption files were found for Caesar, Vigenère, Hill, or Rail Fence.

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
python Code/Vigenere-Cipher/vigenere_encryption.py
python Code/Playfair-Cipher/Playfair-Cipher.py
python Code/Hill-Cipher/hill_encryption.py
python Code/Rail-Fence-Cipher/rail_fence_encryption.py
python Code/Complex-Scheme/complex_scheme.py
```

Interactive lecture scripts prompt for input; the Rail Fence and Complex
Scheme lecture examples run their fixed demonstrations directly. On some
systems, use `python3` instead of `python`.

## Testing

Run the available test/check scripts from the repository root:

```bash
python Code/Caesar-Cipher/tests.py
python Code/Vigenere-Cipher/tests_supplementary.py
python -m unittest discover -s Code/Hill-Cipher -p tests_supplementary.py
python -m unittest discover -s Code/Rail-Fence-Cipher -p tests_supplementary.py
python -m unittest discover -s Code/Columnar-Transposition -p tests_supplementary.py
```

The Caesar and Vigenère checks are print-based scripts. Hill, Rail Fence, and
Columnar tests apply to the separately labeled supplementary implementations,
not the lecture scripts. The Playfair and Complex Scheme folders do not
currently include tests. Install NumPy before running the Hill lecture script.

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
