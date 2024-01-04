import random

def interpret(code):
    output = []
    stack = []

    lines = [[*x] for x in code.split('\n')]

    char = 'None'
    line, index = 0, 0
    dx, dy = 1, 0 

    first = True
    ascii_mode = False
    trampoline = False


    while char != "@":
        if dy > 0:   line -= 1
        elif dy < 0: line += 1

        if dx > 0:   index += 1
        elif dx < 0: index -= 1

        # TODO: Possibly refactor later
        if first:
            first = False
            line, index = 0, 0

        char = lines[line][index]

        if ascii_mode and char != '"':
            stack.append(ord(char))
            continue

        if trampoline:
            trampoline = False
            continue
        if char.isnumeric(): stack.append(int(char))
        elif char == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif char == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif char == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
            pass
        elif char == '/':
            a = stack.pop()
            b = stack.pop()
            if a == 0:
                stack.append(0)
            else:
                stack.append(b // a)
        elif char == '%':
            a = stack.pop()
            b = stack.pop()
            if a == 0:
                stack.append(0)
            else:
                stack.append(b % a)
        elif char == '!':
            a = stack.pop()
            if a == 0:
                stack.append(1)
            else:
                stack.append(0)
        elif char == '`':
            a = stack.pop()
            b = stack.pop()
            if b > a:
                stack.append(1)
            else:
                stack.append(0)
        elif char == '>':
            dx = 1
            dy = 0
        elif char == '<':
            dx = -1
            dy = 0
        elif char == '^':
            dy = 1
            dx = 0
        elif char == 'v':
            dy = -1
            dx = 0
        elif char == '?':
            direction = random.randint(0, 3)
            dy = 0
            dx = 0
            if direction == 0:
                dx = 1
            elif direction == 1:
                dx = -1
            elif direction == 2:
                dy = 1
            elif direction == 3:
                dy = -1
        elif char == '_':
            a = stack.pop()
            dy = 0
            if a == 0:
                dx = 1
            else:
                dx = -1
        elif char == '|':
            a = stack.pop()
            dx = 0
            if a == 0:
                dy = -1
            else:
                dy = 1
        elif char == '"':
            ascii_mode = not ascii_mode
        elif char == ':':
            if len(stack) > 0:
                stack.append(stack[-1])
            else:
                stack.append(0)
        elif char == "\\":
            if len(stack) > 1:
                a = stack.pop()
                b = stack.pop()
                stack.append(a)
                stack.append(b)
            else:
                stack.append(0)
        elif char == '$':
            stack.pop()
        elif char == '.':
            output.append(stack.pop())
        elif char == ',':
            output += chr(stack.pop())
        elif char == '#':
            trampoline = True
        elif char == 'p':
            y = stack.pop()
            x = stack.pop()
            v = stack.pop()
            lines[y][x] = chr(v)
        elif char == 'g':
            y = stack.pop()
            x = stack.pop()
            stack.append(ord(lines[y][x]))
        elif char == '@':
            return ''.join(map(str, output))
        elif char == ' ':
            continue
    return ' '.join(map(str, output))