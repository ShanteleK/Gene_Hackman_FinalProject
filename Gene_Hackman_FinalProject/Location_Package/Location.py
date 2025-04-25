# Location.py
# File Name : Location.py
# Student Name: Abel Yemaneab, Shantele King, Jay Powell, Saivasami Amireddy
# email: yemaneag@mail.uc.edu, king4sl@mail.uc.edu, powela9@mail.uc.edu, amiredsr@mail.uc.edu
# Assignment Number: Final Project
# Due Date:   05/01/2025
# Course #/Section: IS 4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: This final tests the knowledge we have obtained this semester by having us decrypt a location and movie name.
# Brief Description of what this module does.  This module loads the encrypted json document and decrypts it using the UCEnglish.txt to obtain the location for the photo
# Citations:
import json

class LocationDecryptor:
    def __init__(self, english_file_path, encrypted_json_path):
        with open(english_file_path, "r", encoding="utf-8") as f:
            self.english_words = [line.strip() for line in f.readlines()]
        with open(encrypted_json_path, "r", encoding="utf-8") as f:
            self.encrypted_data = json.load(f)

    def decrypt_location(self, team_name):
        encrypted_indices = self.encrypted_data.get(team_name)
        if not encrypted_indices:
            raise ValueError("Team not found in encrypted hints.")
        
        decrypted_words = []
        for index in encrypted_indices:
            line_number = int(index) - 1  # line numbers are 1-based
            if 0 <= line_number < len(self.english_words):
                decrypted_words.append(self.english_words[line_number])
            else:
                decrypted_words.append("[INVALID]")
        
        return " ".join(decrypted_words)

