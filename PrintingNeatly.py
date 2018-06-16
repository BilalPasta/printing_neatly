breakpoint1 = int(input("Total Number of characters: "))
string1 = input("Enter A String: ")
n = len(string1)
list1 = []
pos = 0
base = 0
wordcount = 0
for i in string1:
    if (i == " "):
        list1.append(string1[base:pos])
        space = pos
        base = pos + 1
        wordcount = wordcount + 1
    pos = pos + 1
wordcount = wordcount + 1
list1.append(string1[space+1:])
counter = 0
totallength = 0
print("Neatly Printed Paragraph:")
while counter < wordcount:
    length = len(list1[counter])
    totallength = totallength + length
    if totallength >= breakpoint1:
        totallength = length
        print("")
        print(list1[counter], end = "")
    else:
        if counter == 0:
            print(list1[counter], end = "")
        else:
            totallength = totallength + 1
            print('',list1[counter], end = "")
    counter = counter + 1

