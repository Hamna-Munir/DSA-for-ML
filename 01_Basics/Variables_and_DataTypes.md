# Variables and Data Types

## 1. Concept Explanation 
Variables are used to **store data in a program**, and data types define **what kind of data** a variable can hold.  
In simple terms:
- A **variable** is a container
- A **data type** describes what is inside that container

Every program, from a simple script to a complex Machine Learning pipeline, depends on correct usage of variables and data types.

---

## 2. Visual / Example

Think of variables as labeled boxes:

- `age = 20` → a box holding a number  
- `name = "Model"` → a box holding text  
- `is_trained = True` → a box holding a yes/no value  

In Machine Learning, these boxes may store:
- Feature values
- Model parameters
- Hyperparameters
- Training states

---

## 3. Time & Space Complexity
Variables and data types **do not have time complexity by themselves**, but they affect:

- **Space Complexity** → how much memory is used
- **Performance** → how efficiently algorithms run

Examples:
- `int` uses less memory than `float`
- Lists consume more memory than tuples
- Poor data type choices can increase memory usage in large datasets

Understanding this is critical when working with large-scale ML data.

---

## 4. Python Code

### Basic Data Types
```python
# Integer
epochs = 50

# Float
learning_rate = 0.01

# String
model_name = "LogisticRegression"

# Boolean
is_training = True
```
### Composite Data Types
```python
# List
features = [1.2, 3.4, 5.6]

# Tuple
image_shape = (224, 224, 3)

# Dictionary
hyperparameters = {
    "learning_rate": 0.01,
    "epochs": 50
}

# Set
unique_classes = {0, 1, 2}
```
---

## 5. Common Interview Problems

Typical interview questions related to variables and data types:

- Difference between list and tuple

- Mutable vs immutable data types

- How Python handles dynamic typing

- When to use a dictionary vs a list

- Common bugs caused by incorrect data types

Interviewers expect clarity in both concept and usage.

---

## 6. ML Connection

Variables and data types are deeply connected to Machine Learning:

- Feature vectors are stored in lists, arrays, or tensors

- Model weights and gradients use floating-point numbers

- Dictionaries store model configurations and metadata

- Incorrect data types can cause silent ML bugs or performance issues

Understanding data types prepares you for working with:

- NumPy arrays

- Pandas DataFrames

- PyTorch and TensorFlow tensors

 ---

## 7. Practice Tasks

1. Create variables for a simple ML experiment:

- dataset size

- learning rate

- number of epochs

2. Store model hyperparameters in a dictionary

3. Convert a list of integers into floats

4. Identify which data types are mutable and immutable

5. Write a short script showing type changes using type()

---

**Author:**  
Hamna Munir
