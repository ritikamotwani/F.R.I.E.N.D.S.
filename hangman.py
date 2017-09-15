import turtle
import random
import time
import sys

gameFlag = True
wrongCount = 0
hmTC = (0, 0)
ft = (0, 0)
hm = turtle.Turtle()
hm.speed(0)
state = turtle.Turtle()
state.ht()
state.penup()
state.setpos(-600, -300)
state.pendown()


def correct():
    state.clear()
    state.color("yellow")
    state.write("Correct!", font=("trocchi", 30, "italic"))


def lose():
    state.clear()
    state.color("pink")
    state.write("You Lose :( ", font=("Georgia", 50, "underline"))
    xy = letter[0].pos()
    t = turtle.Turtle()
    t.ht()
    t.speed(0)
    t.color("white")
    t.penup()
    t.setpos(xy[0], xy[1]+40)
    t.pendown()
    t.write("The Character was ", align="left", font=("Arial", 40, "bold"))
    for i in range(len(character)):
        letter[i].color("red")
        letter[i].write(character[i], align="left", font=("Arial", 20, "bold"))


def win():
    state.clear()
    state.color("purple")
    state.write("You Win !! :D ", font=("Georgia", 50, "underline"))


def already():
    state.clear()
    state.color("green")
    state.write("You Already pressed that key.",
                font=("Comicsans", 30, "italic"))


def wrong():
    state.clear()
    state.color("red")
    state.write("wrong", font=("Comicsans", 40, "italic"))


def A():
    evaluate(character, "A")


def B():
    evaluate(character, "B")


def C():
    evaluate(character, "C")


def D():
    evaluate(character, "D")


def E():
    evaluate(character, "E")


def F():
    evaluate(character, "F")


def G():
    evaluate(character, "G")


def H():
    evaluate(character, "H")


def I():
    evaluate(character, "I")


def J():
    evaluate(character, "J")


def K():
    evaluate(character, "K")


def L():
    evaluate(character, "L")


def M():
    evaluate(character, "M")


def N():
    evaluate(character, "N")


def O():
    evaluate(character, "O")


def P():
    evaluate(character, "P")


def Q():
    evaluate(character, "Q")


def R():
    evaluate(character, "R")


def S():
    evaluate(character, "S")


def T():
    evaluate(character, "T")


def U():
    evaluate(character, "U")


def V():
    evaluate(character, "V")


def W():
    evaluate(character, "W")


def X():
    evaluate(character, "X")


def Y():
    evaluate(character, "Y")


def Z():
    evaluate(character, "Z")


def Hangman(num):
    global hmTC
    global ft
    if (num == 0):
        hm.penup()
        hm.setpos(-670, -340)
        hm.pendown()
        hm.ht()
        hm.begin_fill()
        hm.fd(400)
        hm.lt(90)
        hm.fd(50)
        hm.lt(90)
        hm.fd(390)
        hm.rt(90)
        hm.fd(600)
        hm.rt(90)
        hm.fd(400)
        hm.rt(90)
        hm.fd(20)
        hm.lt(90)
        hm.fd(10)
        hm.lt(90)
        hmTC = hm.pos()
        hm.fd(30)
        hm.lt(90)
        hm.fd(420)
        hm.lt(90)
        hm.fd(550)
        hm.end_fill()
        hm.pensize(5)
    elif (num == 1):
        hm.penup()
        hm.setpos(hmTC[0], hmTC[1])
        hm.pendown()
        hm.rt(90)
        hm.circle(40)
    elif (num == 2):
        hm.penup()
        hm.setpos(hmTC[0], hmTC[1]-80)
        ft = (hmTC[0], hmTC[1]-150+40)
        hm.lt(90)
        hm.pendown()
        hm.fd(140)
        hmTC = hm.pos()
    elif (num == 3):
        hm.penup()
        hm.rt(30)
        hm.pendown()
        hm.fd(100)
        hm.rt(60)
        hm.fd(10)
        hm.penup()
        hm.rt(180)
        hm.fd(10)
        hm.rt(30)
        hm.fd(100)
        hm.rt(90)
        hm.pendown()
    elif (num == 4):
        hm.penup()
        hm.setpos(hmTC[0], hmTC[1])
        hm.pendown()
        hm.lt(60)
        hm.fd(100)
        hm.lt(60)
        hm.fd(10)
    elif (num == 5):
        hm.penup()
        hm.setpos(ft[0], ft[1])
        hm.rt(90)
        hm.fd(90)
        hm.lt(180)
        hm.rt(30)
        hm.pendown()
        hm.fd(80)
        hm.rt(60)
    elif (num == 6):
        hm.penup()
        hm.setpos(ft[0], ft[1])
        hm.rt(90)
        hm.fd(90)
        hm.lt(180)
        hm.lt(30)
        hm.pendown()
        hm.fd(80)
    elif (num == 7):
        hm.penup()
        hm.setpos(-235, 265)
        hm.rt(90)
        hm.pendown()
        hm.circle(4)
    elif (num == 8):
        hm.penup()
        hm.setpos(-265, 265)
        hm.rt(90)
        hm.pendown()
        hm.circle(4)
    else:
        hm.penup()
        hm.setpos(hm.pos()[0] + 10, hm.pos()[1]-25)
        hm.pendown()
        hm.rt(30)
        hm.circle(10, 180)


