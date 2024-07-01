import hashlib
import time
import os


class LicenseManager:
    def __init__(self, secret_key, validity_period_days=30, hash_file_path="hash.txt"):
        self.secret_key = secret_key
        self.validity_period_days = validity_period_days
        self.hash_file_path = hash_file_path

    def generate_timed_hash(self):
        current_time = int(time.time())
        validity_period_seconds = self.validity_period_days * 24 * 60 * 60
        expiry_time = current_time + validity_period_seconds
        data_to_hash = f"{self.secret_key}{expiry_time}"
        hash_object = hashlib.sha256(data_to_hash.encode())
        hash_with_time = f"{hash_object.hexdigest()}:{expiry_time}"
        return hash_with_time

    def is_timed_hash_valid(self, hash_with_time):
        try:
            hash_value, expiry_time_str = hash_with_time.split(':')
            expiry_time = int(expiry_time_str)
            current_time = int(time.time())

            if current_time > expiry_time:
                return False  # El hash ha expirado

            data_to_hash = f"{self.secret_key}{expiry_time}"
            expected_hash_object = hashlib.sha256(data_to_hash.encode())
            expected_hash_value = expected_hash_object.hexdigest()

            return expected_hash_value == hash_value
        except ValueError:
            return False  # Formato inválido del hash

    def check_license(self):
        if not os.path.exists(self.hash_file_path):
            print("El archivo de hash no existe. Por favor, contacte al soporte.")
            return False

        with open(self.hash_file_path, "r") as file:
            user_hash = file.read().strip()

        if self.is_timed_hash_valid(user_hash):
            return True
        else:
            print("Clave inválida o expirada. Por favor, contacte al soporte.")
            return False