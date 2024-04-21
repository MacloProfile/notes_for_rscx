import os
from cryptography.fernet import Fernet


class CryptoManager:
    def __init__(self, key_path):
        self.key_path = key_path

    def _load_or_generate_key(self):
        """Загружает ключ шифрования из файла или генерирует новый,
        если файл отсутствует"""
        if os.path.exists(self.key_path):
            with open(self.key_path, "rb") as key_file:
                return key_file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_path, "wb") as key_file:
                key_file.write(key)
            return key

    def set_encryption_key(self, key):
        """Устанавливает ключ шифрования и сохраняет его в файл"""
        with open(self.key_path, "wb") as key_file:
            key_file.write(key)

    def get_cipher(self):
        """Возвращает объект Fernet для шифрования и дешифрования"""
        key = self._load_or_generate_key()
        return Fernet(key)

    def encrypt_text(self, text):
        """Шифрует текст заметки"""
        cipher = self.get_cipher()
        return cipher.encrypt(text.encode())

    def decrypt_text(self, encrypted_text):
        """Дешифрует зашифрованный текст заметки"""
        cipher = self.get_cipher()
        return cipher.decrypt(encrypted_text).decode()
