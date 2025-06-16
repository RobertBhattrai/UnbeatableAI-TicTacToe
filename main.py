import math

# Board setup
board = [' ' for _ in range(9)]  # 3x3 board

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def available_moves():
    return [i for i, spot in enumerate(board) if spot == ' ']

def make_move(position, player):
    board[position] = player

def winner(player):
    win_cond = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[i] == player for i in cond) for cond in win_cond)

def is_full():
    return ' ' not in board

def minimax(is_maximizing):
    if winner('O'):
        return 1
    elif winner('X'):
        return -1
    elif is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves():
            board[move] = 'O'
            score = minimax(False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves():
            board[move] = 'X'
            score = minimax(True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

def best_ai_move():
    best_score = -math.inf
    move = None
    for i in available_moves():
        board[i] = 'O'
        score = minimax(False)
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    return move

# Game loop
def play():
    print("Welcome to Tic-Tac-Toe! You are 'X'. AI is 'O'.")
    print_board()

    while True:
        # Human move
        move = int(input("Enter your move (0-8): "))
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        make_move(move, 'X')
        print_board()
        if winner('X'):
            print("🎉 You win!")
            break
        elif is_full():
            print("It's a tie!")
            break

        # AI move
        print("AI is thinking...")
        ai_move = best_ai_move()
        make_move(ai_move, 'O')
        print_board()
        if winner('O'):
            print("😢 AI wins!")
            break
        elif is_full():
            print("It's a tie!")
            break

# Run the game
play()
