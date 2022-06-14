import random
from itertools import chain

# Write your code here
stock_pieces = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1], [1, 2], [1, 3], [1, 4],
                [1, 5], [1, 6], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [3, 5],
                [3, 6], [4, 4], [4, 5], [4, 6], [5, 5], [5, 6], [6, 6]]

random.shuffle(stock_pieces)
computer_pieces = []
player_pieces = []
domino_snake = []


def show_pieces(pieces):
    count = 1
    for i in pieces:
        print(str(count) + ":" + str(i))
        count += 1


def split_set(pieces):
    for i in range(7):
        pieces.append(stock_pieces.pop(random.randint(0, len(stock_pieces) - 1)))


def turn_status():
    if max(computer_pieces) > max(player_pieces):
        domino_snake.append(computer_pieces.pop(computer_pieces.index(max(computer_pieces))))
        return "player_pieces"
    else:
        domino_snake.append(player_pieces.pop(player_pieces.index(max(player_pieces))))
        return "computer_pieces"


def turn_player(status_check):
    if status_check == "computer_pieces":
        return "player_pieces"
    else:
        return "computer_pieces"


def take_piece_comp_ai(player, snake):
    end_snake = []
    player_snake = []
    scores = []
    aprovement = False
    for i in range(0, len(player)):
        player_snake += player[i]
    for i in range(0, len(snake)):
        end_snake += snake[i]
    final_snake = list(chain(player_snake, end_snake))
    count_number = {0: final_snake.count(0), 1: final_snake.count(1), 2: final_snake.count(2),
                    3: final_snake.count(3), 4: final_snake.count(4), 5: final_snake.count(5), 6: final_snake.count(6)}
    # print("count number:", count_number)
    for domino in player:
        scores.append(count_number[domino[0]] + count_number[domino[1]])
        # print("scores:", scores)
    while not aprovement:
        if all(elem == -1 for elem in scores):
            if len(stock_pieces) > 0:
                player.append(stock_pieces.pop(random.randint(0, len(stock_pieces) - 1)))
            aprovement = True
        else:
            aprovement = take_piece_comp(scores.index(max(scores)), player)
            scores[(scores.index(max(scores)))] = -1
            # print(scores)

    return True


def take_piece_comp(piece, player):
    answer = add_domino_minus(player[piece], domino_snake)
    if answer:
        player.pop(piece)
        return answer
    else:
        answer = add_domino_plus(player[piece], domino_snake)
        if answer:
            player.pop(piece)
            return answer



def print_result():
    print("======================================================================")
    print("Stock size:", len(stock_pieces))
    print("Computer pieces:", len(computer_pieces), "\n")
    # print("comp pieces:", computer_pieces)
    if len(domino_snake) > 6:
        print(str(domino_snake[0]) + str(domino_snake[1]) + str(domino_snake[2]) + "..."
              + str(domino_snake[len(domino_snake) - 3]) + str(domino_snake[len(domino_snake) - 2])
              + str(domino_snake[len(domino_snake) - 1]))

    else:
        print(*domino_snake)
    print("\nYour pieces:")
    show_pieces(player_pieces)
    # print("\nStatus:", status)


def end_condition(snake):
    end_snake = []
    counter = 0
    for i in range(0, len(snake)):
        end_snake += snake[i]
    if end_snake[0] == end_snake[len(end_snake) - 1]:
        for i in end_snake:
            if end_snake[0] == i:
                counter += 1
        if counter >= 8:
            return True


def add_domino_plus(domino, snake):
    end_snake = []
    for i in range(0, len(snake)):
        end_snake += snake[i]
    if domino[0] == end_snake[len(end_snake) - 1]:
        domino_snake.append(domino)
        return True
    elif domino[1] == end_snake[len(end_snake) - 1]:
        domino[0], domino[1] = domino[1], domino[0]
        domino_snake.append(domino)
        return True
    else:
        return False


# answer = add_domino_minus(player.pop((-piece) - 1), domino_snake)
def take_piece(piece, player):
    if piece < 0:
        answer = add_domino_minus(player[(-piece) - 1], domino_snake)
        if answer:
            player.pop((-piece) - 1)
            return answer
        return answer
    elif piece > 0:
        answer = add_domino_plus(player[piece - 1], domino_snake)
        if answer:
            player.pop(piece - 1)
            return answer
        return answer
    else:
        if len(stock_pieces) > 0:
            player.append(stock_pieces.pop(random.randint(0, len(stock_pieces) - 1)))
        return True


def add_domino_minus(domino, snake):
    end_snake = []
    for i in range(0, len(snake)):
        end_snake += snake[i]
    if domino[0] == end_snake[0]:
        domino[0], domino[1] = domino[1], domino[0]
        domino_snake.insert(0, domino)
        return True
    elif domino[1] == end_snake[0]:
        domino_snake.insert(0, domino)
        return True
    else:
        return False


def game_manager():
    counter = 0
    split_set(computer_pieces)
    split_set(player_pieces)
    turn = False
    status_check = turn_status()
    while not turn:
        if end_condition(domino_snake):
            turn = True
            # status = "The game is over. It's a draw!"
            print_result()
            print("\nStatus: The game is over. It's a draw!")
        elif len(computer_pieces) == 0:
            # status = "The game is over. The computer won!"
            print_result()
            print("\nStatus: The game is over. The computer won!")
            turn = True
        elif len(player_pieces) == 0:
            # status = "The game is over. You won!"
            print_result()
            print("\nStatus: The game is over. You won!")
            turn = True
        else:
            if len(stock_pieces) == 0:
                counter += 1
                if counter == 3:
                    print_result()
                    print("\nStatus: The game is over. It's a draw!")
                    turn = True
            if status_check == "player_pieces":
                # status = "It's your turn to make a move. Enter your command."
                print_result()
                print("\nStatus: It's your turn to make a move. Enter your command.")
                input_check = False
                while not input_check:
                    try:
                        choose_piece = int(input())
                        if abs(choose_piece) > len(player_pieces):
                            print("Invalid input. Please try again.")
                            continue
                        else:
                            input_check = take_piece(int(choose_piece), player_pieces)
                            if not input_check:
                                print("Illegal move. Please try again.")
                    except ValueError:
                        print("Invalid input. Please try again.")

            elif status_check == "computer_pieces":
                # status = "Computer is about to make a move. Press Enter to continue..."
                print_result()
                print("\nStatus: Computer is about to make a move. Press Enter to continue...")
                input()
                input_check = False
                while not input_check:
                    input_check = take_piece_comp_ai(computer_pieces, domino_snake)
            status_check = turn_player(status_check)


game_manager()
