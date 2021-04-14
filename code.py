def swap():
    f1 = open("essay.txt")
    f2 = open("fake.txt")
    dataA = f1.read()
    dataB = f2.read()
    f1.write(dataB)
    f2.write(dataA)
swap()