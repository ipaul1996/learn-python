from collections import defaultdict

# Count occurrences without Counter
counts = defaultdict(int)  # default_factory

for fruit in ["apple", "banana", "apple", "kiwi", "banana"]:
    counts[fruit] += 1  # missing keys start at 0


print(counts)
# defaultdict(<class 'int'>, {'apple': 2, 'banana': 2, 'kiwi': 1})