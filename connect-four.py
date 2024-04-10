board = []

print('♥️------------᧔o᧓------------♥️')
print('|      connect four!        |')

def init_board():
    for i in range(6):
        board.append([' - ',' - ',' - ',' - ',' - ',' - ',' - '])

def print_board():
    print('♥️---------------------------♥️')
    print('| 1 | 2 | 3 | 4 | 5 | 6 | 7 |')
    print('♥️---------------------------♥️')
    for row in board:
        print('', end='|')
        for col in row:
            print(col, end='|')
        print() 

playerCounter = 1
init_board()
print_board()

while True:

    token = ' X '
    if playerCounter % 2 == 0:
        token = ' O '

    print('♥️---------------------------♥️')
    print('')
    choice =int(input("choose column (1-7): "))
    print('')
    choice -= 1

    for i in range (5, -1, -1):
        if board[i][choice] == ' - ':
            board[i][choice] = token
            playerCounter += 1
            break

    print_board()

def check_horizontal(row):
    count = 1
    previous_token = row[0]
    for token in row[1:]:
        if token == previous_token and token != ' ':
            count += 1
            if count == 4:
                return True
        else:
            count = 1
        previous_token = token
    return False