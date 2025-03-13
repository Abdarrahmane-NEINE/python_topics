# 60 Python Quiz Questions for Codingame Interview Preparation

Below is a collection of 60 Python quiz questions organized into three main topics: Design, Language Knowledge, and Reliability. Each topic includes 20 questions of varying difficulty (beginner, intermediate, advanced) and a mix of question types (True/False, single-choice, multiple-choice, code completion, and code correction). For each question, the correct answer is provided along with a detailed explanation.

## Topic 1: Design (Object-Oriented Principles & Pythonic Practices)

This section covers object-oriented programming concepts, useful functions for design, and Pythonic code practices. Questions range from basic OOP principles to advanced Python design patterns.

### 1. True or False: In Python, everything (including numbers, functions, and classes) is an object.
**Answer:** True.

**Explanation:** Python is designed with the philosophy that everything is an object. Numbers, strings, functions, classes, modules, etc., are all objects with a type. For example, integers are objects of class int, and functions are objects of class function. This means they can be assigned to variables, passed to functions, and have attributes or methods (where applicable). This uniform object model is a core design feature of Python.

### 2. True or False: Python supports multiple inheritance (a class inheriting from more than one base class).
**Answer:** True.

**Explanation:** Unlike some languages, Python allows a class to inherit from multiple base classes. For instance, you can define `class C(A, B): ...` to inherit from classes `A` and `B`. Python uses the Method Resolution Order (MRO) (specifically, C3 linearization) to determine the order in which base classes are searched when executing a method or accessing an attribute. While powerful, multiple inheritance should be used carefully to avoid complexity (e.g., the “Diamond Problem”) and maintain clear class designs.

### 3. True or False: A `@staticmethod` in Python receives a reference to the class (`cls`) as its first argument by default.
**Answer:** False.

**Explanation:** A method marked with `@staticmethod` does not receive an automatic `self` or `cls` parameter. It behaves like a plain function that happens to live in the class namespace. In contrast, a method marked with `@classmethod` receives the class (`cls`) as its first argument, and a normal instance method receives the instance (`self`). Use `@staticmethod` for utility functions that don't need access to instance or class data, and use `@classmethod` when you need to access or modify class state.

### 4. True or False: In Python classes, an attribute name with a double underscore prefix (e.g. `__attr`) will be mangled to include the class name, making it harder to access from outside.
**Answer:** True.

**Explanation:** Python uses name mangling for class attributes whose names start with double underscores. For example, in a class `MyClass`, an attribute named `__attr` is internally renamed to `_MyClass__attr`. This mechanism is intended to prevent accidental name collisions in subclasses (not truly to enforce privacy). It makes it harder (but not impossible) to access or override such attributes from outside the class or in subclasses. Note that this applies only to identifiers with two leading underscores and not ending in underscores.

### 5. Select the correct answer: How do you designate that class B inherits from class A in Python?
A. `class B extends A:`  
B. `class B(A):`  
C. `class B inherits A:`  
D. `class B -> A:`  

**Answer:** B. `class B(A):`

**Explanation:** In Python, inheritance is indicated by listing the base class(es) in parentheses after the class name. The syntax `class B(A):` means `B` inherits from `A`. Python does not use keywords like `extends` or `implements` for inheritance (those are used in languages like Java or C++). Option B is correct, whereas options A, C, and D use incorrect syntax or keywords for Python.

### 6. Select the correct answer: Which special method is called when a new instance of a class is created (initialized)?
A. `__init__`  
B. `__new__`  
C. `__call__`  
D. `__str__`  

**Answer:** A. `__init__`

**Explanation:** The `__init__` method is the constructor initializer in Python that gets called when a new instance is created. It allows you to initialize the instance’s attributes. Technically, the object is created via `__new__` (an even lower-level method) before `__init__` is called, but in typical use, we override `__init__` to set up a new object’s state. `__call__` is invoked when an object is called like a function, and `__str__` is used to define the string representation (what `str(obj)` returns). Option A is the standard method for initialization.

### 7. Select the correct answer: Which of the following is considered the most Pythonic way to iterate over both indices and values of a list `my_list`?
A. `for i in range(len(my_list)): print(i, my_list[i])`  
B. `for idx, val in enumerate(my_list): print(idx, val)`  
C. `i = 0; while i < len(my_list): print(i, my_list[i]); i += 1`  
D. `for item in my_list: print(my_list.index(item), item)`  

**Answer:** B. `for idx, val in enumerate(my_list): ...`

### 8. Select the correct answer: What does the `@property` decorator do in a class?
A. It defines a method that can be accessed like an attribute (read-only by default).  
B. It designates a class method that operates on the class rather than instance.  
C. It marks the method as private and hides it from outside access.  
D. It converts the function into a static method.  

**Answer:** A. It defines a method that can be accessed like an attribute.

