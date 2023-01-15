from ai import Ai
from board import Board
import time


class Game:

    def __init__(self):
        self.board = Board()
        self.player_1 = 'X'
        self.player_2 = 'O'

    def input_player(self, player):
        while True:
            try:
                column = int(input("Enter the column number (0-7) to drop the piece for player " + player + ": "))
                if 0 <= column < 8:
                    break
                else:
                    print("Invalid input. Please enter a number between 0 and 7.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 7.")
        return column

    def human_vs_human(self):
        print("Starting a game of Human vs Human...")
        result = 0
        # Code to start the game goes here

        while True:

            self.board.print_board()
            result = self.board.check_board(self.player_1, self.player_2)
            if result != 0:
                break
            move = self.input_player(self.player_1)
            self.board.make_move_manuel_player(self.player_1, move)

            self.board.print_board()
            result = self.board.check_board(self.player_1, self.player_2)
            if result != 0:
                break
            move = self.input_player(self.player_2)
            self.board.make_move_manuel_player(self.player_2, move)

    def human_vs_ai(self, heuristic, depth):
        print("Starting a game of Human vs AI...")
        # Code to start the game goes here
        ai = Ai(heuristic)
        ai.depthLimit = int(depth)
        while True:

            self.board.print_board()
            result = self.board.check_board(self.player_1, self.player_2)
            if result != 0:
                break
            start_time = time.time()
            move = ai.ai_move(self.board)
            end_time = time.time()
            run_time = end_time - start_time
            print("Run time: AI player 1", run_time)
            print("move " + str(move))
            self.board.make_move_AI(self.player_1, move)

            self.board.print_board()
            result = self.board.check_board(self.player_1, self.player_2)
            if result != 0:
                break
            move = self.input_player(self.player_2)
            self.board.make_move_manuel_player(self.player_2, move)

    def ai_vs_ai(self, heuristic_1, heuristic_2, depth1, depth2):
        print("Starting a game of AI vs AI...")
        # Code to start the game goes here
        ai_1 = Ai(heuristic_1)
        ai_2 = Ai(heuristic_2)
        ai_1.depthLimit = int(depth1)
        ai_2.depthLimit = int(depth2)
        while True:

            self.board.print_board()
            result = self.board.check_board(self.player_1, self.player_2)
            if result != 0:
                break

            start_time = time.time()
            move = ai_1.ai_move(self.board)
            end_time = time.time()
            run_time = end_time - start_time
            print("Run time: AI player 1", run_time)

            self.board.make_move_AI(self.player_1, move)

            self.board.print_board()
            result = self.board.check_board(self.player_1, self.player_2)
            if result != 0:
                break

            start_time = time.time()
            move = ai_2.ai_move(self.board)
            end_time = time.time()
            run_time = end_time - start_time
            print("Run time: AI player 2", run_time)

            print("move " + str(move))
            self.board.make_move_AI(self.player_2, move)

    def play_game(self):
        self.main_menu()

    def main_menu(self):
        print("Welcome to the Game!")
        print("1. Human vs Human")
        print("2. Human vs AI")
        print("3. AI vs AI")
        choice = input("Please select an option: ")
        if choice == "1":
            self.human_vs_human()
        elif choice == "2":
            print("\n1. h1 is basic")
            print("2. h2 is medium")
            print("3. h3 is hard")
            print("Choose a heuristic :")
            heuristic = input("Please select an option: ")
            if heuristic != '1' and heuristic != '2' and heuristic != '3':
                print("Invalid choice. Please select a valid option.")
                self.main_menu()
            print("\nChoose a depth level for AI Player ")
            depth = input("depth level :")
            self.human_vs_ai(heuristic, depth)
        elif choice == "3":
            print("\n1. h1 is basic")
            print("2. h2 is medium")
            print("3. h3 is hard")
            print("Choose a heuristic for AI Player 1 :")
            heuristic1 = input("Please select an option: ")
            if heuristic1 != '1' and heuristic1 != '2' and heuristic1 != '3':
                print("Invalid choice. Please select a valid option.")
                self.main_menu()
            print("\n1. h1 is basic")
            print("2. h2 is medium")
            print("3. h3 is hard")
            print("Choose a heuristic for AI Player 2 :")
            heuristic2 = input("Please select an option: ")
            if heuristic2 != '1' and heuristic2 != '2' and heuristic2 != '3':
                print("Invalid choice. Please select a valid option.")
                self.main_menu()
            print("\nChoose a depth level for AI Player 1")
            depth1 = input("depth level :")
            print("\nChoose a depth level for AI Player 2")
            depth2 = input("depth level :")
            self.ai_vs_ai(heuristic1, heuristic2, depth1, depth2)
        else:
            print("Invalid choice. Please select a valid option.")
            self.main_menu()


if __name__ == "__main__":
    game = Game()
    game.play_game()
