# Problem Set: Enum Module

Practice problems based on concepts covered in `007_Enum Module`.

You've covered fundamentals through OOP. They still show up here, but the real work is knowing **when named constants beat raw strings or numbers**, and how to use them safely.

For each problem, pick what fits. We won't tell you which enum feature to use.

---

# Problem: Order Status Codes

## Scenario

An e-commerce backend stores order status as integers in the database:

```text
1 → placed
2 → paid
3 → shipped
4 → delivered
5 → cancelled
```

Other parts of the code compare against raw numbers like `if status == 3`. This is hard to read and easy to get wrong.

## Requirements

Replace the magic numbers with a fixed set of named constants for all five statuses.

Your solution needs to support:

- Looking up a status from an integer coming from the database (for example `3` → the shipped status)
- Looking up from a name string coming from a config file (for example `"CANCELLED"`)
- Checking whether a value is one of the defined statuses
- Iterating all statuses in definition order for a dropdown list

Also write a function `describe(status)` that returns a readable sentence:

```text
describe(shipped_status)  → "Order is shipped"
```

## Constraints

- Integer values `1`–`5` must stay exactly as listed (external systems depend on them)
- `describe` must accept only defined status constants, not raw integers
- Do not use a plain dictionary as the only solution — the team wants a single named type for all statuses

## Expected Behavior

```text
from_db = lookup_by_value(3)       → shipped constant
from_config = lookup_by_name("PAID") → paid constant

from_db == 3                         → False  (must not compare equal to raw int)
from_db.value == 3                   → True

1 in all_statuses                    → False  (raw 1 is not a member)
shipped_constant in all_statuses     → True
```

## Deliverables

- Status definitions plus `describe` and demo lookups
- One sentence on why `status == 3` is risky compared to using named constants

## Decisions You Must Make

- How do you look up by value vs by name?
- When do you compare to `.value` vs compare to another constant?
- What does `in` check — the raw number or the constant?

## Questions to Think About

- If two parts of the code both use `3`, how do you know it means "shipped" without comments?
- Why might `from_db == from_config` be useful when both came from different sources?

## Difficulty

Beginner

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Alert Severity Levels

## Scenario

A monitoring system classifies alerts as `INFO`, `WARNING`, `ERROR`, or `CRITICAL`. Other services don't care about the exact numbers — only that each level is distinct and ordered from least to most severe.

A developer accidentally defined two levels with the same underlying value. Nobody noticed until alerts were deduplicated incorrectly.

## Requirements

- Define four severity levels in order: INFO, WARNING, ERROR, CRITICAL
- You don't need to pick numbers yourself — let Python assign distinct values automatically
- Duplicate values must be caught **when the level set is defined**, not at runtime when an alert fires
- Provide `severity_name(level)` that returns the name string (for example `"ERROR"`)

## Constraints

- Exactly four members, all with different values
- If someone adds `ALSO_ERROR` with the same value as `ERROR`, the definition must fail immediately
- Severity set should be iterable in definition order

## Expected Behavior

```text
list(all levels by value)  → [1, 2, 3, 4]  (or similar sequential values)

severity_name(ERROR)       → "ERROR"

# This must fail at class definition time, not later:
# INFO = 1, WARNING = 2, ERROR = 2  → definition error
```

## Deliverables

- Severity level definitions and `severity_name`
- Demo showing iteration order
- Optional: show the failing duplicate definition in a comment or separate snippet

## Decisions You Must Make

- When are automatic values better than hand-picked numbers?
- How do you enforce "no duplicates" at definition time?
- What happens if duplicates are allowed silently (aliases)?

## Questions to Think About

- If ERROR and CRITICAL shared a value, could `{ERROR, CRITICAL}` behave like a set with one item?
- When is an alias useful, and when is it a bug?

## Difficulty

Beginner

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Sensor Reading Normalizer

## Scenario

Hardware sends temperature zone codes as integers. Your system understands:

```text
1 → cold
2 → normal
3 → hot
```

