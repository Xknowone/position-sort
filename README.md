# 🧮 PositionSort

**PositionSort** is a simple, stable, and intuitive **non-comparison-based sorting algorithm**.

Instead of comparing elements directly (`<`, `>`), it maps each value to a virtual position on a number line, then reads them back in order.  
It's conceptually similar to counting sort — but supports **floats**, **negatives**, and **duplicates** with stability.

---

## 🔔 What's New (v2)

- ✅ Rewritten implementation using **bucket arrays** instead of key-sorting dictionaries
- 🔁 **No need to sort keys** → eliminates O(n log n) fallback
- 📉 Achieves O(n) time in ideal cases (uniformly distributed real numbers)
- 🧩 Supports real numbers, negative values, and small bin width control (`bin_width` param)
- 📂 New module: `position_sort.py` replaces old `core.py` logic

---

## ✨ Features

- ✅ No pairwise comparisons (non-comparison sort)
- ➗ Works with floats, negatives, and repeated values
- ♻️ Stable sorting (preserves relative order of equal elements)
- 📦 Zero dependencies — pure Python
- 🧠 Great for educational use, algorithm research, or niche data layouts

---

## 🚀 Quick Start

```python
from position_sort import position_sort  # ← new import!

arr = [3.5, -1.2, 0, 5, -1.2]
sorted_arr = position_sort(arr, bin_width=0.01, sort_within_bucket=True)
print("Before:", arr)
print("After: ", sorted_arr)
# Output: [-1.2, -1.2, 0, 3.5, 5]
```

🧪 More examples: [examples/demo_position_sort.ipynb](examples/demo_position_sort.ipynb)

---

## 📁 Project Structure

```
position-sort/
├── position_sort/                # Core algorithm module
│   ├── core.py                   # (legacy)
│   └── position_sort.py          # ✅ new version (v2)
├── examples/
│   └── demo_position_sort.ipynb
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

PositionSort maps each value `x` to a numeric index (bucket), not a key.  
Then all buckets are traversed in linear order — **eliminating the need to sort keys**.

### v1 (Key Mapping Version):
```python
position_map = {
    -1.2: [-1.2, -1.2],
     0:   [0],
     3.5: [3.5],
     5:   [5]
}
# requires sorted(position_map.keys())
```

### ✅ v2 (Bucket Indexing Version):
```python
index = int((x - min_val) / bin_width)
buckets[index].append(x)

# buckets are linear → no need to sort keys!
```

This reduces the overhead of `O(n log n)` sorting of dictionary keys, and moves toward a pure `O(n)` path when the input is reasonably well-distributed.

---

## ✅ License

This project is licensed under the [MIT License](LICENSE)

---

## 🙌 Author

Created with ❤️ by [@Xknowone](https://github.com/Xknowone)