from Crypto.Cipher import AES
import os

# Generate a random key
key = os.urandom(16)

# Create a new AES cipher object in CBC mode
cipher = AES.new(key, AES.MODE_CBC)

# Encrypt the message with the key
# Make sure to pad the message to the block size (16 bytes for AES)
# You can use a library like PyCryptoPad for this
message = b"This is the secret message flag {isep}"
padded_message = message + b'\x00' * (16 - len(message) % 16)
ciphertext = cipher.encrypt(padded_message)

# Save the key and ciphertext to files
with open("key.bin", "wb") as f:
    f.write(key)
with open("ciphertext.bin", "wb") as f:
    f.write(ciphertext)


# Read in the key and ciphertext
with open("key.bin", "rb") as f:
    key = f.read()
with open("ciphertext.bin", "rb") as f:
    ciphertext = f.read()

# Create a new AES cipher object in CBC mode
cipher = AES.new(key, AES.MODE_CBC)

# Decrypt the ciphertext
# Make sure to remove any padding
plaintext = cipher.decrypt(ciphertext)
plaintext = plaintext.rstrip(b' ')
print(plaintext.decode(errors='ignore'))

