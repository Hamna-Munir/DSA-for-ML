# Variables and Data Types

## Objective
This section explains variables, memory storage, and core data types used in programming.  
A strong understanding of data types is essential for **Data Structures, Algorithms, and Machine Learning**.

---

## What is a Variable?
A **variable** is a named container used to store data in memory so it can be reused and modified during program execution.

```python
x = 10
name = "Hamna"
```
How Variables Work
Variables reference memory locations

Data types define memory usage and allowed operations

Correct usage improves performance and reliability

Data Types in Python
Numeric Types
Type	Example	Description
int	10	Whole numbers
float	3.14	Decimal numbers
complex	2+3j	Complex values

```
a = 5
b = 3.14
c = 2 + 3j
```
Boolean Type
Used for logical operations and decision making.

```
is_trained = True
```
String Type
Used to store text data.

```
course = "Machine Learning"
print(course.upper())
```
Sequence Types
List (Mutable)
```
features = [1, 2, 3]
features.append(4)
```
Tuple (Immutable)
```
shape = (224, 224)
```
Range
```
indexes = range(5)
```
Mapping Type (Dictionary)
Stores data in key–value pairs.

```
dataset = {
  "name": "Iris",
  "samples": 150
}
```
Set Type
Stores unique values only.

```
labels = {0, 1, 2}
```

Mutable vs Immutable
Mutable	Immutable
list	int
dict	float
set	string
tuple

Understanding mutability helps prevent bugs in ML pipelines and hashing operations.

Type Conversion
Used during data preprocessing and cleaning.

```
x = int("10")
y = float(5)
z = str(100)
```
Importance in Machine Learning

- Features must be numeric

- Labels require consistent data types

- Incorrect types can break models

- Memory efficiency impacts scalability

```
import numpy as np

X = np.array([1.2, 3.4, 5.6])
y = np.array([0, 1, 1])
```
Common Mistakes
- Mixing strings with numbers

- Ignoring type conversion

- Using mutable objects as dictionary keys

Practice Problems
- Create variables of all basic data types

- Convert a string to an integer

- Store feature names in a list

- Create a dataset dictionary

Summary
- Variables store data

- Data types define behavior

- Correct types are essential for ML

- Mutability awareness prevents errors

  Author

— Hamna Munir
