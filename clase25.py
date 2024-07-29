with open("./text.txt",'w+') as file:
    for line in file:
        print(line)
    file.write("Nuevas cosas\n")
    file.write("Otra cosa cosas\n")