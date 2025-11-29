import turtle
window = turtle.Screen()
window.bgcolor("pink")
window.title("Turtle")
p=turtle.Turtle()
s=0
while True:
    for i in range(6):
        p.forward(s+1)
        p.left(36)
        s=s-5
    s=s+1