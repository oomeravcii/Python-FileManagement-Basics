########################################################################################################################
##                                                                                                                    ##
##                          Ultimate Python File Management CheatSheet. - Learn basics of Tkinter.                    ##
##                                                                                                                    ##
##                         I recommend you to use "Better Comments" extension for better experience.                  ##
##                                                                                                                    ##
########################################################################################################################


#! File reading "r" -> The file must exist.

# file = open("planlar.txt","r",encoding="utf-8") #? Opens the file. We use "utf-8" to write Turkish characters.

# print(file.read()) #? Reads the file and prints it to the screen.
# print(file.read(50)) #? Reads the specified number of characters from the file and prints them to the screen.
# print(file.readline()) #? Reads the entire line we are on and prints it to the screen.
# print(file.readline(50)) #? Reads the specified number of characters from the line we are on and prints them to the screen.
# print(file.readlines()) #? Reads all lines and creates a list, where each line is an item.
# print(file.tell()) #? Tells us where the cursor is.
# file.seek(5) #? Changes the position of the cursor.

# file.close()

#----------------------------

#! File writing "w" -> If the file does not exist, it is automatically created. (Overwrites existing content.)

# file = open("planlar.txt","w",encoding="utf-8")

# file.write("Hello") #? Writes text to the file.
# file.writelines(["7:30 Breakfast\n","9:00 Running\n","11:00 Reading a Book\n"]) #? Writes lines as a list of items.

# file.close()

#---------------------------

#! File writing "a" -> If the file does not exist, it is automatically created. (Starts writing at the end of existing content.)

# file = open("planlar.txt","a",encoding="utf-8")

# file.write("12:00 Sightseeing\n") #? Writes text to the file.

# file.close()

#-------------------------

# Files can also be used this way. (Files are automatically closed after the operation is finished.)

# with open("planlar.txt","w",encoding="utf-8") as file:
#    file.write("14:00 Reading a Book\n")
#    file.writelines(["15:00 Swimming Lesson\n","16:00 Running\n"])