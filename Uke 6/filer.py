def giveInt(fil):
    infile = open(fil, "r")
    numbers = []

    for line in infile:
        numbers.append(int(line))

    infile.close()    
    return numbers

print(giveInt("fil.txt")[2])