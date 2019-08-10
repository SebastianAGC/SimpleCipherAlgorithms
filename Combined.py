import random

alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipherAlphabet = "zebrascdfghijklmnopqtuvwxyZEBRASCDFGHIJKLMNOPQTUVWXY "

def generateKey(msg):
    message = msg.split(" ")
    key = []
    for i in range(len(message)):
        keys = ""
        for j in range(len(message[i])):
            r = str(random.randint(1, len(message[i])))
            while r in keys:
                r = str(random.randint(1, len(message[i])))
            keys += r

        key.append(keys)
        if (len(message) - 1 > i):
            key += " "

    newKey = "".join(key)
    f = open("key.txt", "w+")
    f.write(newKey)
    f.close()
    print("Llave generada! Su llave se encuentra en el archivo key.txt")

def cipher(msg):
    f = open("key.txt", "r")
    key = f.read()
    f.close()

    cipherMsg = ""
    message = msg.split(" ")
    keys = key.split(" ")

    for i in range(len(message)):

        for j in range(len(message[i])):
            newIndex = int(keys[i][j])
            cipherMsg += message[i][newIndex - 1]

        if len(message) - 1 > i:
            cipherMsg+=" "

    newCipherMsg = ""
    for letter in cipherMsg:
        index = alphabet.index(letter)
        newCipherMsg += cipherAlphabet[index]

    f = open("combinedCipherMessage.txt", "w+")
    f.write(newCipherMsg)
    f.close()
    print("Mensaje cifrado! Su mensaje se encuentra en el archivo combinedCipherMessage.txt")


def decipher():
    f = open("key.txt", "r")
    key = f.read()
    f.close()

    f = open("combinedCipherMessage.txt", "r")
    contents = f.read()
    decipherMsg = ""
    for letter in contents:
        index = cipherAlphabet.index(letter)
        decipherMsg += alphabet[index]

    newDecipherMsg = ""
    message = decipherMsg.split(" ")
    keys = key.split(" ")

    for i in range(len(message)):
        l = list(message[i])
        for j in range(len(keys[i])):
            index = int(keys[i][j]) - 1
            l[index] = message[i][j]

        newDecipherMsg += "".join(l)
        if (len(message) - 1 > i):
            newDecipherMsg += " "

    f = open("CombinedMessage.txt", "w+")
    f.write(newDecipherMsg)
    f.close()
    print("Mensaje descifrado! Su mensaje se encuentra en el archivo CombinedMessage.txt")

def main():
    op = int(input("Bienvenido al menu de cifrado combinado:\n1. Cifrar\n2. Descifrar\nSeleccione una opción: "))
    if op == 1:
        msg = input("Ingrese el mensaje que quiere cifrar: ")
        generateKey(msg)
        cipher(msg)
    elif op == 2:
        decipher()

main()