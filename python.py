text = "Go to the next room and shut the door," " while doing so don't forget to get the keys" ", if got your parent's keys" ", don't forget to close the windows as well"

words = tuple(text.split())

for word in words:
    for letter in word:
        if letter.lower() == 'o':
            print("MR.Zizo")


