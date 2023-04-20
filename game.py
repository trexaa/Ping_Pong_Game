import turtle
import time


window = turtle.Screen()
window.title("Ping Pong Game")
window.setup(width=800, height=600)
window.tracer(0)
window.bgcolor(.1,.1,.1)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_len=1,stretch_wid=1)
ball.goto(x=0,y=0)
ball.penup()

ball_dx, ball_dy = 1,1
ball_speed= .5

center_line = turtle.Turtle()
center_line.speed(0)
center_line.shape("square")
center_line.color("white")
center_line.shapesize(stretch_len=.1,stretch_wid=25)
center_line.penup()
center_line.goto(0, 0)

lin = turtle.Turtle()
lin.speed(0)
lin.shape("square")
lin.color("white")
lin.shapesize(stretch_len=.1,stretch_wid=30)
lin.penup()
lin.goto(400, 0)

lin2 = turtle.Turtle()
lin2.speed(0)
lin2.shape("square")
lin2.color("white")
lin2.shapesize(stretch_len=.1,stretch_wid=30)
lin2.penup()
lin2.goto(-400, 0)

lin3 = turtle.Turtle()
lin3.speed(0)
lin3.shape("square")
lin3.color("white")
lin3.shapesize(stretch_len=40,stretch_wid=.1)
lin3.penup()
lin3.goto(0,300)

lin4 = turtle.Turtle()
lin4.speed(0)
lin4.shape("square")
lin4.color("white")
lin4.shapesize(stretch_len=40,stretch_wid=.1)
lin4.penup()
lin4.goto(0,-300)

player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_len=.5,stretch_wid=6)
player1.color("blue")
player1.penup()
player1.goto(x=-350,y=0)

player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_len=.5,stretch_wid=6)
player2.color("red")
player2.penup()
player2.goto(x=350,y=0)

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(x=0,y=260)
score.write("player1: 0 player2 :0",align="center",font=("Courier",14,"normal"))
score.hideturtle()
p1_score , p2_score = 0 , 0

player_speed= 30

def p1_move_up():
    player1.sety(player1.ycor()+player_speed)

def p1_move_down():
    player1.sety(player1.ycor()-player_speed)

def p2_move_up():
    player2.sety(player2.ycor()+player_speed)

def p2_move_down():
    player2.sety(player2.ycor()-player_speed)


window.listen()
window.onkeypress(p1_move_up,"w")
window.onkeypress(p1_move_down,"s")
window.onkeypress(p2_move_up,"Up")
window.onkeypress(p2_move_down,"Down")

while True:
    window.update()
    
    
    ball.setx(ball.xcor() + (ball_dx * ball_speed))
    ball.sety(ball.ycor() + (ball_dy * ball_speed))
    
    if(ball.ycor()>290):
        ball.sety(290)
        ball_dy *= -1
    
    if(ball.ycor()<-290):
        ball.sety(-290)
        ball_dy *= -1
    
    if ball.xcor()<-340 and ball.xcor()>-350 and ball.ycor()> (player1.ycor()-60)and ball.ycor()<(player1.ycor()+60):
        ball.setx(-340)
        ball_dx *= -1
    
    if ball.xcor()>340 and ball.xcor()<350 and ball.ycor()> (player2.ycor()-60)and ball.ycor()<(player2.ycor()+60):
        ball.setx(340)
        ball_dx *= -1
    
    if(ball.xcor()> 390):
        ball.goto(0 , 0)
        ball_dx *= -1 
        score.clear()
        p1_score +=1
        score.write(f"player1: {p1_score} player2 : {p2_score}",align="center",font=("Courier",14,"normal"))
        
    
    if(ball.xcor()< -390):
        ball.goto(0 , 0)
        ball_dx *= -1
        score.clear()
        p2_score +=1
        score.write(f"player1: {p1_score} player2 : {p2_score}",align="center",font=("Courier",14,"normal"))
        