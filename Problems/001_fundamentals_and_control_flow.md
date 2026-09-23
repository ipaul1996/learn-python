# Problem Set: Fundamentals & Control Flow

Practice problems based on concepts covered in `001_Fundamentals` and `002_Control Flow & Functions`.

For each problem, pick what fits. We won't tell you which tool to use.

---

# Problem: Session Activity Checker

## Scenario

A login system saves every username from sign-in attempts into a list. At the end of the hour, you get that list and need a short report.

## Requirements

Your program receives one list of username strings.

From that list, you must:

1. Find out whether any **valid** username appears more than once
2. Count how many **unique** valid usernames there are
3. Collect all **invalid** usernames, in the order they appeared in the input

A username is **invalid** when it is an empty string (`""`) or contains only spaces (for example `"   "`).

Valid usernames are compared exactly as given: `"Alice"` and `"alice"` are different.

## Constraints

- Typical batch size: 50–500 usernames
- Do not change the original input list
- The solution should stay reasonable if the batch grows much larger

## Expected Behavior

**Input:**

```text
["alice", "bob", "alice", "   ", "carol", ""]
```

**Output (three parts):**

1. Duplicates among valid usernames? → `True` (`"alice"` appears twice)
2. Count of unique valid usernames → `3` (`"alice"`, `"bob"`, `"carol"`)
3. Invalid entries in order → `["   ", ""]`

You may return these as separate values or print them — but all three must be produced.

## Deliverables

- One main function (name your choice) that takes the username list and returns or prints the report
- Short comments only where your design isn't obvious

## Decisions You Must Make

- How do you track which valid usernames you have already seen?
- Do you process the list once or multiple times?
- Where does validation happen — inline, or in a separate helper?

## Questions to Think About

- If you check every username against a growing list of everything seen so far, what happens as the list gets longer?
- Does every part of the output need to preserve input order, or only the invalid list?

## Difficulty

Beginner

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Invoice Reference Normalizer

## Scenario

Finance gets invoice reference codes from vendors. Before storing them, check each code and convert it to a standard form.

## Requirements

A **valid** reference looks like this:

```text
PREFIX-YEAR-SEQUENCE
```

**Valid examples:**

- `INV-2024-00123`
- `ORD-2023-00007`

**Rules for a valid reference:**

| Part | Rule |
|------|------|
| PREFIX | Exactly 3 uppercase letters (`A`–`Z`) |
| YEAR | Exactly 4 digits |
| SEQUENCE | Exactly 5 digits |
| Separators | Exactly two `-` characters, in the positions shown |
| Total length | Exactly 14 characters |

**Invalid examples:**

- `inv-2024-00123` — prefix is lowercase
- `INV-2024-123` — sequence has only 3 digits
- ` INV-2024-00123` — leading space (length is not 14)

For each reference in a batch:

- If **valid** → produce `(prefix, year_as_int, sequence_as_int)`
  - Example: `INV-2024-00123` → `("INV", 2024, 123)`
- If **invalid** → produce `(original_string, reason_string)`
  - Example: `("INV-24-00123", "wrong length")`

Process the whole batch even when some entries fail.

## Constraints

- Up to 1,000 references per batch
- Invalid entries must appear in the error list in the same order as the input
- Valid entries can be in any order — just be ready to explain why

## Expected Behavior

**Input:**

```text
["INV-2024-00123", "bad", "ORD-2023-00007", "INV-2024-00A23"]
```

**Valid results (order is your choice):**

```text
[("INV", 2024, 123), ("ORD", 2023, 7)]
```

**Invalid results (must match input order):**

```text
[("bad", "..."), ("INV-2024-00A23", "...")]
```

(You choose the exact reason strings, but they should be short and meaningful.)

## Deliverables

- Separate logic for: checking one reference, processing a batch
- A demo with at least 6 sample references, including at least two invalid ones

## Decisions You Must Make

- Do you validate everything in one function or split validation and parsing?
- In what order do you check the rules?
- How do you turn the year and sequence parts into integers safely?

## Questions to Think About

- If one long block handles every rule, what becomes harder when finance adds a new rule next month?
- Should you check length first, or check the prefix first?

## Difficulty

Beginner

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Shared Draft Cart

## Scenario

An online shop keeps a customer's cart as a list of item names (strings).

Two functions both receive the cart from the caller:

1. `apply_welcome_offer(cart)` — if `"Free sample"` is not already in the cart, insert it at the **front**
2. `reset_cart_from_saved(cart, saved_items)` — remove everything in the cart and replace it with `saved_items`

