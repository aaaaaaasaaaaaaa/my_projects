# Write your code here
import random


print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
hint = ['-' for i in word]
check = False
letter = set(word)
same = set()
game_check = False
while not game_check:
    play = input('Type "play" to play the game, "exit" to quit: ')
    if play == 'exit':
        game_check = True
    elif play == 'play':
        while not check:
            tries = 8
            while len(letter) > 0:
                if tries > 0:
                    print()
                    print(''.join(hint))
                    answer = input("Input a letter: ")
                    if not answer.isdigit() and len(answer) == 1 and answer.islower():
                        if answer in letter:
                            letter.discard(answer)
                            counter = 0
                            same.add(answer)
                            for i in word:
                                if i == answer:
                                    hint[counter] = answer
                                counter += 1
                        elif answer in same:
                            print("You've already guessed this letter")
                        else:
                            print("That letter doesn't appear in the word")
                            tries -= 1
                            same.add(answer)
                    elif len(answer) != 1:
                        print("You should input a single letter")
                    elif not answer.islower():
                        print("Please enter a lowercase English letter")
                else:
                    print("You lost!\n")
                    break
            if tries > 0:
                print("You guessed the word", word + "!")
                print("You survived!\n")
            check = True
    else:
        continue
