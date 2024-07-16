from turtle import *

#we want draw a house

#draw a square

width(7)

color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of squera

#drawing a door

forward(70)
left(90)

color("yellow")
begin_fill()

forward(100)
right(90)

forward(70)
right(90)

forward(100)
end_fill()

#end of door

#drawing a roof

penup()
goto(200,200)
pendown()

color("red")
begin_fill()

right(150)
forward(200)

left(120)
forward(200)
end_fill()

#end of roof

penup()
goto(35,150)
pendown()

#drawing a windows

color("blue")
begin_fill()

left(30)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

penup()
goto(175,150)
pendown()

forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)
end_fill()

#end of windows

#finish drawing a house

exitonclick()