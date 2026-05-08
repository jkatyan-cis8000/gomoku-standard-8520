class Game:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = 'black'
        self.winner = None
        self.moves = []

    def is_valid_move(self, row, col):
        if not (0 <= row < 15 and 0 <= col < 15):
            return False
        return self.board[row][col] is None

    def make_move(self, row, col):
        if not self.is_valid_move(row, col):
            return False
        self.board[row][col] = self.current_player
        self.moves.append((row, col))
        if self._check_win(row, col):
            self.winner = self.current_player
        else:
            self.current_player = 'white' if self.current_player == 'black' else 'black'
        return True

    def _check_win(self, row, col):
        player = self.board[row][col]
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for d in [1, -1]:
                r, c = row + dr * d, col + dc * d
                while 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == player:
                    count += 1
                    r += dr * d
                    c += dc * d
            if count >= 5:
                return True
        return False

    def is_full(self):
        return all(cell is not None for row in self.board for cell in row)
