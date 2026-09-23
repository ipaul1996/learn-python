# Problem Set: Typing Module

Practice problems based on the selected files in `010_Typing Module`.

You've covered fundamentals through enums. Here the focus is **clear type contracts**: what callers can pass in, what functions return, and the smallest honest annotation for each.

Type hints don't change runtime behavior. Write them for your teammate and the type checker (e.g. mypy).

For each problem, pick what fits. We won't tell you which typing feature to use.

---

# Problem: Safe Integer Parser

## Scenario

A CLI tool reads user input as text. Some commands need a whole number; others need either a whole number or the original text back when parsing fails.

Two helpers are needed:

**`parse_positive_int(text)`**

- Returns a whole number if `text` converts successfully and is greater than zero
- Signal failure your way if `text` isn't a valid integer or is zero/negative

**`parse_number_or_text(text)`**

- Returns a whole number if `text` is a valid integer
- Returns a float if `text` is a valid decimal but not an integer
- Otherwise returns the original string unchanged

## Requirements

- Implement both functions with full parameter and return type annotations
- Annotations must accurately describe every return path
- Do not use a catch-all type that disables checking for the whole function

## Constraints

- Input is always `str`
- No classes required — plain functions are enough
- Annotations should make it obvious to callers when failure is possible

## Expected Behavior

```text
parse_positive_int("42")    → 42
parse_positive_int("0")     → failure signal
parse_positive_int("abc")   → failure signal

parse_number_or_text("10")    → 10 (int)
parse_number_or_text("3.5")   → 3.5 (float)
parse_number_or_text("hello") → "hello" (str)
```

## Deliverables

- Both functions with complete annotations
- Three example calls per function showing how a caller would handle each return possibility

## Decisions You Must Make

- How do you annotate "returns an int or signals failure"?
- How do you annotate three different success types from one function?
- When is a union of concrete types better than a type that accepts anything?

## Questions to Think About

- If the return type were annotated too loosely, what mistakes would a caller make?
- Should failure return `None`, or is another approach clearer in the type signature?

## Difficulty

Beginner

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Log Level Filter

## Scenario

A logging utility accepts a minimum severity level. Only four levels exist in the system:

```text
"DEBUG", "INFO", "WARNING", "ERROR"
```

The filter function receives a level string from a config file. Internal code should only ever pass one of those four exact strings — not arbitrary text like `"TRACE"` or `"info"` (lowercase).

## Requirements

- Define the allowed levels as part of your type contract
- Write `set_min_level(level)` that only accepts those four values
- Write `should_log(event_level, min_level)` where both arguments use the same restricted level type
- Return type of `should_log` is boolean

## Constraints

- Level order for comparison: DEBUG < INFO < WARNING < ERROR
- A type checker should flag `set_min_level("trace")` as wrong before the program runs
- Runtime behavior can stay simple — the focus is correct annotations

## Expected Behavior

```text
set_min_level("INFO")                    → OK
set_min_level("debug")                   → type checker should reject (wrong casing)

should_log("ERROR", "INFO")              → True
should_log("DEBUG", "WARNING")           → False
```

## Deliverables

- Level type definition (however you express the four allowed strings)
- Both functions with annotations
- Demo calls plus one example the type checker should reject (in a comment)

## Decisions You Must Make

- How do you restrict a parameter to exactly four string literals?
- Is a plain `str` annotation honest for this API?
- Where should the ordered comparison logic live?

## Questions to Think About

- What is the difference between validating at runtime and expressing limits in the type system?
- If a fifth level is added later, how many places should need updating?

## Difficulty

Beginner

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Application Config Shape

## Scenario

Every service loads configuration from a dictionary with the same structure:

- `debug` — boolean
- `version` — integer
- `host` — string
- `port` — integer
- `tags` — list of strings (optional; may be absent)

The same shape appears in load functions, merge functions, and validation helpers. Repeating the full dictionary type everywhere is noisy and error-prone.

## Requirements

- Give this configuration shape a single reusable name
- Write `load_defaults()` returning a valid full config (including `tags`)
- Write `load_minimal()` returning a valid config **without** `tags`
- Write `get_port(config)` returning the port as an integer

All three functions must use your reusable config type in their signatures.

## Constraints

