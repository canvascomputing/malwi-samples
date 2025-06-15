import contextlib

import numpy as np
import numpy.typing as npt


# What this gives us:
#   - Detection of int overflow
# What this does not give us
#   - Detection of floats pushed into integer arrays
#   - Detection of floats too precise for the given dtype
@contextlib.contextmanager
def _numpy_strict_validation():
    user_err = np.geterr()
    user_promotion_state = np._get_promotion_state()  # noqa: SLF001
    try:
        # Additional validation for user-provided values
        np.seterr(over="raise", under="raise")
        # https://numpy.org/neps/nep-0050-scalar-promotion.html
        np._set_promotion_state("weak")  # noqa: SLF001

        yield None
    finally:
        np.seterr(**user_err)
        np._set_promotion_state(user_promotion_state)  # noqa: SLF001


def _make_immutable(array: npt.NDArray):
    array.setflags(write=False)


def _validate_and_normalize_numeric_array(
    value, numpy_dtype: np.dtype, n_dims: int
) -> npt.NDArray:
    if isinstance(value, np.ndarray):
        # We rely on NumPy to verify whether a cast can be safely performed,
        # e.g. int32 can be safely cast to int64, provided that the user
        # explicitly requires an int64 field while providing an int32 array.
        array = value.astype(dtype=numpy_dtype, casting="safe", copy=False)
    else:
        with _numpy_strict_validation():
            array = np.array(value, dtype=numpy_dtype)

    if array.ndim != n_dims:
        raise ValueError(f"Expected {n_dims}D value, got {array.ndim}D")

    _make_immutable(array)

    return array
