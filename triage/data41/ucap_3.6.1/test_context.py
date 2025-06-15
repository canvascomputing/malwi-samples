from ucap.common.context import (
    configuration,
    device_name,
    published_parameter_name,
    published_parameter_names,
    published_property_name,
    published_property_names,
    transformation_name,
)

# This test checks what a converter under test would experience. For running transformations the context
# completely is managed by the Python server.


def test_default_context():
    assert device_name == "TEST_DEVICE"
    assert transformation_name == "TEST_TRANSFORMATION"
    assert published_property_name == "TestProperty"
    assert ["TestProperty", "TestProperty2"] == published_property_names
    assert published_parameter_name == "TEST_DEVICE/TestProperty"
    assert [
        "TEST_DEVICE/TestProperty",
        "TEST_DEVICE/TestProperty2",
    ] == published_parameter_names
    assert {} == configuration
