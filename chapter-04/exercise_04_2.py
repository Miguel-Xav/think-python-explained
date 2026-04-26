from jupyturtle import make_turtle, forward, left

def rectangle(length, height): # create a function rectangle with the length and height as parameters
    for i in range(2): # the loop is for the 2 pairs of sides (2+2=4 sides)
        forward(length) # move the turtle forward by the length parameter
        left(90) # turn the turtle left by 90 degrees (to make the right edge)
        forward(height) # move the turtle forward by the height parameter
        left(90) # turn again left by 90 degrees to make the left edge and complete the rectangle

make_turtle() # create the turtle to start drawing
rectangle(length=80, height=40) # call the rectangle function with the length and height values, you can change the values to make different rectangles

#bonus!!
# I don't think this is a real bonus, but since I will use perfect_rectangle in the future, I include it here!

def perfect_rectangle(length): # this function will always make a perfect rectangle with the length and the height being half of the length
    height = length / 2 # this will make the height always half of the length
    for i in range(2): # create a loop to repeat 2 times for the 2 pairs of sides
        forward(length)
        left(90)
        forward(height)
        left(90)

# To test just remove the # on the line below and change the length value to make different perfect rectangles
#perfect_rectangle(length=80)
