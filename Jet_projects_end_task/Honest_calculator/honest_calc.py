# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


def is_digit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def calculate(x, op, y):
    if op == '+':
        return round(float(x) + float(y), 1)
    elif op == '-':
        return round(float(x) - float(y), 1)
    elif op == '*':
        return round(float(x) * float(y), 1)
    else:
        if float(y) == 0:
            return msg_3
        return round(float(x) / float(y), 1)


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    return False


def checking(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)


def manager():
    memory = 0.
    check = False
    while not check:
        x, oper, y = input(msg_0+"\n").split()
        if y == 'M':
            y = memory
        if x == 'M':
            x = memory
        if not is_digit(x) or not is_digit(y):
            print(msg_1)
        elif oper == "+" or oper == "-" or oper == "*" or oper == "/":
            checking(float(x), float(y), oper)
            result = calculate(x, oper, y)
            print(result)
            if result == msg_3:
                continue
            check1 = False
            while not check1:
                answer = input(msg_4+"\n")
                if answer == 'y':
                    check1 = True
                    if not is_one_digit(result):
                        memory = result
                    else:
                        msg_index = [msg_10, msg_11, msg_12]
                        n = 0
                        while n < 3:
                            sureness = input(msg_index[n]+ "\n")
                            if sureness == "y":
                                n += 1
                            elif sureness == "n":
                                break
                            else:
                                continue
                        if n == 3:
                            memory = result
                elif answer == "n":
                    check1 = True

            if input(msg_5 + "\n") == 'n':
                check = True
        else:
            print(msg_2)


manager()
