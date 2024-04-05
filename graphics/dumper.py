def create_lines(data):
    # dataa = []
    # for i in data.split('\n'):
        # while len(i) < 20:
        #     i += " "
        # dataa.append(i)
    # data = '\n'.join(dataa)
    k = 0
    с = 0
    line = []
    lines = ["v2.0 raw\n"]
    for i in data:
        # if i == 'P':
        #     i = ' '
        # if i == "\n":
        #     continue
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

# import os
# for root, dirs, files in os.walk("./graphics"):
#     for filename in files:
#         if filename[-4:] == '.txt':
#             print(filename, end=' ')
#             with open("graphics/" + filename, "r") as inp:
#                 with open("graphics/" + filename[:-4], "w") as out:
#                     data = "\0" + inp.read()
#                     res = create_lines(data)
#                     out.writelines(res)

# with open("graphics/" + "test_map.txt", "r") as inp:
#     with open("graphics/" + "test_map", "w") as out:
#         data = "\0" + chr(4) + chr(3) + chr(2) + inp.read()
#         res = create_lines(data)
#         out.writelines(res)

with open("graphics/texts/items/" + "centipede.txt", "r") as inp:
    with open("graphics/texts/items/" + "centipede", "w") as out:
        data = inp.read()
        res = create_lines(data)
        out.writelines(res)

# with open("graphics/" + "atackBoard.txt", "r") as inp:
#     with open("graphics/" + "atackBoard", "w") as out:
#         data = "\0" + inp.read()
#         res = create_lines(data)
#         out.writelines(res)
