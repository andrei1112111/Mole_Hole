def create_lines(data):
    data = "\0" + data
    dataa = []
    for i in data.split('\n'):
        while len(i) < 52:
            i += " "
        dataa.append(i)
    data = '\n'.join(dataa)
    k = 0
    с = 0
    line = []
    lines = ["v2.0 raw\n"]
    for i in data:
        if k == 15:
            k = 0
            с += len(line)
            lines.append(' '.join(line) + '\n')
            line = []
        if ord(i) > 256:
            i = "#"
        line.append(hex(ord(i))[2:])
        k += 1
    с += len(line)
    lines.append(' '.join(line) + '\n')
    print(с)
    return lines


# inpp = input("Имя исходного: ")
# outt = input("Имя выходного: ")

import os
for root, dirs, files in os.walk("./graphics"):
    for filename in files:
        if filename[-4:] == '.txt':
            print(filename, end=' ')
            with open("graphics/" + filename, "r") as inp:
                with open("graphics/" + filename[:-4], "w") as out:
                    res = create_lines(inp.read())
                    out.writelines(res)

