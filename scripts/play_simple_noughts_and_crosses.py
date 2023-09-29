"""
    Script for playing a simple game of noughts and crosses.
"""

from simple_alpha_zero.meta_noughts_and_crosses.printers import small_board_print
from simple_alpha_zero.meta_noughts_and_crosses.small_board_game import SmallBoard


def check_if_space_available(position, board_state):
    """Check that the position of the space is available"""
    if board_state[position] != " ":
        return False
    else:
        return True


def main():
    """Main script for running a game of noughts and crosses"""
    board = SmallBoard()

    print("Welcome to noughts and crosses, here is your board:")
    small_board_print(board.get_state())

    print("------------------------------------------------")
    print("To play a turn give the board position from 1-9")
    print("------------------------------------------------")
    print("lets play!")

    player = 0
    while not board.decided:
        # Get player input
        player_choice = int(input(f"Player {player + 1}s turn:  ")) - 1
        while not check_if_space_available(player_choice, board.get_state()):
            player_choice = int(input("Position taken! Try again!:  ")) - 1
        board.update_state(player_choice, player)
        small_board_print(board.get_state())
        print("------------------------------------------------")

        # Check if won
        if board.get_decided():
            print(f"Well done player {board.get_won_by() + 1}!")
            print("------------------------------------------------")
            small_board_print(board.get_state())

        # Change player
        player = (player + 1) % 2


if __name__ == "__main__":
    main()
