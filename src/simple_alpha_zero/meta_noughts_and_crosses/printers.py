"""
    Functions for printing the game state within the terminal.
"""
import numpy as np


def small_board_print(state):
    """Print a small board state in ascii.

    Args:
        state: the state of the board as a flattened vector.
    """
    # Check for won state to print big version
    if np.all(state == "X"):
        print("\   /\n \ / \n  X  \n / \ \n/   \ ")
        return
    elif np.all(state == "O"):
        print("/ - \ \n|   |\n|   |\n|   |\n\ _ /")
        return

    horizontal_line = "-|-|-"

    def vertical_line(start_ind):
        return f"{state[start_ind]}|{state[start_ind+1]}|{state[start_ind+2]} "

    s1 = f"{vertical_line(0)}\n{horizontal_line}\n{vertical_line(3)}"
    s2 = f"\n{horizontal_line}\n{vertical_line(6)}"

    print(s1 + s2)
