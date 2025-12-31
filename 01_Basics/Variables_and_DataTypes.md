# Variables and Data Types

## 🎯 Objective
Understand what variables are, how data is stored in memory, and how different data types are used in programming and Machine Learning.

---

## 📌 What is a Variable?
A **variable** is a named container used to store data in memory.  
In programming, variables allow us to reference and manipulate data efficiently.

### Example:
```python
x = 10
name = "Hamna"
🧱 Data Types in Python
1️⃣ Numeric Types
Type	Example	Description
int	10	Integer values
float	3.14	Decimal numbers
complex	2+3j	Complex numbers

python
Copy code
a = 5
b = 2.5
c = 3 + 4j
2️⃣ Boolean Type
Used for True / False logic.

python
Copy code
is_active = True
3️⃣ String Type
Strings are sequences of characters.

python
Copy code
name = "Machine Learning"
4️⃣ Sequence Types
Type	Example	Use Case
list	[1,2,3]	Mutable collection
tuple	(1,2,3)	Immutable collection
range	range(5)	Iteration

python
Copy code
numbers = [1, 2, 3]
coordinates = (10, 20)
5️⃣ Mapping Type
Stores key–value pairs.

python
Copy code
student = {
    "name": "Hamna",
    "age": 21
}
6️⃣ Set Types
Stores unique values.

python
Copy code
unique_ids = {1, 2, 3}
🔄 Mutable vs Immutable
Mutable	Immutable
list	int
dict	float
set	string
tuple

📌 Why important?
Immutable types are safer in ML pipelines and hashing operations.

🔁 Type Conversion (Casting)
python
Copy code
x = int("10")
y = float(5)
z = str(100)
🧠 Why Variables & Data Types Matter in ML
Features are stored as numeric types

Labels are often integers or strings

DataFrames depend on correct data types

Memory efficiency affects model performance

📌 Example:

python
Copy code
import numpy as np

features = np.array([1.2, 3.4, 5.6])
⚠️ Common Mistakes
Mixing strings with numbers

Forgetting type conversion

Using mutable objects as dictionary keys

🧪 Practice Problems
Create variables of all basic data types

Convert a string "100" into an integer

Store ML feature names in a list

Create a dictionary for dataset metadata

📌 Summary
Variables store data

Data types define how data behaves

Correct data types are critical in ML

Understanding mutability prevents bugs

👩‍💻 Author
— Hamna Munir
