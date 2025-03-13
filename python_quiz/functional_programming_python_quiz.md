## Python Functional Programming Quiz (Lambdas, Sorting, Map, Filter)

Below is a set of 10 quiz questions (with answers and explanations) focused on Python lambda functions, sorting with custom keys, the use of `map()` and `filter()`, and related functional programming concepts.

---

### 1. True or False:
A Python lambda function can contain multiple statements, just like a normal function defined with `def`.

**Answer:** False

**Explanation:** Lambda functions in Python are limited to a single expression. Unlike a `def` function, a lambda cannot contain multiple statements or commands. It evaluates and returns the result of one expression only. This means you cannot have assignments, loops, or multiple actions in a single lambda. For any functionality that requires more than one expression or statement, a normal function defined with `def` is more appropriate.

---

### 2. Multiple Choice:
Which of the following is a correct way to define a lambda function that adds 5 to its input?

**A.** `add_five = lambda x: x + 5`  
**B.** `add_five = lambda x: return x + 5`  
**C.** `add_five = lambda: x + 5`  
**D.** `add_five = lambda x: x + 5; print(x)`  

**Answer:** A. `add_five = lambda x: x + 5`

**Explanation:**
- **Option A** is the correct syntax for a lambda that takes one parameter `x` and returns `x + 5`.
- **Option B** is incorrect because you cannot use a `return` statement inside a lambda (the lambda automatically returns the expression’s value).
- **Option C** is invalid because the lambda has no parameter but uses `x` in the expression.
- **Option D** is incorrect because you cannot place two expressions/statements separated by `;` in a lambda (only one expression is allowed).

---

### 3. Multiple Choice:
Which of the following is **not** true about Python lambda functions?

**A.** Lambdas are anonymous functions expressed as a single expression.  
**B.** A lambda can be assigned to a variable and used like a normal function.  
**C.** Lambda functions can include multiple statements separated by semicolons.  
**D.** Lambdas are often used as short callback functions for `map()`/`filter()`/`sorted()`.  

**Answer:** C. Lambda functions can include multiple statements separated by semicolons.

**Explanation:**
- **Option C** is not true – lambda functions cannot include multiple statements (even separated by semicolons). They are limited to a single expression.
- **Options A, B, and D** are true: Lambdas create anonymous functions, you can assign a lambda to a variable (though if you are naming it, `def` is usually preferable), and they are commonly used for short callback or key functions in constructs like `map()`, `filter()`, and `sorted()`.

---

### 4. True or False:
It is recommended to use a lambda function for any complex operation instead of defining a function with `def`, since lambdas make the code shorter.

**Answer:** False

**Explanation:** Lambdas are best used for short, simple functions – typically when a function is needed as an argument (for example, a key function or a simple transform in `map()`/`filter()`). For complex operations or when you need clarity (including documentation or multiple steps), a regular function defined with `def` is preferred. Overusing lambdas for complex logic can make code harder to read and debug.

---

### 5. Code Output – Multiple Choice:
What will be the output of the following code snippet?

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)
print([f() for f in funcs])
```

**A.** `[0, 1, 2]`  
**B.** `[2, 2, 2]`  
**C.** `[None, None, None]`  
**D.** `[0, 0, 0]`  

**Answer:** B. `[2, 2, 2]`

**Explanation:**
- The code appends three lambda functions to the list `funcs`. Each lambda is defined as `lambda: i`, which returns the value of `i` when called.
- However, due to how closures work in Python, all the lambdas capture the same variable `i` (which is mutable and changes during the loop).
- By the time the list comprehension calls each `f()`, the loop has completed and `i` is left at its final value (`2` after `range(3)` finishes).
- Therefore, each lambda returns `2`, producing `[2, 2, 2]`.

To fix this issue, you can use a **default argument** to capture the current value of `i` at each iteration:

```python
for i in range(3):
    funcs.append(lambda i=i: i)
