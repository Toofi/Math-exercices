def createPolynom(degree = int):
    polynom = [0]*(int(degree) + 1)
    for i in range(0,(int(degree) + 1)):
        print("Votre indice pour X ^",i," :")
        polynom[i] = input()
    return polynom

def operateOnPolynoms(polynomA = list, polynomB = list, operation = str):
    polynomC = []
    if len(polynomA)>len(polynomB): polynomC = [float(0)]*len(polynomA)
    else: polynomC = [float(0)]*len(polynomB)
    if operation == "+":
        for i in range(len(polynomA)): polynomC[i] += polynomA[i]
        for i in range(len(polynomB)): polynomC[i] += polynomB[i]
    elif operation == "-":
        for i in range(len(polynomA)): polynomC[i] += polynomA[i]
        for i in range(len(polynomB)): polynomC[i] -= polynomB[i]
    elif operation == "*":
        for i in range(len(polynomA)): polynomC[i] += polynomA[i]
        for i in range(len(polynomB)): polynomC[i] = polynomA[i] * polynomB[i]
    else: print("Vous n'avez pas sélectionné le bon caractère pour effectuer une opération!")
    return polynomC

def polynomView(polynom = list):
    for i in range(len(polynom)): 
        print("",modifySign(polynom[i]),polynom[i],"X ^",i, end="")

def modifySign(number = float):
    if (float(number) >= 0):
        result = "+"
    else:
        result = ""
    return result

print("Vous pouvez effectuer des opérations sur les polynomes en choisissant les opérations suivantes : + pour addition, - pour soustraction, * pour multiplication")
operation = input("Il est temps de choisir votre opération, +, - ou *: ")

degre00 = input("Sélectionner le degré de votre premier polynome : ")
polynom00 = createPolynom(degre00)
polynom00Float = list(map(float, polynom00))
print("Voici votre premier polynome :",polynom00Float)
polynomView(polynom00Float)

degre01 = input("\nSélectionner le degré de votre second polynome : ")
polynom01 = createPolynom(degre01)
polynom01Float = list(map(float, polynom01))
print("Voici votre second polynome :", polynom01Float)

print("Voici le résultat de l'opération :",operateOnPolynoms(polynom00Float, polynom01Float, operation))

print("Et le voici sous forme d'équation :")
polynomView(operateOnPolynoms(polynom00Float, polynom01Float, operation))