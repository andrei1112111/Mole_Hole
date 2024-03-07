#   ---CAAL2O4--- engine
from graphics import *
import os


texts = {0: ("", 37),
         1: ("ВЫ ТКНУЛИ ПАЛКОЙ В ПОЛ. НИЧЕГО НЕ ПРОИЗОШЛО?", 15)}  # количество букв строго четно. число - отступ
directed_mole = {1: list(MDU.split('\n')[1:-1]),
                 2: list(MDR.split('\n')[1:-1]),
                 3: list(MDD.split('\n')[1:-1]),
                 4: list(MDL.split('\n')[1:-1])}

INVENTORY = [DEFAULT_STICK]

CURRENT_TEXT = 0
CURRENT_HP = 10
CURRENT_ST = 0
CURRENT_HG = 1

# парсинг карты
cardd = open("map.txt").read().split('\n')
width, height = len(cardd[0]), len(cardd)
player_cods = [0, 0]
direction = {3: (1, 0), 1: (-1, 0), 4: (0, -1), 2: (0, 1)}
player_direct = 1
"""
    N(1)
W(4)      E(2)
    S(3)
"""
card = [[" " for _ in range(width)] for _ in range(height)]
for y, i in enumerate(cardd):
    for x, j in enumerate(cardd[y]):
        card[y][x] = cardd[y][x]
        if cardd[y][x] == 'P':
            player_cods = [y, x]
            card[y][x] = " "


