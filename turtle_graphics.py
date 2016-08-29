from turtle import *
import random

screen = Screen()
screen.screensize(500,500,"white")

pen = Pen()
pen.speed(90)

size = 20

for i in range (999):

	#r = random.randint(0,255)
	#g = random.randint(0,255)
	#b = random.randint(0,255)
	r = 0
	g = 0
	b = 0

	randcol = (r,g,b)

	colormode(255)

	pen.color(randcol)
	pen.circle(size, steps = 99)
	pen.right(60)
	size += 3


