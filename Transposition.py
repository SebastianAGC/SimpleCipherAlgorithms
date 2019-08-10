import random
globalKey = ""

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

        if(len(message) - 1 > i):
            cipherMsg+=" "

    f= open("cipherMessage.txt","w+")
    f.write(cipherMsg)
    f.close()
    print("Mensaje cifrado! Su mensaje se encuentra en el archivo cipherMessage.txt")

def decipher():
    f = open("key.txt", "r")
    key = f.read()
    f.close()

    f = open("cipherMessage.txt", "r")
    contents = f.read()
    decipherMsg = ""
    message = contents.split(" ")
    keys = key.split(" ")


    for i in range(len(message)):
        l = list(message[i])
        for j in range(len(keys[i])):
            index = int(keys[i][j]) - 1
            l[index] = message[i][j]

        decipherMsg += "".join(l)
        if (len(message) - 1 > i):
            decipherMsg += " "

    f = open("Message.txt", "w+")
    f.write(decipherMsg)
    f.close()
    print("Mensaje descifrado! Su mensaje se encuentra en el archivo Message.txt")

def main():
    op = int(input("Bienvenido al menu de cifrado por Transposición:\n1. Cifrar\n2. Descifrar\nSeleccione una opción: "))
    if op == 1:
        msg = input("Ingrese el mensaje que quiere cifrar: ")
        generateKey(msg)
        cipher(msg)
    elif op == 2:
        decipher()

main()