def print3D(y, x, display):
    to_print = []
    if player_direct in [1, 3]:
        if card[player_cods[0] + direction[player_direct][0]][player_cods[1]] == '#':
            to_print.append(FFl)
        elif card[player_cods[0] + 2 * direction[player_direct][0]][player_cods[1]] == '#':
            to_print.append(FFFl)
        elif card[player_cods[0] + 3 * direction[player_direct][0]][player_cods[1]] == '#':
            to_print.append(FFFFl)
        # right side
        if card[player_cods[0]][player_cods[1] - direction[player_direct][0]] == '#':
            to_print.append(RFl)
            if card[player_cods[0] + direction[player_direct][0]][
                player_cods[1] - direction[player_direct][0]] == '#' and not (FFl in to_print):
                to_print.append(FRFl)
        elif card[player_cods[0] + direction[player_direct][0]][player_cods[1] - direction[player_direct][0]] == '#':
            to_print.append(RFFl)
            if not (FFl in to_print):
                to_print.append(FRFl)
        if card[player_cods[0] + 2 * direction[player_direct][0]][player_cods[1] - direction[player_direct][0]] == '#':
            to_print.append(RFFFl)
        # left side
        if card[player_cods[0]][player_cods[1] + direction[player_direct][0]] == '#':
            to_print.append(LFl)
            if card[player_cods[0] + direction[player_direct][0]][
                player_cods[1] + direction[player_direct][0]] == '#' and not (FFl in to_print):
                to_print.append(FLFl)
        elif card[player_cods[0] + direction[player_direct][0]][player_cods[1] + direction[player_direct][0]] == '#':
            to_print.append(LFFl)
            if not (FFl in to_print):
                to_print.append(FLFl)
        if card[player_cods[0] + 2 * direction[player_direct][0]][player_cods[1] + direction[player_direct][0]] == '#':
            to_print.append(LFFFl)
        # front front left/right
        if not (FFl in to_print or FFFl in to_print):
            if card[player_cods[0] + 2 * direction[player_direct][0]][player_cods[1] - direction[player_direct][0]] == '#':
                to_print.append(FFRFl)
            if card[player_cods[0] + 2 * direction[player_direct][0]][
                player_cods[1] + direction[player_direct][0]] == '#':
                to_print.append(FFLFl)
        if card[player_cods[0] + 3 * direction[player_direct][0]][player_cods[1] + direction[player_direct][0]] == '#' and not (FFLFl in to_print):
            to_print.append(LFFFFl)
        if card[player_cods[0] + 3 * direction[player_direct][0]][player_cods[1] - direction[player_direct][0]] == '#' and not (FFRFl in to_print):
            to_print.append(RFFFFl)

    if player_direct in [2, 4]:
        if card[player_cods[0]][player_cods[1] + direction[player_direct][1]] == '#':
            to_print.append(FFl)
        elif card[player_cods[0]][player_cods[1] + 2 * direction[player_direct][1]] == '#':
            to_print.append(FFFl)
        elif card[player_cods[0]][player_cods[1] + 3 * direction[player_direct][1]] == '#':
            to_print.append(FFFFl)
        # right side
        if card[player_cods[0] + direction[player_direct][1]][player_cods[1]] == '#':
            to_print.append(RFl)
            if card[player_cods[0] + direction[player_direct][1]][
                player_cods[1] + direction[player_direct][1]] == '#' and not (FFl in to_print):
                to_print.append(FRFl)
        elif card[player_cods[0] + direction[player_direct][1]][player_cods[1] + direction[player_direct][1]] == '#':
            to_print.append(RFFl)
            if not (FFl in to_print):
                to_print.append(FRFl)
        if card[player_cods[0] + direction[player_direct][1]][player_cods[1] + 2 * direction[player_direct][1]] == '#':
            to_print.append(RFFFl)
        # left side
        if card[player_cods[0] - direction[player_direct][1]][player_cods[1]] == '#':
            to_print.append(LFl)
            if card[player_cods[0] - direction[player_direct][1]][
                player_cods[1] + direction[player_direct][1]] == '#' and not (FFl in to_print):
                to_print.append(FLFl)
        elif card[player_cods[0] - direction[player_direct][1]][player_cods[1] + direction[player_direct][1]] == '#':
            to_print.append(LFFl)
            if not (FFl in to_print):
                to_print.append(FLFl)
        if card[player_cods[0] - direction[player_direct][1]][player_cods[1] + 2 * direction[player_direct][1]] == '#':
            to_print.append(LFFFl)
        # front front left/right
        if not (FFl in to_print or FFFl in to_print):
            if card[player_cods[0] + direction[player_direct][1]][player_cods[1] + 2 * direction[player_direct][1]] == '#':
                to_print.append(FFRFl)
            if card[player_cods[0] - direction[player_direct][1]][
                player_cods[1] + 2 * direction[player_direct][1]] == '#':
                to_print.append(FFLFl)
        if card[player_cods[0] + direction[player_direct][1]][player_cods[1] + 3 * direction[player_direct][1]] == '#' and not (FFRFl in to_print):
            to_print.append(RFFFFl)
        if card[player_cods[0] - direction[player_direct][1]][player_cods[1] + 3 * direction[player_direct][1]] == '#' and not (FFLFl in to_print):
            to_print.append(LFFFFl)

    for yy, j in enumerate(nothing.split("\n")[1:-1]):
        for xx, k in enumerate(j):
            display[y + yy][x + xx] = k
    for i in reversed(to_print):
        for yy, j in enumerate(i.split("\n")[1:-1]):
            for xx, k in enumerate(j):
                if k != " ":
                    display[y + yy][x + xx] = k


def printText(y, x, display):
    # 74 symbols for text
    for i in range(texts[CURRENT_TEXT][1]):
        display[y][x + i] = ' '
    for i in range(74 - 2 * texts[CURRENT_TEXT][1]):
        display[y][x + texts[CURRENT_TEXT][1] + i] = texts[CURRENT_TEXT][0][i]
    for i in range(texts[CURRENT_TEXT][1]):
        display[y][x + i + 74 - texts[CURRENT_TEXT][1]] = ' '
    pass


