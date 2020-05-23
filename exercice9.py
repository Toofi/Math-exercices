import numpy as np

def equationsResolve(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
    A = np.matrix([ [a1, b1, c1], 
                    [a2, b2, c2], 
                    [a3, b3, c3]])
    B = np.matrix([[d1], [d2], [d3]])
    solution = A.I * B
    return solution

def modifySign(number = float):
    if (float(number) >= 0):
        result = "+"
    else:
        result = ""
    return result

#script
print('Bonjour, nous allons résoudre des équations à trois inconnues')

a1 = (float(input('Veuillez entrer la valeur le coefficient de X pour la première équation: ')))
b1 = (float(input('Veuillez entrer la valeur le coefficient de Y pour la première équation: ')))
c1 = (float(input('Veuillez entrer la valeur le coefficient de Z pour la première équation: ')))
d1 = (float(input('Veuillez entrer la valeur de l\'égalité de la première équation : ')))
a2 = (float(input('Veuillez entrer la valeur le coefficient de X pour la seconde équation: ')))
b2 = (float(input('Veuillez entrer la valeur le coefficient de Y pour la seconde équation: ')))
c2 = (float(input('Veuillez entrer la valeur le coefficient de Z pour la seconde équation: ')))
d2 = (float(input('Veuillez entrer la valeur de l\'égalité de la seconde équation : ')))
a3 = (float(input('Veuillez entrer la valeur le coefficient de X pour la troisième équation: ')))
b3 = (float(input('Veuillez entrer la valeur le coefficient de Y pour la troisième équation: ')))
c3 = (float(input('Veuillez entrer la valeur le coefficient de Z pour la troisième équation: ')))
d3 = (float(input('Veuillez entrer la valeur de l\'égalité de la troisième équation : ')))


print('Voici la première équation :',a1,'X',modifySign(b1),b1,'Y',modifySign(c1),c1,'X = ',d1)
print('Voici la seconde équation :',a2,'X',modifySign(b2),b2,'Y',modifySign(c2),c2,'X = ',d2)
print('Voici la troisème équation :',a3,'X',modifySign(b3),b3,'Y',modifySign(c3),c3,'X = ',d3)


solution = equationsResolve(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3)
print('X, Y et Z ont été trouvées, les voici : ')
print('X = {}'.format(solution[0,0]))
print('Y = {}'.format(solution[1,0]))
print('Z = {}'.format(solution[2,0]))
