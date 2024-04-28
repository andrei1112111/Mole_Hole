from random import choice, randint  # выбирает случайный элемент из списка


# random.seed(1)

"""ГЕНЕРАЦИЯ ЛАБИРИНТА"""
"""
121 byte - maze image
8 byte - getN result
6 byte - variables
100 byte - stack (50 * 2)
------------
Total: 235 byte
"""

# map size
MAPSIZE = 11
start = MAPSIZE + 1  # координаты начальной точки ((x, y) -> (1, 1) на матрице)


def printF(cur):
    print('\n\n')
    #  вывод лабиринта ----------------
    for i in range(MAPSIZE):
        for j in range(MAPSIZE):
            print(chr(mapp[i * MAPSIZE + j]), end=' ')
        print()


def getN(cell):  # получить не занятых соседей клетки
    res = []
    if (cell-1) % MAPSIZE != 0:                   # клетка слева
        res.append((cell - 2, cell - 1))
    if (cell+2) % MAPSIZE != 0:             # клетка справа
        res.append((cell + 2, cell + 1))
    if (cell + MAPSIZE + MAPSIZE) < (MAPSIZE * MAPSIZE):  # клетка снизу
        res.append((cell + MAPSIZE + MAPSIZE, cell + MAPSIZE))
    if (cell - MAPSIZE - MAPSIZE) >= 0:                             # клетка сверху
        res.append((cell - MAPSIZE - MAPSIZE, cell - MAPSIZE))
    return [i for i in res if (mapp[i[0]] == 0)]


# Выход уже был
ext = False  # пока небыло

#  Стартовое поле памяти ----------------
mapp = ([35] * MAPSIZE + ([35] + [0, 35] * (MAPSIZE // 2))) * (MAPSIZE // 2) + [35] * MAPSIZE

# генерация -----------------------
mapp[start] = 102  # ложим палку в стартовую ячейку

stack = [(start, start)]  # стек (добавление в конец | изъятие с конца)

stl = 0

while stack:  # стек пуст - лабиринт сгенерирован
    stl = max(stl, len(stack))
    print(stl)
    cur = stack.pop(-1)
    printF(cur[0])

    if mapp[cur[0]] == 0:                                 # Мы в развилке
        mapp[cur[1]] = 32  # строим к ней путь
        mapp[cur[0]] = 44
        neighbours = getN(cur[0])  # ищем свободных соседей
        for i in neighbours:  # заносим в стек соседей
            stack.append(i)
        continue

    neighbours = getN(cur[0])  # ищем свободных соседей

    if neighbours == []:  # (нет соседей = мы в тупике) или разматываемся
        if not ext:
            mapp[cur[0]] = 69
            ext = True
        continue  # возвращаемся к последней развилке по стеку

    neighbour = choice(neighbours)  # выбираем случайного свободного соседа
    mapp[neighbour[1]] = 32  # строим к ниму путь
    mapp[neighbour[0]] = 44

    for i in neighbours:  # заносим в стек остальных соседей
        if i != neighbour:
            stack.append(i)

    stack.append(neighbour)  # заносим текущую в стек


printF(start)
# print(stl)

"""ЗАПОЛНЕНИЕ ЛАБИРИНТА"""
"""
data = 26
variables = 
queue = (30 * 2)
121 byte - maze image
------------------
total = <217 byte
"""


def getPP(cell):  # получить не занятых соседей клетки
    res = []
    if (cell - 1) % MAPSIZE != 0:  # клетка слева
        res.append((cell - 2, cell - 1))
    if (cell + 2) % MAPSIZE != 0:  # клетка справа
        res.append((cell + 2, cell + 1))
    if (cell + MAPSIZE + MAPSIZE) < (MAPSIZE * MAPSIZE):  # клетка снизу
        res.append((cell + MAPSIZE + MAPSIZE, cell + MAPSIZE))
    if (cell - MAPSIZE - MAPSIZE) >= 0:  # клетка сверху
        res.append((cell - MAPSIZE - MAPSIZE, cell - MAPSIZE))
    return [i for i in res if (mapp[i[1]] == 32 and 44 == mapp[i[0]])]


"""food"""
food = {'a': 10-4, 'b': 6-4, 'c': 15-4, 'd': 20-4}  # BUG SPIDER CENTIPEDE WORM
"""weapon"""
weapon = {'g': 20, 'h': 15, 'i': 10}  # DEFAULT_STICK sharpened_bone OLD_CLAW bone_cudgel BFG9000
"""enemy"""
enemy = {'1': (20, 5), '2': (10, 3), '3': (50, 20), '4': (30, 10)}
"""----"""
queue = [(start, start)]  # очередь (добавление в конец | изъятие с начала)
state = [30, 5]  # 0 - food 1 - weapon dmg
k = 97
# st = 0
while queue:  # очередь пустa - Все предметы расставлены
    cur = queue.pop(0)  # достать первый

    if mapp[cur[1]] == 32:  # Можно поставить предмет
        mapp[cur[0]] = 32
        a = randint(0, 7)
        if 2 >= a >= 1:  # ставим еду
            pass
        elif a == 3:  # ставим оружие
            pass
        elif 5 >= a >= 4:  # ставим враг
            pass  #

    neighbours = getPP(cur[0])  # ищем свободных соседей
    for i in neighbours:  # заносим в очередь соседей
        queue.append(i)
        # st += 1

    printF(start)

printF(start)
# print(st)
