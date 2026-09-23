# Problem Set: Exception Handling

Practice problems based on concepts covered in `006_Exception Handling`.

You've covered fundamentals through typing. They still show up here, but the real work is **knowing when to catch, when to raise, what to raise, and what you must not swallow**.

For each problem, pick what fits. We won't tell you which exception feature to use.

---

# Problem: Payload Division Service

## Scenario

A microservice receives JSON-like dictionaries from other teams. Each payload should contain numeric `numerator` and `denominator` keys. Your function computes the division and doubles the result for reporting.

Payloads are messy. Your service must not crash on bad input.

## Requirements

Write `compute_report(payload)` that:

1. Reads `numerator` and `denominator` from the payload
2. Divides them
3. Doubles the result and returns it on success

On failure, return a **string** error message (do not crash the caller):

| Situation | Return message (exact text) |
|-----------|----------------------------|
| Missing key | `"Missing required field"` |
| Division by zero | `"Cannot divide by zero"` |
| Non-numeric values | `"Values must be numbers"` |

On success, print `"compute_report() finished"` exactly once per call — whether it succeeded or failed.

## Constraints

- Do not use a single catch-all handler as your **only** mechanism — different failures need different messages
- Keep the success path separate from error handling so real bugs don't get hidden
- Caller receives either a `float` (success) or a `str` (error) — document this in a comment

## Expected Behavior

```text
compute_report({"numerator": 10, "denominator": 2})
→ prints "compute_report() finished"
→ returns 10.0

compute_report({"numerator": 5})
→ prints "compute_report() finished"
→ returns "Missing required field"

compute_report({"numerator": 8, "denominator": 0})
→ prints "compute_report() finished"
→ returns "Cannot divide by zero"

compute_report({"numerator": "8", "denominator": 2})
→ prints "compute_report() finished"
→ returns "Values must be numbers"
```

## Deliverables

- `compute_report` and demo for all four cases above
- Short note on where the "finished" log runs and why

## Decisions You Must Make

- Which failure modes happen automatically vs need explicit checks?
- Should doubling happen in the success-only path or inside the main attempt block?
- What runs on every exit path regardless of success?

## Questions to Think About

- If you caught every error with one broad handler, could you still return the four distinct messages?
- What happens to the "finished" log if an unhandled error escapes?

## Difficulty

Beginner

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Profile Age Update

## Scenario

A user profile API accepts an age update. Ages must be whole numbers zero or greater. Callers sometimes send wrong types (`"25"`, `25.5`) or negative values.

The function should **reject bad input immediately** with a clear error — not silently fix or return `False`.

## Requirements

Write `set_age(age)` that:

- Accepts one value
- On valid input (integer `>= 0`): prints `Age set to <age>` and returns nothing (or `None`)
- On wrong type: fails with a type-related error and message containing `must be int`
- On negative integer: fails with a value-related error and message containing `must be >= 0`

Write a small `main` that calls `set_age` three times inside try/except blocks:

1. `set_age(30)` — succeeds
2. `set_age(-1)` — caught, print the error message
3. `set_age("30")` — caught, print the error message

## Constraints

- Validation logic belongs in `set_age`, not only in `main`
- Use the standard built-in error types that match "wrong type" vs "wrong value"
- Do not return `False` for invalid input — raise

## Expected Behavior

```text
set_age(30)       → prints "Age set to 30"
set_age(-1)       → caught: message mentions >= 0
set_age("30")     → caught: message mentions int
```

## Deliverables

- `set_age`, `main`, and output for all three calls

## Decisions You Must Make

- Should you check type before value, or the other way around?
- Is a custom error type justified here, or are built-in categories enough?
- Who should catch — `set_age` or the caller?

## Questions to Think About

- What is the difference between `set_age("30")` failing at conversion vs failing in your validation?
- If you only returned `False`, how would the caller know *why* it failed?

## Difficulty

Beginner

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Unified Record Lookup

## Scenario

A helper fetches one item from either a list (by index) or a dictionary (by key). Callers pass:

- the collection (`list` or `dict`)
- the lookup value (index or key)

Today the code has two separate paths with duplicated error handling. Your task is one function `fetch(collection, key)` that works for both.

## Requirements

- `fetch([10, 20, 30], 1)` → `20`
- `fetch({"a": 10, "b": 20}, "b")` → `20`
- On missing index or missing key: return `None` (do not crash)
- Log `"Lookup failed"` once when a lookup fails

Use one failure-handling path for both "index out of range" and "key not found" if the language allows — do not duplicate identical logic in two separate handlers if one parent category covers both.

## Constraints

- Do not check `isinstance` at the start and branch into two completely separate functions — one `fetch` entry point
- Returning `None` is intentional; do not raise for missing items
- Wrong collection types (e.g. a string) may raise naturally — you do not need to handle every possible type

