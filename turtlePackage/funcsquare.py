import turtle

#to draw square
def square(t,length):
	draw = t.Turtle()
	for i in range(4):
		draw.fd(length)
		draw.lt(90)

#to draw polygon
def polygon(t,length,n):
	draw = t.Turtle()
	for i in range(n):
		draw.fd(length)
		draw.lt(360/n)

#to draw cricle
def cricle(t,radius):
	polygon(t,2*3.14,radius)

def arc(t,radius,angle):
	 draw = t.Turtle()
	 for i in range(angle):
	 	draw.fd(2*3.14)
	 	draw.lt(360/radius)
	 	degree = (360/radius)*180
	 	print(radius, angle, degree)
	 	#degree = 90
	 	#if angle == degree:
	 		#break

#square(turtle,200)
#polygon(turtle,20,6)
arc(turtle,180,45)
#cricle(turtle,50)
turtle.mainloop()