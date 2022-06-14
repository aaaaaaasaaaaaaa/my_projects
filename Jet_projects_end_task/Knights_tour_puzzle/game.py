# Write your code here


def born_board(rows, columns, underscores, chess_board):
    for i in range(columns):
        chess = []
        for x in range(rows):
            chess.append([underscores])
        chess_board.append(chess)


def make_board(show_board, board, space):
    symbol_counter = 0
    stupid_counter = 0
    x = len(board)
    y = len(board[0])
    z = x * y
    for x in board:
        for y in x:
            if 'X' in y:
                show_board.append(space + 'X')
            elif '*' in y:
                show_board.append(space + '*')
            elif '_' not in y:
                show_board.append(((len(str(z)) - len(str(*y))) * ' ') + str(*y))
            else:
                show_board.append(*y)
        stupid_counter += 1
        if stupid_counter == 1:
            symbol_counter = len(show_board)
    return symbol_counter


def draw_cell(cells, second_counter, range_row, symbols, underscore):
    space = ['']
    sec_counter = len(str(second_counter))
    print(*space * sec_counter, '-' * ((symbols * underscore) + symbols + 3))
    print(second_counter, '|', sep='', end='')
    lower_end = ['  ']
    counter = 1
    for i in cells:  # [len(cells):0:-1]:
        print('', i, end='')
        if counter % range_row == 0:
            print(' |\n', end='')
            second_counter -= 1
            if second_counter != 0:
                if sec_counter > 1:
                    if len(str(second_counter)) == 1:
                        print(' ', second_counter, '|', sep='', end='')
                    else:
                        print(second_counter, '|', sep='', end='')
                else:
                    print(second_counter, '|', sep='', end='')
        if not counter > range_row:
            lower_end.append(' ' * (underscore - len(str(counter))) + str(counter))
        counter += 1
    print(*space * sec_counter, '-' * ((symbols * underscore) + symbols + 3))
    print(*lower_end)


def finding_x(chess_board):
    mass1 = 0
    for chess in chess_board:
        mass1 += 1
        mass2 = 0
        for x in chess:
            mass2 += 2
            if x != ['X'] and x != ['*']:
                return False
    return True


# kal
# def poss_moves(pos1,pos2, b_pos1, n_pos1, chess_board, space='', moves=0):
#     counter = 0
#     if pos1 >= 2:
#         if pos2[1] > 0:  # 1
#             if b_pos1 != ['X']:
#                 counter += 1
#             if moves > 0:
#                 b_pos1 = [space + n_pos1, chess_board))]
#
# def p_moves():
#         poss_moves(position[0], pos2, b_pos1, n_pos1, chess_board, space='', moves=0)


# тут можно сделать "офигенный" рефакторинг!
def possible_moves(position, chess_board, space='', moves=0):
    counter = 0
    if position[0] >= 2:
        if position[1] > 0:  # 1
            if chess_board[position[0] - 2][position[1] - 1] != ['X'] \
                    and chess_board[position[0] - 2][position[1] - 1] != ['*']:
                counter += 1
                if moves > 0:
                    chess_board[position[0] - 2][position[1] - 1] = \
                        [space + str(possible_moves([position[0] - 2, position[1] - 1], chess_board))]
        if position[1] < len(chess_board[0]) - 1:  # 2
            if chess_board[position[0] - 2][position[1] + 1] != ['X'] \
                    and chess_board[position[0] - 2][position[1] + 1] != ['*']:
                counter += 1
                if moves > 0:
                    chess_board[position[0] - 2][position[1] + 1] = \
                        [space + str(possible_moves([position[0] - 2, position[1] + 1], chess_board))]

    if position[0] <= len(chess_board) - 3:
        if position[1] > 0:  # 3
            if chess_board[position[0] + 2][position[1] - 1] != ['X'] \
                    and chess_board[position[0] + 2][position[1] - 1] != ['*']:
                counter += 1
                if moves > 0:
                    chess_board[position[0] + 2][position[1] - 1] = \
                        [space + str(possible_moves([position[0] + 2, position[1] - 1], chess_board))]
        if position[1] < len(chess_board[0]) - 1:  # 4
            if chess_board[position[0] + 2][position[1] + 1] != ['X'] \
                    and chess_board[position[0] + 2][position[1] + 1] != ['*']:
                counter += 1
                if moves > 0:
                    chess_board[position[0] + 2][position[1] + 1] = \
                        [space + str(possible_moves([position[0] + 2, position[1] + 1], chess_board))]

    if position[1] >= 2:
        if position[0] > 0:  # 5
            if chess_board[position[0] - 1][position[1] - 2] != ['X'] \
                    and chess_board[position[0] - 1][position[1] - 2] != ['*']:
                counter += 1
                if moves > 0:
                    chess_board[position[0] - 1][position[1] - 2] = \
                        [space + str(possible_moves([position[0] - 1, position[1] - 2], chess_board))]
        if position[0] <= len(chess_board) - 2:  # 6
            if chess_board[position[0] + 1][position[1] - 2] != ['X'] \
                    and chess_board[position[0] + 1][position[1] - 2] != ['*']:
                counter += 1
                if moves > 0:
                    chess_board[position[0] + 1][position[1] - 2] = \
                        [space + str(possible_moves([position[0] + 1, position[1] - 2], chess_board))]

    if position[1] < len(chess_board[0]) - 2:
        if position[0] > 0:  # 7
            if chess_board[position[0] - 1][position[1] + 2] != ['X'] \
                    and chess_board[position[0] - 1][position[1] + 2] != ['*']:
                counter += 1
                if moves > 0:
                    chess_board[position[0] - 1][position[1] + 2] = \
                        [space + str(possible_moves([position[0] - 1, position[1] + 2], chess_board))]
        if position[0] <= len(chess_board) - 2:  # 8
            if chess_board[position[0] + 1][position[1] + 2] != ['X'] \
                    and chess_board[position[0] + 1][position[1] + 2] != ['*']:
                counter += 1
                if moves > 0:
                    chess_board[position[0] + 1][position[1] + 2] = \
                        [space + str(possible_moves([position[0] + 1, position[1] + 2], chess_board))]
    return counter


