import os
import random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def encrypt_file(key, filename):
    chunksize = 64 * 1024
    output_filename = filename + '.encrypted'

    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = ''

    for i in range(16):
        IV += chr(random.randint(0, 0xFF))

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(output_filename, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV.encode('utf-8'))

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))

# Aquí especificamos el nombre del archivo a encriptar
filename = '__main__.py'

# Aquí especificamos la contraseña para generar la clave de cifrado
password = 'tuputamadre'

# Generamos la clave de cifrado a partir de la contraseña
hasher = SHA256.new(password.encode('utf-8'))
key = hasher.digest()

# Encriptamos el archivo especificado
encrypt_file(key, filename)