# JSON (JavaScript Object Notation) is a lightweight, text‑based format for representing structured data.
# It maps naturally to Python built‑ins (dict, list, str, int, etc.), making it ideal for API payloads.
# JSON structure:
# - Object:    {"key": value, ...}      # Like a Python dict
# - Array:     [value, ...]             # Like a Python list
# - Primitives: "text", 123, 3.14, true, false, null

import json

data = {"user": "alice", "active": True, "scores": [42, 73, 58]}


"""
json.dumps(
    obj,
    *,
    skipkeys: bool = False,
    ensure_ascii: bool = True,
    check_circular: bool = True,
    allow_nan: bool = True,
    cls: Optional[Type[JSONEncoder]] = None,
    indent: Optional[int] = None,
    separators: Optional[Tuple[str, str]] = None,
    default: Optional[Callable[[Any], Any]] = None,
    sort_keys: bool = False,
    **kw,
) -> str
"""

# Serialize Python object to a JSON-formatted str
# - indent:   Pretty-print with specified number of spaces
# - sort_keys: Sort dictionary keys in output (default: False)
# - separators: Tuple specifying item and key separators (default: (', ', ': '))
#   For example, separators=(',', ': ') removes spaces after commas, keeps one after colon
# - ensure_ascii: Escape non-ASCII chars if True (default: True)
# - default:  Function to handle non-serializable objects


json_str = json.dumps(data)
print(json_str)  # {"user": "alice", "active": true, "scores": [42, 73, 58]}

# Pretty-print with indentation for readability
json_pretty = json.dumps(data, indent=2)
print(json_pretty)
"""
{
    "user": "alice",
    "active": true,
    "scores": [
        42,
        73,
        58
    ]
}
"""


# sort keys and use custom separators
json_sorted = json.dumps(data, sort_keys=True, separators=(",", ": "))
print(json_sorted)  # {"active": true,"scores": [42,73,58],"user": "alice"}

# allow non-ASCII characters in output
data_unicode = {"name": "André", "city": "München"}
json_unicode = json.dumps(data_unicode, ensure_ascii=False)
print(json_unicode)  # {"name": "André", "city": "München"}


