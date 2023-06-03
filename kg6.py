import os
from Crypto.PublicKey import RSA


if not os.path.exists("Solutions"):
    os.makedirs("Solutions")


key = RSA.generate(1024)


# private key
with open("Solutions/d.key", "wb") as f:
    f.write(key.export_key())


# public key
with open("Solutions/e.key", "wb") as f:
    f.write(key.publickey().export_key())
