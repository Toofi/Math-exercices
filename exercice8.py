import numpy as np

def equationsResolve(a1, b1, c1, a2, b2, c2):
    A = np.matrix([[a1, b1], [a2, b2]])
    B = np.matrix([[c1], [c2]])
    solution = A.I * B
    return solution

def modifySign(number = float):
    if (float(number) >= 0):
        result = "+"
    else:
        result = ""
    return result

#script
print('Bonjour, nous allons résoudre des équations à deux inconnues')

a1 = (float(input('Veuillez entrer la valeur le coefficient de X pour la première équation: ')))
b1 = (float(input('Veuillez entrer la valeur le coefficient de Y pour la première équation: ')))
c1 = (float(input('Veuillez entrer la valeur de l\'égalité de la première équation : ')))
a2 = (float(input('Veuillez entrer la valeur le coefficient de X pour la seconde équation: ')))
b2 = (float(input('Veuillez entrer la valeur le coefficient de Y pour la seconde équation: ')))
c2 = (float(input('Veuillez entrer la valeur de l\'égalité de la seconde équation : ')))


print('Voici la première équation :',a1,'X',modifySign(b1),b1,'Y = ',c1)
print('Voici la seconde équation :',a2,'X',modifySign(b2),b2,'Y = ',c2)

solution = equationsResolve(a1, b1, c1, a2, b2, c2)
print('X et Y ont été trouvées, les voici : ')
print('X = {}'.format(solution[0,0]))
print('Y = {}'.format(solution[1,0]))