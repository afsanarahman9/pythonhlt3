a_list = ["3", " 45", "83", "21"]
textfile = open("numbers.txt", "w")
for element in a_list:
    textfile.write(element + "\n")
textfile.close()
with open("numbers.txt", "r") as textfile:
    data = textfile.read().replace("\n", ",")
    textfile.close()
textfile = open("numbers.txt", "a")
textfile.write("hello")
textfile.close()
