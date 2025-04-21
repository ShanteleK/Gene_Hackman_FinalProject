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

