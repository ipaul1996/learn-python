# Problem Set: Data Structures

Practice problems based on concepts covered in `003_Data Strcutures`.

You've covered fundamentals and control flow. Those still show up here, but the real work is **choosing and combining the right data structures**.

For each problem, pick what fits. We won't tell you which structure to use.

---

# Problem: Server Log Parser

## Scenario

A backend service writes one log entry per line. Each line is a single string in this format:

```text
TIMESTAMP|LEVEL|MESSAGE
```

Example line:

```text
2024-03-15T10:00:01|ERROR|Disk full
```

The ops team needs these lines turned into structured records before they can filter or count them.

## Requirements

Write a function that accepts a list of log lines (strings) and returns a list of records.

Each **valid** line becomes a record with three parts:

- `timestamp` — text before the first `|`
- `level` — text between the first and second `|`
- `message` — everything after the second `|`

**Invalid lines** (skip them, do not stop processing):

- Empty lines or lines with only whitespace
- Lines that do not contain exactly two `|` separators (so three parts total)

Invalid lines should be collected separately, in input order, as `(original_line, reason)`.

## Constraints

- Up to 5,000 lines per batch
- Do not change the original list of lines
- `MESSAGE` may itself contain `|` characters — only the first two pipes split the line

## Expected Behavior

**Input:**

```text
[
  "2024-03-15T10:00:01|ERROR|Disk full",
  "2024-03-15T10:00:02|WARN|Retry|later",
  "   ",
  "bad-line-no-pipes"
]
```

**Valid records:**

```text
[
  ("2024-03-15T10:00:01", "ERROR", "Disk full"),
  ("2024-03-15T10:00:02", "WARN", "Retry|later"),
]
```

**Invalid (in order):**

```text
[
  ("   ", "empty or whitespace"),
  ("bad-line-no-pipes", "wrong number of fields"),
]
```

(Your reason strings may differ, but should be short and clear.)

## Deliverables

- A parser function plus a small demo with at least 5 lines (including invalid ones)
- Split parsing, validation, and batch processing into clear steps

## Decisions You Must Make

- How do you split each line without breaking messages that contain extra separators?
- What do you return — two lists, a grouped object, or something else?
- Where do you trim whitespace, and where do you leave text untouched?

## Questions to Think About

- If you split on every `|`, what happens to the third field in the second valid line?
- Is a record best kept as a grouped value that cannot be changed later, or as a mutable collection?

## Difficulty

Beginner

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Unique Visitors, In Order

## Scenario

An analytics pipeline receives visitor IDs in the order each visit happened. Marketing wants:

1. The list of **unique** visitor IDs
2. In the order each ID **first appeared** in the input

They also want to know how many total visits were duplicates (visits where that ID had already been seen earlier in the batch).

## Requirements

Given a list of visitor ID strings:

- Return the unique IDs in **first-seen order**
- Return the duplicate visit count (how many positions in the input were a repeat of an ID already seen)

## Constraints

- Up to 100,000 visitor IDs per batch
- IDs are case-sensitive (`"User1"` and `"user1"` are different)
- Do not modify the input list
- Lookup while scanning should stay efficient at large batch sizes

## Expected Behavior

**Input:**

```text
["u1", "u2", "u1", "u3", "u2", "u1"]
```

**Output:**

```text
unique_in_order = ["u1", "u2", "u3"]
duplicate_visit_count = 3
```

Explanation of duplicate count:

| Index | ID | Already seen? | Counts as duplicate? |
|-------|----|---------------|----------------------|
| 0 | u1 | No | No |
| 1 | u2 | No | No |
| 2 | u1 | Yes | Yes |
| 3 | u3 | No | No |
| 4 | u2 | Yes | Yes |
| 5 | u1 | Yes | Yes |

## Deliverables

- One function implementing the above
- A short note explaining why your approach keeps first-seen order

## Decisions You Must Make

- What structure gives fast "have I seen this before?" checks?
- Does that same structure preserve first-seen order automatically?
- If not, what else do you need to maintain?

## Questions to Think About

- If you removed duplicates by converting the whole input to a structure that only keeps unique values, would the order always be correct?
- Can you compute both results in one pass?

