import streamlit as st
from PIL import Image
import numpy as np
import os

def preprocess_image(image):
    image = image.resize((180, 180))  # Resize image
    img_array = np.array(image)  # Convert to array
    return img_array

def encrypt(image_array, key):
    rotated_image = np.rot90(image_array, -1)  # Rotate 90 degrees clockwise & shift pixels to left
    encrypted_image = (rotated_image - key + 256) % 256  
    return encrypted_image.astype(np.uint8)

def decrypt(image_array, key):
    rotated_image = np.rot90(image_array, 1)  # Rotate 90 degrees anti-clockwise & shift pixels to right
    decrypted_image = (rotated_image + key) % 256  
    return decrypted_image.astype(np.uint8)

def save_image(image_array, filename):
    save = os.path.join(os.path.expanduser("~"), "Downloads")     # find path to the user's Downloads folder
    img = Image.fromarray(image_array)
    img.save(os.path.join(save, filename))# Save the image to the Downloads folder
    return save

st.title("Pixel Manipulation for Image Encryption")

uploaded_file = st.file_uploader("Upload an Image:", type=["jpg", "jpeg", "png"])

key_input = st.text_input("Enter Key (0-255):")

action = st.selectbox("Select Action", ["Encrypt", "Decrypt"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    img_array = preprocess_image(image)

    st.image(image, caption='Original Image', use_column_width=True)

    if action == "Encrypt":
        if st.button("Encryption"):
            try:
                key = int(key_input)
                if 0 <= key <= 255:
                    encrypted_image = encrypt(img_array, key)
                    download_path = save_image(encrypted_image, 'eimage.png')  # Save encrypted image as 'eimage.png'
                    st.image(encrypted_image, caption='Encrypted Image', use_column_width=True)
                    st.success(f"Encrypted image saved as 'eimage.png' in your Downloads folder: {download_path}")
                else:
                    st.error("Please enter a key between 0 and 255.")
            except ValueError:
                st.error("Invalid key. Please enter a numeric value.")

    elif action == "Decryption":
        if st.button("Decrypt"):
            try:
                key = int(key_input)
                if 0 <= key <= 255:
                    decrypted_image = decrypt(img_array, key)  # Decrypt using the key
                    download_path = save_image(decrypted_image, 'dimage.png')  # Save decrypted image as 'dimage.png'
                    st.image(decrypted_image, caption='Decrypted Image', use_column_width=True)
                    st.success(f"Decrypted image saved as 'dimage.png' in your Downloads folder: {download_path}")
                else:
                    st.error("Please enter a key between 0 and 255.")
            except ValueError:
                st.error("Invalid key. Please enter a numeric value.")