"""
A function that explores the existence condition and returns Yes (True) or No (False) depending on whether that triangle can be formed.
"""

def is_triangle(side1, side2, side3): 
    # A triangle is only valid if the sum of any two sides is greater than the third.
    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        print("Yes")
    else:
        # If any of the statements above is false, it jumps instantly to this else.
        print("No")

# Test case: a triangle with sides 3, 5, and 7.
# Expected result: "Yes" (3+5>7, 3+7>5, 5+7>3).
is_triangle(3, 5, 7)