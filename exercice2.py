import math

key = str
message = str
zero = "0"

def encodeStrings(key, message):
    encodedMessage = []
    for j in range(len(key)):
        for i in range(len(message)):
            if int(key[j]) == i:
                encodedMessage.append(message[i])
    return encodedMessage

def encodeList(key, lists):
    encodedList = []
    for i in range(len(lists)):
        toEncode = lists[i]
        encoded = encodeStrings(key, toEncode)
        stringOutput = ''.join(encoded)
        encodedList.append(stringOutput)
    stringifiedList = ''.join(encodedList)
    return stringifiedList
        
def decodeStrings(key, message):
    decodedMessage = []
    for j in range(len(key)):
        for i in range(len(key)):
            if int(key[i]) == j:
                decodedMessage.append(message[i])
    return decodedMessage

def decodeList(key, lists):
    decodedList = []
    for i in range(len(lists)):
        toDecode = lists[i]
        decoded = decodeStrings(key, toDecode)
        stringOutput = ''.join(decoded)
        decodedList.append(stringOutput)
    stringifiedList = ''.join(decodedList)
    return stringifiedList

def stringify(message):
    stringifiedResult = "".join(message)
    return stringifiedResult

def eightBlocks(liste, lines):
    while len(liste) % 8 != 0:
        liste += zero
    return [liste[i:i+ lines] for i in range(0, len(liste), lines)]

key = input("Sélectionnez votre clé (8 valeurs uniquement, toutes uniques et de 0 à 7): ")
if len(key) == 8 and key.isdigit():
    message = input("Entre le message que vous voulez transposer :  ")
    ##remplit le message de zéro (str) s'il n'est pas multiple de 8
    blocs = eightBlocks(message, 8)
    message = stringify(blocs)
    print("Votre message en longueurs multiples de 8 est : ",message)
    result = encodeList(key, blocs)
    print("Voici le message encodé : ",result)
    reponse = input("Voulez-vous le décoder ? (Y/N) ")
    if (reponse == "Y" or reponse == "y"):
        blocksToDecode = eightBlocks(result, 8)
        decodedResult = decodeList(key, blocksToDecode)
        print("Voici le message décodé : ",decodedResult)
    else:
        print("ok, au revoir alors.")
else:
    print("Votre clé n'a pas 8 chiffres, désolé !")