### 9. Select all that apply: Which of the following are fundamental principles of Object-Oriented Programming (OOP)? (Select all that apply.)
A. Encapsulation  
B. Inheritance  
C. Polymorphism  
D. Indentation  

**Answer:** A, B, and C are correct.

### 10. Select all that apply: Python has several types of comprehensions that provide a Pythonic way to construct new sequences. Which of the following comprehension syntaxes exist in Python? (Select all that apply.)
A. List comprehension (`[...]`)  
B. Dictionary comprehension (`{key: value ...}`)  
C. Set comprehension (`{...}`)  
D. Tuple comprehension (`(...)`)  

**Answer:** A, B, and C are correct.

**Explanation:**
- List comprehensions produce lists, e.g. `[x*2 for x in range(5)]`.
- Dictionary comprehensions produce dictionaries, e.g. `{x: x*2 for x in range(5)}`.
- Set comprehensions produce sets, e.g. `{x*2 for x in range(5)}`.
- Tuple comprehension is a trick option: there’s no dedicated tuple comprehension in Python; `(x*2 for x in range(5))` creates a generator, not a tuple.


### 11. Select all that apply: Which of the following built-in functions can be used to introspect or get information about an object at runtime in Python? (Select all that apply.)
A. type(obj) – to get the object’s type.
B. dir(obj) – to list attributes and methods of the object.
C. hasattr(obj, 'attr') – to check if an object has a given attribute.
D. typeof(obj) – to get the object's type.

**Answer:** A, B, and C are correct.

**Explanation:** Python provides many built-in functions for introspection:
- `type(obj)` returns the type (class) of the object (e.g., `type(5)` returns `<class 'int'>`).
- `dir(obj)` returns a list of attribute names available on the object (its dict entries and methods, including inherited attributes).
- `hasattr(obj, 'attr')` returns True if the object has an attribute named 'attr' (it internally tries to access the attribute and catches exceptions).
- `typeof(obj)` is not a Python function; it’s a distractor here (some languages use `typeof`, but in Python use `type()` instead).

### 12. Select all that apply: The @dataclass decorator (from the dataclasses module in Python 3.7+) helps reduce boilerplate in classes. Which of the following methods can @dataclass generate automatically (when appropriate)? (Select all that apply.)
A. __init__ (constructor)
B. __repr__ (string representation)
C. __eq__ (equality comparison)
D. __len__ (length of the object)

**Answer:** A, B, and C are correct.

**Explanation:** A `@dataclass` will automatically generate several methods based on the class attributes defined:
- `__init__` is always generated to initialize the attributes.
- `__repr__` is generated to provide a convenient string representation for debugging (unless `repr=False` is specified for the dataclass).
- `__eq__` is generated to allow comparison of instances (unless `eq=False` is specified).
- Additionally, dataclasses can generate `__lt__`, `__gt__`, etc., if `order=True` is set.
- `__len__` is not generated by dataclasses; if you need length, you must implement it manually. The dataclass focuses on boilerplate like `__init__`, `__repr__`, `__eq__`, etc. (D is incorrect).

### 13. Complete the code: Fill in the blank to create a list of squares for numbers 0 through 4 using a list comprehension. The resulting list should be `[0, 1, 4, 9, 16]`.
```python
# Create a list of squares from 0 to 4:
squares = [ ____ for i in range(5) ]
print(squares)  # Expected output: [0, 1, 4, 9, 16]
```

**Answer:**
```python
squares = [ i**2 for i in range(5) ]
```

**Explanation:** List comprehensions provide a concise way to generate lists. Here, for each `i` in `range(5)` (0 through 4), we compute `i**2` (i squared). This builds a new list `[0, 1, 4, 9, 16]`. Using a list comprehension is more compact and Pythonic than initializing an empty list and using a loop to append squares.

### 14. Complete the code: The subclass `Child` is supposed to call its parent class `Parent`’s constructor to initialize the value. Fill in the blank with the correct call to Parent’s constructor using `super()`.
```python
class Parent:
    def __init__(self, value):
        self.value = value

class Child(Parent):
    def __init__(self, value, name):
        # Call the parent constructor to set value
        ________________
        self.name = name

child = Child(42, "python")
print(child.value, child.name)  # Expected: 42 python
```

**Answer:**
```python
super().__init__(value)
```

**Explanation:** To ensure the base class (`Parent`) is properly initialized, we use `super().__init__(value)`. The `super()` call returns a proxy to the parent, and calling its `__init__` sets up `self.value`. In Python, failing to call the parent’s `__init__` (when the parent expects it) can leave important initialization undone. Using `super()` is the preferred way to invoke the base class constructor (especially in multiple inheritance scenarios, as it respects MRO).

