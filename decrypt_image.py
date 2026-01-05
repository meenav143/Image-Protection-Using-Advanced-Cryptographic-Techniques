from cryptography.fernet import Fernet
from PIL import Image
import numpy as np

# Load key
with open("key.key", "rb") as file:
    key = file.read()

cipher = Fernet(key)

# Load encrypted data
with open("encrypted_image.bin", "rb") as file:
    encrypted_data = file.read()

# Decrypt bytes
decrypted_bytes = cipher.decrypt(encrypted_data)

# Reconstruct image
original = Image.open("input.png")
shape = np.array(original).shape
dtype = np.array(original).dtype

decrypted_array = np.frombuffer(decrypted_bytes, dtype=dtype)
decrypted_array = decrypted_array.reshape(shape)

# Save decrypted image
Image.fromarray(decrypted_array).save("decrypted.png")

print("🔓 Image decrypted successfully")
