
alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipherAlphabet = "zebrascdfghijklmnopqtuvwxyZEBRASCDFGHIJKLMNOPQTUVWXY "

def cipher(msg):
    cipherMsg = ""
    for letter in msg:
        index = alphabet.index(letter)
        cipherMsg += cipherAlphabet[index]
    f= open("cipherMessage.txt","w+")
    f.write(cipherMsg)
    f.close()
    print("Mensaje cifrado! Su mensaje se encuentra en el archivo cipherMessage.txt")

def decipher():
    f = open("cipherMessage.txt", "r")
    contents = f.read()
    decipherMsg = ""
    for letter in contents:
        index = cipherAlphabet.index(letter)
        decipherMsg += alphabet[index]
    f = open("Message.txt", "w+")
    f.write(decipherMsg)
    f.close()
    print("Mensaje descifrado! Su mensaje se encuentra en el archivo Message.txt")


def main():
    op = int(input("Bienvenido al menu de cifrado por Sustitución:\n1. Cifrar\n2. Descifrar\nSeleccione una opción: "))
    if op == 1:
        msg = input("Ingrese el mensaje que quiere cifrar: ")
        cipher(msg)
    elif op == 2:
        decipher()

main()