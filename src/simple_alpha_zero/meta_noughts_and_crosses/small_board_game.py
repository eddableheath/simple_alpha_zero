"""
    Classes and functions for a small (standard) board game of noughts and crosses.
"""

import numpy as np


class SmallBoard:

    """
    Small board class. Contains information of current state of a small board, with
    possible states:

                            [' ', 'X', 'O]
    """

    def __init__(self) -> None:
        self.state = np.full(9, " ", dtype=str)
        self.player_states = ["X", "O"]
        self.decided = False
        self.won_by = None

    def get_state(self) -> np.ndarray:
        """Get the current state of the board"""
        return self.state

    def get_decided(self) -> bool:
        """Get whether the game has been won or not"""
        return self.decided

    def get_won_by(self) -> int:
        """Get which player won the game"""
        return self.won_by

    def which_positions_available(self) -> np.ndarray:
        """Get the available positions to play"""
        return np.where(self.state == " ")

    def check_if_won(self) -> int or None:
        """Check if a player has won, return which player has won."""
        win_cons = np.array(
            [
                [0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8],
                [0, 4, 8],
                [2, 4, 6],
            ]
        )
        for win_con in win_cons:
            if np.all(self.state[win_con] == "X"):
                self.decided = True
                self.won_by = 0
                return 0
            elif np.all(self.state[win_con] == "O"):
                self.decided = True
                self.won_by = 1
                return 1

        return None

    def update_state(self, position: int, player: int):
        """Update the state of the board based on the position

        Args:
            position: position to update
            player: which player is making a move, int=[0,1]
        """
        self.state[position] = self.player_states[player]

        # Check if there is a winner
        self.check_if_won()
        if self.decided:
            self.state = np.full(9, self.player_states[self.won_by])
