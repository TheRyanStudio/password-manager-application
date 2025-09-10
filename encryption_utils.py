import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from argon2 import PasswordHasher, exceptions

class EncryptionUtils:
    def __init__(self, master_password=None, salt= None, fernet=None):
        # Initialize with either a master password (derive a new key) 
        # Or an existing Fernet key (for users already logged in)
        if fernet:
            self.fernet = fernet
        else:
            #Use argon2 for master password hashing
            self.ph = PasswordHasher()
            self.salt = salt if salt else os.urandom(16)
            self.master_password = master_password
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32, salt=self.salt, iterations=1_200_000,
            )
            self.key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
            self.fernet = Fernet(self.key)

    def hash_password(self):
        password_hash = self.ph.hash(self.master_password)
        return password_hash 

    def verify_password(self, hashed_password):
        # True if master_password matches hashed_password, else False
        try:
            return self.ph.verify(hashed_password, self.master_password)
        except exceptions.VerifyMismatchError:
            return False


    def encrypt(self, data: dict):
        encrypted_data = {}

        # Encrypts each value with fernet and returns the encrypted data 
        for key in data:
            encrypted_data[key] = self.fernet.encrypt(data[key].encode())
        return encrypted_data
    
    def decrypt(self, data: dict):
        decrypted_data = {}

        # Decrypts the values with fernet and returns the decryted data
        for key, value in data.items():
            # Only decrypts what was encrypted, which is organization, username and password
            if key in ("organization", "username", "password"): 
                decrypted_data[key] = self.fernet.decrypt(value).decode()
            else:
                decrypted_data[key] = value 
        return decrypted_data

