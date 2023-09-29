"""
    Classes and functions for a small (standard) board game of noughts and crosses.
"""

from warnings import warn

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

    def update_state(self, position: int, player: int):
        """Update the state of the board based on the position

        Args:
            position: position to update
            player: which player is making a move, int=[0,1]
        """
        if self.state[position] != " ":
            warn("Position already taken! Try Again!")
            return 1

        self.state[position] = self.player_states[player]
