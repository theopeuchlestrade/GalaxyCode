from tkinter import *
import turtle as turtle


def toBinary(a):
    """
    It converts a string into a list of binary numbers

    :param a: the string to be converted to binary
    :return: A list of binary numbers
    """
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
    """
    It adds a 2 and a 3 to the beginning and end of the binary string, respectively, and adds zeros to
    the beginning of the string until it is 8 characters long.

    :param texteBinaire: the binary string to be padded
    :return: a string of 8 bits.
    """
    result = texteBinaire

    while(len(result) < 8):
        result = "0" + result

    result = "2" + result + "3"
    return result


def getFullMessage(texte):
    """
    It takes a string, converts it to binary, converts the length of the string to binary, and then adds
    the length of the string to the beginning of the binary string.

    :param texte: the text to be converted to binary
    :return: The full message in binary
    """
    texteBinaire = toBinary(texte)
    lenMessage = len(texte)

    lenBinaire = bin(lenMessage)
    lenBinaire = lenBinaire[2:]

    # Debugging
    #print(f'Message in alphabetic : {texte}')
    #print(f'Lenght message in algebric : {lenMessage}')
    #print(f'Message in binary : {texteBinaire}')
    #print(f'Lenght message in binary : {lenBinaire}')

    result = remplissage(lenBinaire)
    #print(f'Lenght message in binary : {result}')
    for j in range(4):
        for i in texteBinaire:
            result = result + remplissage(i)
    #print(f'Full message in binary : {result}')
    return result


def main():
    # Variables
    test = len(motEncode) // 10
    r = 5
    decalage = 10
    index = 0

    # Turtle options
    turtle.hideturtle()
    tur = turtle.Turtle()
    tur.hideturtle()
    tur.pensize(0.05)

    # Window options
    wn = turtle.getscreen()
    wn.screensize(5*len(motEncode), 5*len(motEncode))
    wn.bgcolor("white")
    wn.tracer(0)  # stop window refreshing
    tur.speed(10)  # controls turtle's speed

    # List of colours
    color = ["white", "black", "magenta", "cyan"]

    # Drawing
    tur.pu()
    for j in range(1, (test + 2)):
        tur.sety(((r * j)*(-1)))
        if(j == 1):
            for i in range(10):  # 0 to 10
                tur.circle(r * j, extent=360/10)  # 36
                tur.pd()
                tur.color("orange")
                tur.circle(r/2)
                tur.up()
        else:
            # tur.pd()
            tur.circle(r * j, extent=-(decalage * j))
            for i in range(10):  # 0 to 10
                # Start little circle
                tur.circle(r * j, extent=360/10)  # 36
                tur.pd()
                # Compute color's value
                tur.begin_fill()
                if(motEncode[index] == "0"):
                    tur.color("black", color[0])
                elif(motEncode[index] == "1"):
                    tur.color("black", color[1])
                elif(motEncode[index] == "2"):
                    tur.color("black", color[2])
                else:
                    tur.color("black", color[3])
                tur.circle(r/2)
                tur.end_fill()
                # End little circle
                tur.up()
                index += 1
            tur.circle(r * j, extent=(decalage * j))

    # Window update
    wn.update()

    # Image export
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="galaxycode.eps")

    # Show turtle
    turtle.ontimer(main, 250)
    turtle.done()


# Execution
texte = input("Entrez votre mot: ")[:1024]
print("Votre GalaxyCode a été exporté sous le nom 'galaxycode.eps'.\n")

texteBinaire = toBinary(texte)
motEncode = getFullMessage(texte)

main()
