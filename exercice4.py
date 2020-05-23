from math import sqrt

number_a = float(input("Donnez a : "))
number_b = float(input("Donnez b: "))
number_c = float(input("Donnez c: "))

delta = float

def calculateDelta(a = float, b = float, c = float):
    global delta
    delta = (float(b) * float(b)) - (4 * float(a) * float(c)) 
    return delta

def deltaZero(a = float, b = float):
    result = ( - float(b) ) / (2 * float(a) )
    return result

def positiveDelta(a = float, b = float, c = float, delta = float):
    result1 = ( - float(b) + sqrt(delta) ) / ( 2 * a )
    result2 = ( - float(b) - sqrt(delta) ) / ( 2 * a )
    return result1, result2

def modifySign(number = float):
    if (float(number) >= 0):
        result = "+"
    else:
        result = ""
    return result

if (number_a == float(0.00)):
    print("La valeur de A ne peut être nulle ! Il FAUT que X² existe !")
else:
    print("L'équation est comme suit : ",number_a,"x²",modifySign(number_b),number_b,"x",modifySign(number_c),number_c, "= 0")

    print("Delta : ",calculateDelta(number_a, number_b, number_c))

    if (delta < 0):
        print("Aucune solution n'est possible dans les réels! Le delta est négatif !")
    elif (delta == 0):
        print("Le delta est nul, une seule solution est donc possible. Réponse : ",deltaZero(number_a, number_b))
    elif (delta > 0):
        print("Le delta est positif, deux solutions sont donc possibles. Réponses : ", positiveDelta(number_a, number_b, number_c, delta))
    else:
        print("ERR0R ERR0R ERR0R")
