"""
    Script to play the meta noughts and crosses
"""

import numpy as np

from simple_alpha_zero.meta_noughts_and_crosses.base_player_class import SimPlayer
from simple_alpha_zero.meta_noughts_and_crosses.meta_board_game import BigBoard
from simple_alpha_zero.meta_noughts_and_crosses.printers import big_game_printer
from simple_alpha_zero.meta_noughts_and_crosses.random_player import RandomPlayer


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


def player_turn(board: BigBoard, player: int):
    """Player turn function

    Args:
        board: board object.
        player: which player is playing
    """
    # Get player input
    player_choice = input(f"Player {player + 1}s turn:   ")
    while player_choice == "print board" or player_choice == "next moves":
        if player_choice == "next moves":
            next_moves = board.get_possible_moves()
            for move in next_moves:
                print(move)
            player_choice = input(f"Player {player + 1}s turn:   ")
            continue
        elif player_choice == "print board":
            big_game_printer(board.get_states())
            player_choice = input(f"Player {player + 1}s turn:   ")
            continue
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
    return player_choice


def player_player_loop(board: BigBoard):
    """Human player vs human player game loop.

    Args:
        board: game board object
    """
    player = 0
    while not board.decided:
        # Get player input
        player_choice = player_turn(board, player)

        # Update and print board
        board.update_board(player_choice, player)
        big_game_printer(board.get_states())
        print("------------------------------------------------")

        # Check if won
        if board.get_decided():
            print(f"Well done player {board.get_won_by() + 1}!")
            print("------------------------------------------------")
            big_game_printer(board.get_states())
            break

        # Change player
        player = (player + 1) % 2


def sim_player_turn(board: BigBoard, sim_player: SimPlayer):
    """Simulated player

    Args:
        board: game board object
        sim_player: simulated player object
    """
    # Give player possible moves:
    next_moves = board.get_possible_moves()
    return sim_player.make_move(next_moves)


def player_sim_loop(board: BigBoard, sim_player: SimPlayer):
    """Human player sim player loop

    Args:
        board: game board object
        sim_player: simulated player object
    """
    print("Who is going first?")
    first_move_choice = input("For human type human, for sim type sim:  ")
    play_fns = [player_turn, simp]
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
            break

        # Change player
        player = (player + 1) % 2


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
    print("------------------------------------------------")
    opponent_choice = input(
        "To play against a random strategy opponent type random, or human type human: "
    )
    print("------------------------------------------------")
    print("lets play!")

    if opponent_choice == "human":
        print("------------------------------------------------")
        print("Your selection is a human player!")
        player_player_loop(board)


if __name__ == "__main__":
    main()
    main()
