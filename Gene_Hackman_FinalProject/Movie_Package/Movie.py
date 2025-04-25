## Main.py
# File Name : Main.py
# Student Name: Abel Yemaneab, Shantele King, Jay Powell, Saivasami Amireddy
# email: yemaneag@mail.uc.edu, king4sl@mail.uc.edu, powela9@mail.uc.edu, amiredsr@mail.uc.edu
# Assignment Number: Final Project
# Due Date:   05/01/2025
# Course #/Section: IS 4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: This final tests the knowledge we have obtained this semester by having us decrypt a location and movie name.
# Brief Description of what this module does. This module loads the encrypted json document and decrypts it with a key to obtain the movie name
# Citations:ChatGPT
    # https://blog.bytescrum.com/encrypting-and-decrypting-data-with-fernet-in-python#heading-decrypting-data
    # https://stackoverflow.com/questions/55776011/decrypt-with-fernet-python

import json
from cryptography.fernet import Fernet

class MovieDecryptor:
    '''
    Decrypts an encrypted movie title assigned to the group using Fernet symmetric encryption.
    '''
    def __init__(self, encrypted_json_path, encryption_key):
        '''
        Initializes the MovieDecryptor with the path to the encrypted JSON file and the provided Fernet encryption key.
        @param encrypted_json_path: Path to the JSON file containing encrypted movie titles.
        @param encryption_key: An encoded Fernet key used to decrypt the messages.
        '''
        self.encrypted_json_path = encrypted_json_path
        self.fernet = Fernet(encryption_key.encode())

        with open(self.encrypted_json_path, "r", encoding="utf-8") as f:
            self.encrypted_data = json.load(f)

    def decrypt_movie(self, team_name):
        '''
        Retrieves the encrypted message for the specified team and decrypts it using the Fernet encryption key.
        @param team_name: The name of the team whose movie title should be decrypted.
        @return: A decrypted string containing the original movie title.
        '''
        encrypted_message = self.encrypted_data.get(team_name)
        if not encrypted_message:
            raise ValueError("Team not found in encrypted messages.")
        try:
            decrypted_bytes = self.fernet.decrypt(encrypted_message[0].encode())
            return decrypted_bytes.decode("utf-8")
        except Exception as e:
            raise RuntimeError(f"Decryption failed: {e}")


