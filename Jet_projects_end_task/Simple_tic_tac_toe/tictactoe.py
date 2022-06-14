# write your code here
cells = ['_'] * 9
cell = [cells[0:3], cells[3:6], cells[6:9]]


# рисует поле
def draw_cell(cells):
    counter = 0
    second_counter = 0
    print("---------")
    print('|', end='')
    for i in cells:
        if i == 'O' or i == 'X' or i == '_':
            if i == '_':
                i = ' '
            print('', i, end='')
            counter += 1
            second_counter += 1
            if counter == 3:
                if second_counter == 9:
                    print(' |')
                    break
                print(' |\n|', end='')
                counter = 0
            if second_counter == 9:
                break
        else:
            print(" Not correct input")
            exit()
    print("---------")


approve = 0
winner = ''


# считывает три параметра на проверку, есть ли три в ряд
def cells_win_check(x1, x2, x3):
    if x1 == x2 == x3:
        if x1 != '_':
            global approve, winner
            approve += 1
            winner = x1


# считает сколько х, о или _ и высчитывает ситуацию
def counters(cells):
    counter_x = 0
    counter_o = 0
    counter__ = 0
    for i in cells:
        if i == 'X':
            counter_x += 1
        elif i == 'O':
            counter_o += 1
        elif i == '_':
            counter__ += 1


# высчитывает ситуацию на поле
    #if counter_x > counter_o + 1 or counter_o > counter_x + 1:
    #    print("Impossible")
    #elif counter_x + counter_o != 9:
    #    print("Game not finished")
    if counter_x != counter_o:
        if counter__ == 0:
            print("Draw")
            exit()


def win_check():
    cells_win_check(cells[0], cells[3], cells[6])
    cells_win_check(cells[0], cells[4], cells[8])
    cells_win_check(cells[0], cells[1], cells[2])
    cells_win_check(cells[1], cells[4], cells[7])
    cells_win_check(cells[2], cells[5], cells[8])
    cells_win_check(cells[2], cells[4], cells[6])
    cells_win_check(cells[3], cells[4], cells[5])
    cells_win_check(cells[6], cells[7], cells[8])


def game_manager():
    win = False
    while not win:
        draw_cell(cells)
        win_check()
        if approve == 0:
            counters(cells)
            entering_coordinates()
        if approve == 1:
            print(winner, 'wins')
            win = True
        elif approve > 1:
            print("Impossible")
            win = True


turn = True


def entering_coordinates():
    global turn
    checker = False
    coordinate = []
    while not checker:
        coordinate = input("Enter coordinates:").split()
        if len(coordinate) == 2:
            for i in coordinate:
                if i.isdigit():
                    if int(i) == 1 or int(i) == 2 or int(i) == 3:
                        if 4 > int(coordinate[1]) > 0:
                            if cell[int(coordinate[0]) - 1][int(coordinate[1]) - 1] == '_':
                                checker = True
                            else:
                                print("This cell is occupied! Choose another one!")
                                break
                    elif int(i) > 3 or int(i) < 1:
                        print("Coordinates should be from 1 to 3!")
                        break
                else:
                    print("You should enter numbers!")
                    break
        else:
            print("You should enter 2 coordinates!")

    if turn:
        cell[int(coordinate[0]) - 1][int(coordinate[1]) - 1] = 'X'
        turn = False
    elif not turn:
        cell[int(coordinate[0]) - 1][int(coordinate[1]) - 1] = 'O'
        turn = True
    converting_coordinates()


def checks(coordinate):
    if 4 > int(coordinate) > 0:
        return True
    else:
        return False


def converting_coordinates():
    counter1 = 0
    counter2 = 0
    for i in range(len(cells)):
        if i >= 3 and i < 6:
            cells[i] = cell[1][counter1]
            counter1 += 1
        elif i >= 6 and i < 9:
            cells[i] = cell[2][counter2]
            counter2 += 1
        if i < 3:
            cells[i] = cell[0][i]


game_manager()
