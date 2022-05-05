from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode
import getpass

key = getpass.getpass("Enter your decryption password: ")
key = key.encode('UTF-8')
key = pad(key,AES.block_size)

with open('test_img.jpg.enc', 'r') as entry:
    try:
        data = entry.read()
        length = len(data) # finding initialization factor
        iv = data[:24]
        iv = b64decode(iv) # decoding it using base 64
        ciphertext = data[24:length] # remaining text after removong the initialization factor
        ciphertext = b64decode(ciphertext)
        cipher = AES.new(key, AES.MODE_CFB, iv)
        decrypted = cipher.decrypt(ciphertext)
        decrypted = unpad(decrypted, AES.block_size)
        
        # writing decrypted data to a new file
        with open('test_img_decrypted.jpg', 'wb') as data:
            data.write(decrypted)
        data.close()
    except(ValueError, KeyError):
        print("Wrong password!")