### 15. Complete the code: We want a function that takes any number of words and concatenates them into a single string separated by spaces. Fill in the blank to complete the implementation using `*args`.
```python
def concatenate_words(*words):
    # Join all words with a space in between
    return ________________
    
print(concatenate_words("Python", "quiz", "question"))  
# Expected output: "Python quiz question"
```

**Answer:**
```python
return " ".join(words)
```

**Explanation:** The `*words` parameter inside the function collects all positional arguments into a tuple. To concatenate them with spaces, a Pythonic solution is to use `" ".join(iterable)` on the `words` tuple. This joins each word in the sequence with a space as the separator. Using `join` is more efficient and concise than manually looping and concatenating strings.

### 16. Complete the code: The following class is intended to be an iterator that yields numbers from 0 up to `n-1`. Fill in the blank to raise the appropriate exception when the iteration is finished.
```python
class Counter:
    def __init__(self, n):
        self.n = n
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.n:
            result = self.current
            self.current += 1
            return result
        else:
            ________
```

**Answer:**
```python
raise StopIteration
```

**Explanation:** Python iterators signal completion by raising a `StopIteration` exception in their `__next__` method. In this `Counter` iterator, once `self.current` is no longer less than `self.n`, the `else` branch should execute `raise StopIteration` to indicate there are no more values. The `for` loop or any iterator consumer will catch this internally and stop the iteration. Forgetting to raise `StopIteration` (or otherwise ending the sequence) would result in an infinite loop or runtime error in iteration.

---

### 17. Identify and fix the error: What is wrong with the class definition below, and how can it be fixed?

```python
class Dog:
    def __init__(name):
        self.name = name
```

**Answer:**
```python
class Dog:
    def __init__(self, name):
        self.name = name
```

**Explanation:** Python instance methods (including `__init__`) must have `self` as the first parameter. `self` represents the instance and allows access to instance attributes. In the original code, `__init__` is missing `self`, so Python cannot assign `self.name`. This leads to a `NameError` or `TypeError` when creating a `Dog` instance. The fix is to include `self` in the parameter list.

---

### 18. Identify and fix the error: The following class is intended to maintain a separate list of items for each instance, but it doesn’t work as expected. What is the issue and how do you fix it?

```python
class MyClass:
    items = []            # class-level attribute
    def add_item(self, item):
        self.items.append(item)
```

**Answer:**
```python
class MyClass:
    def __init__(self):
        self.items = []   # instance-level attribute
    def add_item(self, item):
        self.items.append(item)
```

**Explanation:** Variables defined directly in the class body (outside any method) are class attributes, shared by all instances. In the original code, all `MyClass` instances share a single list `MyClass.items`. This means adding an item through one instance affects all instances. The fix is to initialize `self.items` inside `__init__`, ensuring each object has its own list. If a class-wide list was intended, one should refer to it as `MyClass.items` explicitly.

---

### 19. Identify and fix the error: In the code below, class `Circle` inherits from `Shape`, but the `color` attribute is not being set for `Circle` instances. What is the problem and how can it be corrected?

```python
class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        # Missing initialization of Shape
        self.radius = radius
```

**Answer:**
```python
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)    # initialize color in base class
        self.radius = radius
```

**Explanation:** When subclassing, if the base class `__init__` does important setup (like assigning `color`), the subclass should call it. In the original code, `Circle.__init__` overrides `Shape.__init__` but doesn’t call it, so `self.color` is never set. The correction uses `super().__init__(color)`, ensuring both `color` and `radius` are properly initialized. Using `super()` is also recommended for multiple inheritance scenarios.

---

### 20. Identify and fix the error: The `Person` class is trying to use a property for `age`, but there is a bug that causes a recursion error. What is wrong and how can it be fixed?

```python
class Person:
    def __init__(self, age):
        self.age = age    # intending to set age
    @property
    def age(self):
        return self.age   # this line is problematic
```

**Answer:**
```python
class Person:
    def __init__(self, age):
        self._age = age           # store in a "private" attribute
    @property
    def age(self):
        return self._age          # return the underlying attribute
```

**Explanation:** The original code causes infinite recursion because the `age` property method calls itself (`return self.age`), leading to a `RecursionError`. The fix is to store the value in a separate attribute (by convention, prefixed with `_`, e.g., `_age`). The `@property` method should return this underlying attribute. If needed, a setter method with `@age.setter` can be added to manage `_age`, ensuring controlled access while avoiding conflicts between the attribute and method.

--- 

## Topic 2: Language Knowledge (Syntax, Data Structures & Built-in Features)

This section quizzes you on core Python language knowledge: syntax rules, data types and their behaviors, standard functions, and general language features. Questions range from basic syntax and data structure properties to more advanced language semantics.

---

### 21. True or False: Python is a statically typed programming language.

**Answer:** False.

