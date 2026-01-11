# Two Pointers Technique

## 1. Concept Explanation 
The Two Pointers technique uses **two indices (pointers)** to traverse a data structure—usually an array or a string—efficiently.

Instead of using nested loops, two pointers move strategically to reduce time complexity. This technique is especially useful for **sorted arrays**, substring problems, and pair-based conditions.

---

## 2. Visual / Example

Consider a sorted array:

[1, 2, 4, 7, 11, 15]
^ ^
left right

- The left pointer starts from the beginning
- The right pointer starts from the end
- Based on a condition, one or both pointers move

This approach avoids unnecessary comparisons.

---

## 3. Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

Two pointers replace nested loops, reducing time from **O(n²)** to **O(n)** in many problems.

---

## 4. Python Code

```python
# Check if a sorted array has two numbers that sum to a target

def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False

numbers = [1, 2, 4, 7, 11, 15]
print(two_sum_sorted(numbers, 9))

```
---

## 5. Common Interview Problems

Frequently asked Two Pointer problems:

- Two Sum (sorted array)

- Reverse an array or string

- Check palindrome

- Container With Most Water

- Remove duplicates from sorted array

These problems test pattern recognition and optimization skills.

---

## 6. ML Connection

Two Pointers help in ML-related tasks such as:

- Efficient data preprocessing

- Optimizing feature selection in sorted data

- Window-based comparisons in time-series

- Reducing memory usage in large datasets

Understanding this technique improves algorithmic efficiency in ML pipelines.

---

## 7. Practice Tasks

1. Check if an array contains a pair with a given sum

2. Reverse a string using two pointers

3. Remove duplicates from a sorted array

4. Check whether a string is a palindrome

5. Compare two sorted arrays efficiently

---

**Author:**  
Hamna Munir

