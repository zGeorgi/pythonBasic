with open("text.txt", "r") as reader:
    content = reader.readlines()
    #reversed(content)       # reverse the content
    with open("text.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)
