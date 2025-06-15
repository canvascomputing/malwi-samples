import math

import numpy as np

from ucap.common import DiscreteFunction, DiscreteFunctionList, ValueType

simple_arguments = [
    (True, ValueType.BOOLEAN),
    (np.array(20, dtype=np.byte), ValueType.BYTE),
    (np.array(20, dtype=np.int16), ValueType.SHORT),
    (np.array(20, dtype=np.intc), ValueType.INT),
    (20, ValueType.LONG),
    (np.array(20, dtype=np.float32), ValueType.FLOAT),
    (20.2, ValueType.DOUBLE),
    (DiscreteFunction((1, 2, 3), [4, 6, 7]), ValueType.DISCRETE_FUNCTION),
    (
        DiscreteFunctionList([DiscreteFunction((1, 2, 3), [4, 6, 7])]),
        ValueType.DISCRETE_FUNCTION_LIST,
    ),
]

numeric_array_arguments = [
    # 1D
    (np.arange(16) > 2, ValueType.BOOLEAN_ARRAY),
    (np.arange(16, dtype=np.byte), ValueType.BYTE_ARRAY),
    (np.arange(16, dtype=np.int16), ValueType.SHORT_ARRAY),
    (np.arange(16, dtype=np.intc), ValueType.INT_ARRAY),
    (np.arange(16, dtype=int), ValueType.LONG_ARRAY),
    (np.linspace(0, 1, num=16, dtype=np.single), ValueType.FLOAT_ARRAY),
    (np.linspace(0, 1, num=16, dtype=np.double), ValueType.DOUBLE_ARRAY),
    # 2D
    (np.arange(16).reshape(2, -1) > 2, ValueType.BOOLEAN_ARRAY_2D),
    (np.arange(16, dtype=np.byte).reshape(2, -1), ValueType.BYTE_ARRAY_2D),
    (np.arange(16, dtype=np.int16).reshape(2, -1), ValueType.SHORT_ARRAY_2D),
    (np.arange(16, dtype=np.intc).reshape(2, -1), ValueType.INT_ARRAY_2D),
    (np.arange(16, dtype=int).reshape(2, -1), ValueType.LONG_ARRAY_2D),
    (
        np.linspace(0, 1, num=16, dtype=np.single).reshape(2, -1),
        ValueType.FLOAT_ARRAY_2D,
    ),
    (
        np.linspace(0, 1, num=16, dtype=np.double).reshape(2, -1),
        ValueType.DOUBLE_ARRAY_2D,
    ),
]

nan_values = (np.nan, math.nan)
inf_values = (np.inf, -np.inf, math.inf, float("inf"), float("-inf"))
