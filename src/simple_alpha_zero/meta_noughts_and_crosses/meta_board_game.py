"""
    Classes and functions for meta noughts and crosses board.
"""

# import numpy as np

from simple_alpha_zero.meta_noughts_and_crosses.small_board_game import SmallBoard


class BigBoard:

    """
    Big board class. Contains 9 smaller games, and rules for moving from one to the
    other.

    The last state is given by (b, s), where b is the position of the small board on the
    bigger board, and s is the position on that small board.
    """

    def __init__(self) -> None:
        self.small_boards = [SmallBoard() for _ in range(9)]
        self.last_move = None

    def get_states(self):
        """Get current state of the board"""
        states = [board.get_state() for board in self.small_boards]
        return states

    def get_possible_moves(self):
        """Get the possible legal next moves"""
        if self.last_move is not None:
            None
