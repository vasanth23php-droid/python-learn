myList = open("test.txt")
print(myList.read())
with open("testFile.txt", mode="r") as myFile:
    print(myFile.readlines())
with open("testFile.txt", mode="r+") as myFile:
    print(myFile.readlines())
with open("testFile.txt", mode="r+") as myFile:
    myFile.write("Another example of file operation in a python")
    print(myFile.readlines())
with open("testFile.txt", mode="w") as myFile:
    myFile.write("Nested example of file operation in a python")
with open("testFile.txt", mode="a") as myFile:
    myFile.write("Another Nested example of file operation in a python")
