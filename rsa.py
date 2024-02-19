#practica de Algoritmo rsa
#Imports
import hashlib
import Crypto.Util.number

#Numero de bits
bits = 1024

#Obtener los primos para Alice y Bob
pA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("pA: ", pA, "\n")
qA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("qA: ", qA, "\n")

pB = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("pB: ", pB, "\n")
qB = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("qB: ", qB, "\n")

#Obtenemos la primera parte de la llave publica de Alice y Bob.
nA = pA * qA
print("nA: ", nA, "\n")

nB = pB * qB
print("nB: ", nB, "\n")

#Calculamos el Indicador de Euler Phi
phiA = (pA - 1)*(qA - 1)
print("phiA: ", phiA, "\n")

phiB = (pB - 1)*(qB - 1)
print("phiB: ", phiB, "\n")

#Por razones de eficiencia usaremos el numero 4 de Fermat, 65537, debido a que es 
#Un primo largo y no es potencia de 2, y como forma parte de la clave public no es necesario calcularlo
e = 65337

#Calcular la llave privada de Alice y Bob
dA = Crypto.Util.number.inverse(e, phiA)
dB = Crypto.Util.number.inverse(e, phiB)

msg="Hola Mundo"
msg_hash = hashlib.sha256(msg.encode()).digest()

#Convertir Hash a Entero
hash_int = int.from_bytes(msg_hash, byteorder='big')
print("Mensaje hash int:",hash_int,"\n")

c = pow(hash_int,dA,nA)
print("Mensaje Cifrado:",c,"\n")

des = pow(c,e,nA)
print("Verificacion de hash int:",des,"\n")

if hash_int==des:
    print("El mensaje fue firmado por Alice")
else:
    print("El mensaje no fue firmado por Alice")