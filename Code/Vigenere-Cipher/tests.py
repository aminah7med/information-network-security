"""Basic verification tests for the Vigenere materials.

Run from the repository root:
    python Code/Vigenere-Cipher/tests.py
"""
import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vigenere_decryption import decrypt  # noqa: E402
from vigenere_encryption import encrypt  # noqa: E402


def run_section(plain, key):
    """Run the instructor's script with the given input and return its output."""
    result = subprocess.run(
        [sys.executable, os.path.join(HERE, "vigenere_section.py")],
        input=f"{plain}\n{key}\n",
        capture_output=True,
        text=True,
        check=True,
    )
    # The prompts are printed without a newline, so keep only the result part.
    return "Ciphertext:" + result.stdout.split("Ciphertext:")[-1].rstrip("\n")


class TestEncryption(unittest.TestCase):
    def test_known_cases(self):
        self.assertEqual(encrypt("cat", "dog"), "foz")
        self.assertEqual(encrypt("bad", "abc"), "bbf")
        self.assertEqual(encrypt("hello", "key"), "rijvs")
        self.assertEqual(encrypt("attackatdawn", "lemon"), "lxfopvefrnhr")

    def test_key_repetition(self):
        # Repeating the key by hand must not change the result.
        self.assertEqual(encrypt("hello", "key"), encrypt("hello", "keyke"))

    def test_same_plain_letter_different_cipher_letters(self):
        # The two 'l' letters in "hello" meet different key letters.
        self.assertEqual(encrypt("hello", "key")[2], "j")
        self.assertEqual(encrypt("hello", "key")[3], "v")

    def test_key_a_changes_nothing(self):
        self.assertEqual(encrypt("hello", "a"), "hello")

    def test_invalid_input_rejected(self):
        with self.assertRaises(ValueError):
            encrypt("hello", "")
        with self.assertRaises(ValueError):
            encrypt("Hello", "key")
        with self.assertRaises(ValueError):
            encrypt("hello world", "key")
        with self.assertRaises(ValueError):
            encrypt("hello", "k3y")


class TestDecryption(unittest.TestCase):
    def test_known_cases(self):
        self.assertEqual(decrypt("foz", "dog"), "cat")
        self.assertEqual(decrypt("bbf", "abc"), "bad")
        self.assertEqual(decrypt("lxfopvefrnhr", "lemon"), "attackatdawn")

    def test_round_trip(self):
        for plain, key in [("hello", "key"), ("network", "net"), ("zzz", "z")]:
            self.assertEqual(decrypt(encrypt(plain, key), key), plain)

    def test_wrap_around_negative_difference(self):
        # c = 'a' (0), k = 'd' (3): (0 - 3) % 26 = 23 -> 'x'
        self.assertEqual(decrypt("a", "d"), "x")


class TestSectionCode(unittest.TestCase):
    def test_matches_practice_encryption(self):
        for plain, key in [("cat", "dog"), ("hello", "key"), ("attackatdawn", "lemon")]:
            self.assertEqual(run_section(plain, key), "Ciphertext: " + encrypt(plain, key))


if __name__ == "__main__":
    unittest.main(verbosity=2)
