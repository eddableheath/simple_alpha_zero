"""
    Classes and functions for meta noughts and crosses board.
"""

from typing import Tuple

import numpy as np

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
        self.decided = False

    def get_states(self):
        """Get current state of the board"""
        states = [board.get_state() for board in self.small_boards]
        return states

    def get_decided(self):
        """Return decided state"""
        return self.decided

    def get_possible_moves(self):
        """Get the possible legal next moves"""
        if self.last_move is not None:
            if not self.small_boards[self.last_move[1]].get_decided():
                return [
                    (self.last_move[1] + 1, position + 1)
                    for position in self.small_boards[
                        self.last_move[1]
                    ].which_positions_available()[0]
                ]
            else:
                moves = []
                for idx, board in enumerate(self.small_boards):
                    if not board.get_decided():
                        moves.append(
                            [
                                (idx + 1, position + 1)
                                for position in board.which_positions_available()[0]
                            ]
                        )
                return sum(moves, [])
        else:
            moves = []
            for idx, board in enumerate(self.small_boards):
                moves.append(
                    [
                        (idx + 1, position + 1)
                        for position in board.which_positions_available()[0]
                    ]
                )
            return sum(moves, [])

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
            if np.all([self.small_boards[i].check_if_won() for i in win_con] == 0):
                self.decided = True
                self.won_by = 0
                return 0
            elif np.all([self.small_boards[i].check_if_won() for i in win_con] == 1):
                self.decided = True
                self.won_by = 1
                return 1

        return None

    def update_board(self, position: Tuple[int, int], player: int):
        """Update the board with a new move"""
        self.small_boards[position[0]].update_state(position[1], player)
        self.last_move = position
        self.check_if_won()
