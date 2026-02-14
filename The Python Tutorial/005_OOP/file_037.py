# Use Case - 2:
# Class Configuration: Modifying or inspecting class-wide settings.


class Config:
    _debug = False

    @classmethod
    def enable_debug(cls):
        cls._debug = True

    @classmethod
    def disable_debug(cls):
        cls._debug = False

    @classmethod
    def toggle_debug(cls):
        cls._debug = not cls._debug

    @classmethod
    def is_debug(cls):
        """Return True if debug mode is enabled, else False."""
        return cls._debug

    @classmethod
    def set_debug(cls, value: bool):
        """Set debug mode to the given boolean value."""
        cls._debug = bool(value)
