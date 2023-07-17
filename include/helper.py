from include.constants import KEY
from cryptography.fernet import Fernet


def encrypt_text(text, key):
    f = Fernet(key)
    encrypted_text = f.encrypt(text.encode())
    return encrypted_text


def decrypt_text(encrypted_text, key):
    f = Fernet(key)
    decrypted_text = f.decrypt(encrypted_text)
    return decrypted_text.decode()



def saveData(filename, text):
    with open(filename, "wb") as file:
        file.write(encrypt_text(text, KEY))
    


def getData(filename):
    with open(filename, "rb") as file:
        data = file.read()
    
    return decrypt_text(data, KEY)
        