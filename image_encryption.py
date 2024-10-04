from PIL import Image
import random

class ImageEncryptor:
    def __init__(self, key):
        self.key = key

    def encrypt(self, image_path, output_path):
       
        img = Image.open(image_path)
        pixels = img.load()

        
        width, height = img.size
        random.seed(self.key)  
        
        
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                
                r, b = b, r
                
                r = (r + self.key) % 256
                g = (g + self.key) % 256
                b = (b + self.key) % 256
                pixels[x, y] = (r, g, b)
        
        
        img.save(output_path)
        print(f"Image encrypted and saved as {output_path}")

    def decrypt(self, image_path, output_path):
        
        img = Image.open(image_path)
        pixels = img.load()

       
        width, height = img.size
        random.seed(self.key) 

        
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                
                r = (r - self.key) % 256
                g = (g - self.key) % 256
                b = (b - self.key) % 256
                
                r, b = b, r
                pixels[x, y] = (r, g, b)
        
        
        img.save(output_path)
        print(f"Image decrypted and saved as {output_path}")


key = 12345  
encryptor = ImageEncryptor(key)


encryptor.encrypt('/Users/praveenshankar/Documents/input_image.png', 'encrypted_image.jpg')



encryptor.decrypt('encrypted_image.jpg', 'decrypted_image.jpg')
