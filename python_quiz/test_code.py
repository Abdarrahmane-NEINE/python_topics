# class MyClass:
#     items = []            # class-level attribute
#     def add_item(self, item):
#         self.items.append(item)
#         print(self.items)
# m = MyClass()
# m.add_item("test")
# m2 = MyClass()
# m2.add_item("test2")
# class MyClass2:
#     def __init__(self):
#         self.items = []            
#     def add_item(self, item):
#         self.items.append(item)
#         print(self.items)
# m = MyClass2()
# m.add_item("test")
# m2 = MyClass2()
# m2.add_item("test2")


# count = 0
# def increment():
#     print(count)
#     return count + 1

# count = increment()

# print(count)

# from functools import reduce
# import math
# numbers = [1, 2, 3, 4]
# product = reduce(lambda x,y : x * y, numbers)
# product2 = math.prod(numbers)
# print(product, product2)  # Expected output: 24


# numbers = [1, 2, 3, 4, 5, 6]
# result = list(map(lambda i: i*i, filter(lambda i:i%2==0, numbers)))
# print(result)  # Expected: [4, 16, 36]

# data = [(1, 3), (2, 1), (3, 2)]
# sorted_data = sorted(data, key=lambda k: k[1])
# print(sorted_data)

# words = ["pear", "apple", "fig", "banana", "kiwi"]
# sorted_words = sorted(words, key=lambda k:(len(k), k))
# print(sorted_words)  # Expected: ['fig', 'kiwi', 'pear', 'apple', 'banana']

# data = [1, "a", 2, "b", 3.5, None]
# nums = list(filter(lambda x: type(x) == int or type(x) == float, data))
# print(nums)  # Expected: [1, 2, 3.5]


# data = [1, "a", 2, "b", 3.5, None]
# nums = list(filter(lambda x: isinstance(x, int) or isinstance(x, float), data))
# print(nums)  # Expected: [1, 2, 3.5]
# print(type(3) == int)
# print(isinstance(3, int))
# funcs = []
# for i in range(3):
#     funcs.append(lambda: i)
# print([f() for f in funcs])
# funcs = []
# for i in range(3):
#     funcs.append(lambda i=i: i)
# print([f() for f in funcs])

# people = [("John", 25), ("Alice", 30), ("Bob", 25)]
# # Sort by age (second element)
# people.sort(key=lambda x: x[1])  
# print(people)
# # Now stable sort by name (first element)
# people.sort(key=lambda x: x[0])  
# print(people)

# numbers = [1, 2, 3, 4]
# letters = ['a', 'b', 'c']
# result = list(map(lambda x, y: str(x) + y, numbers, letters))
# print(result)

# result = [str(x)+y for x,y in zip(numbers,letters)]
# print(result)

# nums = [1, 2, 3, 4]
# filtered = filter(lambda x: x % 2 == 0, nums)
# # Modify the original list after creating the filter object
# nums.append(6)
# print(list(filtered))
# nums = [1, 2, 3, 4]
# filtered = list(filter(lambda x: x % 2 == 0, nums))
# filtered = filter(lambda x: x % 2 == 0, list(nums))
# # Modify the original list after creating the filter object
# nums.append(6)
# print(list(filtered))

# nums = [1, 2, 3]
# result = list(filter(print, nums))
# print("Result:", result)

# nums = [3, 7, 2, 5]
# first_even = filter(lambda x: x % 2 == 0, nums)[0]  # Intended to get the first even number
# print(first_even)

# nums = [3, 7, 2, 5]
# first_even = next(filter(lambda x: x % 2 == 0, nums))  # Intended to get the first even number
# print(first_even)


n = int(20)
# s = {*str(n)}
# a= n+1
# print(s)
# print('-------')
# while {*str(a)}&s:
#     print(s)
#     a+=1


# print(a)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
r=n
u = {*str(n)}
while u & set(str(r)):
    r += 1
    
print(r)

