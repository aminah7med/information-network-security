import unittest

from rail_fence_decryption_supplementary import decrypt
from rail_fence_encryption_supplementary import encrypt


class RailFenceCipherTests(unittest.TestCase):
    def test_lecture_example_encryption(self):
        self.assertEqual(encrypt("Information", 3), "Irinomtofan")

    def test_lecture_example_decryption(self):
        self.assertEqual(decrypt("Irinomtofan", 3), "Information")

    def test_round_trip(self):
        plaintext = "We are learning transposition ciphers!"
        self.assertEqual(decrypt(encrypt(plaintext, 3), 3), plaintext)

    def test_one_rail_leaves_text_unchanged(self):
        self.assertEqual(encrypt("Information", 1), "Information")
        self.assertEqual(decrypt("Information", 1), "Information")

    def test_key_greater_than_or_equal_to_text_length(self):
        for plaintext, key in (("CAT", 3), ("CAT", 5)):
            with self.subTest(plaintext=plaintext, key=key):
                self.assertEqual(encrypt(plaintext, key), plaintext)
                self.assertEqual(decrypt(plaintext, key), plaintext)

    def test_short_plaintexts(self):
        for plaintext in ("A", "AB"):
            with self.subTest(plaintext=plaintext):
                ciphertext = encrypt(plaintext, 3)
                self.assertEqual(ciphertext, plaintext)
                self.assertEqual(decrypt(ciphertext, 3), plaintext)

    def test_empty_text(self):
        self.assertEqual(encrypt("", 3), "")
        self.assertEqual(decrypt("", 3), "")

    def test_rejects_invalid_keys(self):
        for key in (0, -1, True, 2.5, "3"):
            with self.subTest(key=key):
                with self.assertRaisesRegex(ValueError, "positive integer"):
                    encrypt("Information", key)
                with self.assertRaisesRegex(ValueError, "positive integer"):
                    decrypt("Irinomtofan", key)

    def test_rejects_non_string_text(self):
        with self.assertRaisesRegex(ValueError, "Plaintext must be a string"):
            encrypt(None, 3)
        with self.assertRaisesRegex(ValueError, "Ciphertext must be a string"):
            decrypt(None, 3)


if __name__ == "__main__":
    unittest.main()
