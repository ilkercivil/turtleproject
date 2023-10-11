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
'''''
star_turtle=turtle.Turtle()
side_length=100
interior_angle = 180 - (360 / 5)
for i in range(5):
    star_turtle.forward(side_length)
    star_turtle.right(interior_angle)
    star_turtle.forward(side_length)
    star_turtle.left(72 - interior_angle)

turtle.done()

'''''

# Turtle nesnesini oluştur
square_turtle = turtle.Turtle()

# Başlangıç kenar uzunluğu
side_length = 200

# Kareleri çiz
for i in range(10):
    # Kare çiz
    for j in range(4):
        square_turtle.forward(side_length)
        square_turtle.left(90)

    # Sonraki kareye geçmeden önce boyutu küçült
    side_length -= 20

    # Kareler arasındaki boşluğu bırak
    square_turtle.penup()
    square_turtle.forward(10)
    square_turtle.right(90)
    square_turtle.forward(10)
    square_turtle.right(90)
    square_turtle.pendown()

# Çizimi tamamla ve pencereyi kapat
turtle.done()
