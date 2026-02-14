from typing import MutableSequence


# In Python's typing module, MutableSequence is a generic type that represents
# a mutable ordered collection of items i.e., a MutableSequence[T] is an ordered,
# indexed, read‑write collection of items of type T. It can be a list or other user-defined
def add_and_reverse(items: MutableSequence[int], value: int) -> None:
    items.append(value)
    items.reverse()


my_list: MutableSequence[int] = [1, 2, 3]
add_and_reverse(my_list, 4)
print(my_list)

# Things that we can do with a MutableSequence
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
# any(seq)
# all(seq)
# zip(seq1, seq2, …)
# filter(f, seq), map(f, seq)
# seq1 + seq2
# seq * n
# seq[i] = value           # item assignment
# del seq[i]               # item deletion
# seq.append(value)        # add item at end
# seq.extend(iterable)     # add multiple items
# seq.insert(index, value) # insert item
# seq.remove(value)        # remove first occurrence
# seq.pop([index])         # remove and return item
# seq.clear()              # remove all items
# seq.reverse()            # reverse items
