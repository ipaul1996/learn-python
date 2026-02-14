# Iterator

# In Python's typing module, Iterator is a generic type that represents
# an object that produces items one at a time and remembers its state as it iterates.
# Iterator[T] yields items of type T and supports the next() operation.
# All iterators are also iterables, but not all iterables are iterators.

from typing import Iterator


def consume_iterator(it: Iterator[int]) -> None:
    try:
        while True:
            item = next(it)
            print(item)
    except StopIteration:
        pass


my_iter: Iterator[int] = iter([1, 2, 3])
consume_iterator(my_iter)

# Things you can do with an Iterator:
# next(it)                      # get next item, raises StopIteration when done
# for item in it                # iterate items (until exhausted)
# iter(it)                      # returns itself
# list(it), tuple(it), set(it)  # convert to list, tuple, set (consumes iterator)
# any(it), all(it)              # test truthiness
# sorted(it)                    # sorted items (returns a list, consumes iterator)
# min(it), max(it)              # min/max item
# sum(it)                       # sum items
# zip(it1, it2, ...)            # zip multiple iterators
# filter(f, it), map(f, it)     # functional ops on items

# Note: Iterators are single-use and get exhausted after iteration.
# For reusable collections, use Iterable