## Expected Behavior

```text
fetch([1, 2, 3], 0)      → 1
fetch([1, 2, 3], 9)      → None, prints "Lookup failed"
fetch({"x": 5}, "x")     → 5
fetch({"x": 5}, "y")     → None, prints "Lookup failed"
```

## Deliverables

- `fetch` and demo for all four calls
- One sentence on why one handler might cover both failure kinds

## Decisions You Must Make

- Try the lookup and catch, or check membership first?
- Is there a shared parent category for "not found in collection"?
- When is returning `None` better than raising?

## Questions to Think About

- If you handled index and key failures in separate blocks with identical bodies, what would you duplicate?
- Would `fetch` behave differently if you used `collection[key]` for both lists and dicts?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: ATM Withdrawal

## Scenario

A cash machine tracks account balance. `withdraw(balance, amount)` subtracts `amount` from `balance` when allowed.

Business rule: withdrawal is **only** rejected when `amount` exceeds `balance`. Zero withdrawal and exact-balance withdrawal are allowed.

The UI team wants to catch this specific business failure separately from bugs like passing a string as `amount`.

## Requirements

- `withdraw(100, 40)` → `60`
- `withdraw(100, 100)` → `0`
- `withdraw(100, 150)` → must fail with a **dedicated business error type** you define, message: `"Insufficient funds"`
- `withdraw(100, "50")` → should fail with a built-in type error (not your business error)

Write `process_withdrawal(balance, amount)` that calls `withdraw` and returns either the new balance (int) or a user-facing string:

- Business failure → `"Declined: insufficient funds"`
- Type failure → `"Declined: invalid amount"`
- Success → the numeric balance

## Constraints

- Business failure must use a custom error type named meaningfully (your choice of name)
- Do not use the business error type for wrong-type input
- `process_withdrawal` catches errors; `withdraw` raises them

## Expected Behavior

```text
process_withdrawal(100, 40)    → 60
process_withdrawal(100, 150)   → "Declined: insufficient funds"
process_withdrawal(100, "50")  → "Declined: invalid amount"
```

## Deliverables

- Custom business error, `withdraw`, `process_withdrawal`, demo

## Decisions You Must Make

- Custom error vs built-in `ValueError` for insufficient funds — why one over the other?
- Should `withdraw` validate types, or only the balance rule?
- Which handler runs first if you order catches wrong?

## Questions to Think About

- If insufficient funds raised `ValueError`, what else might accidentally match that handler?
- What information should the custom error carry — message only, or more?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Service Outage Router

## Scenario

A background job talks to internal services. Failures are classified as:

- **Database** problems (connection lost, query timeout)
- **Network** problems (host unreachable, DNS failure)
- **Anything else** in application code (unexpected bugs)

All application-specific errors inherit from one common base type you define. Database and network errors are separate subtypes under that base.

## Requirements

Define three application error types (base + two subtypes) and `run_job(mode)` that simulates five modes:

| Mode | Simulated failure |
|------|-------------------|
| `"ok"` | return `"success"` (no error) |
| `"db"` | raise database subtype |
| `"net"` | raise network subtype |
| `"bug"` | raise the application **base** type directly (not db or net) |
| `"system"` | raise the built-in type that represents user interruption (keyboard interrupt) |

Write `handle_job(mode)` that:

- Returns `"Retry DB"` for database failures
- Returns `"Retry network"` for network failures
- Returns `"Unknown app error"` for other application base failures
- Returns `"success"` when `run_job` succeeds
- Re-raises anything that is **not** part of your application error family — `run_job("system")` is your test case for this

## Constraints

- Catching the application base type must also catch its subtypes
- Don't catch base exit/interrupt types in a way that stops `"system"` mode from propagating
- Handler order matters — more specific before more general

## Expected Behavior

```text
handle_job("ok")   → "success"
handle_job("db")   → "Retry DB"
handle_job("net")  → "Retry network"
handle_job("bug")  → "Unknown app error"   (raise base app error directly)
handle_job("system") → propagates (not converted to a string)
```

## Deliverables

- Error hierarchy, `run_job`, `handle_job`, demo with comments for `"system"` case

## Decisions You Must Make

- Why group errors under one application base?
- What must never be caught by a generic "app error" handler?
- How does handler order change which message runs?

## Questions to Think About

- If you caught the widest possible root type, what would happen on `"system"`?
- Why inherit from the standard user-code error root rather than inventing a unrelated parent?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Config File Loader

## Scenario

A service loads settings from a text file path. Failures happen in layers:

1. File does not exist
2. File exists but cannot be read (permission denied)
3. File reads fine but content is not valid (simulated by empty string)

