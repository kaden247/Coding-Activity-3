import turtle

screen = turtle.Screen()  

Kyle = turtle.Turtle()
Kyle.speed(3) 
Kyle.forward(50) 
Kyle.left(45) 
Kyle.forward(50)
Kyle.left(45)
Kyle.forward(50)
Kyle.left(45)
Kyle.forward(50)
Kyle.left(45)
Kyle.forward(50)
Kyle.left(45)
Kyle.forward(50)
Kyle.left(45)
Kyle.forward(50)
Kyle.left(45)
Kyle.forward(50)
Kyle.left(45)

turtle.exitonclick()

ts = turtle.getscreen().getcanvas()
ts.postscript(file="drawing.eps")