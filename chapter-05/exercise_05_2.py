from time import time

now = int(time()) #making int to disregard fractions of seconds (it won't change the final calculation)

days = (now // 86400) #to make seconds days, divide per 86400 (// because we want a whole number)

seconds = now % 60 #the rest of this division is the seconds we need to display the complete time
minutes = (now // 60) % 60 #the first equation will define the minutes since the Epoch, we need the % to fit on a clock
hours = (now // 3600) % 24 #same logic as above, but for hours

"""
The print(f) just allows you to display a variable's value, it will be cover later on the book
"""

print(f"{days} since the Unix/Epoch")
print(f"The time is: {hours}h, {minutes}min, {seconds}s")

