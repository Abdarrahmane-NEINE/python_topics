# NumPy Basics Quiz (Beginner Level)

## Quiz Questions

### True/False
- **True/False:** NumPy uses 0-based indexing (the first element is at index 0).
- **True/False:** Slicing a NumPy array (e.g. `arr[1:4]`) returns a copy of the data by default.
- **True/False:** NumPy operations are generally faster than pure Python loops for numerical computations.
- **True/False:** A NumPy array can contain elements of different data types at the same time.
- **True/False:** Using the `*` operator on two NumPy arrays performs element-wise multiplication.

### Select the Correct Response (Single Choice)
- Which of the following will correctly create a NumPy array containing `[1, 2, 3]`?
  - a. `np.array([1, 2, 3])`
  - b. `np.array(1, 2, 3)`
  - c. `np.array[1, 2, 3]`
  - d. `np.make_array([1, 2, 3])`

- Given `arr = np.array([10, 20, 30, 40])`, what is the result of `arr[1]`?
  - a. 10
  - b. 20
  - c. 30
  - d. 40

- If `arr = np.array([0, 1, 2, 3, 4, 5])`, what is `arr[2:5]`?
  - a. `[2, 3, 4]`
  - b. `[2, 3, 4, 5]`
  - c. `[3, 4, 5]`
  - d. `[0, 1, 2]`

- Which attribute of a NumPy array `arr` gives the total number of elements in the array?
  - a. `arr.size`
  - b. `arr.shape`
  - c. `arr.len`
  - d. `arr.length`

- What will be the shape of the array created by `np.ones((2, 3))`?
  - a. `(2, 3)`
  - b. `(3, 2)`
  - c. `(6,)`
  - d. `(2, 3, 1)`

- For two NumPy arrays `a = np.array([1, 2, 3])` and `b = np.array([4, 5, 6])`, what is the result of `a + b`?
  - a. `[5, 7, 9]`
  - b. `[1, 2, 3, 4, 5, 6]`
  - c. `[4, 10, 18]`
  - d. It will raise a shape mismatch error.

### Multiple Correct Answers (Select all that apply)
- Which of the following are reasons why NumPy can be faster than using Python lists for numerical operations?
  - a. NumPy uses optimized C/C++ (or Fortran) code under the hood for array operations.
  - b. NumPy arrays store data in contiguous memory, which improves cache efficiency.
  - c. NumPy automatically uses multiple CPU cores for every array operation.
  - d. NumPy vectorized operations avoid the overhead of explicit Python loops.
  - e. NumPy stores each element as a full Python object with type information (just like a Python list).

- Which of the following array operations will not produce an error due to shape mismatch (i.e. they are valid due to broadcasting)?
  - a. Adding an array of shape `(3,)` to an array of shape `(3, 4)`
  - b. Adding an array of shape `(1, 4)` to an array of shape `(3, 4)`
  - c. Adding an array of shape `(2, 3)` to an array of shape `(3, 3)`
  - d. Adding an array of shape `(3, 1)` to an array of shape `(3, 3)`
  - e. Adding an array of shape `(3,)` to an array of shape `(3, 1)`

- Which of the following statements about NumPy arrays are true?
  - a. NumPy arrays are 0-indexed (the first element is index 0).
  - b. Slicing a NumPy array returns a view of the original data (no copy) in most cases.
  - c. You can reshape a NumPy array to a new shape as long as the total number of elements remains the same.
  - d. You can append a new element to a NumPy array in-place (just like using `list.append` on a Python list).
  - e. Multiplying two NumPy arrays with `*` yields an element-wise product of the arrays.

### Complete the Code
- Fill in the blank to create a NumPy array of even numbers from 0 to 8 (inclusive) using `np.arange`.

```python
import numpy as np  
even_arr = np.arange(___)
```

- Complete the code to reshape the 1D array into a 2D array of shape `(2, 3)`.

```python
arr = np.array([0, 1, 2, 3, 4, 5])  
arr2d = arr.reshape(___)
```

- Complete the code to compute the element-wise product of two arrays `a` and `b`.

```python
a = np.array([1, 2, 3])  
b = np.array([4, 5, 6])  
product = _____
```

- Fill in the comparison operator to select all elements of `arr` that are greater than 5.

```python
arr = np.array([3, 6, 1, 7, 2, 9])  
mask = arr __ 5  
result = arr[mask]
```

### Correct the Code
- The following code is intended to create a NumPy array `[1, 2, 3]` but it contains an error. What is the correction?

```python
import numpy as np  
arr = np.array(1, 2, 3)  # Intended to create array [1, 2, 3]  
```

- The code below attempts to create a 2x3 array of ones, but it is incorrect. How should it be fixed?

```python
import numpy as np  
ones_arr = np.ones[2, 3]  # Intended to create a 2x3 array of ones  
```

## Answers
- True.
- False. (NumPy slicing returns a view, not a copy, by default.)
- True.
- False. (All elements of a NumPy array must be of the same data type.)
- True.

- a. `np.array([1, 2, 3])`
- b. `20`
- a. `[2, 3, 4]`
- a. `arr.size`
- a. `(2, 3)`
- a. `[5, 7, 9]`
- a, b, d.
- b, d, e.
- a, b, c, e.
- `(0, 10, 2)` – e.g. `even_arr = np.arange(0, 10, 2)`.
- `(2, 3)` – e.g. `arr2d = arr.reshape(2, 3)`.
- `a * b` – using `*` performs element-wise multiplication.
- `>` – e.g. `mask = arr > 5`.
- Use brackets to pass a list: `arr = np.array([1, 2, 3])`.
- Call the function with a tuple shape: `ones_arr = np.ones((2, 3))`.

