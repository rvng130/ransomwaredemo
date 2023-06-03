import sys
import string
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode


filename = input("Enter filename to decrypt:  ") #example.txt.encrypted
filename2 = input("Enter decryption key file:  ") #example.txt.ID.key


# decrypt file with the given key
def decrypt_file(filename, key):
    with open(filename, "rb") as f:
        ciphertext = f.read()


    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
   
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    except ValueError as e:
        print("Padding error:", e)
        return

    print(plaintext)
    # write decrypted file (original file)
    with open(filename[:-10], "wb") as f:
        f.write(plaintext)


    print(f"{filename} decrypted successfully!")


if (__name__ == '__main__'):
    with open(filename2, "rb") as f:
        key = f.read()
    decrypt_file(filename, key)
