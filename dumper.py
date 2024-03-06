def create_lines(data):
    k = 0
    line = []
    lines = ["v2.0 raw\n"]
    for i in data:
        if k == 15:
            k = 0
            lines.append(' '.join(line) + '\n')
            line = []
        line.append(hex(ord(i))[2:])
        k += 1
    return lines


with open(input("Имя исходного: "), "r") as inp:
    with open(input("Имя выходного: "), "w") as out:
        out.writelines(create_lines(inp.read()))

# 16 чисел на строку
