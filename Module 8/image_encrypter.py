from PIL import Image
from lfsr import LFSR  # import LFSR class from use in Image Encrypter


class ImageEncrypter:
    # initialize in ImageEncrypter object with an LFSR and image file name
    def __init__(self, lfsr: LFSR, file_name: str):
        self.lfsr = lfsr
        self.file_name = file_name
        self.image = None
        self.pixels = None

    # open the image specified by "file_name" in the constructor
    def open_image(self):
        self.image = Image.open(self.file_name).convert('RGB')

    # calls open_image()
    # converts the image to a 2D array of R, G, B triples
    def pixelate(self):
        self.open_image()
        width, height = self.image.size
        raw = self.image.load()
        self.pixels = []
        i = 0
        while i < height:
            row = []
            j = 0
            while j < width:
                pixel = raw[j, i]
                row.append([pixel[0], pixel[1], pixel[2]])
                j = j + 1
            self.pixels.append(row)
            i = i + 1

    # encrypts the 2D pixelated "image" returned from pixelate()
    # returns the encrypted 2D array
    def encrypt(self):
        i = 0
        while i < len(self.pixels):
            j = 0
            while j < len(self.pixels[i]):
                # step LFSR adn use resulting state as an 8 bit random value for red
                self.lfsr.step()
                r_rand = int(self.lfsr.state, 2)
                self.pixels[i][j][0] = self.pixels[i][j][0] ^ r_rand

                # step LFSR and use resulting  state as an 8 bit random value  for green
                self.lfsr.step()
                g_rand = int(self.lfsr.state, 2)
                self.pixels[i][j][1] = self.pixels[i][j][1] ^ g_rand

                # step LFSR and use resulting  state as an 8 bit random value  for blue
                self.lfsr.step()
                b_rand = int(self.lfsr.state, 2)
                self.pixels[i][j][2] = self.pixels[i][j][2] ^ b_rand

                j = j + 1
            i = i + 1
        return self.pixels

    # converts the encrypted 2D pixelated image into an image
    # names it (file_name)_(encrypted/decrypted).png
    def save_image(self, file_name: str):
        width = len(self.pixels[0])
        height = len(self.pixels)
        new_image = Image.new('RGB', (width, height))
        raw = new_image.load()
        i = 0
        while i < height:
            j = 0
            while j < width:
                raw[j, i] = (self.pixels[i][j][0], self.pixels[i]
                             [j][1], self.pixels[i][j][2])
                j = j + 1
            i = i + 1
        new_image.save(file_name)

# invokes ImageEncrypter and encrypts/decrypts image
# saves the result to a file


def main():
    # Encrypt the image
    lfsr_enc = LFSR("10011010", 5)
    encrypter = ImageEncrypter(lfsr_enc, "football.png")
    encrypter.pixelate()
    # print("First pixel before encrypt:", encrypter.pixels[0][0])
    encrypter.encrypt()
    # print("First pixel after encrypt:", encrypter.pixels[0][0])
    encrypter.save_image("football_encrypted.png")

    # Decrypt the image
    lfsr_dec = LFSR("10011010", 5)
    decrypter = ImageEncrypter(lfsr_dec, "football_encrypted.png")
    decrypter.pixelate()
    # print("First pixel of encrypted image read back:", decrypter.pixels[0][0])
    decrypter.encrypt()
    # print("First pixel after decrypt:", decrypter.pixels[0][0])
    decrypter.save_image("football_decrypted.png")


if __name__ == '__main__':
    main()