- At runtime these are normal dictionaries
- `get_port` must not modify the config it receives
- Wrong value types (for example `debug: "yes"`) should be caught by a type checker

## Expected Behavior

```text
load_defaults()   → {"debug": False, "version": 1, "host": "localhost", "port": 8080, "tags": []}
load_minimal()    → {"debug": True, "version": 2, "host": "api.internal", "port": 443}
                  (no "tags" key)

get_port(load_defaults())  → 8080
```

## Deliverables

- Reusable config type name and three annotated functions
- Comment showing one invalid config a checker should reject

## Decisions You Must Make

- How do you name and define a complex dictionary type once?
- How do you mark `tags` as optional in the type system?
- Is inheriting or extending an existing dict type the right tool here?

## Questions to Think About

- If you inlined the full dict type in five functions, what happens when `port` becomes optional?
- What is the difference between "key missing" and "key present with value None" in your design?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: First Value Report

## Scenario

Analytics code needs the first numeric value from ordered data. Callers pass different kinds of ordered collections:

- Lists of integers
- Tuples of integers

All of these support indexing and length. A generator does **not** — it can be looped once but not indexed.

Two functions are planned:

**`peek_first(values)`** — returns the first item using indexing

**`print_all(values)`** — loops and prints every item

## Requirements

- Annotate parameters so `peek_first` accepts lists and tuples of integers, but signals it only needs read access — not mutation
- Annotate `print_all` to accept anything that can be used in a `for` loop of integers, including a generator
- Do not annotate both parameters as `list[int]` if a narrower or wider contract is more honest

## Constraints

- `peek_first` must not promise to accept a one-shot generator
- `print_all` must accept `[1, 2, 3]`, `(4, 5)`, and `x for x in range(3)`
- Return type of `peek_first` is `int`

## Expected Behavior

```text
peek_first([10, 20])     → 10
peek_first((5, 6, 7))    → 5

print_all([1, 2, 3])     → prints 1, 2, 3
print_all(range(3))      → prints 0, 1, 2
```

## Deliverables

- Both functions with annotations and implementations
- One paragraph: why `peek_first` and `print_all` use different parameter types

## Decisions You Must Make

- What annotation promises indexing and length without promising mutation?
- What annotation promises only "can loop" without indexing?
- Why is a string of digits not the same contract as a sequence of integers?

## Questions to Think About

- If both functions took `list[int]`, what valid callers would be rejected?
- What goes wrong if `peek_first` receives an exhausted one-shot iterator?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Read-Only Rate Table

## Scenario

A billing service looks up prices from a table mapping product codes to cents (integers). Several modules receive this table. Some only **read** prices; one junior module accidentally called a mutating method and changed prices for everyone.

## Requirements

- Write `lookup_price(table, product_code) -> int` that returns the price or raises a clear error if the code is missing
- Write `format_price_list(table) -> str` that returns a multi-line string of `code: price` for every entry
- Neither function may add, remove, or change entries in the table
- Annotate the `table` parameter to express **read-only** access — not a promise that mutation is allowed

## Constraints

- Callers may pass a built-in dictionary at runtime
- Your annotation should document intent: readers must not mutate
- Do not copy the whole table inside each function unless you need to — the contract is about the signature

## Expected Behavior

```text
table = {"PEN": 199, "PAD": 499}

lookup_price(table, "PEN")     → 199
lookup_price(table, "MUG")     → raises error

format_price_list(table)       → "PEN: 199\nPAD: 499"  (order may vary)
```

## Deliverables

- Both functions with annotations
- Short note: why a plain mutable dictionary type is too permissive for the parameter

## Decisions You Must Make

- What annotation says "key-value lookup and iteration" without "insert/delete/update"?
- Is copying the dict at the start a substitute for a correct parameter type?
- How is this different from the config dictionary problem?

## Questions to Think About

- If a caller passes their only settings dict and a reader mutates it, who is at fault — caller or reader?
- What operations does your function actually need on the table?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Pluggable Discount Rule

## Scenario

A checkout function calculates a final price by applying a discount rule to a subtotal. Different promotions supply different rules:

- Flat ten off: `subtotal - 10` (minimum zero)
- Ten percent off: `subtotal * 0.9`

The checkout logic should not hard-code which rule runs.

## Requirements

