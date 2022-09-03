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

msg_ = {
    0: msg_0,
    1: msg_1,
    2: msg_2,
    3: msg_3,
    4: msg_4,
    5: msg_5,
    6: msg_6,
    7: msg_7,
    8: msg_8,
    9: msg_9,
    10: msg_10,
    11: msg_11,
    12: msg_12
}


def valid_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


def valid_operand(operand):
    return operand in ['+', '-', '*', '/']


def get_input():
    calc = input(msg_0)
    return calc.split()


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and v3 in ['*', '+', '-']:
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


def main_loop():
    global memory
    x, oper, y = get_input()
    if x.lower() == 'm':
        x = memory
    if y.lower() == 'm':
        y = memory
    if not (valid_number(x) and valid_number(y)):
        print(msg_1)
        return True
    elif not (valid_operand(oper)):
        print(msg_2)
        return True

    x = float(x)
    y = float(y)

    check(x, y, oper)

    match oper:
        case '+':
            result = x + y
        case '-':
            result = x - y
        case '*':
            result = x * y
        case '/':
            if y == 0:
                print(msg_3)
                return True
            else:
                result = x / y


    print(result)
    answer = ''
    while answer not in ['y', 'n']:
        answer = input(msg_4).lower()
        if answer == 'y':
            if is_one_digit(result):
                msg_index=10
                while msg_index <= 12 and answer == 'y':
                    answer = ''
                    while answer not in ['y', 'n']:
                        answer = input(msg_[msg_index]).lower()
                        if answer == 'y':
                            msg_index = msg_index + 1
                if answer == 'y':
                    memory = result
            else:
                memory = result
    answer = ''
    while answer not in ['y', 'n']:
        answer = input(msg_5).lower()
        if answer == 'n':
            return False
        else:
            return True


if __name__ == '__main__':
    memory = 0
    while main_loop():
        pass
