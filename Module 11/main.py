import numpy as np
from hillcipher import HillCipher

if __name__ == "__main__":

    cipher = HillCipher()

    # Input 1: 3x2 key matrix (not square, should fail the invertbility check)
    plaintext_1 = "ATTACKATDAWN"
    key_1 = np.array([[19, 8, 4],
                      [3, 12, 7]])

    modulus = 26

    result = cipher.invertible(key_1)
    if result:
        encoded_1 = cipher.encode(plaintext_1)
        print("Plaintext:", plaintext_1)
        print("Plaintext column vectors:", encoded_1)

        ciphertext_vectors_1 = []
        i = 0
        while i < len(encoded_1):
            c_vec = cipher.encrypt(encoded_1[i], key_1)
            ciphertext_vectors_1.append(c_vec)
            i = i + 1

        ciphertext_str_1 = cipher.decode(ciphertext_vectors_1)
        print("Ciphertext:", ciphertext_str_1)
        print("Ciphertext column vectors:", ciphertext_vectors_1)

        dec_key_1 = cipher.get_decryption_key(key_1)
        decrypted_vectors_1 = []
        i = 0
        while i < len(ciphertext_vectors_1):
            p_vec = cipher.decrypt(ciphertext_vectors_1[i], dec_key_1)
            decrypted_vectors_1. append(p_vec)
            i = i + 1

        decrypted_str_1 = cipher.decode(decrypted_vectors_1)
        print("Plaintext:,", decrypted_str_1)
        print("Plaintext colum vectors:", decrypted_vectors_1)

    print()

    # Input 2: 2x2 key matrix invertible
    plaintext_2 = "ATTACKATDAWN"
    key_2 = np.array([[7, 8],
                      [11, 11]])

    result = cipher.invertible(key_2)
    if result:
        encoded_2 = cipher.encode(plaintext_2)
        print("Plaintext:", plaintext_2)
        print("Plaintext column vectors:", encoded_2)

        ciphertext_vectors_2 = []
        i = 0
        while i < len(encoded_2):
            c_vec = cipher.encrypt(encoded_2[i], key_2)
            ciphertext_vectors_2.append(c_vec)
            i = i + 1

        ciphertext_str_2 = cipher.decode(ciphertext_vectors_2)
        print("Ciphertext:", ciphertext_str_2)
        print("Ciphertext column vectors:", ciphertext_vectors_2)

        dec_key_2 = cipher.get_decryption_key(key_2)
        decrypted_vectors_2 = []
        i = 0
        while i < len(ciphertext_vectors_2):
            p_vec = cipher.decrypt(ciphertext_vectors_2[i], dec_key_2)
            decrypted_vectors_2.append(p_vec)
            i = i + 1

        decrypted_str_2 = cipher.decode(decrypted_vectors_2)
        print("Plaintext:", decrypted_str_2)
        print("Plaintext column vectors:", decrypted_vectors_2)

    print()

    # Input 3: 2x2 key matrix, determinant = 0 (should fail)
    plaintext_3 = "ATTACKATDAWN"
    key_3 = np.array([[5, 15],
                     [4, 12]])

    result = cipher.invertible(key_3)
    if result:
        encoded_3 = cipher.encode(plaintext_3)
        print("Plaintext:", plaintext_3)
        print("Plaintext column vectors:", encoded_3)

        ciphertext_vectors_3 = []
        i = 0
        while i < len(encoded_3):
            c_vec = cipher.encrypt(encoded_3[i], key_3)
            ciphertext_vectors_3.append(c_vec)
            i = i + 1

        ciphertext_str_3 = cipher.decode(ciphertext_vectors_3)
        print("Ciphertext:", ciphertext_str_3)
        print("Ciphertext column vectors:", ciphertext_vectors_3)

        dec_key_3 = cipher.get_decryption_key(key_3)
        decrypted_vectors_3 = []
        i = 0
        while i < len(ciphertext_vectors_3):
            p_vec = cipher.decrypt(ciphertext_vectors_3[i], dec_key_3)
            decrypted_vectors_3.append(p_vec)
            i = i + 1

        decrypted_str_3 = cipher.decode(decrypted_vectors_3)
        print("Plaintext:", decrypted_str_3)
        print("Plaintext column vectors:", decrypted_vectors_3)