**Explanation:** Python is dynamically typed, meaning that types are determined at runtime and variables can reference objects of any type. In a statically typed language, types are checked at compile-time, and each variable has a type that is declared or inferred and cannot change. Python does not require variable declarations, and you can reassign variables to different types of objects. (Python is strongly typed in that it doesn’t implicitly convert unrelated types, but it is not static.)

---

### 22. True or False: Tuples in Python are immutable (cannot be changed after creation).

**Answer:** True.

**Explanation:** A tuple is an immutable sequence type. Once a tuple is created, you cannot add, remove, or modify its elements. For example, if `t = (1, 2, 3)`, any attempt to do `t[0] = 99` or `t.append(4)` will result in an error. Immutability makes tuples useful for fixed collections of items or as keys in dictionaries (since they are hashable when containing only immutables). This contrasts with lists, which are mutable (you can change their content in place).

---

### 23. True or False: The `is` operator is the recommended way to check if two strings have the same content.

**Answer:** False.

**Explanation:** The `==` operator should be used to compare values (like the contents of strings). The `is` operator checks for object identity, i.e., whether two references point to the exact same object in memory. Two distinct string objects with the same content (e.g., `a = "hello"`; `b = "".join(["hel", "lo"])`) may be equal (`a == b` is `True`) but not identical (`a is b` could be `False`). Using `is` for string (or general object) equality is a common mistake and can lead to incorrect results. `is` is only appropriate in special cases, such as checking against singleton objects like `None` (e.g., `if x is None:`).

---

### 24. True or False: Dictionary keys in Python must be of an immutable (hashable) type.

**Answer:** True.

**Explanation:** In Python dictionaries, keys must be hashable. Immutability is a requirement for an object to be hashable (its hash value must not change over its lifetime). Immutable built-in types like strings, numbers, and tuples (containing only immutable elements) are all hashable and can be used as keys. Mutable types like lists or dictionaries cannot be dictionary keys because their content (and thus hash) could change, which would disturb the internal hash table. If you attempt to use a mutable object as a key, Python raises a `TypeError`.

---

### 25. Select the correct answer: Which of these is not a built-in data structure (type) in Python?

**A.** List  
**B.** Dictionary  
**C.** Tuple  
**D.** Stack  

**Answer:** D. Stack

**Explanation:** Python’s built-in data structures include lists, dictionaries (`dicts`), tuples, sets, etc. There isn’t a built-in data type called “Stack”. While you can use a list as a stack (using `append()` and `pop()` methods) or import `collections.deque` for stack/queue functionality, “Stack” itself isn’t a native type or keyword. Options A, B, and C (`list`, `dict`, `tuple`) are all fundamental built-in types.

---

### 26. Select the correct answer: What will be the output of the following code snippet?

```python
x = 10
def foo(x):
    x += 5
    return x

print(foo(x), x)
```

**A.** 15 15  
**B.** 15 10  
**C.** 10 15  
**D.** 10 10  

**Answer:** B. 15 10

**Explanation:** When `foo(x)` is called, it takes the value of `x` (which is `10`) and binds it to the parameter `x` inside the function (shadowing the global `x`). Inside `foo`, we do `x += 5`, which does not affect the external `x` – it only changes the local variable `x` in `foo`. The function returns `15`, which gets printed as the first number. The global `x` remains `10`, so that's printed as the second number.

---

### 27. Select the correct answer: Which of the following is the correct syntax for a lambda function that adds two numbers `x` and `y` in Python?

**A.** `lambda x, y: x + y`  
**B.** `lambda (x, y): x + y`  
**C.** `lambda x, y => x + y`  
**D.** `lambda x y: x + y`  

**Answer:** A. `lambda x, y: x + y`

**Explanation:** The correct syntax for an anonymous lambda function in Python uses the form `lambda parameters: expression`. Option A is the proper syntax, taking `x` and `y` as arguments and returning `x + y`. Other options contain invalid syntax.

---

### 28. Select the correct answer: What is the result of the expression `2 ** 3 ** 2` in Python?

**A.** 64  
**B.** 512  
**C.** 16  
**D.** SyntaxError  

**Answer:** B. 512

**Explanation:** Python’s exponentiation operator `**` is right-associative, meaning the expression is evaluated as `2 ** (3 ** 2)`. First, `3 ** 2` is `9`, then `2 ** 9` evaluates to `512`. Option A (64) would be the result if the expression were grouped as `(2 ** 3) ** 2`, but that’s not how Python parses it by default. There is no syntax error here, and the answer is not 16 (which would correspond to `2 ** 3 * 2` or something different). This question tests understanding of operator precedence/associativity.

---

### 29. Select all that apply: Which of the following Python types are immutable? (Select all that apply.)

**A.** list  
**B.** tuple  
**C.** str (string)  
**D.** set  

**Answer:** B and C are correct (tuple and str are immutable).

