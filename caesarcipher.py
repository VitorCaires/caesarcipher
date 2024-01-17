ALP = "abcdefghijklmnopqrstuvwxyz"

def encrypt(key, text):
    if(key>26):
        key = key%26
    cyp = (ALP[key:]+ALP[0:key])
    message = [cyp[ALP.find(c)] for c in text.lower()]
    message = str(message).strip('[]')
    return message

def decrypt(key, text):
    if(key>26):
        key=(key%26)
    message = [ALP[ALP.find(c)-key] for c in text.lower()]
    message = str(message).strip('[]')
    return message

while True:
    op = int(input("1 - decriptar\n2 - encriptar\n"))
    text = input("Qual a mensagem para Encriptar/Decriptar? ")
    key = int(input("Qual a chave usada? "))
    if op == 1:
        print("A menssagem decriptada: ", decrypt(key, text))
        break
    elif op == 2:
        print("A menssagem encriptada: ", encrypt(key, text))
        break
