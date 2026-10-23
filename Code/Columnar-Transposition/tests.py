import unittest

from columnar_decryption import decrypt
from columnar_encryption import encrypt


class ColumnarTranspositionTests(unittest.TestCase):
    def test_first_lecture_example(self):
        key = [4, 2, 3, 1, 5]
        ciphertext = "oinaftImnro"
        self.assertEqual(encrypt("Information", key), ciphertext)
        self.assertEqual(decrypt(ciphertext, key), "Information")

    def test_second_lecture_example(self):
        key = [6, 5, 4, 2, 1, 3]
        ciphertext = "mroteiesnettefcMae"
        self.assertEqual(encrypt("Meet me after section", key), ciphertext)
        self.assertEqual(decrypt(ciphertext, key), "Meetmeaftersection")

    def test_round_trip_removes_whitespace(self):
        plaintext = "This is a transposition example"
        ciphertext = encrypt(plaintext, [3, 1, 4, 2])
        recovered = decrypt(ciphertext, [3, 1, 4, 2])
        self.assertEqual(recovered, "Thisisatranspositionexample")

    def test_complete_rows(self):
        key = [3, 1, 2]
        self.assertEqual(encrypt("ABCDEFGHI", key), "BEHCFIADG")
        self.assertEqual(decrypt("BEHCFIADG", key), "ABCDEFGHI")

    def test_incomplete_final_row(self):
        key = [3, 1, 2, 4]
        ciphertext = encrypt("ABCDEFG", key)
        self.assertEqual(ciphertext, "BFCGAED")
        self.assertEqual(decrypt(ciphertext, key), "ABCDEFG")

    def test_single_column_key(self):
        self.assertEqual(encrypt("Meet me", [1]), "Meetme")
        self.assertEqual(decrypt("Meetme", [1]), "Meetme")

    def test_empty_plaintext(self):
        self.assertEqual(encrypt("", [2, 1]), "")
        self.assertEqual(decrypt("", [2, 1]), "")

    def test_rejects_invalid_keys(self):
        invalid_keys = ([], [1, 1], [0], [-1], [1, 0], [True], "2 1")
        for key in invalid_keys:
            with self.subTest(key=key):
                with self.assertRaises(ValueError):
                    encrypt("MESSAGE", key)
                with self.assertRaises(ValueError):
                    decrypt("MESSAGE", key)

    def test_rejects_non_string_text(self):
        with self.assertRaisesRegex(ValueError, "Plaintext must be a string"):
            encrypt(None, [1])
        with self.assertRaisesRegex(ValueError, "Ciphertext must be a string"):
            decrypt(None, [1])


if __name__ == "__main__":
    unittest.main()
