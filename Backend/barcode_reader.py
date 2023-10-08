# Takes image and returns barcode value if exists
import base64
import re

import cv2
from pyzbar.pyzbar import decode
from PIL import Image
from io import BytesIO

def read_barcode(image_path):
    # Read the image with barcode
    image_str = re.sub('^data:image/.+;base64,', '',image_path)
    imageIO = base64.urlsafe_b64decode(image_str)
    image = Image.open(BytesIO(imageIO))
    # Decode barcode
    barcode = decode(image)

    if barcode:
        # Extract the first detected barcode's data (product number)
        product_number = barcode[0].data.decode('utf-8')

        print(product_number)
        # Return the product number
        return product_number
    else:
        return {'error': 'barcode not found.'}

def read_barcode_local(image_path):
    # Read the image with barcode
    # Decode barcode
    barcode = decode(image_path)

    if barcode:
        # Extract the first detected barcode's data (product number)
        product_number = barcode[0].data.decode('utf-8')

        print(product_number)
        # Return the product number
        return product_number
    else:
        return {'error': 'barcode not found.'}
def main():
    # Replace '/Users/jackyoussef/Documents/GitHub/hackUTA23/API/pastry.jpg' with your image path
    barcode_number = read_barcode_local('/Users/jackyoussef/Documents/GitHub/hackUTA23/API/images/pastry.jpg')

    if barcode_number is not None:
        print("Barcode Number:", barcode_number)
    else:
        print("No barcode detected in the image.")

if __name__ == "__main__":
    main()
