class Board:
    HEIGHT = 7
    WIDTH = 8

    def __init__(self, orig=None):
        if orig:
            self.board = [list(col) for col in orig.board]
        else:
            self.board = [['.' for _ in range(8)] for _ in range(7)]

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print('\n')

    def make_children(self, player):
        children = []
        for i in range(self.WIDTH):
            child = Board(self)
            should_append = child.make_move_AI(player, i)
            if should_append:
                children.append((i, child))
        return children

    def make_move_AI(self, player, column):
        if column < self.WIDTH :
            for i in range(self.HEIGHT - 1, -1, -1):
                if self.board[i][column] == '.':
                    self.board[i][column] = player
                    return True
        else:
            print("Invalid input. AI has a error. The number between 0 and 7.")
            return False

    # Function control input value and move point in board
    def make_move_manuel_player(self, player, column):
        if column < self.WIDTH:
            for i in range(self.HEIGHT - 1, -1, -1):
                if self.board[i][column] == '.':
                    self.board[i][column] = player
                    return
        else:
            print("Invalid input. Please enter a number between 0 and 7.")

    # if games is continuing return 0
    # if player1 win return 1, if Player2 win return 2
    # if board has not empty point return 0
    def check_board(self, player1, player2):
        if self.is_full():
            print("The board is full. Game is a draw.")
            return -1
        if self.check_win(player1):
            print("Player1 wins!")
            return 1
        elif self.check_win(player2):
            print("Player2 wins!")
            return 2
        else:
            return 0

    def is_full(self):
        for row in self.board:
            for col in row:
                if col == '.':
                    return False
        return True

    def check_win(self, player):
        # check for horizontal win
        for row in self.board:
            for i in range(len(row) - 3):
                if row[i] == player \
                        and row[i + 1] == player \
                        and row[i + 2] == player \
                        and row[i + 3] == player:
                    return True

        # check for vertical win
        for col in range(len(self.board[0])):
            for row in range(len(self.board) - 3):
                if self.board[row][col] == player \
                        and self.board[row + 1][col] == player \
                        and self.board[row + 2][col] == player \
                        and self.board[row + 3][col] == player:
                    return True

        # check for diagonal win
        for row in range(len(self.board) - 3):
            for col in range(len(self.board[0]) - 3):
                if self.board[row][col] == player \
                        and self.board[row + 1][col + 1] == player \
                        and self.board[row + 2][col + 2] == player \
                        and self.board[row + 3][col + 3] == player:
                    return True
                if self.board[row][col + 3] == player \
                        and self.board[row + 1][col + 2] == player \
                        and self.board[row + 2][col + 1] == player \
                        and self.board[row + 3][col] == player:
                    return True
        return False