- Write `apply_discount(subtotal: int, rule: ...) -> int` with a fully annotated `rule` parameter
- The rule accepts the subtotal (int) and returns the discounted subtotal (int)
- Write two rule functions and demonstrate passing each into `apply_discount`
- Store a rule in a variable, pass it later — the variable must have a meaningful type too

## Constraints

- Subtotals are non-negative integers; result must be an integer (round if needed)
- `rule` must not be annotated so loosely that any callable with any signature passes checking
- No classes required

## Expected Behavior

```text
apply_discount(100, flat_ten_off)      → 90
apply_discount(100, ten_percent_off)   → 90
apply_discount(5, flat_ten_off)      → 0  (not negative)
```

## Deliverables

- `apply_discount`, two rule functions, typed variable holding a rule, demo

## Decisions You Must Make

- How do you describe "a callable that takes int and returns int" in the type system?
- How is that different from "any callable at all"?
- Should the rule type be reused in multiple places?

## Questions to Think About

- If `rule` were annotated to accept anything, what wrong function could slip through?
- When would you need a callable with no arguments or a different return type?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: One-Shot Stream Totals

## Scenario

A data pipeline receives record counts from a live stream. The stream can only be read **once** — after that it is exhausted. A helper must consume the stream and return the sum.

Another helper in the same file walks any countable collection and also returns a sum. That one may be called multiple times on the same list.

## Requirements

**`total_once(stream)`**

- Accepts a one-shot numeric stream (for example the result of a generator expression)
- Returns the sum of all values
- After `total_once` runs, the same stream object must not be assumed reusable

**`total_repeatable(items)`**

- Accepts any collection that can be looped for integers
- Returns the sum
- Callers may invoke it twice on the same list

Annotate each parameter to match how callers actually use it.

## Constraints

- Do not convert the stream to a list inside `total_once` unless you justify it — the signature should reflect one-shot semantics
- Both return `int`
- Implementations are a few lines each

## Expected Behavior

```text
gen = (x for x in [1, 2, 3])
total_once(gen)           → 6
# using gen again in total_once should not be expected to work

data = [1, 2, 3]
total_repeatable(data)    → 6
total_repeatable(data)    → 6  (same list, still works)
```

## Deliverables

- Both functions with annotations and implementations
- Explanation of why the two parameter types differ

## Decisions You Must Make

- What annotation fits a generator you will exhaust?
- What annotation fits a list you may iterate multiple times?
- Is `Iterable` honest for both, or is one parameter lying?

## Questions to Think About

- What happens if you annotate a one-shot stream as a reusable iterable?
- Why is a list not a one-shot stream?

## Difficulty

Intermediate

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Typed Request Payload

## Scenario

An HTTP API accepts JSON bodies for user signup. Required fields:

- `email` — string
- `password` — string

Optional fields:

- `display_name` — string
- `marketing_opt_in` — boolean (defaults handled elsewhere if missing)

Downstream code expects a dictionary with a known shape. Using a plain `dict[str, Any]` loses track of which keys exist and what types they have.

## Requirements

- Define a type for valid signup payloads
- Write `validate_signup(payload) -> str` that returns `"ok"` when required fields are present with correct types, or an error message string otherwise
- Write `greeting(payload) -> str` that returns `Hello, <display_name>` if present, else `Hello, <email local part>`

Annotate `payload` parameters with your structured type, not a generic dictionary.

## Constraints

- Minimal payload `{"email": "a@b.com", "password": "secret"}` must type-check
- Full payload with all four keys must type-check
- Payload `{"email": "a@b.com"}` (missing password) should be flagged by the type checker if your type is strict enough
- Runtime validation in `validate_signup` still required for data from real JSON

## Expected Behavior

```text
validate_signup({"email": "a@b.com", "password": "x"})           → "ok"
validate_signup({"email": "a@b.com", "password": "x", "display_name": "Ann"}) → "ok"

greeting({"email": "ann@x.com", "password": "x", "display_name": "Ann"}) → "Hello, Ann"
greeting({"email": "ann@x.com", "password": "x"})                        → "Hello, ann"
```

## Deliverables

- Payload type definition and both functions
- Example of a payload that should fail static checking (in a comment)

## Decisions You Must Make

