"""
    Random player class.
"""

from simple_alpha_zero.meta_noughts_and_crosses.base_player_class import SimPlayer


class RandomPlayer(SimPlayer):

    """A random player"""

    def __init__(self, seed=None) -> None:
        super().__init__(seed=None)

    def make_move(self, next_moves):
        return self.rng.choice(next_moves)
