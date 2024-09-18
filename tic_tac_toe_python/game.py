from classAI import TicTacToeAI
from player import Player

class TicTacToeGame:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.ai_agent = TicTacToeAI()
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")
        self.current_player = self.player1
        self.games_played = []

    def display_board(self):
        for i, row in enumerate(self.board):
            print("|".join(f"{cell:^1}" for cell in row))
            if i < 2:
                print("-" * 5)

    def make_move(self, row, col, player):
        """
        Function to make a move on the board.
        """
        if self.board[row][col] == " ":
            self.board[row][col] = player.sign
            return True
        else:
            return False

    def check_winner(self, player):
        """
        Function to check if a player has won.
        """
        for row in self.board:
            if all(cell == player.sign for cell in row):
                return True

        for col in range(len(self.board[0])):
            if all(self.board[row][col] == player.sign for row in range(len(self.board))):
                return True

        if all(self.board[i][i] == player.sign for i in range(len(self.board))) \
                or all(self.board[i][len(self.board) - 1 - i] == player.sign for i in range(len(self.board))):
            return True

        return False

    def play_game(self):
        """
        Function to play a single game of Tic-Tac-Toe.
        """
        while True:
            self.display_board()
            print(f"{self.current_player.name}'s turn")
            if self.current_player == self.player1:
                row = int(input("Enter row number (0, 1, or 2): "))
                col = int(input("Enter column number (0, 1, or 2): "))
            else:
                state = self.ai_agent.get_state(self.board)
                action = self.ai_agent.select_action(state, self.get_available_actions())
                row, col = action
            if self.make_move(row, col, self.current_player):
                if self.check_winner(self.current_player):
                    self.display_board()
                    print(f"{self.current_player.name} wins!")
                    self.games_played.append('win')
                    break
                elif all(all(cell != ' ' for cell in row) for row in self.board):
                    self.display_board()
                    print("It's a draw!")
                    self.games_played.append('draw')
                    break
                else:
                    self.current_player = self.player2 if self.current_player == self.player1 else self.player1
            else:
                print("That position is already taken. Try again.")

    def get_available_actions(self):
        """
        Function to get available actions (empty positions) on the board.
        """
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']

    def play_multiple_games(self, num_games):
        """
        Function to play multiple games of Tic-Tac-Toe.
        """
        for _ in range(num_games):
            self.board = [[" " for _ in range(3)] for _ in range(3)]
            self.current_player = self.player1
            self.play_game()
        self.ai_agent.evaluate_performance(self.games_played)

if __name__ == "__main__":
    game = TicTacToeGame()
    game.play_multiple_games(100)  # Play 100 games and evaluate performance
