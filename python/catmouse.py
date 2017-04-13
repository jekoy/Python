import turtle
import time
#global variable
boxsize=200
caught=False
score=0



def up():
    mouse.forward(10)
    checkbound()
def left():
    mouse.left(45)
def right():
    mouse.right(45)
def back():
    mouse.backward(10)
    checkbound()
def quitTurtles():
    window.bye()

#check collided four aspects
#stop mouse from leaving the square set by box size    
def checkbound():
    global boxsize
    if mouse.xcor()>boxsize:
        mouse.goto(boxsize,mouse.ycor())
    if mouse.xcor()<-boxsize:
        mouse.goto(-boxsize,mouse.ycor())
    if mouse.ycor()>boxsize:
        mouse.goto(mouse.xcor(),boxsize)
    if mouse.ycor()<-boxsize:
        mouse.goto(mouse.xcor(),-boxsize)

#create some sprites
window=turtle.Screen()
mouse=turtle.Turtle()
cat=turtle.Turtle()
mouse.penup()
#up pen to coordinates
mouse.penup()
#define mouse coordinates
mouse.goto(100,100)

window.onkeypress(up,"Up")
window.onkeypress(left,"Left")
window.onkeypress(right,"Right")
window.onkeypress(back,"Down")
window.onkeypress(quitTurtles,"Escape")

#scandf layer about difficulty
difficulty=window.numinput("difficulty","Enter a difficulty from easy(1),for hard(5)",minval=1,maxval=5)


window.listen()
#mainloop
#note how it changes with difficulty
while not caught:
    #cat chase mouse
    cat.setheading(cat.towards(mouse))
    #cat have a speed 
    cat.forward(8+difficulty)
    score=score+1
    if cat.distance(mouse)<5:
        caught=True
    time.sleep(0.2-(0.01*difficulty))
window.textinput("GAME OVER","Well done.you scored: "+str(score*difficulty))
window.bye()
    