def createDash(num):
    dash = []
    letter = []
    for i in range(num):
        dash.append(turtle.Turtle())
        dash[i].color("#800000", "white")
        dash[i].pensize(4)
        letter.append(turtle.Turtle())
        dash[i].ht()
        dash[i].speed(0)
        letter[i].ht()
        dash[i].penup()
        letter[i].penup()
        dash[i].setpos(-600 + i * 50, -200)
        letter[i].setpos(-595 + i * 50, -200)
        dash[i].pendown()
        letter[i].pendown()
        if(i in ch_space_pos):
            dash[i].pendown()
            continue
        dash[i].begin_fill()
        dash[i].fd(30)
        dash[i].lt(90)
        dash[i].fd(30)
        dash[i].lt(90)
        dash[i].fd(30)
        dash[i].lt(90)
        dash[i].fd(30)
        dash[i].end_fill()
    return letter


def evaluate(character, user_input):
    global wrongCount
    global gameFlag
    if gameFlag is True:
        if(user_input in character and user_input not in user_list_correct):
            for i in range(len(character)):
                if(character[i] == user_input):
                    letter[i].write(user_input, align="left",
                                    font=("Arial", 20, "bold"))
                    user_list_correct.append(user_input)
                    correct()
                    if(len(user_list_correct) == len(character)):
                        win()
                        gameFlag = False

        else:
            if(user_input in user_list_correct):
                already()
            else:
                wrong()
                user_list_wrong.append(user_input)
                wrongCount += 1
                if(wrongCount >= 9):
                    lose()
                    gameFlag = False
                Hangman(wrongCount)


f = open("characters.txt")
ch_list = []
for line in f:
    line = line.strip()
    ch_list.append(line)

character = random.choice(ch_list)
character = character.upper()
l = len(character)
character = list(character)
ch_space_count = 0
ch_space_pos = []
user_list_correct = []
user_list_wrong = []
user_input = []
for c in range(len(character)):
    if(character[c] == ' '):
        ch_space_count += 1
        ch_space_pos.append(c)
        user_list_correct.append(' ')


wn = turtle.Screen()
wn.setup(width=768, height=432)
wn.bgpic("imain.png")
wn.tracer(2)
Hangman(0)
letter = createDash(len(character))
wn.tracer(1)
wn.onkey(A, "a")
wn.onkey(B, "b")
wn.onkey(A, "a")
wn.onkey(A, "A")
wn.onkey(B, "b")
wn.onkey(B, "B")
wn.onkey(C, "c")
wn.onkey(C, "C")
wn.onkey(D, "d")
wn.onkey(D, "D")
wn.onkey(E, "e")
wn.onkey(E, "E")
wn.onkey(F, "f")
wn.onkey(F, "F")
wn.onkey(G, "g")
wn.onkey(G, "G")
wn.onkey(H, "h")
wn.onkey(H, "H")
wn.onkey(I, "i")
wn.onkey(I, "I")
wn.onkey(J, "j")
wn.onkey(J, "J")
wn.onkey(K, "k")
wn.onkey(K, "K")
wn.onkey(L, "l")
wn.onkey(L, "L")
wn.onkey(M, "m")
wn.onkey(M, "M")
wn.onkey(N, "n")
wn.onkey(N, "N")
wn.onkey(O, "o")
wn.onkey(O, "O")
wn.onkey(P, "p")
wn.onkey(P, "P")
wn.onkey(Q, "q")
wn.onkey(Q, "Q")
wn.onkey(R, "r")
wn.onkey(R, "R")
wn.onkey(S, "s")
wn.onkey(S, "S")
wn.onkey(T, "t")
wn.onkey(T, "T")
wn.onkey(U, "u")
wn.onkey(U, "U")
wn.onkey(V, "v")
wn.onkey(V, "V")
wn.onkey(W, "w")
wn.onkey(W, "W")
wn.onkey(X, "x")
wn.onkey(X, "X")
wn.onkey(Y, "y")
wn.onkey(Y, "Y")
wn.onkey(Z, "z")
wn.onkey(Z, "Z")
if gameFlag is True:
    wn.listen()
turtle.mainloop()