**Explanation:**
- **Tuple:** Immutable – once created, its elements cannot be changed or reassigned.
- **Str (string):** Immutable – any operation that seems to modify a string actually creates a new string.
- **List:** Mutable – lists can have their elements changed, removed, or new elements appended.
- **Set:** Mutable – sets allow adding or removing elements. (There is a `frozenset` type that is immutable, but the normal set is mutable.)

---

### 30. Select all that apply: In Python, some values are considered “falsy,” meaning they evaluate to False in a boolean context. Which of the following values are falsy? (Select all that apply.)

**A.** `0`  
**B.** `""`  
**C.** `[]`  
**D.** `"False"`  

**Answer:** A, B, and C are falsy.
**Explanation:**
- The number 0 (of any numeric type, e.g., 0, 0.0) is falsy.
- Empty sequences or collections like "" (empty string), [] (empty list), () (empty tuple), {} (empty dict), and set() - (empty set) are falsy.
- None is also falsy.
- The string "False" (option D) is a non-empty string, which is truthy despite its content. Any non-empty string will evaluate to True in a boolean context, so the word "False" as text is actually True when checked as a boolean.

---

### 31. Select all that apply: Which of the following are valid Python loop constructs/syntax? (Select all that apply.)

**A.** `for i in range(5): ...`  
**B.** `for(int i=0; i<5; i++): ...`  
**C.** `while x < 5: ...`  
**D.** `repeat until x == 5: ...`  

**Answer:** A and C are valid.

**Explanation:**  
- Option A is the standard Python `for` loop syntax, which iterates over an iterable (in this case, `range(5)` produces 0 through 4).
- Option C is the Python `while` loop syntax, which repeats as long as the condition (`x < 5`) is `True`.
- Option B is using a C-style `for` loop syntax, which is not valid in Python – Python doesn’t use that syntax or the `++` operator.
- Option D is pseudocode style; Python has no `repeat ... until` loop. (Python’s loops are `for ... in ...` and `while`, possibly with `break` for early exit.)

---

### 32. Select all that apply: Which of the following are Python keywords? (Select all that apply.)

**A.** `def`  
**B.** `lambda`  
**C.** `var`  
**D.** `yield`  

**Answer:** A, B, and D are keywords.

**Explanation:**  
- `def` is a keyword used to define functions.
- `lambda` is a keyword used to define anonymous functions.
- `yield` is a keyword used inside generators to produce a value and pause the function.
- `var` is not a Python keyword. Some other languages use `var` to declare variables, but Python has no need for a variable declaration keyword.

---

### 33. Complete the code: Fill in the blank to print the number of items in the list `my_list` using a built-in function.

```python
my_list = [2, 4, 6, 8]
# Print the number of elements in my_list
print( ______________ )
```

**Answer:**

```python
print(len(my_list))
```

**Explanation:** The built-in function `len()` returns the length of a sequence or collection. Here, `len(my_list)` gives the number of elements in the list (which is 4). Using `len` is the idiomatic way to get sizes in Python.

---

### 34. Complete the code: Use a dictionary comprehension to create a dictionary `squares` that maps numbers 1 through 3 to their squares.

```python
# Create a dict mapping 1->1, 2->4, 3->9
squares = { i: ____________ for i in range(1, 4) }
```

**Answer:**

```python
squares = { i: i**2 for i in range(1, 4) }
```

**Explanation:** Dictionary comprehensions use the syntax `{key: value for ... in ...}`. In this case, for each `i` in 1, 2, 3, we map `i` to `i**2`. The resulting dictionary would be `{1: 1, 2: 4, 3: 9}`.

---

### 35. Complete the code: Python allows swapping two variables in one line without using a temporary variable. Fill in the blank to swap `a` and `b`.

```python
a = 5
b = 7
# Swap a and b
a, b = ______________
print(a, b)  # Expected output: 7 5
```

**Answer:**

```python
a, b = b, a
```

**Explanation:** Python’s tuple packing and unpacking make it easy to swap variables without needing a temporary variable.

---

### 36. Complete the code: Write a generator expression to generate the squares of even numbers from 0 to 10 (inclusive). Fill in the blank in the generator expression.

```python
# Generator for squares of even numbers from 0 to 10
gen = ( x**2 for x in range(11) if ________________ )
print(list(gen))  # Expected output: [0, 4, 16, 36, 64, 100]
```

**Answer:**

```python
gen = ( x**2 for x in range(11) if x % 2 == 0 )
```

**Explanation:** This generator expression iterates `x` from 0 to 10 and uses `if x % 2 == 0` to filter only even numbers.

---

### 37. Identify and fix the error: The following code is intended to print a message if `x` is 5, but it has a syntax error. What is wrong?

```python
x = 5
if x == 5
    print("x is 5")
```

**Answer:** It’s missing a colon at the end of the `if` statement. It should be:

