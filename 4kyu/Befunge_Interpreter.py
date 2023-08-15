import random

def interpret(code):
    output = []
    stack = []

    lines = [[*x] for x in code.split('\n')]
    for l in lines:
        print(l)

    char = ' '

    line = 0
    index = 0

    vertical = 0  # 1 = up, -1 = down, 0 = still
    horizontal = 1  # 1 = right, -1 = left, 0 = still

    first = True
    ascii_mode = False
    trampoline = False


    while char != "@":
        # TODO: HANDLE QUOTES / ASCII Output
        if vertical > 0:
            line -= 1
        elif vertical < 0:
            line += 1

        if horizontal > 0:
            index += 1
        elif horizontal < 0:
            index -= 1

        if first:
            first = False
            line = 0
            index = 0
        char = lines[line][index]

        if ascii_mode and char != '"':
            stack.append(ord(char))
            continue

        print(f'Char: {char}')
        print(line, index)
        print(stack)
        print(output)

        if trampoline:
            trampoline = False
            print('BOUNCING')
            continue
        '''
'01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@'
		'''
        if char.isnumeric():
            stack.append(int(char))
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
            horizontal = 1
            vertical = 0
        elif char == '<':
            horizontal = -1
            vertical = 0
        elif char == '^':
            vertical = 1
            horizontal = 0
        elif char == 'v':
            vertical = -1
            horizontal = 0
        elif char == '?':
            direction = random.randint(0, 3)
            vertical = 0
            horizontal = 0
            if direction == 0:
                horizontal = 1
            elif direction == 1:
                horizontal = -1
            elif direction == 2:
                vertical = 1
            elif direction == 3:
                vertical = -1
        elif char == '_':
            a = stack.pop()
            vertical = 0
            if a == 0:
                horizontal = 1
            else:
                horizontal = -1
        elif char == '|':
            a = stack.pop()
            horizontal = 0
            if a == 0:
                vertical = -1
            else:
                vertical = 1
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


# print(interpret('>987v>.v\nv456<  :\n>321 ^ _@'))
# print(interpret('>25*"!dlroW olleH":v\n                v:,_@\n                >  ^\n'))
# print(interpret('08>:1-:v v *_$.@ \n  ^    _$>\:^'))
# print(interpret('01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@'))