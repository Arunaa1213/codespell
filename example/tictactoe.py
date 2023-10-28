def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    return board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player

def is_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    while True:
        print_board(board)
        row, col = map(int, input(f"Player {player}, enter row and column (e.g., 1 2): ").split())
        
        if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == ' ':
            board[row - 1][col - 1] = player
            if check_win(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            elif is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            player = 'X' if player == 'O' else 'O'
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
