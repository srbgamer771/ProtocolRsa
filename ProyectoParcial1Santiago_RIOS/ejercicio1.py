from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
import hashlib

# Generar las claves de Alice y Bob
key_size = 2048
alice_key = RSA.generate(key_size)
bob_key = RSA.generate(key_size)

# Mensaje de Alice
message = "M" * 1050

# Dividir el mensaje en partes más pequeñas
message_parts = [message[i:i+128] for i in range(0, len(message), 128)]

# Cifrar los mensajes con la llave pública de Bob
encrypted_messages = []
for message_part in message_parts:
    rsa_cipher = PKCS1_OAEP.new(bob_key)
    encrypted_message = rsa_cipher.encrypt(message_part.encode())
    encrypted_messages.append(encrypted_message)

# Descifrar los mensajes con la llave privada de Bob
decrypted_messages = []
for encrypted_message in encrypted_messages:
    rsa_cipher = PKCS1_OAEP.new(bob_key)
    decrypted_message = rsa_cipher.decrypt(encrypted_message).decode()
    decrypted_messages.append(decrypted_message)

# Concatenar los mensajes descifrados para obtener el mensaje original
decrypted_message = "".join(decrypted_messages)

# Generar el hash del mensaje original
message_hash = hashlib.sha256(message.encode()).hexdigest()

# Generar el hash del mensaje descifrado
decrypted_message_hash = hashlib.sha256(decrypted_message.encode()).hexdigest()

# Comparar si los hashes son iguales
if message_hash == decrypted_message_hash:
    print("El mensaje es auténtico.")
else:
    print("El mensaje no es auténtico.")