# Много ненужных аргументов...
def erase_moves(position, chess_board, space='', counter=''):
    if position[0] >= 2:
        if position[1] > 0:  # 1
            if chess_board[position[0] - 2][position[1] - 1] != ['*'] \
                    and chess_board[position[0] - 2][position[1] - 1] != [counter]:
                chess_board[position[0] - 2][position[1] - 1] = [space]
        if position[1] < len(chess_board[0]) - 1:  # 2
            if chess_board[position[0] - 2][position[1] + 1] != ['*'] \
                    and chess_board[position[0] - 2][position[1] - 1] != [counter]:
                chess_board[position[0] - 2][position[1] + 1] = [space]

    if position[0] <= len(chess_board) - 3:
        if position[1] > 0:  # 3
            if chess_board[position[0] + 2][position[1] - 1] != ['*'] \
                    and chess_board[position[0] - 2][position[1] - 1] != [counter]:
                chess_board[position[0] + 2][position[1] - 1] = [space]
        if position[1] < len(chess_board[0]) - 1:  # 4
            if chess_board[position[0] + 2][position[1] + 1] != ['*'] \
                    and chess_board[position[0] - 2][position[1] - 1] != [counter]:
                chess_board[position[0] + 2][position[1] + 1] = [space]

    if position[1] >= 2:
        if position[0] > 0:  # 5
            if chess_board[position[0] - 1][position[1] - 2] != ['*'] and \
                    chess_board[position[0] - 2][position[1] - 1] != [counter]:
                chess_board[position[0] - 1][position[1] - 2] = [space]
        if position[0] <= len(chess_board) - 2:  # 6
            if chess_board[position[0] + 1][position[1] - 2] != ['*'] and \
                    chess_board[position[0] - 2][position[1] - 1] != [counter]:
                chess_board[position[0] + 1][position[1] - 2] = [space]

    if position[1] < len(chess_board[0]) - 2:
        if position[0] > 0:  # 7
            if chess_board[position[0] - 1][position[1] + 2] != ['*'] and \
                    chess_board[position[0] - 2][position[1] - 1] != [counter]:
                chess_board[position[0] - 1][position[1] + 2] = [space]
        if position[0] <= len(chess_board) - 2:  # 8
            if chess_board[position[0] + 1][position[1] + 2] != ['*'] and \
                    chess_board[position[0] - 2][position[1] - 1] != [counter]:
                chess_board[position[0] + 1][position[1] + 2] = [space]


