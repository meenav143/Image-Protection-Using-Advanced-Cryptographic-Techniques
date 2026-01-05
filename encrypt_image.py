from cryptography.fernet import Fernet
from PIL import Image
import numpy as np

# Load key
with open("key.key", "rb") as file:
    key = file.read()

cipher = Fernet(key)

# Load image
img = Image.open("input.png")
img_array = np.array(img)

# Convert to bytes and encrypt
img_bytes = img_array.tobytes()
encrypted_data = cipher.encrypt(img_bytes)

# Save encrypted data
with open("encrypted_image.bin", "wb") as file:
    file.write(encrypted_data)

print("🔐 Image encrypted successfully")
