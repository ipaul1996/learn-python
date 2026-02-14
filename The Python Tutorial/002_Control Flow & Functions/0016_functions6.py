# Arguments may be passed to a Python function either by position or explicitly by keyword.
# For readability and performance, it makes sense to restrict the way arguments can be passed
# so that a developer need only look at the function definition to determine if items are
# passed by position, by position or keyword, or by keyword.

"""
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |                 |             |
        |        Positional or keyword  |
        |                               |
    Positional only                Keyword only
"""
# Here, / and * are optional. If used, these symbols indicate the kind of parameter by
# how the arguments may be passed to the function: positional-only, positional-or-keyword,
# and keyword-only. Keyword parameters are also referred to as named parameters.
# If / and * are not present in the function definition, arguments may be passed
# to a function by position or by keyword.
# Positional-only parameters are placed before a / (forward-slash). The / is used to
# logically separate the positional-only parameters from the rest of the parameters.
# If there is no / in the function definition, there are no positional-only parameters.
# Parameters following the / may be positional-or-keyword or keyword-only.
# To mark parameters as keyword-only, we place an * in the arguments list just before
# the first keyword-only parameter.


def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):
    print(arg)


def kwd_only_arg(*, arg):
    print(arg)


def combined_example(pos_only, /, pos_or_kwd, *, kwd_only):
    print(pos_only, pos_or_kwd, kwd_only)


# ******************************************************
# This function demonstrates a potential collision between a positional argument 'name'
# and a keyword argument 'name' passed via **kwds. If 'name' is passed as a keyword,
# it will override the positional argument, which can lead to confusion.
def foo(name, **kwds):
    # Checks if 'name' is present in the keyword arguments
    return "name" in kwds


# The following call would raise a TypeError because 'name' is given both positionally and as a keyword:
# foo(1, name=2)  # Parameter "name" is already assigned
# foo(1, **{'name': 2}) # Parameter "name" is already assigned


# To avoid this ambiguity, we can make 'name' a positional-only parameter using the '/' syntax.
def fooV2(name, /, **kwds):
    # Now, 'name' must be passed positionally, and any 'name' in **kwds is a separate entry.
    return "name" in kwds


# Here, 'name' is passed as a keyword argument, so 'name' is present in kwds and returns True.
print(fooV2(1, name=2))  # Output: True

# Here, 'name' is passed via dictionary unpacking, so again 'name' is present in kwds and returns True.
print(fooV2(1, **{"name": 2}))  # Output: True
