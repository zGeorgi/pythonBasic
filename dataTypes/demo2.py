# list
values = [1, 2, "String", 4.5]

print(values[0])  # print frist value
print(values)

print(values[-1])  # print last value

print(values[1:3])  # print sublist from <index> to <index-1>

values.insert(3, "zayakov")  # insert value in the list
print(values)

values.append(5)  # add value to the end on the list
# update value
values[2] ="GEORGI"

del values[0]  # delete value on the firs location