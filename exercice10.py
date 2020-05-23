import numpy as np

operation = int

def createMatrix(lines, columns):
    a = np.arange(lines * columns).reshape(lines , columns)
    i = 0
    while i < lines:
        j = 0
        while j < col:
            print("colonne :",j+1," et ligne : ",i+1)
            b = int(input("entrez la valeur : "))
            a[i][j] = b
            j += 1
        i += 1 
    return a

def printMatrixNumber(operation):
    if (operation < 3):
        print("Nous allons créer notre première matrice.")
    else:
        print("Nous allons créer notre matrice.")

def operationMatrix(operation, matrix1, matrix2 = 1, scalar = 1):
    print(matrix1)
    if(operation == 1):
        print("+")
        result = matrix1 + matrix2
        print(matrix2)
    elif(operation == 2):
        print("*")
        result = matrix1 * matrix2
        print(matrix2)
    elif(operation == 3):
        print("*")
        result = matrix1 * scalar
        print(scalar)
    elif(operation == 4):
        result = np.transpose(matrix1)
        print("Voici votre matrice :")
        print(matrix1)
        print("Voici sa transposée :")
    if (1 <= operation <= 3):
        print("=")
    print(result)

print("1. Addition de deux matrices")
print("2. Multiplication de deux matrices")
print("3. Multiplication d'une matrice par un scalaire")
print("4. Transposition d'une matrice")
operation = int(input("Veuillez choisir votre opération : "))
print("operation = ",operation)

if(1<= operation <= 4):
    printMatrixNumber(operation)
    lin = int(input("Entre le nombre de lignes :"))
    col = int(input("Entre le nombre de colonnes :"))
    matrix1 = createMatrix(lin, col)
    if(operation < 3):
        print("Nous allons créer notre deuxième matrice")
        matrix2 = createMatrix(lin, col)
        if(operation == 1):
            operationMatrix(1, matrix1, matrix2)
        elif(operation == 2):
            operationMatrix(2, matrix1, matrix2)
    elif(operation == 3):
        scalar = (int(input("Veuillez entrer une valeur pour le scalaire :")))
        operationMatrix(3, matrix1, scalar = scalar)
    elif(operation == 4):
        operationMatrix(4, matrix1)