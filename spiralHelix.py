import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("yellow")
turtle_screen.title("Python Turtle")

turtle_instance = turtle.Turtle()
turtle.speed(0)

color_list = ['red', 'blue', 'purple', 'green', 'orange']

for i in range(6):
    turtle_instance.color(color_list[i % len(color_list)])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)

turtle.mainloop()

