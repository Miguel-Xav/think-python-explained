from jupyturtle import make_turtle, forward, left

def parallelogram(length, height, angle):
    for i in range(2): # the loop is for the 2 pairs of sides
        forward(length) 
        left(angle)
        forward(height)
        left(180 - angle) # the angle between the sides is 180 - angle


def perfect_rectangle_v1(length):
    height = length / 2 # the height is half of the length
    angle = 90 # the angle between the sides is 90 degrees, on the parallelogram function, the angle is 180 - 90 = 90 degrees, so it will be a rectangle
    parallelogram(length, height, angle) #the function is called with the length, height and angle values of perfect_rectangle_v1()

def perfect_rhombus(length):
    height = length
    angle = 60 # the angle between the sides is 60 degrees, on the parallelogram function, the angle is 180 - 60 = 120 degrees, so it will be a rhombus
    parallelogram(length, height, angle)

"""
if you want to make via input (rectangle(length=x, height=y, angle=z))
just put parallelogram(length, height, angle)
"""

# To make the drawn equal to the book

from jupyturtle import right, penup, pendown

def jump(length):
    penup()
    forward(length)
    pendown()


def make_draws(length, height, angle): # change the function because now we will have a parallelogram shape
    for i in range(2):
        forward(length)
        left(angle)
        forward(height)
        left(180 - angle)


def perfect_rectangle(length): # same thing
    angle = 90
    height = length / 2
    make_draws(length, height, angle)

def rhombus(length): # same thing
    angle = 60
    height = length
    make_draws(length, height, angle)

def parallelogram2(length): # we will fuse the rectangle with the rhombus to make a parallelogram
    angle = 60 # angle of the rhombus
    length_double = length * 2 # to have the same length as the rectangle we need to double, if not it will be a rhombus
    height = length
    make_draws(length_double, height, angle)


make_turtle()

# to start the drawing from the left
left(180)
jump(125)
right(180)
# to make the drawing aligned, the values need to be this
perfect_rectangle(60)
jump(80)
rhombus(35)
jump (70)
parallelogram2(35)

# I didn't make an automatic function to calculate because some of the things needed to do this are further in the book