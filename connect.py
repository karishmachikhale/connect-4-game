class Connect4:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.cols * 2 - 1))

    def is_valid_move(self, col):
        return 0 <= col < self.cols and self.board[0][col] == ' '

    def make_move(self, col):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                break

    def check_winner(self):
        # Check rows
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if (
                    self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] == self.board[row][col + 3]
                    and self.board[row][col] != ' '
                ):
                    return True

        # Check columns
        for col in range(self.cols):
            for row in range(self.rows - 3):
                if (
                    self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == self.board[row + 3][col]
                    and self.board[row][col] != ' '
                ):
                    return True

        # Check diagonals
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if (
                    self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == self.board[row + 3][col + 3]
                    and self.board[row][col] != ' '
                ):
                    return True

        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if (
                    self.board[row][col] == self.board[row - 1][col + 1] == self.board[row - 2][col + 2] == self.board[row - 3][col + 3]
                    and self.board[row][col] != ' '
                ):
                    return True

        return False

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.print_board()
            col = int(input(f"Player {self.current_player}, choose a column (0-{self.cols - 1}): "))
            if self.is_valid_move(col):
                self.make_move(col)
                if self.check_winner():
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    break
                elif self.is_board_full():
                    self.print_board()
                    print("It's a tie!")
                    break
                else:
                    self.switch_player()
            else:
                print("Invalid move. Try again.")


if __name__ == "__main__":
    game = Connect4()
    game.play()
