# LeetCode & NeetCode Submissions

My solutions to data structures and algorithms problems from [LeetCode](https://leetcode.com) and the [NeetCode](https://neetcode.io) roadmap. Most are in **C++**, with a few in **C** and **Python**.

![Languages](https://img.shields.io/badge/languages-C%2B%2B%20%7C%20C%20%7C%20Python-blue)
![Problems](https://img.shields.io/badge/problems-15-brightgreen)

## Repository Structure

```
.
├── Data Structures & Algorithms/     # NeetCode roadmap problems (synced)
│   └── <problem-name>/
│       └── submission-N.cpp          # one file per accepted submission
├── 0003-longest-substring-.../       # LeetCode problems (synced)
│   ├── README.md                     # problem statement
│   └── <solution file>
├── 0136-single-number/
└── stats.json                        # auto-generated solve stats
```

Some problems have more than one submission file. These show how a solution improved over time, for example going from brute force to an optimised approach.

## NeetCode: Data Structures & Algorithms

### Arrays & Hashing

| Problem | Difficulty | Approach | Time | Space |
|---|---|---|---|---|
| [Contains Duplicate](Data%20Structures%20%26%20Algorithms/duplicate-integer) | Easy | Hash set | O(n) | O(n) |
| [Valid Anagram](Data%20Structures%20%26%20Algorithms/is-anagram) | Easy | Sort both strings and compare | O(n log n) | O(1) |
| [Two Sum](Data%20Structures%20%26%20Algorithms/two-integer-sum) | Easy | Brute force (nested loops) | O(n²) | O(1) |
| [Group Anagrams](Data%20Structures%20%26%20Algorithms/anagram-groups) | Medium | Hash map keyed by sorted word | O(m · k log k) | O(m · k) |
| [Top K Frequent Elements](Data%20Structures%20%26%20Algorithms/top-k-elements-in-list) | Medium | Frequency map + bucket sort | O(n) | O(n) |
| [Encode and Decode Strings](Data%20Structures%20%26%20Algorithms/string-encode-and-decode) | Medium | Length-prefix encoding (`len#str`) | O(n) | O(n) |
| [Product of Array Except Self](Data%20Structures%20%26%20Algorithms/products-of-array-discluding-self) | Medium | Prefix and suffix products | O(n) | O(n) |
| [Valid Sudoku](Data%20Structures%20%26%20Algorithms/valid-sudoku) | Medium | Sets for each row, column and 3×3 box | O(1)* | O(1)* |
| [Longest Consecutive Sequence](Data%20Structures%20%26%20Algorithms/longest-consecutive-sequence) | Medium | Hash set, counting only from sequence starts | O(n) | O(n) |

<sub>*The board is always 9×9.</sub>

### Two Pointers

| Problem | Difficulty | Approach | Time | Space |
|---|---|---|---|---|
| [Valid Palindrome](Data%20Structures%20%26%20Algorithms/is-palindrome) | Easy | Two pointers, skipping non-alphanumeric characters | O(n) | O(1) |
| [Two Sum II (Sorted Input)](Data%20Structures%20%26%20Algorithms/two-integer-sum-ii) | Medium | Two pointers from both ends | O(n) | O(1) |
| [3Sum](Data%20Structures%20%26%20Algorithms/three-integer-sum) | Medium | Brute force + set to remove duplicates | O(n³) | O(n) |

### Stack

| Problem | Difficulty | Approach | Time | Space |
|---|---|---|---|---|
| [Valid Parentheses](Data%20Structures%20%26%20Algorithms/validate-parentheses) | Easy | Stack of opening brackets | O(n) | O(n) |

## LeetCode

| # | Problem | Difficulty | Language | Approach |
|---|---|---|---|---|
| 3 | [Longest Substring Without Repeating Characters](0003-longest-substring-without-repeating-characters) | Medium | C | Sliding window + visited array |
| 136 | [Single Number](0136-single-number) | Easy | Python | XOR all elements |

## How Solutions Are Added

Solutions are pushed to this repo automatically when they are accepted:

- **LeetCode** problems are synced with [LeetHub](https://github.com/QasimWani/LeetHub). It creates one folder per problem with the statement and the solution, and updates `stats.json`.
- **NeetCode** problems are synced from NeetCode's GitHub integration into `Data Structures & Algorithms/`.

## Next Up

- [ ] Rewrite **Two Sum** with a hash map (O(n))
- [ ] Rewrite **3Sum** with sorting + two pointers (O(n²))
- [ ] Continue the NeetCode roadmap: Sliding Window, Binary Search, Linked List
