"""
    Functions for printing the game state within the terminal.
"""
import numpy as np


def small_game_formatter(state):
    """Format the values of a small game into sensible thing to pass to printer"""
    print_array = np.full((5, 5), " ", dtype=str)
    if np.all(state == "X"):
        print_array = np.array(
            [
                ["\\", " ", " ", " ", "/"],
                [" ", "\\", " ", "/", " "],
                [" ", " ", "X", " ", " "],
                [" ", "/", " ", "\\", " "],
                ["/", " ", " ", " ", "\\"],
            ]
        )
        return print_array
    elif np.all(state == "O"):
        print_array = np.array(
            [
                ["/", " ", "-", " ", "\\"],
                ["|", " ", " ", " ", "|"],
                ["|", " ", "O", " ", "|"],
                ["|", " ", " ", " ", "|"],
                ["\\", " ", "-", " ", "/"],
            ]
        )
        return print_array

    horizontal_line = np.array(["-", "|", "-", "|", "-"])

    def val_line(ind_start):
        return np.array(
            [state[ind_start], "|", state[ind_start + 1], "|", state[ind_start + 2]]
        )

    for idx, _ in enumerate(print_array):
        if idx % 2 == 0:
            print_array[idx] = val_line(int(idx * 1.5))
        else:
            print_array[idx] = horizontal_line

    return print_array


def small_board_print(state):
    """Print a small board state in ascii.

    Args:
        state: the state of the board as a flattened vector.
    """
    print_array = small_game_formatter(state)
    st = ""
    for row in print_array:
        for element in row:
            st += element
        st += "\n"
    print(st)


def big_game_print_(states: np.ndarray):
    """Print a big game made of small games, on an input of their states

    states: (9, 9)
    """
    print_array = np.full((17, 17), "|", dtype=str)

    small_boards = [small_game_formatter(state) for state in states]
    horiz_line = np.full(5, "-", dtype=str)

    print_array[0:5, 0:5] = small_boards[0]
    print_array[6:11, 0:5] = small_boards[1]
    print_array[12:, 0:5] = small_boards[2]
    print_array[0:5, 6:11] = small_boards[3]
    print_array[6:11, 6:11] = small_boards[4]
    print_array[12:, 6:11] = small_boards[5]
    print_array[0:5, 12:] = small_boards[6]
    print_array[6:11, 12:] = small_boards[7]
    print_array[12:, 12:] = small_boards[8]

    print_array[5, 0:5] = horiz_line
    print_array[5, 6:11] = horiz_line
    print_array[5, 12:] = horiz_line
    print_array[11, 0:5] = horiz_line
    print_array[11, 6:11] = horiz_line
    print_array[11, 12:] = horiz_line

    st = ""
    for row in print_array:
        for element in row:
            st += element
        st += "\n"
    print(st)
