import cv2
import os

def encrypt_image(img_path, msg, password):
    # Load the image
    img = cv2.imread(img_path)
    if img is None:
        print("Error: Image not found or unable to load.")
        return

    # Ensure the message length fits within the image
    if len(msg) > img.shape[0] * img.shape[1]:
        print("Error: Message too long for the image.")
        return

    # Embed the secret message into the image
    index = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):  # Iterate over RGB channels
                if index < len(msg):
                    img[i, j, k] = ord(msg[index])  # Embed character ASCII value
                    index += 1
                else:
                    break

    # Save the encrypted image in a lossless format
    encrypted_image_path = "encryptedImage.png"
    cv2.imwrite(encrypted_image_path, img)
    print(f"Image encrypted and saved as {encrypted_image_path}")

    # Save the password and message length to a file
    with open("encryption_info.txt", "w") as f:
        f.write(f"{password}\n{len(msg)}")

    # Open the encrypted image (for Windows)
    os.system(f"start {encrypted_image_path}")

# Inputs for encryption
img_path = "mypic.jpg"  # Replace with the correct image path
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Perform encryption
encrypt_image(img_path, msg, password)
