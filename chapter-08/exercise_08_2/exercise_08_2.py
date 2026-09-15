"""
"!Head" Shell command in Python!

This is a function that simulates the !Head shell Command in Python
"""

"""
receive as parameter the file you want to read, the number of lines (if the parameter is not fulfilled,
attribute 10 as value of lines you want to read), and the file you want to write the lines you abstracted (if the
parameter is not fulfilled, attribute None as value of file_write)
"""
def head(file_read, lines=10, file_write=None):
    reader = open(file_read, 'r') #open the file you want to read
    #write in the file you want to write, if the destination file is not given, attribute None as value of writer
    writer = open(file_write, 'w') if file_write is not None else None

#create a loop for the quantity of lines you want to read
    for i in range(lines):
        line = reader.readline() #stores the loop number line in the variable line
        if not line:
            break #if you put more lines to read than the file_read has, stop the program in the last one

        if writer is None:
            print(line.strip()) #print the lines the program has read
        else:
            writer.write(line) #write the lines the program has read in the file you want to write

    reader.close() #close the open file, always do this to save memory
    if writer: #if writer has opened a file to write, close
        writer.close()

#this will print the first 10 lines of the Dracula's book
head("pg345.txt")

#this will write the 50 first lines of the Dracula's book in the head_result.txt file
head("pg345.txt", 50, "head_result.txt")



