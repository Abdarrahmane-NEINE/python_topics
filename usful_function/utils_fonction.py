# all function 
numbers = '1 2 4 8 16'
# numbers = '2 4 6 8 10'
numbers = [int(n) for n in numbers.split(" ")]
is_arithmetic = all(numbers[i] - numbers[i - 1] == numbers[1] - numbers[0] for i in range(2, len(numbers)))
is_geometric = False
if 0 not in numbers: 
    is_geometric = all(numbers[i] == numbers[i-1] * (numbers[1]/numbers[0]) for i in range(2,len(numbers)))
print("Arithmetic Progression") if is_arithmetic else print("Geometric Progression") if is_geometric else print("Random")



# map and zip function

# maximum absolute difference between any two consecutive numbers.
numbers = '3 4 34'
# splitting and converting to integers
# the map function applies the int() function to each substring
# *a= unpacks all the integers from the iterator into the list a, similar to a=list(map(int, numbers.split()))
*a,= map(int, numbers.split())
# Computing the maximum absolute difference
# zip(a, a[1:]): creates pairs of consecutive numbers from the list a. For a = [3, 4, 34], the pairs will be: (3, 4) and (4, 34)
print(max(abs(x-y) for x, y in zip(a, a[1:])))
