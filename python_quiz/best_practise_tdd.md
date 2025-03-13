# Python Best Practices Quiz

## Beginner Level (7 Questions)

### Question 1 (True/False):
**Python uses indentation to define code blocks (such as loops, functions, and classes) instead of braces or keywords.**  
**Answer:** True.  
**Explanation:** Python enforces indentation to indicate code structure, making it visually clear and enforcing consistency.

---

### Question 2 (Multiple Choice):
**Which of the following is NOT a built-in Python data type?**  
A. list  
B. tuple  
C. dict (dictionary)  
D. tree  

**Answer:** D. tree  
**Explanation:** Python does not have a built-in `tree` data type. Lists, tuples, and dictionaries are built-in.

---

### Question 3 (Multiple Select):
**Which of the following are valid Python variable names?**  
A. my_var  
B. 2cool  
C. _data  
D. total$  

**Answer:** A and C (my_var and _data)  
**Explanation:** Python variable names must start with a letter or an underscore and cannot contain special characters like `$`.

---

### Question 4 (Code Completion):
**Fill in the blank to complete the for loop that prints each name in the list:**
```python
names = ["Alice", "Bob", "Charlie"]
for ____ in names:
    print(name)
```
**Answer:** `name`  
**Explanation:** The correct syntax is:
```python
for name in names:
    print(name)
```

---

### Question 5 (Code Debugging):
**Fix the error in the following code:**
```python
for i in range(5)
    print(i)
```
**Answer:** The loop is missing a colon. It should be:
```python
for i in range(5):
    print(i)
```

---

### Question 6 (Multiple Choice):
**What will be the output of the following code?**
```python
x = 5
if x % 2 == 0:
    print("even")
else:
    print("odd")
```
A. even  
B. odd  
C. even odd  
D. No output  

**Answer:** B. odd  
**Explanation:** `x % 2 == 0` evaluates to `False` for `x = 5`, so the `else` block executes.

---

### Question 7 (Multiple Choice):
**Which keyword is used to define a function in Python?**  
A. func  
B. def  
C. function  
D. define  

**Answer:** B. def  
**Explanation:** In Python, functions are defined using the `def` keyword.

---

## Intermediate Level (7 Questions)

### Question 8 (Multiple Choice):
**What will be printed by the following code?**
```python
def greet(name="world"):
    print(f"Hello, {name}!")

greet()
greet("Python")
```
A. Hello, world!  
B. Hello, Python!  
C. Hello, world! \n Hello, Python!  
D. Hello, Python! \n Hello, world!  

**Answer:** C. Hello, world! \n Hello, Python!

---

### Question 9 (Multiple Choice):
**Which of the following is a correct `__init__` method definition inside a Python class?**
A. `def __init__(self, x): self.x = x`  
B. `def __init__(x): self.x = x`  
C. `def __init__(self): self.x = x`  
D. `def __init__(): self.x = x`  

**Answer:** A. `def __init__(self, x): self.x = x`

---

### Question 10 (Multiple Choice):
**What will the following code output?**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done")
```
A. Cannot divide by zero \n Done  
B. Cannot divide by zero \n Division succeeded \n Done  
C. Division succeeded \n Done  
D. Done  

**Answer:** A. Cannot divide by zero \n Done

---

### Question 11 (Multiple Choice):
**Which of the following best describes Test-Driven Development (TDD)?**  
A. Write tests before writing the code.  
B. Write all code first, then write tests.  
C. Write tests only when necessary.  
D. Skip automated tests in favor of manual testing.  

**Answer:** A. Write tests before writing the code.

---

### Question 12 (Multiple Select):
**Which of the following are recommended Python style guidelines according to PEP 8?**  
A. Use 4 spaces for indentation.  
B. Use `snake_case` for variables and functions.  
C. Keep line length to 79 characters.  
D. Use `CamelCase` for all variables.  

**Answer:** A, B, and C.

---

## Advanced Level (6 Questions)

### Question 15 (True/False):
**Python allows a class to inherit from more than one base class (multiple inheritance).**  
**Answer:** True.

---

### Question 16 (Multiple Choice):
**Which of the following is a characteristic of Behavior-Driven Development (BDD)?**  
A. Writing tests only after all code is written.  
B. Using "Given-When-Then" format.  
C. Focusing only on unit tests.  
D. Eliminating automated tests.  

**Answer:** B. Using "Given-When-Then" format.

---

### Question 17 (Multiple Choice):
**What is the difference between `==` and `is`?**  
A. `==` compares values, `is` compares object identity.  
B. `==` and `is` are the same.  
C. `is` is for strings, `==` is for numbers.  
D. `is` compares values, `==` compares identity.  

**Answer:** A. `==` compares values, `is` compares object identity.

---

### Question 18 (Code Completion):
**Fill in the blank to create a list of squares:**
```python
squares = [ __________ for i in range(5) ]
print(squares)
```
**Answer:** `i**2`

---

### Question 19 (Code Debugging):
**Identify and fix the issue in this function:**
```python
def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list
```
**Fixed version:**
```python
def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list
```
**Explanation:** Using `None` prevents unintended list sharing between function calls.

---

### Question 20 (Multiple Select): Which of the following practices can help improve the performance or efficiency of Python code? (Choose all that apply.)
A. Using list comprehensions instead of equivalent for loops when building new lists.
B. Using generator expressions (or other iterators) for large datasets to avoid loading everything into memory at once.
C. Rewriting built-in functions (like len, sum) in pure Python to make them faster.
D. Minimizing the use of global variables in favor of local variables or function parameters.
Answer: A, B, and D.
Explanation: Option A: List comprehensions are typically faster and more concise than an equivalent Python for loop building a list, because the looping in a list comprehension happens in C (the Python interpreter’s native code) rather than in Python bytecode. Option B: Generator expressions produce one item at a time and are excellent for efficiency when dealing with large data streams, because they don’t materialize the whole list in memory. This can greatly reduce memory usage and sometimes improve performance by avoiding unnecessary computations. Option D: Using local variables and passing data as function arguments is usually better than using globals. In Python, access to local variables is faster than global variables, and avoiding globals also makes code cleaner and less error-prone. (While the performance gain is not huge, it’s still a good practice for code organization and can improve speed in tight loops.) Option C is incorrect because Python’s built-in functions and libraries (often written in C) are highly optimized. Rewriting them in pure Python would almost always be slower, not faster. A better practice is to use those built-in functions and data structures whenever possible, rather than “reinventing the wheel.”
