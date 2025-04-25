# Main.py
# File Name : Main.py
# Student Name: Abel Yemaneab, Shantele King, Jay Powell, Saivasami Amireddy
# email: yemaneag@mail.uc.edu, king4sl@mail.uc.edu, powela9@mail.uc.edu, amiredsr@mail
# Assignment Number: Final Project
# Due Date:   05/01/2025
# Course #/Section: IS 4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: This final tests the knowledge we have obtained this semester by having us decrypt a location and movie name.
# Brief Description of what this module does. This module initializes the classes and runs the project.
# Citations:ChatGPT
from Image_Package.Image import load_Photo
from Location_Package.Location import LocationDecryptor
from Movie_Package.Movie import MovieDecryptor




if __name__ == "__main__":
    def main():
        #Set Files, Team Name, and Key up
        Team_Name = "Gene Hackman"
        Encrypted_Movie_File = "./Data/TeamsAndEncryptedMessagesForDistribution.json"
        Encrypted_Location_File = "./Data/EncryptedGroupHints Spring 2025.json"
        Key = "gZ-B245rFoIIlbHgz7m02gTatB9bTUmU-JFvdWuh2mQ="
        UCEnglish = "./Data/UCEnglish.txt"

        #Initialize and Print Location
        Location = LocationDecryptor(UCEnglish,Encrypted_Location_File)
        Location.decrypt_location(Team_Name)
        print(f"The Decrypted Location is: {Location.decrypt_location(Team_Name)}")

        #Initialize and Print Movie
        Movie = MovieDecryptor(Encrypted_Movie_File,Key)
        Movie.decrypt_movie(Team_Name)
        print(f"The Decrypted Movie Name is: {Movie.decrypt_movie(Team_Name)}")
        
        #Initialize and Print Photo
        image = load_Photo()
        image.show()

    main()
