# Type Alias
# A type alias gives a shorter or more meaningful name to a complex type.
# When a type hint is long or repeated often, an alias makes code cleaner and easier to read.

from typing import Dict, Union

# We use the 'type' statement for type aliases:
type ConfigType = Dict[str, Union[str, int, bool, None]]
# This declares an alias named ConfigType.


def load_config() -> ConfigType:
    return {
        "debug": True,
        "version": 2,
        "path": None,
    }


# Alternatively,
ConfigTypeV2 = Dict[str, Union[str, int, bool, None]]


def load_config_v2() -> ConfigTypeV2:
    return {
        "debug": True,
        "version": 2,
        "path": None,
    }
