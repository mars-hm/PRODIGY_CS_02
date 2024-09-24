# PRODIGY_CS_02
This repository contains python code for Prodigy Infotech Internship Task 2 Pixel Manipulation for Image Encryption

## Task 2: Pixel Manipulation for Image Encryption 
Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.


## NOTE: Deployment
The following python tool has been deployed using Streamlit

### Streamlit Link: https://pixelmanipulationmars.streamlit.app/

## Implementation
#### Image Rotation: Using rot90 function from the NumPy library, the image is rotated during both encryption and decryption
Encryption: Rotate the image by 90 degrees clockwise.
Decryption: Rotate the image by 90 degrees Anti-clockwise.

#### Pixel Manipulation: The pixel values are manipulated using the Pillow (PIL) library
Encryption: The pixel values are shifted to the left by subtracting it with shift key.
Decryption: The pixel values are shifted to the right by adding it with shift key.
