file = open("Git_comands")

list = file.readlines()    #return lines in a List

print(list[1])
for ln in list:
    print(ln)

file.close()