from random import choice
# write your code here
test_luck = []
number_of_frens = int(input("Enter the number of friends joining (including you):\n"))
if number_of_frens > 0:
    print("\nEnter the name of every friend (including you), each on a new line:")
    frens_dict = {}
    for i in range(number_of_frens):
        name = input()
        test_luck.append(name)
        frens_dict[name] = 0
    final_bill = int(input("\nEnter the total bill value:\n"))
    each_bill = final_bill / number_of_frens
    each_bill = round(each_bill, 2)
    for i in frens_dict:
        frens_dict[i] = each_bill
    print()
    answer = input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:\n")
    print()
    if answer == 'Yes':
        lucky = choice(test_luck)
        print(lucky, "is the lucky one!")
        lucky_bill = frens_dict[lucky] / (number_of_frens - 1)
        for i in frens_dict:
            if i == lucky:
                frens_dict[i] = 0
            else:
                frens_dict[i] = round(each_bill + lucky_bill, 2)

        print(frens_dict)

    else:
        print("No one is going to be lucky\n")
        print(frens_dict)
else:
    print("\nNo one is joining for the party")
