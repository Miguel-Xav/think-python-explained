from jupyturtle import make_turtle, forward, left

def rhombus(length, angle): # differently from the rectangle, the rhombus has an angle parameter to make the inclination
    complementary_angle = 180 - angle # the complementary angle is the angle between the sides, it is 180 - angle because the sum of the angles in a parallelogram is 360 degrees, and we have 2 angles of angle and 2 angles of complementary_angle, so we need to subtract the angle from 180 to get the complementary_angle
    for i in range(2): # the loop to make the 2 pairs of sides
        forward(length) 
        left(angle) # this will make the obtuse inclination
        forward(length)
        left(complementary_angle) # this will make the acute inclination and complete the rhombus
# !REMEMBER THAT THE ANGLE IS NOT OF THE DRAWN, IT'S FOR THE TURTLE TO TURN!

make_turtle()
rhombus(length=50, angle=60)

##bonus!!
# same thing as the perfect rectangle, i will use this perfect_rhombus function in the future, so i include it here

def perfect_rhombus(length):
    angle = 60
    complementary_angle = 180 - angle # to calculate the complementary angle
    for i in range(2):
        forward(length)
        left(angle)
        forward(length)
        left(complementary_angle)