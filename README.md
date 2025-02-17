This repository contains Python scripts for encrypting and decrypting secret messages within images using steganography. The scripts allow you to hide a message in an image and later extract it using a passcode.
Files Included


    encryption.py: Encrypts a secret message into an image.

    decryption.py: Decrypts the secret message from the encrypted image.

    stegocode.py: Combines both encryption and decryption functionalities in a single script.

Requirements

    Python 3.x

    OpenCV (cv2) library

    OS library (for opening the image)

To install the required libraries, run:
bash


pip install opencv-python

Usage
1. Encryption (encryption.py)

This script hides a secret message in an image. The encrypted image is saved as encryptedImage.jpg.
Steps:

    Place the image you want to use (e.g., mypic.jpg) in the same directory as the script.

    Run the script:
    bash
 

    python encryption.py

    Enter the secret message and a passcode when prompted.

    The encrypted image will be saved as encryptedImage.jpg and automatically opened.

2. Decryption (decryption.py)

This script extracts the hidden message from the encrypted image.
Steps:

    Ensure the encrypted image (encryptedImage.jpg) is in the same directory as the script.

    Run the script:
    bash


    python decryption.py

    Enter the passcode used during encryption.

    The decrypted message will be displayed in the terminal.

3. Combined Encryption and Decryption (stegocode.py)

This script combines both encryption and decryption functionalities. It allows you to encrypt a message into an image and then decrypt it using a passcode.
Steps:

    Place the image you want to use (e.g., mypic.jpg) in the same directory as the script.

    Run the script:
    bash


    python stegocode.py

    Enter the secret message and a passcode when prompted.

    The encrypted image will be saved as encryptedImage.jpg and automatically opened.

    To decrypt the message, enter the passcode when prompted.

    If the passcode is correct, the decrypted message will be displayed. Otherwise, an error message will appear.

How It Works
Encryption Process:

    The script reads the image and converts it into a pixel matrix.

    Each character of the secret message is encoded into the pixel values (R, G, B channels) of the image.

    The modified image is saved as encryptedImage.jpg.

Decryption Process:

    The script reads the encrypted image and extracts the pixel values.

    The pixel values are converted back into characters using the same encoding scheme.

    The original message is reconstructed and displayed.

Notes

    The length of the message is limited by the size of the image. Ensure the image has enough pixels to accommodate the message.

    The passcode is used for verification during decryption but is not part of the encryption algorithm itself.

    The scripts are designed for simplicity and may not be suitable for highly secure applications.

Example
Encryption:
bash


$ python encryption.py
Enter secret message: Hello, World!
Enter a passcode: mypassword

    The message "Hello, World!" is encrypted into the image mypic.jpg and saved as encryptedImage.jpg.

Decryption:
bash


$ python decryption.py
Enter the passcode to decrypt the message: mypassword
Decrypted message: Hello, World!

License

This project is open-source and available under the MIT License. Feel free to modify and distribute it as needed.

For any questions or issues, please open an issue in the repository or contact the author.
