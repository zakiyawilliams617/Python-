import numpy as np


class HillCipher:
    # letter to nummber mapping (A=0, B=1, ..., Z=25)
    LETTER_TO_NUM = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
        'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
        'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
        'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
    }

    NUM_TO_LETTER = {
        0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G',
        7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N',
        14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U',
        21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'
    }

    def determinant(self, key_matrix):
        """
        Accepts a key matrix and returns its determinant as an integer.
        Uses numpy's linalg.det and rounds to nearest integer.
        """
        det = np.linalg.det(key_matrix)
        return round(det)

    def invertible(self, key_matrix):
        """
        Checks if a key matrix is invertible.
        Returns True if invertible, False otherwise.
        Prints the reason if not invertible.
        """

        # Checks if the matrix is square
        rows = key_matrix.shape[0]
        cols = key_matrix.shape[1]
        if rows != cols:
            print("The matrix is not square.")
            return False

        # Check if determinant is zero
        det = self.determinant(key_matrix)
        if det == 0:
            print("The determinant = 0.")
            return False

        print("The matrix is invertible.")
        return True

    def mod_inverse(self, determinant, modulus):
        """
        Accepts a determinant and a modulus.
        Returns the modular multiplicative inverse of determinant mod modulus.
        Uses an interative method checking values from 1 to modulus-1.
        """
        # Normalize determinant to be positive within modulus range
        det_mod = determinant % modulus
        i = 1
        while i < modulus:
            if (det_mod * i) % modulus == 1:
                return i
            i = i + 1
        return None

    def encode(self, str_):
        """
        Accepts a plaintext string and returns a list of 2x1 NumPy 
        column vectors representingts the encoded message.
        Each pair of characters becomes one column vector.
        """
        encoded_list = []
        i = 0
        while i < len(str_):
            num1 = self.LETTER_TO_NUM[str_[i]]
            num2 = self.LETTER_TO_NUM[str_[i + 1]]
            vector = np.array([[num1], [num2]])
            encoded_list.append(vector)
            i = i + 2
        return encoded_list

    def decode(self, numeric_vectors):
        """
        Accepts a list of 2x1 NumPy column vectors (numeric) and
        returns the decoded plaintext string.
        """
        result = ""
        i = 0
        while i < len(numeric_vectors):
            vec = numeric_vectors[i]
            result = result + self.NUM_TO_LETTER[int(vec[0][0])]
            result = result + self.NUM_TO_LETTER[int(vec[1][0])]
            i = i + 1
        return result

    def encrypt(self, plaintext_vector, key):
        """
        Accepts a single 2x1 plaintext column vector and an encryption key matrix
        Returns the encrypted 2x1 ciphertext column vector (mod 26).
        C = K x P mod m
        """
        modulus = 26
        result = np.matmul(key, plaintext_vector)
        # Apply mod 26 element wise without using dunder methods
        rows = result.shape[0]
        i = 0
        while i < rows:
            result[i][0] = result[i][0] % modulus
            i = i + 1
        return result

    def get_decryption_key(self, key):
        """
        Accepts an encryption key matrix.
        Returns the corresponding decryption key matrix (mod 26).
        K_inv = dev_inv * adjugate(K) mod 26
        """
        modulus = 26
        det = self.determinant(key)
        det_inv = self.mod_inverse(det, modulus)

        # Build adjugate (for 2x2: swap diagonal, negate off diagonal)
        a = int(key[0][0])
        b = int(key[0][1])
        c = int(key[1][0])
        d = int(key[1][1])

        adjugate = np.array([[d, -b], [-c, a]])

        # Multiple by modular inverse of determinant and take mod 26
        rows = adjugate.shape[0]
        cols = adjugate.shape[1]
        decryption_key = np.zeros((rows, cols), dtype=int)
        i = 0
        while i < rows:
            j = 0
            while j < cols:
                decryption_key[i][j] = (det_inv * adjugate[i][j]) % modulus
                j = j + 1
            i = i + 1

        return decryption_key

    def decrypt(self, ciphertext_vector, key):
        """
        Accepts a single 2x1 ciphertext column vector and a decryption key matrix.
        Returns the decrypted 2x1 plaintext column vector (mod 26).
        P = K_inv x C mod m
        """
        modulus = 26
        result = np.matmul(key, ciphertext_vector)
        rows = result.shape[0]
        i = 0
        while i < rows:
            result[i][0] = result[i][0] % modulus
            i = i + 1
        return result
