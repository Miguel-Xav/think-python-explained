""""
I've take the solution from github.com/dexhunter/TP_solutions and translate to JupyTurtle and Python 3
Go and support the dexhunter solutions too, it's another way to see the same process!
I will explain the diferences from the dexhunter code line por line
"""


import math
from jupyturtle import make_turtle, forward, left, right

# a problem i've noticed in the dexhunter is make the calculation of the petals everytime inside each loop
# the only change i made was to separate these processes 
def arc(s_len, s_ang, n_steps):
    for i in range(n_steps):
        forward(s_len)
        left(s_ang)
# now the arc is a loop to draw individual petals

def flower(n_petal, size_petal, angle):
    """"
    Drawn a flower with radial symmetry, based on github.com/dexhunter/TP_solutions/blob/master/ex04_02.py

    Args:
        n_petals (int): quantity of petals
        petal_size (float): radius of curvature
        angle (float): opening of the petal arch in degrees
    """
    arc_l = size_petal * math.radians(angle)
    n_steps = int(arc_l / 12) + 1  
    s_len = arc_l / n_steps
    s_ang = float(angle) / n_steps
    rotation = 360.0 / n_petal
    # the calculus is out of the loop

    for _ in range(n_petal): # the underscore is used when you not need the value of the index
        for _ in range(2):
            arc(s_len, s_ang, n_steps)
            left(180 - angle)
        right(rotation)
    # loop calling the arc for each petal that is going to be drawn

make_turtle(delay=0)
flower(n_petals=50, petal_size=70, angle=80)
# try change the values and play with the code!