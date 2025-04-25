
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