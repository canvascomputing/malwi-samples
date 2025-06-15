#
# Copyright (c) @YEAR@ European Organisation for Nuclear Research (CERN), All Rights Reserved.
#
import logging
from typing import List

from ucap.common import (
    AcquiredParameterValue,
    Event,
    FailSafeParameterValue,
    ValueHeader,
    ValueType,
)
from ucap.common.context import device_name, transformation_name


def convert(event: Event) -> List[FailSafeParameterValue]:
    """
    My event to many converter.
    """
    logger = logging.getLogger(__name__)
    logger.info("template test for %s/%s", device_name, transformation_name)

    header = (
        event.trigger_value.header if event.trigger_value else ValueHeader()
    )

    # Publishing results
    apv = AcquiredParameterValue(f"{device_name}/Acquisition", header)
    apv.update_value("doubleField", 20.0)
    apv.update_value("intField", 1908)

    apv2 = AcquiredParameterValue(f"{device_name}/LongTest", header)
    apv2.update_value("longField", 1908, ValueType.LONG)

    fspv = FailSafeParameterValue(apv)
    fspv2 = FailSafeParameterValue(apv2)

    # return [] to not publish this time
    return [fspv, fspv2]
