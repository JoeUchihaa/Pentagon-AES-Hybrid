import unittest
from Crypto.Random import get_random_bytes
from pentagon_aes_hybrid import PentagonAESHybrid

class TestPentagonAESHybrid(unittest.TestCase):

    def setUp(self):
        self.key = get_random_bytes(64)
        self.pentagon_aes = PentagonAESHybrid(self.key)
        self.plaintext = "This is a test message."

    def test_encryption_decryption(self):
        encrypted_data = self.pentagon_aes.encrypt(self.plaintext)
        decrypted_data = self.pentagon_aes.decrypt(encrypted_data)
        self.assertEqual(self.plaintext, decrypted_data)

    def test_encryption_decryption_empty_string(self):
        plaintext = ""
        encrypted_data = self.pentagon_aes.encrypt(plaintext)
        decrypted_data = self.pentagon_aes.decrypt(encrypted_data)
        self.assertEqual(plaintext, decrypted_data)

if __name__ == '__main__':
    unittest.main()
