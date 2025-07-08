# PositionSort

A simple, stable, non-comparison sorting algorithm that maps values to a number line and reads them back in order.

## Features
- Supports floats, negatives, duplicates
- No comparisons (`<`, `>`) between elements
- Stable and intuitive

## Example

```python
from position_sort.core import position_sort

arr = [3.1, -1.5, 0, 2.0, -1.5]
print(position_sort(arr))  # ➜ [-1.5, -1.5, 0, 2.0, 3.1]