def manager():
    dim_check = False
    dimension = []
    while not dim_check:
        dimension = input("Enter your board dimensions: ").split()
        if len(dimension) != 2:
            print("Invalid dimensions!")
        elif not dimension[0].isdigit() or not dimension[1].isdigit():
            print("Invalid dimensions!")
        elif int(dimension[0]) < 1 or int(dimension[1]) < 1:
            print("Invalid dimensions!")
        else:
            dim_check = True
            dimension = dimension
    check = False
    while not check:
        answer = input("Enter the knight's starting position: ").split()
        if len(answer) != 2:
            print("Invalid position!")
        elif not answer[0].isdigit() or not answer[1].isdigit():
            print("Invalid position!")
        elif 1 > int(answer[0]) or int(answer[0]) > int(dimension[0]) or 1 > int(answer[1]) \
                or int(answer[1]) > int(dimension[1]):
            print("Invalid position!")
        else:
            vis_squares = 1
            chess_board = []
            all_elements = int(dimension[0]) * int(dimension[1])
            underscores = '_' * len(str(all_elements))
            spaces = ' ' * ((len(str(all_elements))) - 1)
            born_board(int(dimension[0]), int(dimension[1]), underscores, chess_board)
            row = int(dimension[1]) - int(answer[1])
            column = int(answer[0]) - 1
            chess_board[row][column] = ['X']
            show_board = []
            x_position = [row, column]
            moves = 1
            possible_moves(x_position, chess_board, spaces, moves)
            q_ans = input("Do you want to try the puzzle? (y/n): ")
            if q_ans == 'n':
                che_board = solveKT(int(dimension[0]), int(dimension[1]), int(answer[0]) - 1,
                                    int(dimension[1]) - (int(answer[1])))
                if che_board == 1:
                    print("No solution exists!")
                    check = True
                    continue
                else:
                    print("\nHere's the solution!")
                    show_board = []
                    symbol_counter = make_board(show_board, che_board, spaces)
                    draw_cell(show_board, int(dimension[1]), int(dimension[0]), symbol_counter, len(underscores))
                    check = True
                    continue
            elif q_ans == 'y':
                che_board = solveKT(int(dimension[0]), int(dimension[1]), int(answer[0]) - 1,
                                    int(dimension[1]) - (int(answer[1])))
                if che_board == 1:
                    print("No solution exists!")
                    check = True
                    continue
                symbol_counter = make_board(show_board, chess_board, spaces)
                draw_cell(show_board, int(dimension[1]), int(dimension[0]), symbol_counter, len(underscores))
                check1 = False
                while not check1:
                    print("\nEnter your next move: ", end='')
                    next_move = input().split()
                    if len(next_move) != 2:
                        print("Invalid position!")
                    elif not next_move[0].isdigit() or not next_move[1].isdigit():
                        print("Invalid position!")
                    elif 1 > int(next_move[0]) or int(next_move[0]) > int(dimension[0]) or 1 > int(next_move[1]) \
                            or int(next_move[1]) > int(dimension[1]):
                        print("Invalid position!")

                    elif chess_board[int(dimension[1]) - int(next_move[1])][int(next_move[0]) - 1] == [underscores] or \
                            chess_board[int(dimension[1]) - int(next_move[1])][int(next_move[0]) - 1] == ['X'] or \
                            chess_board[int(dimension[1]) - int(next_move[1])][int(next_move[0]) - 1] == ['*']:
                        print('invalid move', end='')
                    else:
                        erase_moves(x_position, chess_board, underscores)
                        chess_board[row][column] = ['*']
                        row = int(dimension[1]) - int(next_move[1])
                        column = int(next_move[0]) - 1
                        chess_board[row][column] = ['X']
                        show_board = []
                        x_position = [row, column]  # finding_x(chess_board)
                        game_over = possible_moves(x_position, chess_board, spaces, moves)
                        symbol_counter = make_board(show_board, chess_board, spaces)
                        draw_cell(show_board, int(dimension[1]), int(dimension[0]), symbol_counter, len(underscores))
                        vis_squares += 1
                        if game_over == 0 and not finding_x(chess_board):
                            print("\nNo more possible moves!\nYour knight visited", vis_squares, "squares!")
                            check1 = True
                        elif finding_x(chess_board):
                            print("\nWhat a great tour! Congratulations!")
                            check1 = True
                check = True
            else:
                print("Invalid input!")
                continue





def isSafe(x, y, board, n1, n2):
    '''
        A utility function to check if i,j are valid indexes
        for N*N chessboard
    '''
    # print(x, y, n1, n2)
    if 0 <= x < n1 + 1 and 0 <= y < n2 + 1:
        try:
            if board[y][x] == -1:
                return True
        except IndexError:
            print("Error x, y:", x, y)
    return False

def printSolution(board, n2):
    '''
        A utility function to print Chessboard matrix
    '''
    f_mass = []
    full_mass = []
    for mas in range(n2 + 1):
        for i in board[mas]:
            f_mass.append([(str(i))])
        full_mass.append(f_mass)
        f_mass = []
    return full_mass

def solveKT(bo1, bo2, pos1, pos2):

    # print(pos1, pos2)
    # Initialization of Board matrix
    board = [[-1 for i in range(bo1)] for i in range(bo2)]
    n1 = bo1 - 1
    n2 = bo2 - 1
    # move_x and move_y define next move of Knight.
    # move_x is for next value of x coordinate
    # move_y is for next value of y coordinate
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Since the Knight is initially at the first block
    board[pos2][pos1] = 1

    # Step counter for knight's position
    pos = 2

    # Checking if solution exists or not
    if not solveKTUtil(n1, n2, board, pos1, pos2, move_x, move_y, pos):
        return 1  # no solution exist
    else:
        return printSolution(board, n2)


def solveKTUtil(n1, n2, board, curr_x, curr_y, move_x, move_y, pos):
    
    # print(board)
    if pos == (n1 + 1) * (n2 + 1) + 1:
        return True

    # Try all next moves from the current coordinate x, y
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if isSafe(new_x, new_y, board, n1, n2):
            # print("aprove", pos)
            board[new_y][new_x] = pos
            if solveKTUtil(n1, n2, board, new_x, new_y, move_x, move_y, pos + 1):
                return True

            # Backtracking
            board[new_y][new_x] = -1
    return False

manager()

