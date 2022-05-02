import turtle


def toBinary(a):
    l = []
    m = []
    result = []
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))

    for i in range(len(m)):
        result.append(str(m[i]))
    return result


def remplissage(texteBinaire):
    result = texteBinaire

    while(len(result) < 8):
        result = "0" + result

    result = "2" + result + "3"
    return result


def getFullMessage(texte):
    texteBinaire = toBinary(texte)
    lenMessage = len(texte)

    lenBinaire = bin(lenMessage)
    lenBinaire = lenBinaire[2:]

    print(f'Message in alphabetic : {texte}')
    print(f'Lenght message in algebric : {lenMessage}')
    print(f'Message in binary : {texteBinaire}')
    print(f'Lenght message in binary : {lenBinaire}')

    result = remplissage(lenBinaire)
    print(f'Lenght message in binary : {result}')
    for i in texteBinaire:
        result = result + remplissage(i)
    for i in texteBinaire:
        result = result + remplissage(i)
    print(f'Full message in binary : {result}')
    return result


def main():
    # !!!!!!!!!!!!!!!!! A FAIRE !!!!!!!!!!!!!!!!!
    # - Permettre d'avoir une palette de couleurs prédéfinies.
    # - Banque de données de Langue permettant de déterminer le mot si il y a des erreurs.
    # - Donner assez d'informations dans le QR Code afin de pouvoir détecter les erreurs lors de la lecture (Code de Hamming pour la détection des erreurs).

    tur = turtle.Turtle()
    # Fenetre de dessin
    wn = tur.screen

    # Arrete les mises à jour de l'écran
    wn.tracer(0)

    # Ton dessin
    r = 10
    test = len(motEncode) // 10
    tur.speed(10)
    for i in motEncode:
        tur.pu()

        for j in range(test):
            tur.circle(r * j)
            tur.up()
            tur.sety((r * j)*(-1))
            tur.down()

        tur.color("black", coloriage[int(i)])
        tur.pd()
        tur.begin_fill()
        tur.circle(r//2)
        tur.end_fill()

    # Mise à jour de la fenêtre
    wn.update()

    # Garde la fenentre ouverte après execution
    wn.mainloop()


texte = input("Entrez votre mot: ")[:1024]

coloriage = ["white", "black", "cyan", "magenta"]

texteBinaire = toBinary(texte)

motEncode = getFullMessage(texte)

main()
