import math #import of the module math to use the value of pi

#part 1
radius = 5 #defining the radius of the sphere
volume = (4/3) * math.pi * radius**3 #calculation of the volume of the sphere
print (round(volume, 2)) #print the result of the volume with 2 decimals

#part 2
x = 42 #defining x as 42
print ((math.cos(x))**2 + (math.sin(x))**2) #calculating to see if this will be = 1

#part 3
#the book recommend to do this part with a AI, but i will show the solutions
print (math.e**2) #elevating e to the power of 2
print (math.pow(math.e, 2)) #elevating e to the power of 2 with the function pow
print (math.exp(x)) #elevating e to the power of x (42) with the function exp