The caller creates one cart and passes it to both functions, one after the other.

A common **buggy** implementation of `reset_cart_from_saved` looks like this:

```python
def reset_cart_from_saved(cart, saved_items):
    cart = list(saved_items)  # reassigns only the local parameter name
```

After `apply_welcome_offer` then `reset_cart_from_saved`, the caller still sees the old cart contents — the reset never reached the caller's list.

Show that bug first, then fix it.

## Requirements

Build a small program that:

1. Creates a starting cart (for example `["Notebook", "Pen"]`)
2. Calls `apply_welcome_offer(cart)`
3. Calls `reset_cart_from_saved(cart, saved_items)` with `saved_items = ["Notebook"]`
4. Prints the cart after each step — first using a **buggy** version that shows the problem
5. Repeats the same steps with your **fixed** version

Also test once with `saved_items = []` (empty list).

## Constraints

- Cart items are plain strings
- No database or network code
- Do not use a global variable as your main fix
- Callers shouldn't need to know how the functions work inside

## Expected Behavior

**Buggy run (required — rebinding the parameter):**

```text
Start:           ["Notebook", "Pen"]
After offer:     ["Free sample", "Notebook", "Pen"]
After reset:     ["Free sample", "Notebook", "Pen"]   # reset had no effect on caller's cart
```

**Optional second demo — aliasing:** if `cart_a` and `cart_b` refer to the same list, show how mutating through one name affects the other.

**Fixed run (in-place reset — example):**

```text
Start:           ["Notebook", "Pen"]
After offer:     ["Free sample", "Notebook", "Pen"]
After reset:     ["Notebook"]   # caller's cart updated; free sample removed
```

With `saved_items = []`, the fixed cart after reset should be `[]`.

Explain your fix in 3–5 sentences.

## Deliverables

- `apply_welcome_offer` and `reset_cart_from_saved`
- A `main` block (or similar) showing buggy behavior, then fixed behavior
- A short explanation of the root cause

## Decisions You Must Make

- Should these functions change the cart they receive, or return a new cart?
- When two variables refer to the same cart, who sees the changes?
- When is copying needed, and when is it wasted work?

## Questions to Think About

- If `cart_a` and `cart_b` point to the same list, and you change `cart_a`, what does `cart_b` show?
- If you assign a brand-new list to `cart_a`, does `cart_b` change?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: HTTP Status Router

## Scenario

An API gateway gets HTTP status codes (like `200`, `404`, `500`) from other services. Turn each code into a short label for logging.

## Requirements

**Single-code rules:**

| Status code | Label |
|-------------|-------|
| `200` | `success` |
| `201` or `204` | `created_or_empty` |
| `400`, `401`, `403`, or `422` | `client_error` |
| `500`, `502`, or `503` | `server_error` |
| Any other code from `100` to `599` | `unknown` |
| Anything below `100` or above `599` | `invalid` |

**Batch processing:**

For a list of status codes, produce three results:

1. A list of labels — same order as the input
2. How many codes got the label `client_error`
3. Whether **any** code got the label `invalid` (`True` or `False`)

## Constraints

- Up to 10,000 codes per batch
- More code groups will be added later — your single-code logic should be easy to extend
- Keep the mapping easy to read in a code review

## Expected Behavior

**Input:**

```text
[200, 404, 999, 503, 1500]
```

**Output:**

1. Labels: `["success", "unknown", "unknown", "server_error", "invalid"]`
   - `404` is not in the client-error list above, so it is `unknown`
   - `999` is between 100 and 599, but not listed elsewhere, so it is `unknown`
   - `1500` is above 599, so it is `invalid`
2. Client error count: `0`
3. Any invalid: `True`

## Deliverables

- One function: classify a single status code → label string
- One function: process a list → the three results above
- Be able to explain how you structured the single-code function

## Decisions You Must Make

- How do you organize the single-code rules so adding a new group is straightforward?
- For the batch, do you compute all three results in one pass or several?
- Is a long chain of conditions the clearest option here, or is something else?

## Questions to Think About

- If every code went through one giant generic branch, would debugging get harder?
- To answer "any invalid?", do you need the full label list first?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Shift Hours Report

## Scenario

HR sends shift data as **two lists of the same kind of row**:

- List 1: employee IDs
- List 2: hours worked

Row `0` in list 1 pairs with row `0` in list 2. Row `1` pairs with row `1`, and so on.

## Requirements

**Step 1 — Build pairs**

Walk both lists together. If one list is longer, ignore the extra rows in the longer list.

**Step 2 — Filter out bad rows**

Skip a pair when:

