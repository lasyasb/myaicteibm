import cv2
import os

# Read the image
img = cv2.imread("mypic.jpg")  # Replace with the correct image path
if img is None:
    print("Error: Image not found or unable to read")
    exit()

# Input secret message and passcode
msg = input("Enter secret message:")
password = input("Enter a passcode:")

# Create dictionaries for encoding and decoding
d = {}
for i in range(255):
    d[chr(i)] = i

# Initialize variables
m = 0
n = 0
z = 0

# Encrypt the message into the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows
