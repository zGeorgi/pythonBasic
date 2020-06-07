try:
    with open("/georgi/PycharmProjects/PythonBasic/files/text.txt", "r") as reader:
        reader.read()
except:
    print("Something fail in try block!")

try:
    with open("/georgi/PycharmProjects/PythonBasic/files/text.txt", "r") as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("cleaning up")