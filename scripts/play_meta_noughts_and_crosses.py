"""
    Script to play the meta noughts and crosses
"""

from simple_alpha_zero.meta_noughts_and_crosses.meta_board_game import BigBoard
from simple_alpha_zero.meta_noughts_and_crosses.printers import big_game_printer


def main():
    """Main script for running a game of meta noughts and crosses"""
    board = BigBoard()

    print("Welcome to meta noughts and crosses, here is your board:")
    # states = board.get_states()
    # print(states)
    big_game_printer(board.get_states())

    print("------------------------------------------------")
    print("To play the first turn give the board position (small board, position)")
    print("------------------------------------------------")
    print("lets play!")

    # player = 0
    # while not board.decided:
    #     # Get player input
    #     player_choice = int(input(f"Player {player + 1}s turn:  ")) - 1
    #     while not check_if_space_available(player_choice, board.get_state()):
    #         player_choice = int(input("Position taken! Try again!:  ")) - 1
    #     board.update_state(player_choice, player)
    #     small_board_print(board.get_state())
    #     print("------------------------------------------------")

    #     # Check if won
    #     if board.get_decided():
    #         print(f"Well done player {board.get_won_by() + 1}!")
    #         print("------------------------------------------------")
    #         small_board_print(board.get_state())

    #     # Change player
    #     player = (player + 1) % 2


if __name__ == "__main__":
    main()
