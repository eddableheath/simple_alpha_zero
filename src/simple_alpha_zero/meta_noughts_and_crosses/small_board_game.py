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

    def get_state(self):
        """Get the current state of the board"""
        return self.state

    def which_positions_available(self):
        """Get the available positions to play"""
        return np.where(self.state == " ")

    def check_if_won(self):
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
                return 0
            elif np.all(self.state[win_con] == "O"):
                return 1

        return None

    def update_state(self, position: int, player: int):
        """Update the state of the board based on the position

        Args:
            position: position to update
            player: which player is making a move, int=[0,1]
        """
        if self.state[position] != " ":
            print("Position already taken! Try again!")
            return

        self.state[position] = self.player_states[player]

        player_win = self.check_if_won()
        if player_win is not None:
            self.state = np.full(9, self.player_states[player_win])
