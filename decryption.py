import cv2

def decrypt_image(encrypted_image_path, password):
    # Load the encrypted image
    img = cv2.imread(encrypted_image_path)
    if img is None:
        print("Error: Encrypted image not found or unable to load.")
        return

    # Read the password and message length from the file
    try:
        with open("encryption_info.txt", "r") as f:
            saved_password = f.readline().strip()
            msg_length = int(f.readline().strip())
    except FileNotFoundError:
        print("Error: Encryption info file not found.")
        return

    # Verify the passcode
    if password != saved_password:
        print("YOU ARE NOT AUTHORIZED")
        return

    # Extract the secret message from the image
    message = ""
    index = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):  # Iterate over RGB channels
                if index < msg_length:
                    message += chr(img[i, j, k])  # Extract character from pixel value
                    index += 1
                else:
                    break

    print("Decrypted message:", message)

# Inputs for decryption
encrypted_image_path = "encryptedImage.png"
pas = input("Enter passcode for Decryption: ")

# Perform decryption
decrypt_image(encrypted_image_path, pas)
