import turtle
drawing_board= turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Python Turtle")
turtle_instance= turtle.Turtle()
'''''
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)

turtle.done()
'''
'''
for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.left(90)
turtle.done()
'''
star_turtle=turtle.Turtle()
side_length=100
interior_angle = 180 - (360 / 5)
for i in range(5):
    star_turtle.forward(side_length)
    star_turtle.right(interior_angle)
    star_turtle.forward(side_length)
    star_turtle.left(72 - interior_angle)

turtle.done()
