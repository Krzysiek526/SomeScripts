#!/usr/bin/python3
import turtle
import sys

wn = turtle.Screen()
wn.bgcolor("lightgreen")      # Background color
wn.title("Hello, Tess!")      # Title

tess = turtle.Turtle()
tess.color("blue")            # Change pen color
tess.pensize(7)               # Set pen width

#tess.forward(50)
#tess.left(120)
for i in range (100):
  tess.forward(200+i%7)
  tess.left(95)


turtle.done()

