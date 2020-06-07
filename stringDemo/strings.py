str = "some string for handle! "
str1 = "+ somthing to concatenate"
str2 = "Some"

print(str[0])       #pring index from string

print(str[0:5])  # extract substring from string

print(str + str1)   # concatenate strings(only two strings or more)

print(str2 in str)      # check if substring is in the string

var = str.split("o")    # split the string on parts
print(var)

str3 = " for trim "
print(str3)
print(str3.strip())     # trim the white spaces on both sides
print(str3.lstrip())    # trim the left side
print(str3.rstrip())    # trimt the right side

print(str2.__len__())   #size like a number of charachters
var2 = str.__contains__("for")
print(var2)

print(str.capitalize())     # make first letter to be uppercase
print(str.replace("for", "to"))  # replace first with the second str
print(str2.lower())     #return lowercase string
