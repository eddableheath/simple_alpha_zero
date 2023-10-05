"""
    Base classes for simulated players for meta noughts and crosses.
"""

from abc import ABC, abstractmethod

import numpy as np


class SimPlayer(ABC):

    """Base class for simulated player"""

    def __init__(self, seed=None) -> None:
        super().__init__()
        self.rng = np.random.default_rng(seed)

    @abstractmethod
    def make_move(self, next_moves):
        """Method for making a new move based on next available moves"""
        raise NotImplementedError
