import math


def swap_alpha(temp, best_score):
    return temp > best_score


def swap_beta(temp, best_score):
    return temp < best_score


def swap_player(player):
    return 'X' if player == 'O' else 'O'


class Ai:

    def __init__(self, heuristic):
        print("hello i am ai")
        self.depthLimit = 0
        self.heuristic = self.heuristic2
        if heuristic == 1:
            self.heuristic = self.heuristic1
        elif heuristic == 2:
            self.heuristic = self.heuristic2
        elif heuristic == 3:
            self.heuristic = self.heuristic3

    def ai_move(self, board):
        score, move = self.alpha_beta(board, self.depthLimit, 'X', -math.inf, math.inf)
        return move

    def alpha_beta(self, board, depth, player, alpha, beta):

        if board.is_full():
            return -math.inf if player == 'X' else math.inf, -1
        elif depth == 0:
            return self.heuristic(board, player), -1

        if player == 'X':
            bestScore = -math.inf
            swap = swap_alpha
        else:
            bestScore = math.inf
            swap = swap_beta

        bestMove = -2

        children = board.make_children(player)

        for child in children:
            move, childboard = child
            # print(child)
            temp = self.alpha_beta(childboard, depth - 1, swap_player(player), alpha, beta)[0]
            if swap(temp, bestScore):
                bestScore = temp
                bestMove = move

            if player == 'X':
                alpha = max(alpha, temp)
            else:
                beta = min(beta, temp)
            if alpha >= beta:
                break
        return bestScore, bestMove

    def heuristic1(self, board, player):
        score = 0
        state = board.board
        # check rows
        for row in range(7):
            for col in range(4):
                if state[row][col] == player and state[row][col + 1] == player and state[row][col + 2] == player and board[row][col + 3] == player:
                    score += 1
        # check columns
        for col in range(7):
            for row in range(3):
                if state[row][col] == player and state[row + 1][col] == player and state[row + 2][col] == player and state[row + 3][col] == player:
                    score += 1
        # check diagonals
        for row in range(3):
            for col in range(4):
                if state[row][col] == player and state[row + 1][col + 1] == player and state[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                    score += 1
        for row in range(3):
            for col in range(3, 7):
                if state[row][col] == player and state[row + 1][col - 1] == player and state[row + 2][col - 2] == player and board[row + 3][col - 3] == player:
                    score += 1
        return score

    def heuristic2(self, board, player):
        score = 0
        opponent = 'X' if player == 'O' else 'O'
        state = board.board
        for row in range(board.HEIGHT):
            for col in range(board.WIDTH):
                if state[row][col] == player:
                    if row < 3:
                        if state[row + 1][col] == player and state[row + 2][col] == player and state[row + 3][col] == player:
                            score += 1
                    if col < 4:
                        if state[row][col + 1] == player and state[row][col + 2] == player and state[row][col + 3] == player:
                            score += 1
                    if row < 3 and col < 4:
                        if state[row + 1][col + 1] == player and state[row + 2][col + 2] == player and state[row + 3][col + 3] == player:
                            score += 1
                    if row < 3 and col > 2:
                        if state[row + 1][col - 1] == player and state[row + 2][col - 2] == player and state[row + 3][col - 3] == player:
                            score += 1
                        for row in range(board.HEIGHT):
                            for col in range(board.WIDTH):
                                if state[row][col] == opponent:
                                    if row < 3:
                                        if state[row + 1][col] == opponent and state[row + 2][col] == opponent and state[row + 3][col] == opponent:
                                            score -= 1
                                    if col < 4:
                                        if state[row][col + 1] == opponent and state[row][col + 2] == opponent and state[row][col + 3] == opponent:
                                            score -= 1
                                    if row < 3 and col < 4:
                                        if state[row + 1][col + 1] == opponent and state[row + 2][col + 2] == opponent and state[row + 3][col + 3] == opponent:
                                            score -= 1
                                    if row < 3 and col > 2:
                                        if state[row + 1][col - 1] == opponent and state[row + 2][col - 2] == opponent and state[row + 3][col - 3] == opponent:
                                            score -= 1
        return score


    def heuristic3(self, board, player):
        player_1 = 'X'
        player_2 = 'O'
        score = 0
        state = board.board
        for i in range(0, board.HEIGHT):
            for j in range(0, board.WIDTH):
                # check horizontal streaks
                try:
                    # add player one streak scores to score
                    if state[i][j] == state[i + 1][j] == player_1:
                        score += 10
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == player_1:
                        score += 100
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == state[i + 3][j] == player_1:
                        score += 10000

                    # subtract player two streak score to score
                    if state[i][j] == state[i + 1][j] == player_2:
                        score -= 10
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == player_2:
                        score -= 100
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == state[i + 3][j] == player_2:
                        score -= 10000
                except IndexError:
                    pass

                # check vertical streaks
                try:
                    # add player one vertical streaks to score
                    if state[i][j] == state[i][j + 1] == player_1:
                        score += 10
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == player_1:
                        score += 100
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == state[i][j + 3] == player_1:
                        score += 10000

                    # subtract player two streaks from score
                    if state[i][j] == state[i][j + 1] == player_2:
                        score -= 10
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == player_2:
                        score -= 100
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == state[i][j + 3] == player_2:
                        score -= 10000
                except IndexError:
                    pass

                # check positive diagonal streaks
                try:
                    # add player one streaks to score
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == player_1:
                        score += 100
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == player_1:
                        score += 100
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == state[i + 3][j + 3] == player_1:
                        score += 10000

                    # add player two streaks to score
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == player_2:
                        score -= 100
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == player_2:
                        score -= 100
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == state[i + 3][j + 3] == player_2:
                        score -= 10000
                except IndexError:
                    pass

                # check negative diagonal streaks
                try:
                    # add  player one streaks
                    if not j - 3 < 0 and state[i][j] == state[i + 1][j - 1] == player_1:
                        score += 10
                    if not j - 3 < 0 and state[i][j] == state[i + 1][j - 1] == state[i + 2][j - 2] == player_1:
                        score += 100
                    if not j - 3 < 0 and state[i][j] == state[i + 1][j - 1] == state[i + 2][j - 2] == state[i + 3][j - 3] == player_1:
                        score += 10000

                    # subtract player two streaks
                    if not j - 3 < 0 and state[i][j] == state[i + 1][j - 1] == player_2:
                        score -= 10
                    if not j - 3 < 0 and state[i][j] == state[i + 1][j - 1] == state[i + 2][j - 2] == player_2:
                        score -= 100
                    if not j - 3 < 0 and state[i][j] == state[i + 1][j - 1] == state[i + 2][j - 2] == state[i + 3][j - 3] == player_2:
                        score -= 10000
                except IndexError:
                    pass
        return score
