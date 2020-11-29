board = list(range(1,10))
print('-' * 15)

def print_board():
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-' * 15)

print_board()

def func_turn_x():
    turn_x = int(input('Введите поле для ввода x: '))
    if 1 <= turn_x <= 9:
        if board[turn_x - 1] != 'x' and board[turn_x - 1] != 'o':
            board.pop(turn_x - 1)
            board.insert(turn_x - 1, 'x')

            print_board()
        else:
            print('Клетка уже занята.')
            func_turn_x()
    else:
        print('Вы ввели неверное число.')
        func_turn_x()

def func_turn_o():
    turn_o = int(input('Введите поле для ввода o: '))
    if 1 <= turn_o <= 9:
        if board[turn_o - 1] != 'x' and board[turn_o - 1] != 'o':
            board.pop(turn_o - 1)
            board.insert(turn_o - 1, 'o')

            print_board()
        else:
            print('Клетка уже занята.')
            func_turn_o()
    else:
        print('Вы ввели неверное число.')
        func_turn_o()

def win_cond():
    for i in range (3):
        if board[0 + i*3] == 'x' and board[1 + i*3] == 'x' and board[2 + i*3] == 'x' or \
            board[i] == 'x' and board[i + 3] == 'x' and board[i + 6] == 'x' or \
            board[0] == 'x' and board[4] == 'x' and board[8] == 'x' or \
            board[2] == 'x' and board[4] == 'x' and board[6] == 'x':
            return 'X won'
        if board[0 + i*3] == 'o' and board[1 + i*3] == 'o' and board[2 + i*3] == 'o' or \
            board[i] == 'o' and board[i + 3] == 'o' and board[i + 6] == 'o' or \
            board[0] == 'o' and board[4] == 'o' and board[8] == 'o' or \
            board[2] == 'o' and board[4] == 'o' and board[6] == 'o':
            return 'O won'
    else:
        return False

def draw():
    if ('x' and 'o' in board[0:3] and 'x' and 'o' in board[3:6] and 'x' and 'o' in board[6:9]) and \
        ('x' and 'o' in board[::3] and 'x' and 'o' in board[1::3] and 'x' and 'o' in board[2::3]) and \
        ('x' and 'o' in board[::4]) and ('x' and 'o' in [board[2], board[4], board[6]]):
        return 'Draw'
    else:
        return False

while True:
    if win_cond():
        print(win_cond())
        break
    if draw():
        print(draw())
        break
    if win_cond() is False and draw() is False:
        func_turn_x()
    if win_cond() is False and draw() is False:
        func_turn_o()

