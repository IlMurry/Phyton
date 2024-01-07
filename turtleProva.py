import turtle

num = int(input("inserisci il numero di lati: "))

finestra = turtle.Screen()
alice = turtle.Turtle()

alice.speed(3)

alice.begin_fill()
for i in range(0, num):
    alice.forward(25)
    alice.left(360/num)
    alice.color('purple')
alice.end_fill()

finestra.mainloop()

