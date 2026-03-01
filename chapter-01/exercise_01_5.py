## How many seconds exists in 42 minutes and 42 seconds?
# remembering that * multiplies and + adds
print ((42*60)+42)    #first transform the 42 minutes in seconds, and add the 42 seconds. Print is the command to show the result in the terminal, this will be covered further in the book

## How many miles exists in 10 kilometers?
mile = 1.61             #miles in kilometers
# remembering that / divide
print (round(10/mile))

## If you print 10km in 42 minutes and 42 seconds, what is gone be your pace? (time x miles in seconds)
print ( round( ( (42*60)+42 ) / (10/mile) ) )  # with this count you will have the result pace/seconds in miles

## What is your average pace in minutes and seconds per mile?
minutes = int((42+ (42/60)) / (10/mile))
seconds = (minutes * 6)
print (f"pace per mile: {minutes}min and {seconds}s")
# focus only on the raw calculation, the print(f) will be addressed later, and I did it this way for better code organization

## What is your avarege speed in miles per hour?
speed_per_hour = 42/60 + 42 / 3600
print (round((10/mile) / speed_per_hour))