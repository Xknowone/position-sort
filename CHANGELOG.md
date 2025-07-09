# 📓 Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com),
and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [v2.0.0] - 2025-07-08
### Added
- ✅ Introduced `position_sort.py`: a bucket-based, real-number sort implementation
- 🧠 Supports `bin_width` control for float precision
- 📉 Avoids `sorted(keys)` → faster key traversal in O(n)
- ✅ Optional bucket-internal sorting via `sort_within_bucket`

### Changed
- 🔁 Replaces older `core.py` logic with bucket array approach
- 🔧 Updated README to reflect new usage and internals

---

## [v1.0.0] - 2025-07-07
### Added
- 📦 Initial release: basic position-based sorting via value-to-key mapping
- 🎯 Handles negative numbers and duplicates
- 🧪 Demo notebook with visualization
