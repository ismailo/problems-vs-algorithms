# Basic Algorithms – Problems vs Algorithms

Seven classic algorithm and data structure problems implemented in Python, completed as part of the Udacity Data Structures & Algorithms Nanodegree.

---

## Problems

| # | Problem | Algorithm | Time | Space |
|---|---------|-----------|------|-------|
| 1 | Square Root of an Integer | Binary search | $O(\log n)$ | $O(1)$ |
| 2 | Search in a Rotated Sorted Array | Modified binary search | $O(\log n)$ | $O(1)$ |
| 3 | Rearrange Array Digits | Merge sort + alternating assignment | $O(n \log n)$ | $O(n)$ |
| 4 | Dutch National Flag | Three-pointer single traversal | $O(n)$ | $O(1)$ |
| 5 | Autocomplete with Tries | Trie + DFS suffix collection | $O(m)$ lookup | $O(n)$ |
| 6 | Min and Max in Unsorted Array | Single-pass two-variable scan | $O(n)$ | $O(1)$ |
| 7 | HTTP Router using a Trie | Segment-level RouteTrie | $O(d)$ per op | $O(R \cdot d)$ |

---

## Project Structure

```
├── problem_1.py
├── problem_2.py
├── problem_3.py
├── problem_4.py
├── problem_5.ipynb       # Jupyter Notebook with interactive widget
├── problem_6.py
├── problem_7.py
├── explanation_1.md
├── explanation_2.md
├── explanation_3.md
├── explanation_4.md
├── explanation_5.md
├── explanation_6.md
└── explanation_7.md
```

---

## Usage

```bash
# Run any problem
python problem_1.py

# Run Problem 5 (requires Jupyter + ipywidgets)
pip install notebook ipywidgets
jupyter notebook problem_5.ipynb
```

Each `explanation_N.md` documents the reasoning, design decisions, and complexity analysis for the corresponding problem.