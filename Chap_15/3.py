import turtle
import random
def tree(branchLen,t):
    t.pensize(branchLen/10)
    A=random.randint(10,30)
    B=random.randint(12,15)
    if branchLen > 5:
        t.pencolor('brown')
        t.forward(branchLen)
        t.right(A)
        tree(branchLen-B,t)
        t.left(2*A)
        t.pencolor('lightgreen')
        tree(branchLen-B,t)
        t.right(A)
        t.backward(branchLen)
        t.pencolor('brown')

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.speed(0)
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()