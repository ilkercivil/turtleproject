import turtle

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
