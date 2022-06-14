import random


def game_manager(user, name, score, variants, computer):
    if variants.index(user) == 0:
        right_options = []
        for i in range(1, len(variants)):
            right_options.append(variants[i])
        right_options.append(variants[0])
    else:
        beating = []
        get_defeated = []
        for i in range(variants.index(user) + 1, len(variants)):
            beating.append(variants[i])
        for i in range(0, variants.index(user)):
            get_defeated.append(variants[i])
        right_options = beating + get_defeated
    rating = 0
    half = len(right_options) // 2
    lose = "Sorry, but the computer chose"
    draw = "There is a draw ("
    win = "Well done. The computer chose"
    if user == computer:
        print(draw + user + ")")
        rating += 50
        rating_adder(rating, name, score)
    elif right_options.index(computer) + 1 <= half:
        print(lose, computer)
        rating_adder(rating, name, score)
    elif right_options.index(computer) + 1 > half:
        print(win, computer, "and failed")
        rating += 100
        rating_adder(rating, name, score)


def rating_adder(rating, name, score):
    if name in score:
        score[name] += rating
        file1 = open("rating.txt", "w")
        for key in score.keys():
            print(key + " " + str(score[key]), file=file1, flush=True)
        file1.close()
    else:
        file = open("rating.txt", "a")
        print(name, rating, file=file, flush=True)
        file.close()


def show_rating(name, score):
    if name in score:
        print("Your rating:", score[name])
    else:
        print("Your rating: 0")


def main():
    options = ["rock", "gun", "lightning", "devil", "dragon", "water", "air", "paper", "sponge",
               "wolf", "tree", "human", "snake", "scissors", "fire"]
    check = False
    name = input("Enter your name: ")
    print("Hello,", name)
    chosen_options = input().split(",")
    if len(chosen_options) > 2:
        variants = []
        for option in chosen_options:
            if option in options:
                variants.append(option)
    else:
        variants = ["rock", "paper", "scissors"]
    print("Okay, let's start")
    while not check:
        file1 = open("rating.txt", "r")
        scores = {}
        for line in file1:
            score_rating = line.split()
            if len(score_rating) == 2:
                scores_add = {score_rating[0]: int(score_rating[1])}
                scores.update(scores_add)
        file1.close()
        answer = input()
        answer.islower()
        if answer == "!exit":
            check = True
            print("Bye!")
            continue
        elif answer == "!rating":
            show_rating(name, scores)
        elif answer in variants:
            comp_ans = random.choice(variants)
            game_manager(answer, name, scores, variants, comp_ans)
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