## Difficulty

Beginner

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Warehouse Stock Counter

## Scenario

A warehouse records every stock movement as a string:

```text
"<SKU>|<signed_quantity>"
```

Examples:

- `"A100|5"` — received 5 units of SKU `A100`
- `"A100|-2"` — shipped 2 units of SKU `A100`

At the end of the day, you receive a list of these movement strings and must compute the **current quantity per SKU**.

## Requirements

- Parse each movement string
- Skip invalid rows (wrong format, empty SKU, quantity that is not a whole number)
- Combine all valid movements per SKU into a running total
- Return a mapping from SKU → final quantity (only SKUs that appear in valid rows)
- Also return how many rows were skipped

## Constraints

- Up to 50,000 movement rows
- SKU is a non-empty string after stripping spaces
- Final quantities may be zero or negative (oversold) — do not clamp them
- Input list must not be modified

## Expected Behavior

**Input:**

```text
["A100|5", "B200|10", "A100|-2", "A100|1", "bad-row", "C300|abc"]
```

**Totals:**

```text
A100 → 4   (5 - 2 + 1)
B200 → 10
```

**Skipped:** 2 rows (`"bad-row"`, `"C300|abc"`)

## Deliverables

- Parsing, validation, and aggregation in readable separate pieces
- Demo with the example above

## Decisions You Must Make

- What structure maps each SKU to its running total?
- How is that different from keeping a list of every movement and scanning it repeatedly?
- Where do you parse the string — and how do you split reliably?

## Questions to Think About

- If you stored movements in a list grouped by SKU, how many scans would a report need?
- When two movements affect the same SKU, how do you update without losing the previous total?

## Difficulty

Beginner

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Print Job Queue

## Scenario

A small print server receives jobs one at a time and processes them in **first-in, first-out** order: the oldest submitted job prints first.

Jobs are identified by strings like `"report_Q1.pdf"`, `"invoice_882.pdf"`.

The system must support:

- `submit(job_id)` — add a job to the waiting line
- `process_next()` — remove and return the next job to print; if nothing is waiting, return a clear signal (your choice: `None`, empty string, or raise an error — document it)
- `pending_count()` — how many jobs are waiting

## Requirements

Implement the print server with the three operations above.

## Constraints

- Up to 10,000 jobs may be submitted over a session
- Jobs must leave in the exact order they arrived
- `process_next()` may be called when the queue is empty — handle it consistently
- Performance matters: jobs are added at the **back** and removed from the **front** on every cycle

## Expected Behavior

```text
submit("A")
submit("B")
submit("C")
pending_count()     → 3
process_next()      → "A"
process_next()      → "B"
pending_count()     → 1
process_next()      → "C"
process_next()      → (your documented empty behavior)
pending_count()     → 0
```

## Deliverables

- The print server (as a simple class or as functions with shared state — your choice, but justify it)
- A demo script running the scenario above

## Decisions You Must Make

- What structure represents the waiting line?
- Is the structure you use for "add to back, remove from front" equally efficient at both ends?
- What happens if you use a structure optimized for only one end?

## Questions to Think About

- If you always removed from position 0 of a linear collection, what happens to the remaining items?
- Is there a structure designed for fast operations at both ends?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Text Editor Undo History

## Scenario

A simple text editor stores a history of document states. Every time the user makes an edit, the new state is saved. The user can **undo** repeatedly to go back to earlier states.

Behavior:

- `save(state)` — user made an edit; push the new document state
- `undo()` — move one step backward and return the state you are now viewing
- If there is nothing to undo, return a clear signal (document your choice)

States are strings (the full document text).

## Requirements

Implement the history with `save` and `undo` as described.

## Constraints

- Up to 1,000 undo steps in a session
- The most recently saved state is the current document
- `undo` always moves exactly one step backward
- States are immutable strings — you are storing references, not modifying old states in place

## Expected Behavior

```text
save("Hello")
save("Hello world")
save("Hello world!")
undo()   → "Hello world"
undo()   → "Hello"
undo()   → (your documented empty behavior)
```

## Deliverables

- Implementation plus demo matching the example
- One sentence on why your structure matches "last in, first out"

