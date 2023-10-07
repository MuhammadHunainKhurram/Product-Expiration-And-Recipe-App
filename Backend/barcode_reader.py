# Takes image and returns barcode value if exists

import cv2
from pyzbar.pyzbar import decode

def read_barcode(image_path):
    # Read the image with barcode
    image = cv2.imread(image_path)

    # Decode barcode
    barcode = decode(image)

    if barcode:
        # Extract the first detected barcode's data (product number)
        product_number = barcode[0].data.decode('utf-8')

        # Return the product number
        return product_number
    else:
        return {'error': 'barcode not found.'}

def main():
    # Replace '/Users/jackyoussef/Documents/GitHub/hackUTA23/API/pastry.jpg' with your image path
    barcode_number = read_barcode('/Users/jackyoussef/Documents/GitHub/hackUTA23/API/images/pastry.jpg')

    if barcode_number is not None:
        print("Barcode Number:", barcode_number)
    else:
        print("No barcode detected in the image.")

if __name__ == "__main__":
    main()
