# Type Alias
# A type alias gives a shorter or more meaningful name to a complex type.
# When a type hint is long or repeated often, an alias makes code cleaner and easier to read.
# Without alias:
# ConfigType = Dict[str, Union[str, int, bool, None]]

from typing import TypeAlias, Dict, Union

# Without alias:
# ConfigType = Dict[str, Union[str, int, bool, None]]
# Simple assignment (ConfigType) is just a variable pointing to a type;
# static analyzers may or may not recognize it as an alias.

ConfigType: TypeAlias = Dict[str, Union[str, int, bool, None]]
# It declares an alias named ConfigType.


def load_config() -> ConfigType:
    return {
        "debug": True,
        "version": 2,
        "path": None,
    }
