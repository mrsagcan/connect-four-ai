import math


#Swap Function for Alpha Values
def swap_alpha(temp, best_score):
    return temp > best_score

#Swap Function for Beta Values
def swap_beta(temp, best_score):
    return temp < best_score

#Swap Function for Player Value
def swap_player(player):
    return 'X' if player == 'O' else 'O'


class Ai:


    def __init__(self, depthLimit, heuristic_choice):
        self.depthLimit = depthLimit
        self.heuristic = None
        self.choose_heuristic(heuristic_choice)

    #Chooses a heuristic according to input. 
    def choose_heuristic(self, heuristic_choice):
        if heuristic_choice == '1':
            self.heuristic = self.heuristic1
        elif heuristic_choice == '2':
            self.heuristic = self.heuristic2
        elif heuristic_choice == '3':
            self.heuristic = self.heuristic3
        else:
            print("ERROR: Your heuristic choice is invalid.")

    #Makes a move for AI
    def ai_move(self, board):
        score, move = self.alpha_beta(board, self.depthLimit, 'X', -math.inf, math.inf)
        return move

    #Alpha-Beta Pruning
    def alpha_beta(self, board, depth, player, alpha, beta):

        #If board is full returns infinite values because no one won.
        if board.is_full():
            return -math.inf if player == 'X' else math.inf, -1
        #If depth limit is reached looks for a score using current heuristic
        elif depth == 0:
            return self.heuristic(board, player), -1

        #Sets alpha and beta values before starting the recursion.
        if player == 'X':
            best_score = -math.inf
            swap = swap_alpha
        else:
            best_score = math.inf
            swap = swap_beta

        best_move = -2

        #Creates a children list of future moves.
        children = board.make_children(player)

        #Negamax starts
        for child in children:

            #Takes two values from tuple. Move is the column value and childboard is the state after that move.
            move, childboard = child
            temp = self.alpha_beta(childboard, depth - 1, swap_player(player), alpha, beta)[0] #Gets the heuristic return value.

            #Sets if there is a new max score.
            if swap(temp, best_score):
                best_score = temp
                best_move = move

            if player == 'X':
                alpha = max(alpha, temp)
            else:
                beta = min(beta, temp)
            if alpha >= beta:
                break
        return best_score, best_move

    @staticmethod
    def heuristic1(board, player):
        score = 0
        state = board.board
        # checks rows
        for row in range(7):
            for col in range(4):
                if state[row][col] == player and state[row][col + 1] == player and state[row][col + 2] == player and state[row][col + 3] == player:
                    score += 1
        # checks columns
        for col in range(7):
            for row in range(3):
                if state[row][col] == player and state[row + 1][col] == player and state[row + 2][col] == player and state[row + 3][col] == player:
                    score += 1
        # checks diagonals
        for row in range(3):
            for col in range(4):
                if state[row][col] == player and state[row + 1][col + 1] == player and state[row + 2][col + 2] == player and state[row + 3][col + 3] == player:
                    score += 1
        for row in range(3):
            for col in range(3, 7):
                if state[row][col] == player and state[row + 1][col - 1] == player and state[row + 2][col - 2] == player and state[row + 3][col - 3] == player:
                    score += 1
        return score

    @staticmethod
    def heuristic2(board, player):
        score = 0
        opponent = 'X' if player == 'O' else 'O'
        state = board.board
        for row in range(board.HEIGHT):
            for col in range(board.WIDTH):
                if state[row][col] == player:
                    # checks rows
                    if row < 3:
                        if state[row + 1][col] == player and state[row + 2][col] == player and state[row + 3][col] == player:
                            score += 1
                    # checks columns
                    if col < 4:
                        if state[row][col + 1] == player and state[row][col + 2] == player and state[row][col + 3] == player:
                            score += 1
                    #checks diagonals
                    if row < 3 and col < 4:
                        if state[row + 1][col + 1] == player and state[row + 2][col + 2] == player and state[row + 3][col + 3] == player:
                            score += 1
                    if row < 3 and col > 2:
                        if state[row + 1][col - 1] == player and state[row + 2][col - 2] == player and state[row + 3][col - 3] == player:
                            score += 1
                        for row in range(board.HEIGHT):
                            for col in range(board.WIDTH):
                                if state[row][col] == opponent:
                                    # does the same checks for opponent
                                    if row < 3:
                                        if state[row + 1][col] == opponent and state[row + 2][col] == opponent and state[row + 3][col] == opponent:
                                            score -= 1
                                    if col < 4:
                                        if state[row][col + 1] == opponent and state[row][col + 2] == opponent and state[row][col + 3] == opponent:
                                            score -= 1
                                    if row < 3 and col < 4:
                                        if state[row + 1][col + 1] == opponent and state[row + 2][
                                            col + 2] == opponent and state[row + 3][col + 3] == opponent:
                                            score -= 1
                                    if row < 3 and col > 2:
                                        if state[row + 1][col - 1] == opponent and state[row + 2][
                                            col - 2] == opponent and state[row + 3][col - 3] == opponent:
                                            score -= 1
        return score

    @staticmethod
    def heuristic3(board, player):
        player_1 = player
        player_2 = 'X' if player == '0' else '0'
        score = 0
        state = board.board
        for i in range(0, board.HEIGHT):
            for j in range(0, board.WIDTH):
                # checks rows
                try:
                    # adds scores gradually for that state if player_1 plays
                    if state[i][j] == state[i + 1][j] == player_1:
                        score += 10
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == player_1:
                        score += 100
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == state[i + 3][j] == player_1:
                        score += 10000

                    # subtracts scores gradually for that state if player_2 plays
                    if state[i][j] == state[i + 1][j] == player_2:
                        score -= 10
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == player_2:
                        score -= 100
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == state[i + 3][j] == player_2:
                        score -= 10000
                except IndexError:
                    pass

                # checks columns
                try:
                    # adds scores gradually for that state if player_1 plays
                    if state[i][j] == state[i][j + 1] == player_1:
                        score += 10
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == player_1:
                        score += 100
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == state[i][j + 3] == player_1:
                        score += 10000

                    # subtracts scores gradually for that state if player_2 plays
                    if state[i][j] == state[i][j + 1] == player_2:
                        score -= 10
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == player_2:
                        score -= 100
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == state[i][j + 3] == player_2:
                        score -= 10000
                except IndexError:
                    pass

                # checks positive diagonals
                try:
                    # adds scores gradually for that state if player_1 plays
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == player_1:
                        score += 10
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == state[i + 2][
                        j + 2] == player_1:
                        score += 100
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == \
                            state[i + 3][j + 3] == player_1:
                        score += 10000

                    # subtracts scores gradually for that state if player_2 plays
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == player_2:
                        score -= 10
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == state[i + 2][
                        j + 2] == player_2:
                        score -= 100
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == \
                            state[i + 3][j + 3] == player_2:
                        score -= 10000
                except IndexError:
                    pass

                # checks negative diagonals
                try:
                    # adds scores gradually for that state if player_1 plays
                    if not j - 3 < 0 and state[i][j] == state[i + 1][j - 1] == player_1:
                        score += 10
                    if not j - 3 < 0 and state[i][j] == state[i + 1][j - 1] == state[i + 2][j - 2] == player_1:
                        score += 100
                    if not j - 3 < 0 and state[i][j] == state[i + 1][j - 1] == state[i + 2][j - 2] == state[i + 3][
                        j - 3] == player_1:
                        score += 10000

                    # subtracts scores gradually for that state if player_2 plays
                    if not j - 3 < 0 and state[i][j] == state[i + 1][j - 1] == player_2:
                        score -= 10
                    if not j - 3 < 0 and state[i][j] == state[i + 1][j - 1] == state[i + 2][j - 2] == player_2:
                        score -= 100
                    if not j - 3 < 0 and state[i][j] == state[i + 1][j - 1] == state[i + 2][j - 2] == state[i + 3][
                        j - 3] == player_2:
                        score -= 10000
                except IndexError:
                    pass
        return score
