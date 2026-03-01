#Part 1
# remembering that * multiplies and + adds
print ((42*60)+42)    #first transform the 42 minutes in seconds, and add the 42 seconds. Print is the command to show the result in the terminal, this will be covered further in the book

#Part 2
mile = 1.61             #miles in kilometers
# remembering that / divide
print (round(10/mile))

#Part 3
print ( round( ( (42*60)+42 ) / (10/mile) ) )  # with this count you will have the result pace/seconds in miles

#Part 4
minutes = int((42+ (42/60)) / (10/mile))
seconds = (minutes * 6) 
print (f"pace per mile: {minutes}min and {seconds}s")
# focus only on the raw calculation, the print(f) will be addressed later, and I did it this way for better code organization

#Part 5
speed_per_hour = 42/60 + 42 / 3600 #first transform the 42 minutes in hours, and then the 42 seconds in hours, and add them together to have the speed per hour
print (round((10/mile) / speed_per_hour)) #first transform the 10 miles in kilometers, and then divide by the speed per hour to have the time in hours