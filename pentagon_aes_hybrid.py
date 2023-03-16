from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class PentagonAESHybrid:
    def __init__(self, key, rounds=14):
        self.key = key
        self.rounds = rounds

    def encrypt(self, plaintext):
        plaintext_bytes = plaintext.encode('utf-8')
        padded_plaintext = pad(plaintext_bytes, 16)
        nonce = get_random_bytes(16)
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce, mac_len=16)
        ciphertext, tag = cipher.encrypt_and_digest(padded_plaintext)
        return nonce + tag + ciphertext

    def decrypt(self, encrypted_data):
        nonce = encrypted_data[:16]
        tag = encrypted_data[16:32]
        ciphertext = encrypted_data[32:]
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce, mac_len=16)
        decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
        return unpad(decrypted_data, 16).decode('utf-8')