```python
if x == 5:
    print("x is 5")
```

**Explanation:** In Python, control structures (`if`, `for`, `while`, function definitions, etc.) require a colon (`:`) at the end of the header line to indicate the start of the indented block.

---

### 38. Identify and fix the error: You have a list and attempt to use a method to add an element, but it’s causing an `AttributeError`. What is the problem in the code below and how can it be corrected?

```python
my_list = [1, 2, 3]
my_list.push(4)  # Error here
```

**Answer:** The list method is named incorrectly. Python lists use `append()` to add an element, not `push()`. It should be:

```python
my_list.append(4)
```

**Explanation:** Python lists do not have a `push()` method; the correct method to add an element to the end of a list is `append()`.

---

### 39. Identify and fix the error: The code below tries to modify a tuple, resulting in an error. How can this be fixed?

```python
t = (10, 20, 30)
t[1] = 99  # trying to change the second element
```

**Answer:** The error is due to trying to modify an immutable tuple. Tuples cannot be changed in place. To “modify” it, you must create a new tuple. For example:

```python
t = (10, 20, 30)
t = t[0], 99, t[2]  # create a new tuple with the desired value
```

Alternatively, use a list instead of a tuple if mutability is needed.

**Explanation:** Tuples are immutable, so any assignment to `t[1]` will cause a `TypeError`. If a mutable sequence is needed, use a list instead (`my_list = [10,20,30] then my_list[1] = 99`).

---


### 40. Identify and fix the error: The code below attempts to copy a list but ends up modifying the original list as well. What went wrong and how can you fix it?

```python
original = [1, 2, 3]
copy = original
copy.append(4)
print(original)  # Expected [1, 2, 3], got [1, 2, 3, 4]
```

**Answer:** The code assigns `copy` as a reference to the same list as `original`, so they both refer to one list. To actually copy the list, create a new list with the same contents. For example:

```python
copy = original[:]          # slicing to create a shallow copy
# or use copy = original.copy()
```

Now `copy.append(4)` will not affect `original`.

**Explanation:** In Python, variables hold references to objects. Doing `copy = original` makes `copy` point to the same list object as `original`. Thus, `append(4)` through `copy` modifies that single list. To fix this, you need to create a separate list object with the same content. Common ways are slicing (`list[:]`), the `list()` constructor (`list(original)`), or the `copy()` method. After copying, modifying one list won’t affect the other. This is an important concept when working with mutable objects.

---

## Topic 3: Reliability (Robustness, Exception Handling & Debugging)

This section focuses on writing robust Python code: handling errors and exceptions properly, writing tests, and debugging. The questions cover best practices to make code reliable and maintainable, from basic exception handling to more advanced debugging and testing concepts.

---

### 41. True or False: Using a bare `except:` (catching all exceptions indiscriminately) is considered good practice in Python error handling.

**Answer:** False.

**Explanation:** A bare `except:` will catch every exception, including ones you might not intend to catch (like keyboard interrupts or system exit events). This can make bugs harder to find and handle because it swallows exceptions indiscriminately. Best practice is to catch specific exceptions that you expect and know how to handle. For example, catch `ValueError` or `KeyError` specifically, or at least use `except Exception:` (which still skips system-exiting exceptions). Catching all exceptions without distinction is generally discouraged unless you re-raise or handle them in a very controlled manner.

---

### 42. True or False: A `finally` clause in a `try/except` block will always execute, regardless of whether an exception was raised or handled.

**Answer:** True.

**Explanation:** The `finally` block is guaranteed to run after the `try` (and any `except`) blocks, whether an exception occurred or not. This makes `finally` ideal for cleanup actions like closing files or releasing resources, as it runs no matter what. The only situations where `finally` might not run are extreme cases like the program being abruptly terminated. In normal execution flow (even if you `return` or `break` inside `try/except`), the `finally` block executes. This reliability of `finally` is a key feature in writing robust code.

---

### 43. True or False: Using `assert` statements is not recommended for validating function arguments from external users, because assertions can be disabled at runtime.

**Answer:** True.

**Explanation:** The `assert` statement is meant for internal self-checks (conditions that should always be true if the code is correct). They can be globally disabled by running Python with the `-O` (optimize) flag, which removes `assert` statements. Therefore, you should not rely on `assert` for critical runtime validation (especially for user inputs or function arguments in production code). Instead, raise appropriate exceptions (like `ValueError`) for actual runtime validation. Assertions are better used to catch programming errors during development (for instance, checking invariants).

---

### 44. True or False: Generously using global variables in a program makes it easier to ensure the code is reliable and free of bugs.

**Answer:** False.