Lower layers should add context before passing the error up. The top layer turns known failures into short codes for the UI.

## Requirements

**`read_raw(path)`** — opens and reads the file text (real file I/O is fine, or simulate with a dict mapping paths to outcomes for testing)

- Missing file → let the appropriate built-in file error propagate
- Permission denied → let the appropriate built-in permission error propagate

**`parse_config(text, path)`** — if `text` is empty, raise a **custom config error** that stores both `path` and a short `msg`, and formats a full message like: `Empty config (in /path/to/file)`

**`load_config(path)`** — reads the file, then parses it:

- On file-not-found: return `"MISSING"`
- On permission error: return `"DENIED"`
- On your custom config error: call `add_note("while loading config")` on the caught exception, then return `"INVALID"`
- On success: return the parsed text (non-empty string)

**Traceback demo (required):** also write `show_parse_failure_trace(path)`. It should read a file, call `parse_config`, call `add_note("while loading config")`, then let the error propagate so you can see the note in the traceback. `load_config` returns `"INVALID"` to the UI; this demo is only for inspecting notes on re-raise.

## Constraints

- Custom config error must expose `.path` and `.msg` attributes
- Use real exception notes API for at least the parse failure re-raise path
- Do not return `"MISSING"` for permission problems

## Expected Behavior

With a test setup you control:

```text
load_config("/exists/ok.txt")     → file contents
load_config("/missing.txt")       → "MISSING"
load_config("/locked.txt")        → "DENIED"
load_config("/empty.txt")         → "INVALID"
```

## Deliverables

- All three functions plus `show_parse_failure_trace`, custom config error class, test paths (real files or mock map)
- Traceback snippet or written description showing the note on the parse-failure path

## Decisions You Must Make

- Which layer catches vs raises?
- When do you add notes vs change the message in a custom error?
- File errors vs config errors — built-in vs custom?

## Questions to Think About

- If `load_config` swallowed every error as `"INVALID"`, what would the UI lose?
- Why store `path` on the exception object instead of only in the string message?

## Difficulty

Advanced

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Connection Session Guard

## Scenario

A function opens a connection, performs work, and must **always** release the connection when done — whether work succeeds, fails with a handled error, or fails with an unexpected error.

Simulate a connection with an object:

```python
class Connection:
    def __init__(self, name):
        self.name = name
        self.open = False
    def connect(self):
        self.open = True
        print(f"OPEN {self.name}")
    def close(self):
        self.open = False
        print(f"CLOSE {self.name}")
```

Work function `do_work(conn, mode)`:

- `"ok"` → returns `42`
- `"fail"` → raises a value-related error
- `"boom"` → raises an unexpected application error

## Requirements

Write `run_session(mode)` that:

1. Creates a connection, connects it
2. Calls `do_work`
3. On value-related failure from `do_work`: return `"bad input"` (do not re-raise)
4. On success: return the work result
5. On unexpected errors: let them propagate **after** cleanup runs
6. **Always** closes the connection if it was opened — on every path including early return and re-raise

## Constraints

- Connection close must not be duplicated in three places (success handler, error handler, end of function)
- `CLOSE` must print even when `mode` is `"fail"` or `"boom"`
- Do not catch the unexpected error only to close — close must happen for propagation cases too

## Expected Behavior

```text
run_session("ok")    → OPEN c / returns 42 / CLOSE c
run_session("fail")  → OPEN c / CLOSE c / returns "bad input"
run_session("boom")  → OPEN c / CLOSE c / then unexpected error propagates
```

## Deliverables

- `Connection` (or use provided), `do_work`, `run_session`, demo for three modes
- For `"boom"`, show that `CLOSE` printed before the traceback

## Decisions You Must Make

- Where does cleanup live — every branch, or one guaranteed block?
- What is the difference between handling an error and letting it propagate after cleanup?
- Should `else` be used for the success return?

## Questions to Think About

- If you only closed the connection in the success path, what leaks on failure?
- Why is copying `conn.close()` into every `except` block risky?

## Difficulty

Advanced

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

## How to Use This Set

1. Work through the problems in order — catching comes before hierarchies and cleanup.
2. For each problem, list which errors you **handle**, which you **raise**, and which you **let through**.
3. After solving, check: did any handler accidentally swallow Ctrl+C or exit signals?
4. Submit when you're ready for review.

## What This Set Trains

| Skill | Problems |
|-------|----------|
| Specific vs broad catching, else/finally | 1, 7 |
| Proactive raise with built-in types | 2 |
| Shared parent for lookup failures | 3 |
| Custom business exceptions | 4 |
| Exception hierarchies and handler order | 5 |
| Custom errors with attributes, notes, re-raise | 6 |
| Guaranteed cleanup on all paths | 7 |
