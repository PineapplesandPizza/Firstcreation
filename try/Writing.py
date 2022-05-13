
EEE_file = open("EEE.txt", "a")

#If I use w instead of a it'll overwrite all existing text not add
#Also can use w to create a new file. EEE_file = open("EEE1.txt", "w")
#                                     EEE_file.write("\nSpongebob Squarepants")
EEE_file.write("\nFUN")

EEE_file.close()

#EEE_file = open("index.html", "w")
#EEE_file.write("<p>This is HTML<\p>")