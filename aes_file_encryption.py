from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode

key = input("Please enter your encryption password: ") # getting user password
key = key.encode('UTF-8')
key = pad(key, AES.block_size)

# encrypt function 
def encrypt(file_name, key):
    # opening anf reading the file
    with open(file_name, 'rb') as entry:
        data = entry.read()
        cipher = AES.new(key, AES.MODE_CFB) 
        ciphertext = cipher.encrypt(pad(data, AES.block_size)) # encryption
        iv = b64encode(cipher.iv).decode('UTF-8') # iv is initialization vector
        ciphertext = b64encode(ciphertext).decode('UTF-8') # encrypted text
        to_write = iv + ciphertext # writing encrypted text in the file

    entry.close()

    # writing encrypted data to a new file
    with open(file_name+'.enc','w') as data:
        data.write(to_write)
    data.close()

encrypt('test_img.jpg', key)



