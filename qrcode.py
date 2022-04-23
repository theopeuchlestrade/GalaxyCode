import turtle

tur = turtle.Turtle()
r = 8

tur.speed(10)

for i in range(100):
    tur.pu()
    # tur.forward(2*r+5)
    # tur.left(35-i/10)
    tur.circle(4*r + i*2, 40)
    tur.color("red")
    tur.pd()
    tur.begin_fill()
    tur.circle(r)
    tur.end_fill()


def visualUpdate():
    # Fenetre de dessin
    wn = tur.Screen()

    # Arrete les mises à jour de l'écran
    wn.tracer(0)

    # Ton dessin
    # BLABLABLA MON CODE DE DESSIN

    # Fin déplacement de la tortue
    tur.done()

    # Mise à jour de la fenêtre
    wn.update()

    # Garde la fenentre ouverte après execution
    wn.mainloop()
