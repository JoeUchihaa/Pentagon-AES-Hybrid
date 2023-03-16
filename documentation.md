# Pentagon-AES Hybrid Encryption Method Documentation

Pentagon-AES Hybrid is an experimental, educational encryption algorithm inspired by the Pentagon shape and AES, featuring a 512-bit key and 10-25 iterative rounds. This documentation provides an overview of the algorithm steps, key generation, data preparation, data assignment, data transformation, final round, and decryption process.

**Note:** This encryption method is for educational purposes and not recommended for securing sensitive information in real-world applications. Use established encryption algorithms like AES, RSA, or ECC instead.

## Algorithm Steps

1. **Key Generation**: Generate a 512-bit key using a secure random number generator. This key will be used for AES operations.

2. **Data Preparation**: Convert the input plaintext message into bytes and pad it to ensure the length is a multiple of 16 bytes (128 bits), as required by the AES algorithm.

3. **Data Assignment**: Divide the padded plaintext data into 5 equal parts, assigning each part to one of the 5 triangles (g1, g2, g3, g4, g5) in the Pentagon.

4. **Data Transformation**: Perform AES operations, including SubBytes, ShiftRows, MixColumns, and AddRoundKey, on each of the 5 data parts. Repeat the process for the specified number of iterative rounds (10-25).

5. **Final Round**: Combine the transformed data from the 5 triangles to form the final ciphertext.

6. **Decryption Process**: Reverse the encryption process by separating the data parts, performing the inverse AES operations for the specified number of rounds, reassembling the data, and removing the padding.

## Python Implementation

The Python implementation of the Pentagon-AES Hybrid Encryption Method uses the PyCryptodome library to handle the underlying AES operations. The `PentagonAESHybrid` class provides `encrypt` and `decrypt` methods for processing plaintext messages and encrypted data.

For example usage and further details, please refer to the `examples.py` file in the GitHub repository.

## Testing

The `tests.py` file in the repository contains unit tests to ensure the correctness and reliability of the Pentagon-AES Hybrid implementation. You can run the tests using the `unittest` framework provided by Python.
