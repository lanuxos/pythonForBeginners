import turtle, random
tao = turtle.Turtle()
tao.shape('turtle')
tao.pensize(5)
color = ['red', 'orange', 'blue', 'grey', 'green',
         'black', 'yellow', 'purple', 'brown', 'cyan']
for i in color:
    tao.color(i)
    f = random.randint(50, 100)
    for j in range(4):
        tao.forward(f)
        tao.left(90)
    tao.penup()
    tao.goto(random.randint(-100, 100), random.randint(-100,100))
    tao.pendown()