- The employee ID is blank after removing leading/trailing spaces, **or**
- Hours worked is negative

**Step 3 — Compute two flags** (using only the remaining valid rows)

- `overtime_present` → `True` if **any** row has hours **greater than 8**
- `all_within_limit` → `True` if **every** row has hours from `0` to `24` (inclusive)
- If **no valid rows** remain after filtering: `overtime_present` → `False`, `all_within_limit` → `False`

**Step 4 — Sort**

Return the valid rows sorted by hours **highest first**.

When two employees have the same hours, keep their original order (stable sort).

## Constraints

- Up to 2,000 rows
- Do not modify the original two input lists
- Input is not pre-sorted

## Expected Behavior

**Input:**

```text
employees = ["E01", "E02", "  ", "E04"]
hours       = [7.5,   9.0,   5.0,  6.0]
```

**Index pairs:**

| Index | Employee | Hours | Keep? | Why |
|-------|----------|-------|-------|-----|
| 0 | E01 | 7.5 | Yes | |
| 1 | E02 | 9.0 | Yes | overtime (> 8) |
| 2 | `"  "` | 5.0 | No | blank ID |
| 3 | E04 | 6.0 | Yes | |

**Valid rows before sorting:** `(E01, 7.5)`, `(E02, 9.0)`, `(E04, 6.0)`

**After sorting by hours (high → low):** `(E02, 9.0)`, `(E04, 6.0)`, `(E01, 7.5)`

**Flags:**

- `overtime_present` → `True` (E02 has 9.0 hours)
- `all_within_limit` → `True` (all valid hours are between 0 and 24)

**Return** all three: the two flags and the sorted list of pairs.

## Deliverables

- One function taking the two lists and returning the report
- At least four test cases written by you, including:
  - Lists of different lengths
  - At least one row with hours above 24 (should make `all_within_limit` false)

## Decisions You Must Make

- How do you walk two lists together when they may differ in length?
- Do you filter first and then compute flags, or do everything in one pass?
- How do you tell the sorter to use hours as the main key?

## Questions to Think About

- If two employees both worked exactly 8.0 hours, who should appear first in the output?
- If one valid row has 25 hours, which flags change?
- When no valid rows remain, why return `False` for both instead of saying "all rows are fine"?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Per-Client Rate Limiter

## Scenario

A file-upload service limits how many uploads each API client can make. Each client has its own limit. The program must **remember** how many uploads each client has already made during the run.

## Requirements

Your module must support three operations:

**1. Register a client**

```text
register("web", limit=3)
```

Each client has a string ID and a numeric limit (maximum allowed uploads).

**2. Record an upload**

```text
record("web")
```

Each call counts as one upload attempt for that client.

**3. Query a client**

Return two pieces of information:

- `attempts` — how many uploads have been recorded so far
- `can_upload` — `True` if the client may upload again, `False` if they have reached their limit

**Rule for `can_upload`:**

```text
can_upload is True  when  attempts < limit
can_upload is False when  attempts >= limit
```

**Registering the same client ID twice:**

Pick one consistent behavior (ignore the second registration, update the limit, or raise an error) and document it in a comment.

**Recording or querying an unregistered client:**

Pick one consistent behavior (raise an error, or treat as zero attempts with `can_upload=False`) and document it.

## Constraints

- Do not store all counters in one global variable at module level
- Up to 50 clients; thousands of upload records
- Counters for `"web"` and `"worker"` must stay independent

## Expected Behavior

Walk through this exact scenario in your demo:

```text
register("web",    limit=3)
register("worker", limit=1)

record("web")    →  attempts=1, can_upload=True
record("web")    →  attempts=2, can_upload=True
record("web")    →  attempts=3, can_upload=False   # limit reached
record("web")    →  attempts=4, can_upload=False   # still over limit

record("worker") →  attempts=1, can_upload=False   # worker limit is 1
```

`"web"` and `"worker"` must not share a counter.

## Deliverables

- `register`, `record`, and a query function (name your choice)
- A runnable demo matching the scenario above
- A short paragraph explaining how each client's count stays separate

## Decisions You Must Make

- Where does each client's counter live?
- What happens when `register` is called twice for the same ID?
- Should `record` return the updated status, or only the query function provides that?

## Questions to Think About

- Why does one shared counter for all clients break the requirements?
- If you build a factory that returns helper functions, what does each helper remember?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Audited Admin Commands

## Scenario

An admin tool has several operations (deactivate user, reset token, change quota). Every operation should log when it starts, when it finishes, and how long it took — **without** pasting the same logging code into every function.

## Requirements

