#
# Copyright (c) @YEAR@ European Organisation for Nuclear Research (CERN), All Rights Reserved.
#
import logging
from typing import Optional

from ucap.common import (
    AcquiredParameterValue,
    FailSafeParameterValue,
    ValueType,
)
from ucap.common.context import (
    device_name,
    published_parameter_name,
    transformation_name,
)


def convert(
    input_data: FailSafeParameterValue
) -> Optional[FailSafeParameterValue]:
    """
    My one to one converter.
    """
    logger = logging.getLogger(__name__)
    logger.info("template test for %s/%s", device_name, transformation_name)

    # Publishing results
    apv = AcquiredParameterValue(published_parameter_name, input_data.header)
    apv.update_value("doubleField", 20.0)
    apv.update_value("intField", 1908)
    apv.update_value("longField", 1908, ValueType.LONG)

    # return None to not publish this time
    return FailSafeParameterValue(apv)
