file = open("Git_comands")

line = file.readline()  #return line from the file

while line != "":
    print(line)
    line = file.readline()

list = file.readlines()    #return lines in a List
file.close()