**Explanation:** Overusing global variables is generally a poor practice for reliability. Global state can be modified from many places, making the program’s behavior harder to predict and bugs harder to track down. It can lead to unintentional interactions between different parts of the code. Instead, it’s better to encapsulate state within functions or classes, and pass needed data as parameters or return values. If global variables are used, they should be limited and managed carefully. Minimizing side effects and shared mutable state tends to result in more robust, maintainable code.

---

### 45. Select the correct answer: Which exception is raised when you try to access a list index that is out of range?

**A.** `IndexError`  
**B.** `KeyError`  
**C.** `ValueError`  
**D.** `TypeError`  

**Answer:** A. `IndexError`

**Explanation:** An `IndexError` is raised when a sequence subscript is out of bounds — for example, accessing `my_list[10]` when the list has only 5 elements. `KeyError` is for invalid keys in mappings (like accessing a non-existent key in a `dict`), `ValueError` is for operations with valid type arguments but inappropriate values, and `TypeError` is for operations applied to an object of an inappropriate type.

---

### 46. Select the correct answer: What is a best practice for handling exceptions in Python?

**A.** Catch and suppress (ignore) all exceptions to prevent program crashes.  
**B.** Catch only the exceptions you expect and know how to handle.  
**C.** Use exceptions for general flow control instead of `if/else`.  
**D.** Don’t use `try/except` at all; let the program crash on errors.  

**Answer:** B. Catch only the exceptions you expect and know how to handle.

**Explanation:** Best practice is to anticipate specific errors and handle them gracefully, while not interfering with exceptions you don’t know how to handle.

---

### 47. Select the correct answer: Which module in the Python standard library is commonly used for writing unit tests?

**A.** `unittest`  
**B.** `pytest`  
**C.** `nose`  
**D.** `selenium`  

**Answer:** A. `unittest`

**Explanation:** The `unittest` module (sometimes referred to as “PyUnit”) is the built-in framework for writing unit tests in Python.

---

### 48. Select the correct answer: Consider the following code. What will it output when executed?

```python
try:
    print("a")
    raise Exception("boom")
    print("b")
except Exception as e:
    print("c")
finally:
    print("d")
```

**A.** `a b c d`  
**B.** `a c d`  
**C.** `a d c`  
**D.** `c d`  

**Answer:** B. The output will be:

```
a  
c  
d  
```

**Explanation:** Here’s the flow: The `try` block prints `"a"`, then raises an `Exception`. Once the exception is raised, the rest of the `try` block (printing `"b"`) is skipped. The control goes to the `except Exception as e:` block, which prints `"c"`. After handling the exception, the `finally` block executes and prints `"d"`.

---

### 49. Select all that apply: Which of the following are built-in exception types in Python? (Select all that apply.)

**A.** `NameError`  
**B.** `TypeError`  
**C.** `ValueError`  
**D.** `SegmentationFault`  

**Answer:** A, B, and C are built-in exceptions.

**Explanation:**
- `NameError` is raised when you try to use a variable or name that hasn’t been defined in that scope.
- `TypeError` is raised when an operation or function is applied to an object of inappropriate type.
- `ValueError` is raised when an operation or function receives an argument of the right type but an inappropriate value.
- `SegmentationFault` is **not** a Python exception; it’s a low-level crash error typically coming from the C layer or OS when a program accesses invalid memory.

---


### 50. Select all that apply: What are some practices or tools that help in writing bug-free, reliable code in Python? (Select all that apply.)

**A.** Writing unit tests to cover your code’s functionality.  
**B.** Using assertions to catch internal errors during development.  
**C.** Using a debugger or print statements to trace and fix issues.  
**D.** Catching and ignoring all exceptions so the program never crashes.  

**Answer:** A, B, and C are good practices/tools.

**Explanation:**  
- **Unit tests (A):** Writing tests (using frameworks like `unittest` or `pytest`) helps verify that your code works correctly and catches regressions when making changes.
- **Assertions (B):** Asserts help catch conditions that “should never happen” during development, identifying logic mistakes early.
- **Debuggers/print (C):** Using the Python debugger (`pdb`) or adding print/log statements are common ways to trace program execution and inspect state.
- **Ignoring all exceptions (D):** This is a bad practice. It prevents crashes but can mask problems, leading to unpredictable behavior.

---

### 51. Select all that apply: You opened a file for processing. Which of the following approaches ensure that the file is properly closed after operations are done? (Select all that apply.)

**A.** Using a `try/finally` block where you call `file.close()` in the `finally` clause.  
**B.** Using the `with open(...) as f:` context manager to handle opening and closing.  
**C.** Relying on Python’s garbage collector to eventually close the file.  
**D.** Opening the file with mode "x" to guarantee closing.  

**Answer:** A and B are correct.

**Explanation:**  
- **`try/finally` (A):** Ensures that `file.close()` is called regardless of exceptions.
- **`with` statement (B):** The Pythonic way to handle files; ensures automatic closing.
- **Garbage collector (C):** Unreliable for timely closure, as collection timing varies.
- **File mode "x" (D):** Has nothing to do with automatic closing; it only affects file creation behavior.