def printInv(y, x, display):
    # PRINT BARS
    for i in range(0, CURRENT_HP):
        display[y][x+55+i] = '#'
    for i in range(CURRENT_HP, 9):
        display[y][x+55+i] = ' '
    if CURRENT_HP == 10:
        display[y][x + 67] = '1'
        display[y][x + 68] = '0'
    else:
        display[y][x + 68] = str(CURRENT_HP)

    for i in range(0, CURRENT_ST):
        display[y+1][x+55+i] = '#'
    for i in range(CURRENT_ST, 9):
        display[y+1][x+55+i] = ' '
    if CURRENT_ST == 10:
        display[y+1][x + 67] = '1'
        display[y+1][x + 68] = '0'
    else:
        display[y+1][x + 68] = str(CURRENT_ST)

    for i in range(0, CURRENT_HG):
        display[y+2][x+55+i] = '#'
    for i in range(CURRENT_HG, 9):
        display[y+2][x+55+i] = ' '
    if CURRENT_HG == 10:
        display[y+2][x + 67] = '1'
        display[y+2][x + 68] = '0'
    else:
        display[y+2][x + 68] = str(CURRENT_HG)
    # PRINT ITEMS (10 symbols between)
    for k, item in enumerate(INVENTORY):
        item = list(item.split('\n')[1:-1])
        for yy in range(4):
            for xx in range(9):
                display[y+yy][x+(k*10)+xx] = item[yy][xx]
    pass


def printMmap(y, x, display):
    c = 3  # координата центра на карте
    miniMap = [["░" for _ in range(7)] for _ in range(7)]
    for i in [-3, -2, -1, 0, 1, 2, 3]:
        for j in [-3, -2, -1, 0, 1, 2, 3]:
            if (0 <= player_cods[0] + i < height) and (0 <= player_cods[1] + j < width):
                miniMap[i + 3][j + 3] = card[player_cods[0] + i][player_cods[1] + j]
                if miniMap[i + 3][j + 3] == "#":
                    miniMap[i + 3][j + 3] = "█"
    for i in range(0, 20, 3):
        for j in range(0, 20, 3):
            for xx in range(3):
                for yy in range(3):
                    display[y + i + yy][x + j + xx] = miniMap[i//3][j//3]
    for xx in range(3):
        for yy in range(3):
            display[y + 9 + yy][x + 9 + xx] = directed_mole[player_direct][yy][xx]


def move():
    global player_direct, CURRENT_TEXT
    CURRENT_TEXT = 0
    inp = input("Type: (W, A, D, Q, 1-5 item number)")
    if inp == 'a':
        player_direct -= 1
        if player_direct < 1:
            player_direct = 4
    elif inp == 'd':
        player_direct += 1
        if player_direct > 4:
            player_direct = 1
    elif inp == 'w':
        if player_direct in [1, 3] and card[player_cods[0] + direction[player_direct][0]][player_cods[1]] != "#":
            player_cods[0] += direction[player_direct][0]
        elif player_direct in [2, 4] and card[player_cods[0]][player_cods[1] + direction[player_direct][1]] != "#":
            player_cods[1] += direction[player_direct][1]
    elif inp == 'q':
        exit(0)
    elif '1' <= inp <= '5':
        if len(INVENTORY) >= int(inp):
            a = INVENTORY[int(inp)-1]
            if INVENTORY[int(inp)-1] == DEFAULT_STICK:
                CURRENT_TEXT = 1


def fprint(display):
    os.system('clear')
    for i in display:
        for j in i:
            print(j, end='')
        print()


if __name__ == "__main__":
    # display init
    display = [["#"] * 76]
    for i in range(21):
        display.append(["#"] + [" "] * 52 + ["#"] + [" "] * 21 + ["#"])
    display.append(["#"] + [" "] * 52 + ["#"] * 23)
    for i in range(5):
        display.append(["#"] + [" "] * 52 + ["#"] + [" "] * 21 + ["#"])
    display.append(["#"] * 76)
    display.append(["#"] + [" "] * 74 + ["#"])
    display.append(["#"] * 76)
    display.append(list("#         #         #         #         #         # HP |          |(  /10) #"))
    display.append(list("#         #         #         #         #         # ST |          |(  /10) #"))
    display.append(list("#         #         #         #         #         # HG |          |(  /10) #"))
    display.append(list("#         #         #         #         #         #                        #"))
    display.append(["#"] * 76)
    # game loop
    while True:
        print3D(1, 1, display)
        printMmap(1, 54, display)
        printText(29, 1, display)
        printInv(31, 1, display)
        fprint(display)
        move()