```

Now, each lambda has its own default `i` value (`0`, then `1`, then `2`), and the list comprehension will output `[0, 1, 2]` as intended.

---

### 6. True or False:
Calling the list’s `sort()` method in Python (e.g., `my_list.sort()`) will return the sorted list.

**Answer:** False

**Explanation:**
- The `list.sort()` method **sorts the list in place** and **returns `None`**.
- If you need a sorted result **without modifying** the original list, use the built-in `sorted()` function, which returns a new sorted list.

Example:

```python
numbers = [3, 1, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3]
print(numbers.sort())  # Output: None
```

---

### 7. Code Completion:
Fill in the blank to sort the list `words` by the length of each word, from shortest to longest.

```python
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=__________)
print(sorted_words)
```

**Answer:**

```python
sorted_words = sorted(words, key=len)
```

**Explanation:**
- The built-in function `len` can be used as the `key` function to sort by length.
- This will produce `['date', 'apple', 'banana', 'cherry']` because "date" (4 letters) is shortest, followed by "apple" (5), "banana" (6), and "cherry" (6).
- Using `key=lambda x: len(x)` would achieve the same result but is more verbose.

---

## Python Functional Programming Quiz (Sorting, Map, Filter)

### 8. Multiple Choice:
You have a list of tuples: `items = [(1, 'a'), (3, 'c'), (2, 'b')]`. How would you sort this list by the second element of each tuple (the letter) in ascending alphabetical order?

**A.** `sorted(items, key=lambda x: x[1])`  
**B.** `sorted(items, key=lambda x: x[0])`  
**C.** `items.sort(key=lambda x: x[1]); items`  
**D.** `sorted(items, key=item[1])`  

**Answer:** A. `sorted(items, key=lambda x: x[1])`

**Explanation:** To sort by the second element of each tuple, use the `key` parameter with a function (or lambda) that extracts the second element (`x[1]`).
- **Option A** correctly returns a new sorted list: `[(1, 'a'), (2, 'b'), (3, 'c')]`.
- **Option B** sorts by the first element (the numbers) instead.
- **Option C** is nearly correct, but `items.sort(key=lambda x: x[1])` sorts the list in place and returns `None`.
- **Option D** is invalid syntax; you cannot use `item[1]` directly as a key without a lambda or function.

---

### 9. Code Completion:
Fill in the blank to sort the list `words` by the length of each word, from shortest to longest.

```python
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=__________)
print(sorted_words)
```

**Answer:**

```python
sorted_words = sorted(words, key=len)
```

**Explanation:** The built-in function `len` can be used as the `key` function to sort by length. This will produce `['date', 'apple', 'banana', 'cherry']` because "date" (4 letters) is shortest, followed by "apple" (5), "banana" (6), and "cherry" (6).

---

### 10. Multiple Choice:
Which of the following snippets correctly sorts a dictionary `d` by its values in ascending order? (Assume `d` is a regular dict mapping keys to values.)

**A.** `sorted(d)`  
**B.** `sorted(d.values())`  
**C.** `sorted(d.items(), key=lambda x: x[1])`  
**D.** `d.sort(key=lambda item: item[1])`  

**Answer:** C. `sorted(d.items(), key=lambda x: x[1])`

**Explanation:**
- **Option C** sorts dictionary items by value.
- **Option A** sorts keys, not values.
- **Option B** sorts values but loses key-value pairs.
- **Option D** is invalid since dictionaries don’t have a `sort()` method.

---

### 11. True or False:
Python’s built-in sorting (`sorted()` or `list.sort()`) is stable, meaning that if two items have equal keys, their original order is preserved in the sorted output.

**Answer:** True

**Explanation:** Python’s sorting algorithm (Timsort) is **stable**. When sorting, if two elements are equal in terms of the sorting key, they will appear in the same order as in the input. This is useful for multi-level sorting.

Example:

```python
people = [("John", 25), ("Alice", 30), ("Bob", 25)]
people.sort(key=lambda x: x[1])  # Sort by age
people.sort(key=lambda x: x[0])  # Then sort by name (stable)
print(people)
```

The stable sort keeps `("John", 25)` before `("Bob", 25)`, preserving their original relative order.

---

### 12. True or False:
In Python 3, the `map()` function returns a list of results.

**Answer:** False

**Explanation:** In Python 3, `map()` returns a **lazy iterator** (`map` object), not a list. To convert it into a list, use:

```python
list(map(str.upper, ["a", "b", "c"]))  # Output: ['A', 'B', 'C']
```

This lazy nature means `map()` computes results **on-demand**, improving memory efficiency.

---

### 13. Multiple Choice:
What will the following code print?

```python
result = map(lambda x: x**2, [1, 2, 3, 4])
print(result)
```

**A.** `<map object at 0x...>` (some map object representation)  
**B.** `[1, 4, 9, 16]`  
**C.** `None`  
**D.** An error is raised at runtime.  

**Answer:** A. `<map object at 0x...>`

**Explanation:**
- `map()` returns a **map object** (a lazy iterator).
- Printing `result` directly **does not iterate** over the values, so the output will be something like `<map object at 0x...>`.
- To get `[1, 4, 9, 16]`, convert it to a list first: `print(list(result))`.
- No error occurs, so Option D is incorrect.

---

### 14. True or False:
The list comprehension `[f(x) for x in iterable]` is generally equivalent to `list(map(f, iterable))` in terms of the final result (for the same function `f`).

**Answer:** True

**Explanation:**
A list comprehension that applies a function `f` to each element of an iterable produces the same list as using `map(f, iterable)` and converting to a list. For example:

```python
[x*2 for x in nums]  # Equivalent to list(map(lambda x: x*2, nums))
```

Both approaches create a transformed list. However, key differences include:
- **Readability:** List comprehensions are generally preferred for simple cases.
- **Iterator vs List:** `map()` returns a lazy iterator in Python 3, whereas list comprehensions generate a list immediately.

---

### 15. Code Output – Multiple Choice:
What will be the result of the following code?

```python
numbers = [1, 2, 3, 4]
letters = ['a', 'b', 'c']
result = list(map(lambda x, y: str(x) + y, numbers, letters))
print(result)
```

**A.** `['1a', '2b', '3c', '4None']`  
**B.** `['1a', '2b', '3c']`  
**C.** `['1a', '2b', '3c', '4']`  
**D.** `['1a', '2b', '3c', '4c']`  

**Answer:** B. `['1a', '2b', '3c']`

**Explanation:**
- The `map()` function stops when the shortest iterable is exhausted.
- Since `letters` has only three elements, mapping stops after `('3', 'c')`.
- Option A is incorrect because `map()` does not automatically pair missing values with `None`.

---

### 16. True or False:
Calling `filter(None, sequence)` will remove all “falsy” values (`0`, `''`, `None`, `False`) from the given sequence.

**Answer:** True

**Explanation:**
If `None` is passed as the function, `filter()` uses the identity function, keeping only truthy elements. Example:

```python
list(filter(None, [0, 1, '', 'hello', None, 3]))  # Output: [1, 'hello', 3]
```

This is equivalent to `[x for x in sequence if x]`.

---

### 17. Code Output:
What will the following code output?

```python
nums = [1, 2, 3, 4]
filtered = filter(lambda x: x % 2 == 0, nums)
nums.append(6)
print(list(filtered))
```

**Answer:** `[2, 4, 6]`

**Explanation:**
- `filter()` is a lazy iterator and references `nums`.
- When `list(filtered)` is called, it sees the updated `nums` list, which now includes `6`.
- `2, 4, 6` pass the filtering condition.

---

### 18. Code Output:
Consider the following code snippet:

```python
nums = [1, 2, 3]
result = list(filter(print, nums))
print("Result:", result)
```

**Answer:**
```
1
2
3
Result: []
```

**Explanation:**
- `filter(print, nums)` calls `print(x)` for each element.
- `print()` always returns `None`, which is falsy.
- The result list is empty because `filter()` only includes truthy results.

---

### 19. Code Correction:
The following code is intended to get the first even number from a list but does not work. Fix it.

```python
nums = [3, 7, 2, 5]
first_even = filter(lambda x: x % 2 == 0, nums)[0]  # Intended to get the first even number
print(first_even)
```

**Answer:**

```python
first_even = list(filter(lambda x: x % 2 == 0, nums))[0]  # OR
first_even = next(filter(lambda x: x % 2 == 0, nums))
```

**Explanation:**
- `filter()` returns an **iterator**, which is not subscriptable.
- **Solution 1:** Convert `filter()` to a list and index `[0]`.
- **Solution 2:** Use `next()` to efficiently retrieve the first match.

---

### 20. Multiple Choice:
What happens when you try to sort a list in Python 3 that contains mixed incomparable types, for example: `sorted([3, "1", 2])`?

**A.** It returns `[2, 3, "1"]` (numbers sorted before strings).  
**B.** It returns `['1', 2, 3]` (sorted as if all were strings).  
**C.** It raises a `TypeError` at runtime.  
**D.** It sorts the list by type name (e.g., all numbers then all strings).  

**Answer:** C. It raises a `TypeError` at runtime.

**Explanation:**
- Python 3 **does not allow** comparisons between different data types without a key function.
- `sorted([3, "1", 2])` raises: `TypeError: '<' not supported between instances of 'str' and 'int'`.
- To sort mixed types, provide a **key function**:
  ```python
  sorted([3, "1", 2], key=str)  # Sorts as strings: ['1', 2, 3]
  ```

---
### 21. Select the correct answer:
Which built-in method sorts a list in place?

**A.** `sorted(my_list)`  
**B.** `my_list.sort()`  
**C.** `sort(my_list)`  
**D.** `order(my_list)`  

**Answer:** B. `my_list.sort()`

**Explanation:** The `sort()` method is called on the list object and sorts the list in place. In contrast, `sorted(my_list)` returns a new sorted list without modifying the original.

---

### 22. Complete the code:
Fill in the blank so that the `map()` function converts all strings in the list to uppercase.

```python
words = ["python", "quiz", "lambda"]
upper_words = list(map(__________, words))
print(upper_words)  # Expected: ['PYTHON', 'QUIZ', 'LAMBDA']
```

**Answer:**

```python
upper_words = list(map(lambda s: s.upper(), words))
```

**Explanation:** A lambda is used to define an inline function that takes each string `s` and calls its `.upper()` method. Wrapping the `map()` in `list()` converts the returned iterator into a list.

---

### 23. Code Correction:
The following code is intended to filter out even numbers from a list, but it produces an error. Correct it.

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 = 0, numbers))
print(even_numbers)
```

