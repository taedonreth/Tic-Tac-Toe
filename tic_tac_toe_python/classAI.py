import random

class TicTacToeAI:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = {}
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration-exploitation tradeoff parameter

    def initialize_q_table(self, states, actions):
        """
        Function to initialize the Q-table with zeros.
        """
        for state in states:
            for action in actions:
                self.q_table[(state, action)] = 0.0

    def get_state(self, board):
        """
        Function to get the hashable representation of the current board state.
        """
        state_string = ''
        for row in board:
            for cell in row:
                state_string += cell
        return state_string

    def select_action(self, state, actions):
        """
        Function to select an action using epsilon-greedy strategy.
        """
        if random.random() < self.epsilon:
            return random.choice(actions)  # Explore: choose random action
        else:
            return max(actions, key=lambda a: self.q_table.get((state, a), 0))  # Exploit: choose action with max Q-value

    def q_learning_update(self, prev_state, action, reward, next_state, next_actions):
        """
        Function to update the Q-value of the previous state-action pair using the Q-learning update rule.
        """
        max_q_value = max(self.q_table.get((next_state, a), 0) for a in next_actions)
        self.q_table[(prev_state, action)] += self.alpha * (reward + self.gamma * max_q_value - self.q_table.get((prev_state, action), 0))

    def evaluate_performance(self, games_played):
        """
        Function to evaluate the performance of the AI agent.
        """
        win_count = sum(1 for result in games_played if result == 'win')
        draw_count = sum(1 for result in games_played if result == 'draw')
        win_rate = win_count / len(games_played) if games_played else 0
        draw_rate = draw_count / len(games_played) if games_played else 0
        print(f"Win rate: {win_rate}, Draw rate: {draw_rate}")
