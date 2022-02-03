import turtle
import os

window = turtle.Screen()
window.title("Pong by Samuel Ginzburg")
window.bgcolor("black") #change background color of window to black
window.setup(width = 800, height = 600)
window.tracer(0)

# Score
score_l = 0
score_r = 0

# paddle_l = Left paddle
paddle_l = turtle.Turtle()
paddle_l.speed(0) #sets paddle to max animation speed for maximized efficency
paddle_l.shape("square")
paddle_l.color("white")
paddle_l.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_l.penup()
paddle_l.goto(-350, 0)

# paddle_r = Right paddle
paddle_r = turtle.Turtle()
paddle_r.speed(0) #sets paddle to max animation speed for maximized efficency
paddle_r.shape("square")
paddle_r.color("white")
paddle_r.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_r.penup()
paddle_r.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) #sets paddle to max animation speed for maximized efficency
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Ball movement 
ball.dx = .4
ball.dy = -.4

# Pen: Scoring 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() 
pen.goto(0, 260)
pen.write("P1: 0                              P2: 0", align = "center", font=("Courier", 24, "normal"))

# Paddle Movement with keyboard
# Functions
def paddle_l_up():
    y = paddle_l.ycor() # .ycor() method: turtle module -> returns Y coordinate 
    y += 20 # adds 20 pixels to the y coordinate
    paddle_l.sety(y) 
    
def paddle_l_down():
    y = paddle_l.ycor() # .ycor() method: turtle module -> returns Y coordinate 
    y -= 20 # adds 20 pixels to the y coordinate
    paddle_l.sety(y) 

def paddle_r_up():
    y = paddle_r.ycor() # .ycor() method: turtle module -> returns Y coordinate 
    y += 20 # adds 20 pixels to the y coordinate
    paddle_r.sety(y) 
    
def paddle_r_down():
    y = paddle_r.ycor() # .ycor() method: turtle module -> returns Y coordinate 
    y -= 20 # adds 20 pixels to the y coordinate
    paddle_r.sety(y) 


# Keyboard binding
window.listen() # listens to keyboard input
window.onkeypress(paddle_l_up, "w") # When user presses w key, call function "paddle_l_up()"
window.onkeypress(paddle_l_down, "s") # When user presses s key, call function "paddle_l_down()"
window.onkeypress(paddle_r_up, "Up") # When user presses up arrow key, call function "paddle_r_up()"
window.onkeypress(paddle_r_down, "Down") # When user presses down arrow key, call function "paddle_r_down()"


#Main game loop
while True:
    window.update() # updates screen while loop runs

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # reverses direction of the ball (multiply the x velocity of the ball by -1)
        os.system("afplay bounce.wav&")
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 # reverses direction of the ball
        os.system("afplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0) # place ball back to center 
        ball.dx *= -1 # reverses direction of the ball 
        score_l += 1
        pen.clear() # Deletes previous score before updating
        pen.write("P1: {}                              P2: {}".format(score_l, score_r), align = "center", font=("Courier", 24, "normal")) # Updates printed score on screen


    if ball.xcor() < -390:
        ball.goto(0, 0) # place ball back to center 
        ball.dx *= -1 # reverses direction of the ball   
        score_r += 1 
        pen.clear() # Deletes previous score before updating
        pen.write("P1: {}                              P2: {}".format(score_l, score_r), align = "center", font=("Courier", 24, "normal")) # Updates printed score on screen


    # Paddle & Ball Collision: Right Paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_r.ycor() + 40 and ball.ycor() > paddle_r.ycor() -40): # if edges are touching AND the ball is along the paddle AND the ball is in between the top and bottom of the paddle 
        ball.setx(340) # moves ball back 10 pixels to the left   
        ball.dx *= -1 # reverses direction of the ball 
        os.system("afplay bounce.wav&")
    
    # Paddle & Ball Collision: Left Paddle
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_l.ycor() + 40 and ball.ycor() > paddle_l.ycor() -40): 
        ball.setx(-340) # moves ball back 10 pixels to the left   
        ball.dx *= -1 # reverses direction of the ball
        os.system("afplay bounce.wav&")
        

 