# Package: A package is a folder containing an __init__.py file (can be empty)
# and one or more modules.

"""
my_package/
    __init__.py
    math_utils.py
    string_utils.py
"""


"""
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
"""



# Library: A library is a collection of modules and/or packages that provide useful tools.
# It’s a general term—a library can be a single module, a package, or a group of packages.

# The requests library is a single module.
# The numpy library is a package with many modules.