from cryptography.fernet import Fernet

# This code that is commented out generates a key to be used in the key.txt file

# import base64
# import os
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


# Un-comment and run to generate a key, then place it inside of key.txt without the b'' part.
# def gen_pass():
#     password_provided = 'keycode' # REPLACE KEYCODE with specific password
#     password = password_provided.encode()

#     salt = b'\xce\xbb\xde\xe0\xd5\\\xf2\x13\xe8\xce\xff\xa8\x91\xf3\xe8\xd8'
#     kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
#     key = base64.urlsafe_b64encode(kdf.derive(password))
#     print(key)

# gen_pass()

def encrypt(x): # Encrypts text based off of the key given
    encoded = x.encode()
    file = open('key/key.txt', 'r')
    key = file.read()
    file.close()
    f = Fernet(key)
    encrypted = f.encrypt(encoded)
    return encrypted

def decrypt(x): # Decrypts text based off of the key given
    file = open('key/key.txt', 'r')
    key = file.read()
    file.close()
    f = Fernet(key)
    decrypted = f.decrypt(x)
    decrypted = decrypted.decode()
    return decrypted
