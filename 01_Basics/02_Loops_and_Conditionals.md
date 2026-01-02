# Loops and Conditionals

## 1. Concept Explanation 
Loops and conditionals control **how a program makes decisions and repeats actions**.

- **Conditionals** (`if`, `elif`, `else`) allow a program to choose what to do based on conditions.
- **Loops** (`for`, `while`) allow a program to repeat tasks efficiently.

In Data Structures, Algorithms, and Machine Learning, these constructs form the backbone of data processing and model training logic.

---

## 2. Visual / Example

### Conditionals
Think of conditionals as decision checkpoints:
- If the condition is true → execute code
- Otherwise → skip or choose another path

### Loops
Think of loops as repetitive tasks:
- Processing each data point
- Iterating through epochs
- Traversing arrays or datasets

In ML, loops often represent **training iterations** or **data traversal**.

---

## 3. Time & Space Complexity
Loops and conditionals directly affect **time complexity**:

- A single loop over `n` elements → **O(n)**
- Nested loops → **O(n²)** or higher
- Conditionals themselves are **O(1)**

Space complexity depends on:
- Variables created inside loops
- Data structures used during iteration

Efficient loop design is critical for scalable ML systems.

---

## 4. Python Code

### Conditionals
```python
loss = 0.25

if loss < 0.3:
    status = "Good Model"
else:
    status = "Needs Improvement"
```
### Loops
```python
# For loop
for epoch in range(5):
    print("Training epoch:", epoch)

# While loop
epochs = 0
while epochs < 3:
    print("Epoch:", epochs)
    epochs += 1
```
### Combined Example
```python
for epoch in range(10):
    if epoch % 2 == 0:
        print("Evaluating model at epoch", epoch)
```
---

## 5. Common Interview Problems

Frequently asked interview topics:

- Difference between for and while loops

- Use cases of break, continue, and pass

- Time complexity of nested loops

- Common infinite loop mistakes

- Conditional logic optimization

Interviewers often test logic clarity and efficiency.

---

## 6. ML Connection

Loops and conditionals are used extensively in ML workflows:

- Iterating over datasets and batches

- Running training loops for epochs

- Applying conditional checks for early stopping

- Handling validation and testing phases

Most ML frameworks abstract loops, but understanding them is essential for debugging and optimization.

---

## 7. Practice Tasks

1. Write a loop to simulate 10 training epochs

2. Use a conditional to stop training when loss falls below a threshold

3. Print only even-numbered epochs using a loop

4. Write a nested loop and analyze its time complexity

5. Refactor a while loop into a for loop

---

**Author:**  
Hamna Munir
