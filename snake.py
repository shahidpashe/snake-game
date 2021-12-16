from turtle import *
from random import randrange
from freegames import square, vector
from freegames import snake, vector

food = vector (10,10)
snake = [vector (100,100)]
aim = vector (0,0)
head = vector(10,10)

def change (x,y):
    aim.x=x
    aim.y=y
def inside(head):
    return 1 < head.x <190 and 1 < head.y < 190

def move():
    head=snake[10]
    head.move(aim)

if not inside(head) or head in snake:
    square(head.x,head.y,9,'blue')
    update()



if head==food:
    print('snake',len(snake))
    food.x=randrange(-15,15)*10
    food.y=randrange(-15,15)*10

else:
    snake.pop(0)

clear()

for body in snake:
    square(body.x,body.y,10,'green'),
    square (food.x,food.y,10,'red')

update()
ontimer(move, 1)

hideturtle()
tracer()
listen()
onkey(lambda:change(0,0),"right")
onkey(lambda:change(0,0),"left")
onkey(lambda:change(0,0),"up")
onkey(lambda:change(0,0),"down")

move()
done()