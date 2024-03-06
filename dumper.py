def create_lines(data):
    data = "\0" + data
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
        line.append(hex(ord(i))[2:])
        k += 1
    с += len(line)
    lines.append(' '.join(line) + '\n')
    print(с)
    return lines


with open(input("Имя исходного: "), "r") as inp:
    with open(input("Имя выходного: "), "w") as out:
        res = create_lines(inp.read())
        out.writelines(res)

# 16 чисел на строку
