import unittest

from hill_decryption import decrypt, inverse_key_matrix
from hill_encryption import encrypt


class HillCipherTests(unittest.TestCase):
    def setUp(self):
        self.key = [[3, 3], [2, 5]]

    def test_known_example_encryption(self):
        self.assertEqual(encrypt("HELP", self.key), "HIAT")

    def test_known_example_decryption(self):
        self.assertEqual(decrypt("HIAT", self.key), "HELP")

    def test_round_trip_with_padding(self):
        prepared_plaintext = "CATX"
        ciphertext = encrypt("CAT", self.key)
        self.assertEqual(len(ciphertext) % len(self.key), 0)
        self.assertEqual(decrypt(ciphertext, self.key), prepared_plaintext)

    def test_encryption_is_case_insensitive(self):
        self.assertEqual(encrypt("help", self.key), "HIAT")

    def test_empty_plaintext(self):
        self.assertEqual(encrypt("", self.key), "")
        self.assertEqual(decrypt("", self.key), "")

    def test_rejects_non_square_key(self):
        with self.assertRaisesRegex(ValueError, "square"):
            encrypt("HELP", [[1, 2, 3], [4, 5, 6]])

    def test_rejects_empty_key(self):
        with self.assertRaisesRegex(ValueError, "non-empty square"):
            encrypt("HELP", [])

    def test_rejects_non_integer_key_entries(self):
        with self.assertRaisesRegex(ValueError, "integers"):
            encrypt("HELP", [[1, 2], [3, 2.5]])

    def test_rejects_out_of_range_key_entries(self):
        with self.assertRaisesRegex(ValueError, "0 to 25"):
            encrypt("HELP", [[1, 2], [3, 26]])

    def test_rejects_key_not_invertible_modulo_26(self):
        with self.assertRaisesRegex(ValueError, "not invertible modulo 26"):
            inverse_key_matrix([[2, 4], [2, 6]])

    def test_rejects_ciphertext_with_incomplete_block(self):
        with self.assertRaisesRegex(ValueError, "divisible"):
            decrypt("ABC", self.key)

    def test_rejects_non_alphabetic_input(self):
        with self.assertRaisesRegex(ValueError, "English letters"):
            encrypt("HELLO!", self.key)


if __name__ == "__main__":
    unittest.main()
