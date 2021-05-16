import turtle
sc=turtle.Screen()
sc.setup(100,100)
d=turtle.Turtle()
d.speed(10)
sc.bgcolor("black")
col=["yellow","blue","white","green"]
c=0
for i in range(50):
	d.forward(i*10)
	d.right(144)
	d.color(col[c])
	if c==3:
		c=0
	else:
		c=c+1
