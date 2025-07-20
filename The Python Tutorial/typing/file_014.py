from typing import Sequence

# In Python's typing module, Sequence is a generic type that represents
# an immutable ordered collection of items i.e., a Sequence[T] is an ordered,
# indexed, read‑only collection of items of type T. It can be a list, tuple, str.


def first_item(items: Sequence[int]) -> int:
    return items[0]


def first_item_v2(items: Sequence) -> int:
    return items[0]


first_item_v2("Hello")

# Things that we can do with a Sequence
# seq[i]
# seq[start:stop]
# seq[start:stop:step]
# seq[::-1] (Reverse Copy)
# len(seq)
# for item in seq
# iter(seq)
# x in seq / x not in seq
# seq.count(x)
# seq.index(x[, start[, stop]])
# list(seq), tuple(seq), set(seq)
# sorted(seq) (returns a new list)
# min(seq), max(seq), sum(seq)
# any(seq) -> stops and returns True as soon as it finds a truthy element; otherwise False.
# all(seq) -> stops and returns False as soon as it finds a falsy element; otherwise True.
# zip(seq1, seq2, …)
# filter(f, seq), map(f, seq)
# seq1 + seq2
# seq * n