**Answer:**

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Expected: [2, 4, 6]
```

**Explanation:** The error is caused by using the assignment operator (`=`) instead of the equality operator (`==`). Changing `x % 2 = 0` to `x % 2 == 0` fixes the error.

---

### 24. Select all that apply:
Which parameters can you pass to the built-in `sorted()` function in Python 3? (Select all that apply.)

**A.** `key`  
**B.** `reverse`  
**C.** `cmp`  
**D.** `default`  

**Answer:** A and B

**Explanation:**
Python 3’s `sorted()` accepts the parameters `key` (a function to extract a sort key from each element) and `reverse` (a Boolean to reverse the sort order). The `cmp` parameter was removed in Python 3, and there’s no parameter called `default` in `sorted()`.

---

### 25. True or False:
Lambda functions can be assigned to a variable and later invoked like a normal function.

**Answer:** True

**Explanation:** A lambda expression returns a function object that can be assigned to a variable. For example:

```python
f = lambda x: x + 1
print(f(2))  # Output: 3
```

This creates a function that can be called with `f(2)` to return `3`.

---

### 26. Complete the code:
Use the `sorted()` function with a lambda function to sort a list of strings by their length.

```python
words = ["apple", "kiwi", "banana", "cherry"]
sorted_words = sorted(words, key=__________)
print(sorted_words)  # Expected: ['kiwi', 'apple', 'cherry', 'banana']
```

**Answer:**

```python
sorted_words = sorted(words, key=lambda word: len(word))
```

**Explanation:** The `key` parameter accepts a function that extracts a value to be used for sorting. Here, the lambda function returns the length of each word, causing the sort to be based on string length.

---

### 27. Select the correct answer:
What does the `map()` function do in Python?

**A.** It filters items in an iterable based on a condition.  
**B.** It applies a function to every item of an iterable and returns an iterator.  
**C.** It sorts items in an iterable.  
**D.** It reduces an iterable to a single cumulative value.  

**Answer:** B. It applies a function to every item of an iterable and returns an iterator.

**Explanation:** `map()` takes a function and an iterable, applies the function to each element, and returns a map object (an iterator) with the results.

---

### 28. Code Correction:
The following lambda function is intended to compute the cube of a number but is written incorrectly. Fix it.

```python
cube = lambda x: return x ** 3
print(cube(3))
```

**Answer:**

```python
cube = lambda x: x ** 3
print(cube(3))  # Expected output: 27
```

**Explanation:** Lambda functions cannot contain statements like `return`; they must be a single expression. Simply writing `x ** 3` after the colon is the correct syntax.

---

### 29. Select all that apply:
Which statements about the `filter()` function in Python are correct? (Select all that apply.)

**A.** It returns an iterator in Python 3.  
**B.** It applies a function to each item and returns a new list of results.  
**C.** It only includes items for which the provided function returns `True`.  
**D.** If the function is `None`, it filters out items that are false in a Boolean context.  

**Answer:** A, C, and D

**Explanation:**
- **A:** In Python 3, `filter()` returns an iterator rather than a list.
- **C:** It includes only those items for which the lambda (or function) returns `True`.
- **D:** If `None` is passed as the function, `filter()` removes all elements that are false (e.g., empty, zero, or `None`) from the iterable.
- **Option B** is incorrect because `filter()` does not return a list by default in Python 3.

---

### 30. Complete the code:
Use `reduce()` (from the `functools` module) with a lambda to calculate the product of numbers in a list.

```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(__________, numbers)
print(product)  # Expected output: 24
```

**Answer:**

```python
product = reduce(lambda a, b: a * b, numbers)
```

**Explanation:**
- `reduce()` applies the lambda cumulatively to the items of the list, multiplying the numbers together.
- For the list `[1, 2, 3, 4]`, it computes `(((1*2)*3)*4)`, which equals `24`.

---

### 31. Select the correct answer:
What is the purpose of the `key` parameter in the `sorted()` function?

**A.** It determines whether the list is sorted in ascending or descending order.  
**B.** It specifies a function of one argument that is used to extract a comparison key from each list element.  
**C.** It is used to pass additional arguments to the sorting algorithm.  
**D.** It indicates the position of the element in the list to compare.  

**Answer:** B. It specifies a function of one argument that is used to extract a comparison key from each list element.

**Explanation:**
The `key` parameter lets you provide a function that transforms each element before comparisons are made. This is especially useful for sorting by attributes or computed properties.

---

### 32. Code Correction:
The following code is intended to sort a list of dictionaries by the `'age'` key, but it produces an error. Fix it.

```python
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
sorted_people = sorted(people, key=lambda person: person.age)
print(sorted_people)
```

**Answer:**

```python
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
sorted_people = sorted(people, key=lambda person: person["age"])
print(sorted_people)
```

**Explanation:**
Since `people` is a list of dictionaries, you must access the `'age'` value using dictionary indexing (`person["age"]`) rather than attribute notation (`person.age`), which would work only if `person` were an object with an `age` attribute.

---

### 33. True or False:
Lambda functions in Python can contain exception handling (`try`/`except` blocks) within them.

**Answer:** False

**Explanation:**
Lambda functions are limited to a single expression and cannot include statements like `try/except`. If you need exception handling, you must define a regular function using `def`.

---

### 34. Select all that apply:
Which practices help make the use of higher-order functions (like `map()`, `filter()`, and `lambda`) more reliable and readable in your code? (Select all that apply.)

**A.** Writing lambda functions that are pure (no side effects).  
**B.** Using list comprehensions when they improve readability.  
**C.** Keeping lambda expressions simple and avoiding overly complex one-liners.  
**D.** Embedding multiple statements in a lambda for conciseness.  

**Answer:** A, B, and C

**Explanation:**
- **A:** Pure functions (without side effects) are easier to test and debug.
- **B:** When a list comprehension is clearer than a lambda with `map()` or `filter()`, it should be used.
- **C:** Simplicity aids in readability and maintenance.
- **D:** **Incorrect** because lambda functions cannot contain multiple statements. Complex logic should be moved to a named function.

---

### 35. Complete the code:
Chain `filter()` and `map()` in one line to filter out odd numbers from a list and then square the even numbers.

```python
numbers = [1, 2, 3, 4, 5, 6]
result = list(map(________, filter(________, numbers)))
print(result)  # Expected: [4, 16, 36]
```

**Answer:**

```python
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
```

**Explanation:**
- `filter(lambda x: x % 2 == 0, numbers)` selects only the even numbers.
- `map(lambda x: x**2, ...)` squares each even number.
- Wrapping the result in `list()` converts the iterator to a list.

---

### 36. Code Correction:
The following code attempts to sort a list of tuples by their second element using a comparison function (as in Python 2), but it fails in Python 3. Correct it.

```python
data = [(1, 3), (2, 1), (3, 2)]
sorted_data = sorted(data, cmp=lambda a, b: a[1] - b[1])
print(sorted_data)
```

**Answer:**

```python
data = [(1, 3), (2, 1), (3, 2)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Expected: [(2, 1), (3, 2), (1, 3)]
```

**Explanation:**
Python 3 removed the `cmp` parameter from sorting functions. Instead, use the `key` parameter to extract the comparison key—in this case, the second element of each tuple.

---

### 37. Select the correct answer:
Which statement is true regarding variable scope in lambda functions?

**A.** Lambda functions create a new global variable scope.  
**B.** Lambda functions do not capture variables from the surrounding scope.  
**C.** Lambda functions create closures by capturing variables from the surrounding scope by name.  
**D.** Lambda functions require all variables to be passed explicitly as parameters.  

**Answer:** C. Lambda functions create closures by capturing variables from the surrounding scope by name.

**Explanation:**
Lambda functions (like normal functions) form closures. They capture variables from the enclosing scope by name, meaning if the variable’s value changes later, the lambda will see the updated value unless a default is specified.

---
