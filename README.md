# 🧮 PositionSort

**PositionSort** is a simple, stable, and intuitive **non-comparison-based sorting algorithm**.

Instead of comparing elements directly (`<`, `>`), it maps each value to a virtual position on a number line, then reads them back in order.  
It's conceptually similar to counting sort — but supports **floats**, **negatives**, and **duplicates** with stability.

---

## ✨ Features

- ✅ No direct comparisons between elements
- ➗ Works with floats, negatives, and repeated values
- ♻️ Stable sorting (preserves relative order of equal elements)
- 📦 Zero dependencies — pure Python
- 🧠 Great for educational use, algorithm research, or niche data layouts

---

## 🚀 Quick Start

```python
from position_sort.core import position_sort

arr = [3.5, -1.2, 0, 5, -1.2]
print("Before:", arr)
print("After: ", position_sort(arr))
# Output: [-1.2, -1.2, 0, 3.5, 5]
```

🧪 More examples: [examples/demo_position_sort.ipynb](examples/demo_position_sort.ipynb)

---

## 📁 Project Structure

```
position-sort/
├── position_sort/                # Core algorithm module
│   └── core.py
├── examples/
│   └── demo_position_sort.ipynb  # Jupyter demo notebook
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🧰 Requirements

- Python 3.6 or higher
- No external libraries required

---

## 📚 Theory

PositionSort maps each value `x` to a list at key `x`.  
After placing all values, it flattens the keys in order to produce a sorted list — without pairwise comparisons.

```
Input  →  [3.5, -1.2, 0, 5, -1.2]
Mapping:
  {
    -1.2: [-1.2, -1.2],
     0:   [0],
     3.5: [3.5],
     5:   [5]
  }
Sorted Output → [-1.2, -1.2, 0, 3.5, 5]
```

---

## ✅ License

This project is licensed under the [MIT License](LICENSE)

---

## 🙌 Author

Created with ❤️ by [@Xknowone](https://github.com/Xknowone)
