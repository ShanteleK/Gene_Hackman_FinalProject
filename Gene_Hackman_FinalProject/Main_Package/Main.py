from Image_Package.Image import load_Photo





if __name__ == "__main__":

    image = load_Photo()

if image:
    # Display the image using the default image viewer
    image.show()
