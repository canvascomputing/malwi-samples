#
# Copyright (c) @YEAR@ European Organisation for Nuclear Research (CERN), All Rights Reserved.
#

from __future__ import annotations

import logging

from ucap.common import (
    AcquiredParameterValue,
    FailSafeParameterValue,
    ValueType,
)
from ucap.common.context import device_name, transformation_name


def convert(input_data: FailSafeParameterValue) -> list[FailSafeParameterValue]:
    """
    My one to many converter.
    """
    logger = logging.getLogger(__name__)
    logger.info("template test for %s/%s", device_name, transformation_name)

    # Publishing results
    apv = AcquiredParameterValue(
        f"{device_name}/Acquisition", input_data.header
    )
    apv.update_value("doubleField", 20.0)
    apv.update_value("intField", 1908)

    apv2 = AcquiredParameterValue(f"{device_name}/LongTest", input_data.header)
    apv2.update_value("longField", 1908, ValueType.LONG)

    fspv = FailSafeParameterValue(apv)
    fspv2 = FailSafeParameterValue(apv2)

    # return [] to not publish this time
    return [fspv, fspv2]