---

### 52. Select all that apply: Which of the following statements about exception handling in Python are true? (Select all that apply.)

**A.** You can have an `else` clause after a `try/except` which runs if no exception occurred in the `try`.  
**B.** Raising an exception in Python uses the `raise` keyword.  
**C.** If an exception isn’t caught in the current function, it propagates upward (to the caller).  
**D.** The `finally` block only runs if an exception was raised in the `try` block.  

**Answer:** A, B, and C are true.

**Explanation:**  
- **Else clause (A):** Runs if no exception occurs in the `try` block.
- **Raise keyword (B):** Used to manually throw exceptions, e.g., `raise ValueError("Bad input")`.
- **Exception propagation (C):** Exceptions bubble up the call stack if not caught.
- **Finally block (D):** Runs **regardless** of whether an exception was raised or not, making D false.

---

### 53. Complete the code: The following code is supposed to handle invalid integer conversion. Fill in the blank to catch the specific exception when conversion fails.

```python
try:
    num = int(user_input)
    print("Valid integer:", num)
except ________________:
    print("Input is not a valid integer.")
```

**Answer:**

```python
except ValueError:
```

**Explanation:** `int("abc")` raises a `ValueError`, so catching `ValueError` ensures that only this expected exception is handled.

---

### 54. Complete the code: Raise an exception if a condition is not met.

```python
def set_positive(x):
    if x <= 0:
        ________________ ValueError("x must be positive")
```

**Answer:**

```python
        raise ValueError("x must be positive")
```

**Explanation:** `raise` is used to manually throw an exception, halting execution.

---

### 55. Complete the code: Assert that `result` is non-negative.

```python
result = compute_value()
____________ result >= 0, "Result should not be negative"
```

**Answer:**

```python
assert result >= 0, "Result should not be negative"
```

**Explanation:** `assert` checks conditions during development. If `result < 0`, an `AssertionError` is raised.

---

### 56. Complete the code: Use a context manager to read from a file.

```python
# Read contents of "data.txt" into data
with open("data.txt", "r") __ f:
    data = f.read()
```

**Answer:**

```python
with open("data.txt", "r") as f:
```

**Explanation:** The `with` statement ensures that the file is automatically closed.

---

### 57. Identify and fix the error: The function below has a common bug related to default argument values.

```python
def add_to_list(element, lst=[]):
    lst.append(element)
    return lst
```

**Answer:** The default value `[]` is evaluated once, causing unintended sharing between function calls. Fix:

```python
def add_to_list(element, lst=None):
    if lst is None:
        lst = []
    lst.append(element)
    return lst
```

**Explanation:** Using `None` ensures each function call gets a fresh list.

---

### 58. Identify and fix the error: The code below fails with an `UnboundLocalError`.

```python
count = 0
def increment():
    count += 1
    return count
```

**Answer:** Python treats `count` as local due to assignment, leading to an error. Fix:

```python
count = 0
def increment():
    global count
    count += 1
    return count
```

**Explanation:** Using `global count` tells Python to modify the global variable instead of treating it as a new local variable.

---

### 59. Identify and fix the error: The exception handling is too broad.

```python
try:
    result = risky_operation()
except:
    print("An error occurred")
```

**Answer:** A bare `except:` catches all exceptions (including system exit events). Instead, catch specific exceptions:

```python
try:
    result = risky_operation()
except ValueError as e:
    print("Invalid value:", e)
except IOError as e:
    print("IO error:", e)
```

**Explanation:** Catching only expected exceptions improves debugging and prevents masking real issues. If catching all exceptions is necessary, use `except Exception:` to avoid catching system-exiting exceptions like `KeyboardInterrupt`.

---

### 60. Identify and fix the error: The following code opens a file and reads data but never closes the file. Why is this a problem, and how can it be fixed?

```python
f = open("data.txt", "r")
data = f.read()
# ... (no close called)
```

**Answer:** Not closing the file can lead to resource leaks (file descriptors left open). The fix is to ensure the file is closed after use. For example:

```python
f = open("data.txt", "r")
try:
    data = f.read()
finally:
    f.close()
```

Better yet, use a `with` statement:

```python
with open("data.txt", "r") as f:
    data = f.read()
```

This automatically closes the file.

**Explanation:** Each open file uses system resources. If you forget to close files, you might hit limits on how many files can be open, and data might not be flushed properly. Although Python will close the file when the file object is garbage-collected, it’s not deterministic when that happens. The safe approach is to explicitly close the file. The `with` statement is the Pythonic way to handle this, as it guarantees closure. The provided fix with `try/finally` also ensures `f.close()` runs. Both solutions prevent the resource leak and potential issues like locked files or running out of file handles.

