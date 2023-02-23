import copy
import random

space = " "
winner = None
board = [[space for i in range(3)] for j in range(3)]


def print_board(board):
    for i, v in enumerate(board):
        if i != 0:
            print("-----")
        print(*v, sep = "|")


def make_move(board,x,y,char):
    if  board[x][y] == space:
        board[x][y] = char
        return True
    else:
        return False

def get_move():
    try:
        x, y = map(int, input("Введите индекс клетки: ").split())
        return make_move(board, x, y, "X")
    except (ValueError, IndexError):
        print("Неправильный индекс")
        return False

def is_full(board):
    if any([space in i for i in board]):
        return False
    else:
        return True


def check_winner(board):
    if board[0][0] == board[0][1] == board[0][2] == "O" or \
board[1][0] == board[1][1] == board[1][2] == "O" or \
board[2][0] == board[2][1] == board[2][2] == "O" or \
board[0][0] == board[1][0] == board[2][0] == "O" or \
board[0][1] == board[1][1] == board[2][1] == "O" or \
board[0][2] == board[1][2] == board[2][2] == "O" or \
board[0][0] == board[1][1] == board[2][2] == "O" or \
board[0][2] == board[1][1] == board[2][0] == "O":
        return "O"
    elif board[0][0] == board[0][1] == board[0][2] == "X" or \
board[1][0] == board[1][1] == board[1][2] == "X" or \
board[2][0] == board[2][1] == board[2][2] == "X" or \
board[0][0] == board[1][0] == board[2][0] == "X" or \
board[0][1] == board[1][1] == board[2][1] == "X" or \
board[0][2] == board[1][2] == board[2][2] == "X" or \
board[0][0] == board[1][1] == board[2][2] == "X" or \
board[0][2] == board[1][1] == board[2][0] == "X":
        return "X"
    elif is_full(board):
        return "draw"
    else:
        return None



def computer_move(board):
    for i in range(3):
        for j in range(3):
            cop = copy.deepcopy(board)
            make_move(cop, i, j, "O")
            if check_winner(cop) == "O":
                return i, j
    for i in range(3):
        for j in range(3):
            cop = copy.deepcopy(board)
            make_move(cop, i, j, "X")
            if check_winner(cop) == "X":
                return i, j
    if board[1][1] == space:
        return 1, 1
    moves = []
    cop = copy.deepcopy(board)
    for i, j in [(0, 0),(2, 0),(0, 2),(2, 2)]:
        if make_move(cop,i,j,"O"):
            moves.append((i,j))
    if moves != []:
        i, j = random.choice(moves)
        return i, j
    for i, j in [(0, 1),(1, 2),(2, 1),(1, 1)]:
        if make_move(cop,i,j,"O"):
            moves.append((i,j))
    if moves != []:
        i, j = random.choice(moves)
        return i, j
    return 0, 0
    

while winner == None:
    print_board(board)
    if get_move():
        pass
    else:
        continue
    winner = check_winner(board)
    i, j = computer_move(board)
    make_move(board, i, j, "O")
    winner = check_winner(board)
else:
    if winner == "X":
        print_board(board)
        print("Вы победили!")
    elif winner == "O":
        print_board(board)
        print("Победил компьютер!")
    elif winner == "draw":
        print_board(board)
        print("Ничья!")