Sometimes firmware sends unknown codes after an update. The pipeline should not crash — it should map unknown codes to a dedicated `UNKNOWN` fallback and log a warning.

## Requirements

- Define the four zones above (including `UNKNOWN` with its own distinct code, for example `99`)
- When converting an integer:
  - Known codes → the matching zone
  - Unknown codes → `UNKNOWN`, and print `Warning: unknown zone code <n>`
- Valid lookups must still return the same singleton object each time

## Constraints

- Do not use a long `if/elif` chain as the **only** mechanism — the conversion hook for missing values should live with the zone definition
- `UNKNOWN` must be a real member, not `None`
- Known code `2` must satisfy: `lookup(2) is lookup(2)` → `True`

## Expected Behavior

```text
lookup(1)    → cold
lookup(2)    → normal
lookup(99)   → UNKNOWN   (if 99 is your UNKNOWN code)
lookup(42)   → UNKNOWN, prints warning
lookup(1) is lookup(1)  → True
```

## Deliverables

- Zone definitions with lookup behavior and demo
- Brief note: what happens without a missing-value handler when code `42` arrives?

## Decisions You Must Make

- Where does fallback logic live — in the enum definition or in external code?
- Should unknown codes raise an error instead? Why did this problem choose fallback?
- How is `UNKNOWN` different from returning `None`?

## Questions to Think About

- If every unknown code needed a different fallback, would one `UNKNOWN` member still work?
- When is strict failure (raise an error) better than silent fallback?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Background Job Lifecycle

## Scenario

A job runner moves jobs through states:

```text
QUEUED → RUNNING → SUCCEEDED
                 ↘ FAILED
```

Rules:

- `SUCCEEDED` and `FAILED` are terminal — no further moves
- From `QUEUED`, only `RUNNING` or `FAILED` are allowed
- From `RUNNING`, only `SUCCEEDED` or `FAILED` are allowed
- A job is "finished" when it is `SUCCEEDED` or `FAILED`
- A job is "in progress" when it is `QUEUED` or `RUNNING`

## Requirements

Attach behavior to the state constants so callers can ask:

- `state.is_finished` → boolean
- `state.is_in_progress` → boolean
- `state.can_move_to(other_state)` → boolean
- `advance(state)` → returns the next state in the linear order `QUEUED, RUNNING, SUCCEEDED, FAILED`, but **only** if `can_move_to` allows that transition; otherwise returns the same state unchanged

## Constraints

- Transition rules must be defined in one place
- `advance` from `RUNNING` goes to `SUCCEEDED` (next in list), not to `FAILED`
- `advance` from `SUCCEEDED` returns `SUCCEEDED` (no change)
- Use the state constants themselves — not strings like `"RUNNING"`

## Expected Behavior

```text
s = QUEUED
s.is_in_progress                    → True
s.can_move_to(RUNNING)              → True
s.can_move_to(SUCCEEDED)            → False

advance(QUEUED)                     → RUNNING
advance(RUNNING)                    → SUCCEEDED
advance(SUCCEEDED)                  → SUCCEEDED

FAILED.is_finished                  → True
RUNNING.can_move_to(FAILED)         → True
SUCCEEDED.can_move_to(RUNNING)      → False
```

## Deliverables

- State definitions with the queries above, plus `advance`
- Demo walking one job from `QUEUED` to `SUCCEEDED`

## Decisions You Must Make

- Should behavior live on each constant, in standalone functions, or in a separate class?
- How do you represent allowed transitions — mapping, methods, or something else?
- Is a plain enum without methods enough for this problem?

## Questions to Think About

- If transition rules were copied in three different files, what breaks when a new state is added?
- Why attach `is_finished` as a property instead of checking two names everywhere?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: User Role Permissions

## Scenario

An admin panel assigns roles: `VIEWER`, `EDITOR`, `ADMIN`. Each role maps to a set of allowed actions:

