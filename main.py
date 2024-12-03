import TicTacToe

def main():
    print("Welcome to Tic Tac Toe! Enter 'exit' at any time to quit.")
    game = TicTacToe.Board()
    current_player = 'X'
    while not game.current_winner:
        print(game)
        move = input(f"Player {current_player}, enter your move as 'row,col': ")
        try:
            if move.lower() == 'exit':
                print("Exiting game.")
                break
            x, y = map(int, move.split(','))
            x, y = x-1, y-1
            winner = game.make_move(x, y, current_player)
            print(game)
            if winner:
                if winner == 'Draw':
                    print("The game is a draw!")
                else:
                    print(f"Player {winner} wins!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        except Exception as e:
            print(e)
            print("Invalid move. Please try again.")

if __name__ == "__main__":
    main()