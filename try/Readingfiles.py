# r read, w write, a append, r+ read and write 

EEE_file = open("EEE.txt", "r")

print(EEE_file.readline())
for Color in  EEE_file.readlines():
    print(Color)
print(EEE_file.readlines()[1])
#Puts each line in an array
print(EEE_file.read())

EEE_file.close()
#Always close a file afterwords