| Role | Actions |
|------|---------|
| VIEWER | `read` |
| EDITOR | `read`, `write` |
| ADMIN | `read`, `write`, `delete` |

The system receives a user's role and must check permissions quickly. The same role constant must work as a key in a lookup table.

## Requirements

- Define the three roles
- Build a permission lookup: role → set of allowed action strings
- Implement `can(role, action)` → `True` or `False`
- Implement `roles_with(action)` → all roles that allow that action (any order)

## Constraints

- Use role constants as keys in your lookup — not role name strings
- Two variables holding `ADMIN` must refer to the same object (`is` check passes)
- Adding the same role to a set twice must not create duplicates
- `can(VIEWER, "delete")` → `False`; `can(ADMIN, "read")` → `True`

## Expected Behavior

```text
can(EDITOR, "write")        → True
can(VIEWER, "write")        → False

roles_with("read")          → {VIEWER, EDITOR, ADMIN}  (as role constants)

{ADMIN, ADMIN, EDITOR}      → effectively two distinct roles in a set
ADMIN is lookup[ADMIN]      → True (same object as key)
```

## Deliverables

- Role definitions, permission lookup, `can`, `roles_with`, and demo

## Decisions You Must Make

- Why use role constants as dict keys instead of strings like `"ADMIN"`?
- What happens if you used integer `1, 2, 3` as keys and someone passed the wrong number?
- Can role constants live in a set? Why?

## Questions to Think About

- If two roles accidentally shared the same underlying value, how would a set of roles behave?
- Why does `ADMIN == "ADMIN"` fail for a plain enum but might work for a different kind of enum?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: API Environment Tag

## Scenario

A deployment tool tags each build with an environment: `dev`, `staging`, or `prod`. These tags are:

- Stored in JSON config files as strings
- Passed to functions that expect `str`
- Compared in code like `if env == "prod":`
- Shown in log messages and Slack notifications

A junior developer used a plain named-constant type (not mixed with `str`). Serialization failed, and `env == "prod"` returned `False` even when the right member was selected.

## Requirements

Fix the design so that:

- Only `dev`, `staging`, `prod` are valid environment tags
- `json.dumps({"env": selected})` produces `{"env": "prod"}` without manual `.value`
- A function `def is_production(env: str)` works when called as `is_production(selected_prod_member)` → `True`
- `selected_prod_member == "prod"` → `True`
- Invalid string `"production"` still fails lookup (does not silently match)

## Constraints

- Tag strings in JSON must be exactly `"dev"`, `"staging"`, `"prod"`
- Do not convert to string manually at every call site if the type can do it automatically
- `@unique` or equivalent — no duplicate tags

## Expected Behavior

```text
tag = ... lookup "prod" ...

tag == "prod"                              → True
is_production(tag)                         → True
json.dumps({"env": tag})                   → '{"env": "prod"}'

lookup("production")                       → fails (invalid)
```

## Deliverables

- Environment tag definitions
- Demo: JSON export, string comparison, and `is_production`
- A few sentences on what broke with the plain constant type, and why the fix works

## Decisions You Must Make

- Plain named constants vs constants that also behave as strings — when does each fit?
- Where does the built-in type go in the inheritance list?
- When is comparing to `.value` still necessary?

## Questions to Think About

- If you used integers `1, 2, 3` for environments, would JSON export be as clear?
- Could a dictionary `{"dev": ..., "prod": ...}` solve this without a named-constant type? What would you lose?

## Difficulty

Advanced

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

## How to Use This Set

1. Work through the problems in order — each adds a layer (lookup → safety → behavior → collections → serialization).
2. After each solution, list every place you used `.value` and ask if it was really needed.
3. Submit when you're ready for review.

## What This Set Trains

| Skill | Problems |
|-------|----------|
| Replace magic numbers/strings | 1 |
| Auto values and duplicate prevention | 2 |
| Unknown input handling | 3 |
| Behavior on constants | 4 |
| Constants in sets and dict keys | 5 |
| String-compatible constants for APIs | 6 |
