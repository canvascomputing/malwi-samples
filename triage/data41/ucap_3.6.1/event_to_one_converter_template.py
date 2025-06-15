#
# Copyright (c) @YEAR@ European Organisation for Nuclear Research (CERN), All Rights Reserved.
#
import logging
from typing import Optional

from ucap.common import (
    AcquiredParameterValue,
    Event,
    FailSafeParameterValue,
    ValueHeader,
    ValueType,
)
from ucap.common.context import (
    device_name,
    published_parameter_name,
    transformation_name,
)


def convert(event: Event) -> Optional[FailSafeParameterValue]:
    """
    My event to one converter.
    """
    logger = logging.getLogger(__name__)
    logger.info("template test for %s/%s", device_name, transformation_name)

    header = (
        event.trigger_value.header if event.trigger_value else ValueHeader()
    )

    # Publishing results
    apv = AcquiredParameterValue(published_parameter_name, header)
    apv.update_value("doubleField", 20.0)
    apv.update_value("intField", 1908)
    apv.update_value("longField", 1908, ValueType.LONG)

    # return None to not publish this time
    return FailSafeParameterValue(apv)
