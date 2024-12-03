class Board:
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_winner = None

    def __str__(self):
        s = '---------\n'
        for row in self.board:
            s += '|'
            for cell in row:
                s += ' ' if cell is None else cell
                s += '|'
            s += '\n---------\n'
        return s

    def make_move(self, x, y, player):
        if self.board[x][y] is None:
            self.board[x][y] = player
        else:
            raise Exception('Invalid move')
        return self.check_winner()
    
    def check_winner(self):
        # check rows
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] is not None:
                self.current_winner = row[0]
                return row[0]
        
        # check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] is not None:
                self.current_winner = self.board[0][col]
                return self.board[0][col]
        
        # check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            self.current_winner = self.board[0][0]
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            self.current_winner = self.board[0][2]
            return self.board[0][2]
        
        # check for draw
        if all(cell is not None for row in self.board for cell in row):
            return 'Draw'
        
        return None