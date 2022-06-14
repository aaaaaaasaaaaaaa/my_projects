# write your code here
help = """Available formatters: plain bold italic header link inline-code new-line
Special commands: !help !done"""
check = False
commands = {"plain": '', "bold": '**', "italic": '*', "header": '#', 'link': '', "inline-code": '`', "new-line": '\n',
            "unordered-list": False, "ordered-list": True}
lists = []
final_text = ''


def var_list(form):
    numb = False
    if not form:
        while not numb:
            n_rows = int(input("Number of rows: "))
            if n_rows > 0:
                f_list = make_lists(n_rows, False)
                return f_list
            else:
                print("The number of rows should be greater than zero")
    elif form:
        while not numb:
            try:
                n_rows = int(input("Number of rows: "))
            except ValueError:
                print("You need to print a number!")
                continue
            if n_rows > 0:
                f_list = make_lists(n_rows, True)
                return f_list
            else:
                print("The number of rows should be greater than zero")


def make_lists(rows, formatt):
    final_list = []
    if formatt:
        for elem in range(rows):
            row = input("Row #{}: ".format(elem + 1))
            add_row = ("{}. {}\n").format(elem + 1, row)
            final_list.append(add_row)
    else:
        for elem in range(rows):
            row = input("Row #{}: ".format(elem + 1))
            add_row = ("* {}\n").format(row)
            final_list.append(add_row)
    return final_list


while not check:
    answer = input("Choose a formatter: ")
    if answer in commands:
        pr_text = []
        check_list = False
        if answer == 'header':
            ch1 = False
            while not ch1:
                mult = int(input("Level: "))
                if 0 < mult < 7:
                    dop = commands['header'] * mult
                    text = input("Text: ")
                    pr_text.append(dop + ' ' + text)
                    pr_text.append('\n')
                    ch1 = 1
                else:
                    print("The level should be within the range of 1 to 6")

        elif answer == 'link':
            label = input("Label: ")
            url = input("URL: ")
            text = ('[' + label + ']' + '(' + url + ')')
            pr_text.append(text)
        elif answer == 'new-line':
            pr_text.append(commands[answer])

        elif answer == 'unordered-list':
            pr_text = (var_list(commands[answer]))
            check_list = True
        elif answer == 'ordered-list':
            pr_text = (var_list(commands[answer]))
            check_list = True

        else:
            text = input("Text: ")
            pr_text.append(commands[answer] + text + commands[answer])
        # for text in pr_text:
        #     print(text, end='')
        for tex in pr_text:
            final_text += tex
        print(final_text)


    elif answer == "!help":
        print(help)
    elif answer == "!done":
        file = open("output.md", 'w')
        file.write(final_text)
        file.close()
        check = True
    else:
        print("Unknown formatting type or command")




