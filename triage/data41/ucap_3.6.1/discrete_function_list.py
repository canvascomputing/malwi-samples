from dataclasses import dataclass
from typing import Sequence

from .discrete_function import DiscreteFunction


@dataclass(frozen=True)
class DiscreteFunctionList:
    """
    List of discrete functions.

    All the DiscreteFunctions within a DiscreteFunctionList must be continuous with each other.
    i.e. the last y-coordinate of preceding DiscreteFunction must be equal to the first y-coordinate of the
    following function.

    Attributes
        functions : Tuple
                tuple with DiscreteFunction instances

    """

    functions: Sequence[DiscreteFunction]

    def __post_init__(self):
        super().__setattr__("functions", tuple(self.functions))

    def __getitem__(self, key: int) -> DiscreteFunction:
        """
        Returns a function specified with its index.

        Parameters
        ----------
        key : int
            the index of the function

        Returns
        -------
        DiscreteFunction
            a function corresponding to the index

        """
        return self.functions[key]

    def __len__(self) -> int:
        """
        Returns the number of functions in the list.

        Returns
        -------
        int
            the number of functions in the list.

        """
        return len(self.functions)
