import random
import keyboard
import time
import os

WIDTH = 16
HEIGHT = 8


def on_key_press(event):
    global key
    if event.name == 'q':
        exit()
    else:
        key = event.name


keyboard.on_press(on_key_press)


class PythonPart:
    def __init__(self, y, x):
        self.x = x
        self.y = y


def print_board(b):
    os.system("cls")
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(b[y][x], end=' ')
        print()
    print()


key = ''
board = []
applePlaced = False

for i in range(HEIGHT):
    r = []
    for j in range(WIDTH):
        r.append('.')
    board.append(r)

x0, y0 = random.randint(1, WIDTH - 2), random.randint(1, HEIGHT - 2)
x1, y1 = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])

python = [PythonPart(y0, x0),
          PythonPart(y0 + y1, x0 + x1)]

for cell in python:
    board[cell.y][cell.x] = '#'
board[python[0].y][python[0].x] = '%'

print_board(board)

board[python[0].y][python[0].x] = '#'

while key not in ('w', 'a', 's', 'd'):
    time.sleep(0.1)


# start food
while True:
    food_x, food_y = random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)
    if board[food_y][food_x] == '.':
        board[food_y][food_x] = '@'
        break

while True:
    # change direction
    if key == 'w':
        new_x, new_y = python[0].x, python[0].y - 1
    elif key == 'a':
        new_x, new_y = python[0].x - 1, python[0].y
    elif key == 's':
        new_x, new_y = python[0].x, python[0].y + 1
    elif key == 'd':
        new_x, new_y = python[0].x + 1, python[0].y
    else:
        print_board(board)
        continue

    # collision
    if new_x < 0 or new_x >= WIDTH or new_y < 0 or new_y >= HEIGHT:
        print("LOOOSE")
        break
    if board[new_y][new_x] == '#':
        print("LOOOSE")
        break

    python.insert(0, PythonPart(new_y, new_x))

    # move
    if board[new_y][new_x] == '@':
        board[new_y][new_x] = '%'
        applePlaced = False

        # create new apple
        if applePlaced is False:
            while True:
                food_x, food_y = random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)
                if board[food_y][food_x] == '.':
                    board[food_y][food_x] = '@'
                    applePlaced = True
                    break

    else:
        tail = python.pop()
        board[tail.y][tail.x] = '.'
        board[new_y][new_x] = '%'

    print_board(board)

    board[new_y][new_x] = '#'

    if len(python) == WIDTH * HEIGHT:
        print("WIN!!!")
        break

    time.sleep(0.5)
