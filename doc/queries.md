# Queries

## Supported parameters format

### Number

accurate: 100
more than: >100
not less than: >=100
less than: <100
not more than: <=100
some accurate: 100,200,300
range: 100..200(inclusive)

### Date

format: 2025-1-29

### Boolean

True: true, t, yes, y, on, 1
False: false, f, no, n, off, 0

### Asterisks *

Please use `\*` as wildcards.

## post.json?

Parameters:

- limit
- page
- search: search[...]
  - id
  - created_at
  - updated_at
  - order

