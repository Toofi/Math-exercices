from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3, venn3_circles

threeDividedList = ['3','105','21','15']
fiveDividedList = ['5','105','15','35']
sevenDividedList = ['7','105','35','21']
i = 0

def appendToLists(number):
    if int(number) % 3 == 0:
        threeDividedList.append(number)
    if int(number) % 5 == 0:
        fiveDividedList.append(number)
    if int(number) % 7 == 0:
        sevenDividedList.append(number)
    if int(number) % 3 != 0 and int(number) % 5 != 0 and int(number) % 7 != 0:
        print("L'entrée",number,"n'est divisible ni par 3, ni par 5, ni par 7 ! Elle ne figurera pas dans le diagramme !")

def vennConstructor(threeDividedNumbers, fiveDividedNumbers, sevenDividedNumbers):
    plt.figure(figsize=(8,8))
    plt.title("Diagramme représentant les chiffres divisibles par 3, 5 ou 7")
    threeDivided = set(threeDividedNumbers)
    fiveDivided = set(fiveDividedNumbers)
    sevenDivided = set(sevenDividedNumbers)
    labels = venn3([threeDivided, fiveDivided, sevenDivided], ('Divisible par 3', 'Divisible par 5', 'Divisible par 7'))
    labels.get_label_by_id('001').set_text('\n'.join(sevenDivided-threeDivided-fiveDivided))
    labels.get_label_by_id('010').set_text('\n'.join(fiveDivided-threeDivided-sevenDivided))
    labels.get_label_by_id('100').set_text('\n'.join(threeDivided-sevenDivided-fiveDivided))
    labels.get_label_by_id('101').set_text('\n'.join(threeDivided&sevenDivided-fiveDivided))
    labels.get_label_by_id('110').set_text('\n'.join(threeDivided&fiveDivided-sevenDivided))
    labels.get_label_by_id('011').set_text('\n'.join(sevenDivided&fiveDivided-threeDivided))
    labels.get_label_by_id('111').set_text('\n'.join(threeDivided&fiveDivided&sevenDivided))
    plt.show()

vennConstructor(threeDividedList,fiveDividedList,sevenDividedList)