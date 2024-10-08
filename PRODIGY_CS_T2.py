import streamlit as st
from PIL import Image
import numpy as np
import os
from io import BytesIO

def preprocess_image(image):
    image = image.resize((180, 180))  # Resize image
    img_array = np.array(image)  # Convert to array
    return img_array

def encrypt(image_array, key):
    rotated_image = np.rot90(image_array, -1)  # Rotate 90 degrees clockwise & shifts pixels to the left
    encrypted_image = (rotated_image - key + 256) % 256  
    return encrypted_image.astype(np.uint8)

def decrypt(image_array, key):
    rotated_image = np.rot90(image_array, 1)  # Rotate 90 degrees counterclockwise & shifts the pixels to the right
    decrypted_image = (rotated_image + key) % 256 
    return decrypted_image.astype(np.uint8)

def save(image_array, filename):
    img = Image.fromarray(image_array)
    download = BytesIO()
    img.save(download, format="PNG")
    return download

# ---- Streamlit ----
st.markdown(
    "<h1 style='text-align: center;'>Pixel Manipulation for Image Encryption</h1>", 
    unsafe_allow_html=True
)

input = st.file_uploader("Upload an Image:", type=["jpg", "jpeg", "png"])

shift_key = st.text_input("Enter Key (0-255):")

choice = st.selectbox("Select Action", ["Encryption", "Decryption"])

if input is not None:
    image = Image.open(input).convert('RGB')
    img_array = preprocess_image(image)

    st.image(image, caption='Original Image', use_column_width=True)

    if choice == "Encryption":
        if st.button("Encrypt"):
            try:
                key = int(shift_key)
                if 0 <= key <= 255:
                    encrypted_image = encrypt(img_array, key)
                    st.image(encrypted_image, caption='Encrypted Image', use_column_width=True)

                    eimage = save(encrypted_image, 'eimage.png')
                    st.download_button(
                        label="Download Encrypted Image",
                        data=eimage.getvalue(),
                        file_name="eimage.png",
                        mime="image/png"
                    )
                else:
                    st.error("Please enter a key between 0 and 255.")
            except ValueError:
                st.error("Invalid key. Please enter a numeric value.")

    elif choice == "Decryption":
        if st.button("Decrypt"):
            try:
                key = int(shift_key)
                if 0 <= key <= 255:
                    decrypted_image = decrypt(img_array, key)  
                    st.image(decrypted_image, caption='Decrypted Image', use_column_width=True)

                    dimage = save(decrypted_image, 'dimage.png')
                    st.download_button(
                        label="Download Decrypted Image",
                        data=dimage.getvalue(),
                        file_name="dimage.png",
                        mime="image/png"
                    )
                else:
                    st.error("Please enter a key between 0 and 255.")
            except ValueError:
                st.error("Invalid key. Please enter a numeric value.")
