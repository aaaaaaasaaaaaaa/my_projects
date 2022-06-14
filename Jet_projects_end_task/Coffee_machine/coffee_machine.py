# Write your code here


def info():
    print("\nThe coffee machine has:")
    print(ingredients['water'], "of water")
    print(ingredients['milk'], "of milk")
    print(ingredients['coffee'], "of coffee beans")
    print(ingredients['dis_cups'], "of disposable cups")
    print("$" + str(ingredients['money']), "of money\n")


def making_coffee(sort):
    checker = False
    for ing in ingredients:
        for some in sort:
            if ing == some:
                if ingredients[ing] > sort[some]:
                    checker = True
                else:
                    print("Sorry, not enough", str(ing) + '!\n')
                    return
    if checker:
        print("I have enough resources, making you a coffee!\n")
        for ing in ingredients:
            for some in sort:
                if ing == some:
                    if ing == 'money':
                        ingredients[ing] += sort[some]
                    else:
                        ingredients[ing] -= sort[some]


def buying():
    checking = False
    while not checking:
        print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        choice = input()
        if choice == 'back':
            print()
            return
        if choice.isdigit():
            if int(choice) == 1:
                making_coffee(espresso)
                return
            elif int(choice) == 2:
                making_coffee(latte)
                return
            elif int(choice) == 3:
                making_coffee(cappuccino)
                return

    print()


def filling():
    print("\nWrite how many ml of water you want to add:")
    water_fill = int(input())
    print("Write how many ml of milk you want to add:")
    milk_fill = int(input())
    print("Write how many grams of coffee beans you want to add:")
    coffee_fill = int(input())
    print("Write how many disposable coffee cups you want to add:")
    dis_cups_fill = int(input())
    ingredients['water'] += water_fill
    ingredients['milk'] += milk_fill
    ingredients['coffee'] += coffee_fill
    ingredients['dis_cups'] += dis_cups_fill
    print()


def take_money():
    print("\nI gave you $" + str(ingredients['money']))
    ingredients['money'] -= ingredients['money']
    print()


# def manager():
#     check = False
#     while not check:
#         print("Write action (buy, fill, take, remaining, exit):")
#         action = input()
#         if action == 'buy':
#             buying()
#         elif action == 'fill':
#             filling()
#         elif action == 'take':
#             take_money()
#         elif action == 'remaining':
#             info()
#         elif action == 'exit':
#             check = True


ingredients = {'water': 400, 'milk': 540, 'coffee': 120, 'dis_cups': 9, 'money': 550}
espresso = {'water': 250, 'coffee': 16, 'dis_cups': 1, 'money': 4}
latte = {'water': 350, 'milk': 75, 'coffee': 20, 'dis_cups': 1, 'money': 7}
cappuccino = {'water': 200, 'milk': 100, 'coffee': 12, 'dis_cups': 1, 'money': 6}




class CoffeeMachine:
    def __init__(self):
        self.user_input = None

    def take_a_string(self, user_input):
        check = False
        self.user_input = user_input
        while not check:
            if self.user_input == 'buy':
                buying()
            elif self.user_input == 'fill':
                filling()
            elif self.user_input == 'take':
                take_money()
            elif self.user_input == 'remaining':
                info()
            elif self.user_input == 'exit':
                return

            print("Write action (buy, fill, take, remaining, exit):")
            self.user_input = input()


user_action = CoffeeMachine()
print("Write action (buy, fill, take, remaining, exit):")
user_action.take_a_string(input())
