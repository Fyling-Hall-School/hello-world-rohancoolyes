def filename():
    shakes1 = []
    file = open("shakes1.txt","r")
    for line in file:
        shakes1.append(line.strip())
    print(shakes1)
