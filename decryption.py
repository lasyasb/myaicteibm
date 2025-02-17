import cv2

# Read the encrypted image
img = cv2.imread("encryptedImage.jpg")  # Replace with the correct image path
if img is None:
    print("Error: Encrypted image not found or unable to read")
    exit()

# Input passcode for verification (optional)
password = input("Enter the passcode to decrypt the message:")

# Create dictionaries for decoding
d = {}
for i in range(255):
    d[i] = chr(i)

# Initialize variables
m = 0
n = 0
z = 0

# Decrypt the message from the image
decrypted_msg = ""
for i in range(len(msg)):  # Assuming the length of the message is known or can be determined
    decrypted_msg += d[img[n, m, z]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

# Output the decrypted message
print("Decrypted message:", decrypted_msg)
