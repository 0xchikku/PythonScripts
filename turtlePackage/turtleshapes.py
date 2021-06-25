import turtle
import math


draw = turtle.Turtle()

def polyline(t, lineSegment, length, angle):
	for i in range(lineSegment):
		t.fd(length)
		t.lt(angle)

def square(t,length):
	"""
	This Function is used to Draw Square
	"""
	angle = 90
	length = length
	side = 360/angle
	for i in range(int(side)):
		t.fd(length)
		t.lt(angle)

def polygon(t,length,side):
	angle = 360/side
	length = length
	#side = 360/side
	polyline(t,side,length,angle)

#cricle with length of the each line segment is 3
def circles(t,radius):
	"""
	This Function is used to Draw Cricle
	"""
	circumference = 2 * math.pi * radius
	side = int(circumference/3)+1 #line Segment
	length = circumference/side #length of each line segment
	polygon(t,length,side)
	area = math.pi * radius**2
	print(f'Circumference = {circumference}, Radius = {radius}, Area = {area}, length = {length}, Side = {side}')

#cricle with line segment as constant
def circle(t,radius,side):
	"""
	This Function is used to Draw Cricle
	"""
	circumference = 2 * math.pi * radius
	#side #line segment
	length = circumference/side #length of each line segment
	polygon(t,length,side)
	area = math.pi * radius**2
	print(f'Circumference = {circumference}, Radius = {radius}, Area = {area}, length = {length}, Side = {side}')

def arc(t,radius,angle):
	"""
	This Function is used to Draw An Arc
	"""
	arc_length = 2 * math.pi * radius * angle / 360
	lineSegment = int(arc_length/3) + 1
	step_length = arc_length / lineSegment
	step_angle = angle / lineSegment

	polyline(t, lineSegment, step_length, step_angle)
	print(f'Arc_length = {arc_length}, radius = {radius}, lineSegment = {lineSegment}, step_length = {step_length}, step_angle = {step_angle}, angle = {angle}')
 
# square(draw,80)
# polygon(draw,80,6)
# circles(draw,90)
# circle(draw,90,50)
# circle(draw,100,20)
# for i in range(10):
# 	circle(draw,30)
# arc(draw,90,360)

turtle.mainloop()