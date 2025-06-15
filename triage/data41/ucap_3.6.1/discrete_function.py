from __future__ import annotations

from typing import Sequence

import numpy as np
import numpy.typing as npt

from .internal.numeric_array_validation import (
    _validate_and_normalize_numeric_array,
)


class DiscreteFunction:
    """
    Defines a discrete function. A discrete function is a list of points strictly ordered by their x-coordinates.

    A discrete function can support gap. A gap is an undefined part in the discrete function with no value.
    A gap is created by having an y value equals to `math.nan`. For instance, if p1(x1, y1), p2(x2, math.nan)
    and p3(x3, y3) are 3 successive points, the part between x1 and x3 is undefined

    Attributes
        x : tuple[float]
                X coordinates
        y : tuple[float]
                Y coordinates

    """

    def __init__(
        self,
        x: Sequence[float] | npt.NDArray[np.float64],
        y: Sequence[float] | npt.NDArray[np.float64],
    ):
        if len(x) != len(y):
            raise ValueError("X array length does not match Y array")

        self._x = _validate_and_normalize_numeric_array(
            x, np.dtype(np.float64), 1
        )
        self._y = _validate_and_normalize_numeric_array(
            y, np.dtype(np.float64), 1
        )

    @property
    def x(self) -> npt.NDArray[np.float64]:
        return self._x

    @property
    def y(self) -> npt.NDArray[np.float64]:
        return self._y

    def __getitem__(self, key: int) -> tuple[float, float]:
        """
        Returns an x-y pair specified with its index.

        Parameters
        ----------
        key : int
            the index of the x-y pair

        Returns
        -------
        tuple[float]
            an x-y pair corresponding to the index

        """
        return self.x[key], self.y[key]

    def __len__(self) -> int:
        """
        Returns the number of points that defines this function

        Returns
        -------
        int
            the number of points that defines this function

        """
        return len(self.x)

    def __eq__(self, other):
        if not isinstance(other, DiscreteFunction):
            return False
        return np.array_equal(
            self.x, other.x, equal_nan=True
        ) and np.array_equal(self.y, other.y, equal_nan=True)

    def __repr__(self):
        return f"DiscreteFunction(x={self.x}, y={self.y})"