## Decisions You Must Make

- What structure naturally supports "most recent first" retrieval?
- After the user undos one or more times and then saves a new state, should the old "future" states be discarded? Pick one behavior, document it, and use it consistently in your demo.

## Questions to Think About

- How is this different from the print queue problem, even though both add and remove items?
- Would inserting at the front of a linear collection on every save be a good idea?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Skill Overlap Report

## Scenario

A learning platform tracks which skills each user has completed. Product wants a comparison report between two users.

Each user's skills arrive as a list of skill name strings. The same skill may appear more than once in the input — treat that as one skill.

## Requirements

Given two users' skill lists (`user_a`, `user_b`), produce:

| Report field | Meaning |
|--------------|---------|
| `only_a` | Skills that A has but B does not |
| `only_b` | Skills that B has but A does not |
| `both` | Skills that both have |
| `all_unique` | Every distinct skill from either user |

Return each field as something the caller can loop over. Order doesn't matter unless you sort for readability (say so if you do).

## Constraints

- Each user may have up to 500 skill entries (with duplicates)
- Skill names are case-sensitive
- Do not modify the input lists
- Don't use nested loops that compare every skill of A against every skill of B

## Expected Behavior

**Input:**

```text
user_a = ["Python", "SQL", "Git", "Python"]
user_b = ["SQL", "Docker", "Git", "Git"]
```

**Output (contents; order may vary):**

```text
only_a    = {"Python"}
only_b    = {"Docker"}
both      = {"SQL", "Git"}
all_unique = {"Python", "SQL", "Git", "Docker"}
```

## Deliverables

- One function returning the four parts of the report
- Demo with the example above plus one case where one user has an empty skill list

## Decisions You Must Make

- How do you remove duplicates from each user's input before comparing?
- What operations express "in A but not in B" without manual pairwise comparison?
- Do you need four separate structures, or can some be derived from others?

## Questions to Think About

- If you kept skills as plain lists and used membership checks, what is the cost when lists grow?
- Are there operations that combine two collections in one step?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Seat Assignment Lookup

## Scenario

An airline assigns passengers to seats. Each seat is identified by a **row number** (integer) and a **seat letter** (single uppercase letter `A`–`F`).

The system must:

- Record an assignment: row + letter → passenger name
- Look up who sits at a given row and letter
- List all passengers on a given row
- Report whether a specific seat is already taken

## Requirements

Design storage and functions for:

- `assign(row, letter, passenger_name)` — book a seat
- `lookup(row, letter)` — return passenger name, or a clear "not found" signal
- `passengers_on_row(row)` — return all passenger names on that row (any order is fine)
- `is_taken(row, letter)` — return `True` or `False`

If `assign` is called for a seat that is already taken, do not overwrite silently — return a failure indicator or raise an error (your choice; document it).

## Constraints

- Up to 300 seats on a flight
- Row numbers are positive integers; letters are single characters
- Passenger names are strings
- Lookups by row+letter should be direct, not a full scan of every assignment on each call

## Expected Behavior

```text
assign(12, "A", "Priya")
assign(12, "B", "James")
assign(14, "C", "Lee")

lookup(12, "A")           → "Priya"
is_taken(12, "B")         → True
is_taken(12, "C")         → False
passengers_on_row(12)     → ["Priya", "James"]  (order may vary)

assign(12, "A", "Someone") → failure (seat already taken)
```

## Deliverables

- Storage design plus the four operations
- Demo covering successful assign, lookup, row listing, and double-booking

## Decisions You Must Make

- How do you represent a seat as a single lookup key?
- Can every part of that key be used safely for fast lookup?
- How do you find all passengers on one row without scanning unrelated rows?

## Questions to Think About

- If you used a mutable collection as part of a lookup key, what would happen?
- Is one big flat lookup enough, or do you need a second structure for "all seats on row X"?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Application Settings Merge

## Scenario

A desktop app stores user settings as nested groups. On startup, it loads **default settings** and then applies a **user patch** that overrides some values.

Defaults:

```text
{
  "theme": "light",
  "editor": {
    "font_size": 14,
    "tab_width": 4
  },
  "notifications": True
}
```