- How do you mark some keys required and others optional in one type?
- Is this a class, a typed dictionary, or something else?
- How do optional keys differ from keys that may be `None`?

## Questions to Think About

- Why is `dict[str, str]` too weak for `marketing_opt_in`?
- Will real `json.loads` output satisfy your type automatically, or is conversion needed?

## Difficulty

Advanced

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Generic Single-Slot Container

## Scenario

A utility library provides a wrapper that holds exactly one value and returns it later. The library is used for integers, strings, and custom types. If the wrapper is typed loosely, callers lose autocomplete and checkers cannot catch mixing types.

## Requirements

- Implement a container type that:
  - Is constructed with one value
  - Returns that same value from a `get()` method with a correct return type
  - Preserves the type of what was stored (storing `int` means `get()` is known to return `int`)
- Demonstrate:

```text
int_container = ... holding 42 ...
str_container = ... holding "hi" ...

int_container.get()   → 42   (checker knows int)
str_container.get()     → "hi" (checker knows str)
```

## Constraints

- One class definition must work for multiple value types
- Do not write separate `IntBox` and `StrBox` classes
- Use the standard library typing tools from your study set — no external validation libraries

## Deliverables

- Container class with full generic annotations
- Demo with at least two different stored types
- One sentence on what would break if `get()` were annotated to return a union of all possible types

## Decisions You Must Make

- How does the class parameterize the stored type?
- Where does the type variable appear in `__init__` and `get`?
- Is a type variable needed, and if so, constrained or unconstrained?

## Questions to Think About

- If you stored an `int` but `get()` returned `int | str`, what safety do you lose?
- How is this different from a box annotated as holding `Any`?

## Difficulty

Advanced

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

# Problem: Documented Field Constraints

## Scenario

A schema describes a product record for an internal admin API. Two fields need more than a plain type:

- `product_id` — must be a positive integer; tools should see a note that it is "unique catalog identifier"
- `quantity` — must be a non-negative integer; tools should see a note that zero means "out of stock"

You're **not** building a full validation framework. You're designing type annotations so tools can read the base type **and** any metadata you attach — all from one declaration.

## Requirements

- Define a product record type (dictionary-shaped or class-shaped — your choice) with at least those two fields
- Wrap each field's type with metadata describing the constraint message (plain strings as metadata are enough — no external libraries required)
- Write `describe_product(record) -> str` returning a one-line summary: `ID <id>, qty <quantity>`

## Constraints

- Metadata must ride alongside the type, not replace it — `product_id` is still an `int` at its core
- Do not use a catch-all type for the whole record
- Implementation of `describe_product` is trivial; focus on the annotation design

## Expected Behavior

```text
record = {"product_id": 101, "quantity": 0}
describe_product(record)  → "ID 101, qty 0"
```

A type checker should still treat `product_id` as an integer for assignment purposes.

## Deliverables

- Record type with annotated fields including metadata
- `describe_product` and one example record
- Two sentences: what metadata you attached and who might consume it besides humans

## Decisions You Must Make

- How do you attach a string note to a type without changing runtime behavior?
- Is a typed dictionary or a class clearer for this record?
- How is this different from putting constraints only in a comment above the field?

## Questions to Think About

- If a validator library ran later, where would it find your "positive integer" rule?
- Does metadata execute at runtime by itself, or must something read it?

## Difficulty

Advanced

## Concepts Potentially Relevant

You figure out which concepts apply — we don't list them here on purpose.

---

## How to Use This Set

1. Work through the problems in order — type contracts get stricter as you go.
2. Run a type checker on your solutions if you can (`mypy` or your IDE).
3. For each parameter, ask: what's the smallest promise I can make and still be honest?
4. Submit when you're ready for review.

## What This Set Trains

| Skill | Problems |
|-------|----------|
| Return types and optional/union results | 1 |
| Restricted literal values | 2 |
| Reusable complex types and optional keys | 3, 8 |
| Sequence vs iterable vs iterator | 4, 7 |
| Read-only mapping contract | 5 |
| Callable parameters | 6 |
| Generic type-preserving containers | 9 |
| Type + metadata wrappers | 10 |

## Note on Scope

These problems use only concepts from the included typing files. We left out protocols, overloads, `NewType`, `ParamSpec`, and similar topics. Use `Final` where module constants shouldn't be reassigned.