**Part 1 — Write three admin operations**

Each operation is a normal function with a **different** signature (different arguments). Examples of what they might do:

- Deactivate a user by ID
- Reset a token (maybe takes two arguments)
- Change a quota (maybe uses a keyword argument like `amount=10`)

Simulate the work with `time.sleep(0.01)` or simple calculations — no real database.

**Part 2 — Add uniform logging around them**

When an operation runs:

```text
Starting <operation_name>
Finished <operation_name> in <duration> seconds
```

If the operation crashes:

```text
Failed <operation_name>: <error message>
```

Then let the error continue to the caller (do not hide it).

The logging code must **not** be duplicated inside each operation's body.

**Part 3 — Demo**

Call each operation at least once. Make one operation fail on purpose so the failure log appears.

## Constraints

- You may use the `time` module
- At least one operation takes multiple positional arguments
- At least one operation takes a keyword argument
- The logging layer must not contain a hard-coded list of all operation names

## Expected Behavior

**Successful call:**

```text
Starting deactivate_user
Finished deactivate_user in 0.012304 seconds
```

The operation's return value must still be returned to the caller.

**Failed call:**

```text
Starting reset_token
Failed reset_token: <message>
```

Then the exception reaches the caller.

## Deliverables

- Three admin operations
- One reusable way to attach logging to any operation
- A demo script showing success and failure cases

## Decisions You Must Make

- How do you wrap an operation that takes different arguments?
- How do you make sure the wrapper returns the real result?
- Where does the wrapper live vs. the business logic?

## Questions to Think About

- If the wrapper does not forward arguments correctly, what breaks first?
- If you copy-pasted logging into every function, what would maintenance look like after ten operations?

## Difficulty

Advanced

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Daily Sales Snapshot

## Scenario

A shop exports end-of-day sales as two lists:

- Product codes
- Units sold

Position `0` in both lists is one sale. Position `1` is the next sale, and so on.

Sometimes the two lists have different lengths. Some rows have bad data.

## Requirements

**Step 1 — Walk rows together**

Process pairs only up to the length of the **shorter** list. Ignore extra rows in the longer list.

**Step 2 — Skip bad rows**

Skip a row when:

- The product code is empty after stripping spaces, **or**
- The quantity is not a valid whole number greater than zero

Quantities may arrive as integers **or** strings that represent whole numbers (for example `"2"`). Invalid examples: `0`, `-1`, `2.5`, `"abc"`, `"2.5"`

**Step 3 — Add up totals**

The same product code may appear on multiple rows. Combine them: total units sold per product.

**Step 4 — Rank products**

Sort products by:

1. Total units sold — highest first
2. If tied, product code — alphabetical (A before B)

**Step 5 — Count skipped rows**

Report how many rows were skipped for each reason (for example: empty product, bad quantity).

## Constraints

- Up to 20,000 rows
- Do not modify the input lists
- Validation rules should live in one place — not copy-pasted in three different parts of the code

## Expected Behavior

**Input:**

```text
products  = ["A1", "B2", "A1", "",   "C3"]
quantities = [2,   1,   3,   5,    0]
```

**Row-by-row:**

| Index | Product | Qty | Valid? | Notes |
|-------|---------|-----|--------|-------|
| 0 | A1 | 2 | Yes | |
| 1 | B2 | 1 | Yes | |
| 2 | A1 | 3 | Yes | same product again |
| 3 | `""` | 5 | No | empty product |
| 4 | C3 | 0 | No | zero quantity |

**Totals:**

```text
A1 → 5  (2 + 3)
B2 → 1
```

**Ranking:**

```text
1. A1  (5 units)
2. B2  (1 unit)
```

**Skip counts (example shape):**

```text
empty product: 1
invalid quantity: 1
```

**Second demo case:** `products` has 3 items and `quantities` has 5 — only the first 3 rows are processed.

## Deliverables

- Clear separation between: validation, totals, ranking, skip counting
- A runnable demo with the example above plus the mismatched-length case

## Decisions You Must Make

- How do you pair the two lists safely when lengths differ?
- What structure holds the running totals per product?
- How do you sort by two rules (units first, then code)?
- One big loop, or several focused steps?

## Questions to Think About

- If you ranked rows before combining duplicate product codes, would the ranking be correct?
- If validation logic is written twice in two places, what risk does that create?

## Difficulty

Advanced

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

## How to Use This Set

1. Work through the problems in order — they get harder as you go.
2. Write down your design choices before you code.
3. When you're done, ask: could a simpler design still meet the requirements?
4. Submit your solution when you're ready for review.
