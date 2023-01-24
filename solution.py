from Crypto.Cipher import AES


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