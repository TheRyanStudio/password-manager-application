from argon2.exceptions import VerifyMismatchError, InvalidHash
from argon2 import PasswordHasher


class Authenticate: 

    def __init__(self):
        self.ph = PasswordHasher()

    def verify_password(self, stored_hash, master_password):
        try:
            # Returns True if the password matches
            # Raises an exception if the password doesn't match
            self.ph.verify(stored_hash, master_password)
            return True
        except VerifyMismatchError:
            # Password does not match
            return False
        except InvalidHash:
            # The stored hash has an invalid format
            print("Invalid hash format. The hash may be corrupted.")
            return False