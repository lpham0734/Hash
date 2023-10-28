#!/usr/bin/env/python
#from VietNam 🇻🇳
# I Love You so much ❤
import hashlib
import platform
import os
if platform.system() == "Linux":
    os.system("clear")
elif platform.system() == "Windows":
    os.system("cls")
else:
    pass

print("The MD5 hash with the salt is extremely complex and has been hashed to sha256")
in_text = input("Enter the text string to Hash MD5: ")
# chuỗi muối của md5 được hash từ sha256 riêng!!
salt = "9CB$FV5U5/E09V*@0.^0JNB[SG=7Y7HE%K$9_G$V/$Y0@C"

# Kết hợp muối với chuỗi văn bản
salted_text = salt + in_text

# Mã hóa chuỗi với MD5
md5_hash = hashlib.md5(salted_text.encode()).hexdigest()

print("MD5 string after encryption: ", md5_hash)
