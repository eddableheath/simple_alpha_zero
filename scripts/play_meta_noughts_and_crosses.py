"""
    Script to play the meta noughts and crosses
"""

import numpy as np

from simple_alpha_zero.meta_noughts_and_crosses.meta_board_game import BigBoard
from simple_alpha_zero.meta_noughts_and_crosses.printers import big_game_printer


def check_if_space_available_and_valid(position, board_state, possible_moves) -> bool:
    """Check that the position of the space is available"""
    board_state = np.asarray(board_state)
    if board_state[position[0], position[1]] != " ":
        return False
    else:
        if (position[0] + 1, position[1] + 1) in possible_moves:
            return True
        else:
            return False


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
    print("To get the next possible moves input 'next moves'")
    print("------------------------------------------------")
    print("To print board again input 'print board'")
    print("lets play!")

    player = 0
    while not board.decided:
        # Get player input
        player_choice = input(f"Player {player + 1}s turn:   ")
        if player_choice == "next moves":
            next_moves = board.get_possible_moves()
            for move in next_moves:
                print(move)
            continue
        elif player_choice == "print board":
            big_game_printer(board.get_states())
            continue
        else:
            player_choice = eval(player_choice)
            player_choice = (int(player_choice[0]) - 1, int(player_choice[1]) - 1)
        while not check_if_space_available_and_valid(
            player_choice, board.get_states(), board.get_possible_moves()
        ):
            old_player_choice = player_choice
            player_choice = input("Position taken or invalid! Try again!:  ")
            if player_choice == "next moves":
                next_moves = board.get_possible_moves()
                for move in next_moves:
                    print(move)
                player_choice = old_player_choice
                continue
            elif player_choice == "print board":
                big_game_printer(board.get_states())
                player_choice = old_player_choice
                continue
            else:
                player_choice = eval(player_choice)
                player_choice = (int(player_choice[0]) - 1, int(player_choice[1]) - 1)
        board.update_board(player_choice, player)
        big_game_printer(board.get_states())
        print("------------------------------------------------")

        # Check if won
        if board.get_decided():
            print(f"Well done player {board.get_won_by() + 1}!")
            print("------------------------------------------------")
            big_game_printer(board.get_states())

        # Change player
        player = (player + 1) % 2


if __name__ == "__main__":
    main()