User patch:

```text
{
  "theme": "dark",
  "editor": {
    "font_size": 16
  }
}
```

Expected result after merge:

```text
{
  "theme": "dark",
  "editor": {
    "font_size": 16,
    "tab_width": 4
  },
  "notifications": True
}
```

Only `font_size` inside `editor` changes; `tab_width` stays from defaults.

## Requirements

- Write `merge_settings(defaults, patch)` that returns a **new** merged settings object
- Top-level keys from `patch` override top-level keys in `defaults`
- For nested groups (values that are themselves mappings), merge **one level deep** the same way — patch keys override, unmentioned keys stay from defaults
- Neither `defaults` nor `patch` may be modified by your function

## Constraints

- Nesting is at most two levels (group → key → value); values are strings, numbers, or booleans
- After merging, changing the returned result must not change `defaults` or `patch`
- Up to 50 top-level keys

## Expected Behavior

Use the defaults and patch above. After `merge_settings`:

- `result["theme"]` → `"dark"`
- `result["editor"]["font_size"]` → `16`
- `result["editor"]["tab_width"]` → `4`
- `result["notifications"]` → `True`
- `defaults["theme"]` → still `"light"` (unchanged)

## Deliverables

- `merge_settings` with demo
- A test case where you mutate `result["editor"]` after merging and show that `defaults["editor"]` is unaffected — or explain why your test fails if you did not copy deeply enough

## Decisions You Must Make

- How do you combine two mappings without changing the originals?
- When a nested group appears in the patch, do you replace the whole group or merge inside it?
- Is a shallow duplicate of the top level enough?

## Questions to Think About

- If you copied only the outer mapping and then changed a nested mapping inside the copy, who else sees that change?
- What is the difference between updating in place and building a new merged result?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Word Frequency Leaderboard

## Scenario

A content team pastes article text and wants to know which words appear most often. Words should be compared case-insensitively (`"The"` and `"the"` count together).

## Requirements

Given a string of article text:

1. Split it into words (words are separated by whitespace)
2. Strip punctuation attached to the ends of words: `"hello,"` → `"hello"`, `"don't"` → `"don't"` (keep internal apostrophes)
3. Ignore empty tokens after cleaning
4. Count how many times each word appears
5. Return a ranking: list of `(word, count)` pairs sorted by count **highest first**; when counts tie, sort words **alphabetically** (case-insensitive)

## Constraints

- Articles up to 50,000 words
- Do not modify the input string
- Punctuation to strip from ends: `.,!?;:"` (only at start or end of each token)
- The ranking must not change the original word casing in the output — use the form that appeared most often, or the first seen form (document your choice)

## Expected Behavior

**Input:**

```text
"Hello hello world! Hello, world."
```

**After cleaning tokens:**

```text
["Hello", "hello", "world", "Hello", "world"]
```

**Counts (case-insensitive key):**

```text
hello → 3
world → 2
```

**Ranking:**

```text
[("Hello", 3), ("world", 2)]
```

(If you always keep first-seen casing, `"Hello"` is fine for the hello group.)

## Deliverables

- End-to-end function from raw text to ranking
- Demo with the example plus a short paragraph with at least three punctuation edge cases you handled

## Decisions You Must Make

- How do you normalize for counting vs how you display words?
- What structure holds the counts?
- How do you produce a sorted ranking without destroying the count data you still need?

## Questions to Think About

- If you sorted the words before counting, would that help or hurt?
- Is an in-place sort on your count structure always safe if callers still need the original mapping?

## Difficulty

Advanced

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Access Control Audit

## Scenario

A company manages permissions for apps. You receive:

1. A list of `(user_id, role)` pairs — a user may appear more than once with different roles
2. A list of `required_roles` for a specific action

Decide which users can perform the action and produce an audit summary.

Rules:

- A user **can** perform the action if they have **at least one** role that is in `required_roles`
- Role matching is case-sensitive
- Duplicate `(user_id, role)` pairs in the input should be treated as one

## Requirements

Given `assignments` (list of pairs) and `required_roles` (list of strings), return:

| Field | Meaning |
|-------|---------|
| `allowed_users` | User IDs who have at least one required role, sorted alphabetically |
| `denied_users` | User IDs who appear in assignments but have none of the required roles, sorted alphabetically |
| `role_coverage` | For each required role, how many **distinct** users have that role |

Also return `unknown_roles`: roles that appear in assignments but are not in `required_roles` and are not needed for the action (distinct, any order).

## Constraints

- Up to 10,000 assignment rows; up to 200 distinct users
- Do not modify the input lists
- A user with zero matching roles but no entries at all does not appear in `denied_users`

## Expected Behavior

**Input:**

```text
assignments = [
  ("u1", "admin"),
  ("u2", "viewer"),
  ("u1", "editor"),
  ("u3", "viewer"),
  ("u2", "viewer"),
]

required_roles = ["admin", "editor"]
```

**Output:**

```text
allowed_users   = ["u1"]
denied_users    = ["u2", "u3"]
role_coverage   = {"admin": 1, "editor": 1}
unknown_roles   = {"viewer"}
```

## Deliverables

- One function producing all four parts of the audit
- Demo with the example plus one case where `required_roles` is empty (define sensible behavior and document it)

## Decisions You Must Make

- How do you group all roles per user without losing users?
- How do you test whether a user has any required role efficiently?
- Which structures help with distinct users, distinct roles, and counts — and which would duplicate work?

## Questions to Think About

- If you stored assignments as a flat list and, for each user, scanned the entire list, what would scale poorly?
- Can one structure answer "users with role X" and another answer "all roles for user Y", or is one enough?

## Difficulty

Advanced

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Recent Search Buffer

## Scenario

A search box remembers the user's recent searches. Behavior rules:

1. When the user searches for something, that term moves to the **front** of the recent list (most recent first)
2. If the term is already in the list, remove the old position first — no duplicates
3. Comparison is case-insensitive for duplicate detection (`"Python"` and `"python"` are the same search)
4. Display should keep the casing from the **most recent** submission
5. The buffer holds at most **5** terms; when a sixth is added, the oldest falls off

Operations:

- `record_search(term)` — user submitted a search
- `get_recent()` — return the recent terms, most recent first (as a plain list)

## Requirements

Implement the buffer with the two operations above.

## Constraints

- Up to 1,000 `record_search` calls per session
- Maximum 5 stored terms at any time
- `get_recent` must return a snapshot — changing the returned list must not change the internal buffer

## Expected Behavior

```text
record_search("Python")
record_search("SQL")
record_search("python")
get_recent() → ["python", "SQL"]

record_search("Git")
record_search("Docker")
record_search("API")
record_search("SQL")
record_search("Rust")
get_recent() → ["Rust", "SQL", "API", "Docker", "Git"]
```

Explanation of last line: buffer size is 5; `"Python"` / `"python"` was pushed out as oldest after enough new entries.

## Deliverables

- Implementation plus demo tracing through the example step by step
- Brief note on every structure you used and what job it does

## Decisions You Must Make

- How do you move a term to the front efficiently?
- How do you detect duplicates case-insensitively but store the latest casing?
- What do you return from `get_recent` so callers cannot accidentally corrupt internal state?
- Do you need more than one structure working together?

## Questions to Think About

- If you scanned the whole buffer on every search to remove duplicates, is that acceptable for 5 items? For 5,000?
- Which parts of this problem look like a queue, which like a stack, and which like neither?

## Difficulty

Advanced

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

## How to Use This Set

1. Work through the problems in order — they get harder and combine earlier ideas.
2. For each problem, write down which structures you considered and which you dropped.
3. After solving, ask: did I pick this because it was familiar, or because it fit?
4. Submit when you're ready for review.

## What This Set Trains

| Skill | Problems that stress it most |
|-------|------------------------------|
| Parsing text into structure | 1, 3, 9 |
| Order vs fast lookup | 2, 9, 10 |
| Aggregation and counting | 3, 9, 10 |
| FIFO vs LIFO choice | 4, 5, 10 |
| Comparing collections | 6 |
| Keys and lookup design | 7, 10 |
| Copying vs mutating nested data | 8 |
| Combining multiple structures in one feature | 7, 10 |
