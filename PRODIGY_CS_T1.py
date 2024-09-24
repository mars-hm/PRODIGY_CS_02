import streamlit as st

# Define the encryption function
def encrypt(ptext, key):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    cipher = ''
    for char in ptext:
        if char in letters:
            i = (letters.index(char) + key) % len(letters)
            cipher += letters[i]
        else:
            cipher += char
    return cipher

# Define the decryption function
def decrypt(ctext, key):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    plaintext = ''
    for char in ctext:
        if char in letters:
            i = (letters.index(char) - key) % len(letters)
            plaintext += letters[i]
        else:
            plaintext += char
    return plaintext

# Streamlit application layout
st.title("Caesar Cipher")

# Get user input for encryption
st.header("Encryption")
ptext = st.text_input("Enter the Plain Text", "")
key = st.number_input("Shift Key", min_value=0, step=1)

if st.button("Encrypt"):
    if ptext and key:
        cipher_text = encrypt(ptext, key)
        st.success(f"Cipher Text: {cipher_text}")
    else:
        st.error("Please enter both text and key.")

# Get user input for decryption
st.header("Decryption")
ctext = st.text_input("Enter the Cipher Text", "")
key_decrypt = st.number_input("Shift Key for Decryption", min_value=0, step=1, key='decrypt_key')

if st.button("Decrypt"):
    if ctext and key_decrypt:
        plain_text = decrypt(ctext, key_decrypt)
        st.success(f"Plain Text: {plain_text}")
    else:
        st.error("Please enter both cipher text and key.")
