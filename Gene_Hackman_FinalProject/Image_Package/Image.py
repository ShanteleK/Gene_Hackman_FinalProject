# Image.py
# File Name : Image.py
# Student Name: Abel Yemaneab, Shantele King, Jay Powell, Saivasami Amireddy
# email: yemaneag@mail.uc.edu, king4sl@mail.uc.edu, powela9@mail.uc.edu, amiredsr@mail.uc.edu
# Assignment Number: Final Project
# Due Date:   05/01/2025
# Course #/Section: IS 4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: This final tests the knowledge we have obtained this semester by having us decrypt a location and movie name.
# Brief Description of what this module does. This module loads the image we took at the decrypted location.
# Citations:
from PIL import Image
import os

def load_Photo():
    """  
    Loads an image file named 'FinalPhoto.jpg' from the '../FinalPhoto/' directory 

    @param: None

    @return: Final Photo image taken with quote from Hoosier.
    """
    # Get the absolute path of the image
    image_path = os.path.join(os.path.dirname(__file__), "../FinalPhoto/FinalPhoto.jpg")
    
    try:
        img = Image.open(image_path)
        return img
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return None