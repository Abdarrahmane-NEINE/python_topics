# Python OOP Cheat Sheet

This cheat sheet covers the main concepts of Object-Oriented Programming (OOP) in Python, including classes, objects, inheritance, polymorphism, encapsulation, and more. Use this as a quick reference for Python OOP.

---

## 1. Basic Concepts

### Classes and Objects
- **Class**: A blueprint for creating objects (instances).
- **Object**: An instance of a class.

**Example:**
```python
class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

# Creating an object (instance) of Dog
dog1 = Dog("Buddy", 3)
dog1.bark()  # Output: Buddy says woof!
```

## 2. Constructors and Initialization
- `__init__`: Special method called when a new object is instantiated.
- `self`: Refers to the current instance of the class.

**Example:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

person = Person("Alice", 30)
person.greet()  # Output: Hi, I'm Alice and I'm 30 years old.
```

## 3. Instance, Class, and Static Methods

### Instance Methods
Operate on an instance. Must have `self` as the first parameter.

**Example:**
```python
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(2, 3))  # Output: 5
```

### Class Methods
Operate on the class rather than instances. Use the `@classmethod` decorator. First parameter is `cls` (the class itself).

**Example:**
```python
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

a = MyClass()
b = MyClass()
print(MyClass.get_count())  # Output: 2
```

### Static Methods
Do not modify object or class state. Use the `@staticmethod` decorator.

**Example:**
```python
class Math:
    @staticmethod
    def multiply(a, b):
        return a * b

print(Math.multiply(3, 4))  # Output: 12
```

## 4. Encapsulation
Encapsulation: Bundling data (attributes) and methods within a single unit (class). Used to hide internal object state.

### Public, Protected, and Private Members
- **Public**: Accessible from anywhere.
- **Protected** (`_` prefix): Intended for internal use.
- **Private** (`__` prefix): Name mangled to prevent accidental access.

**Example:**
```python
class Example:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected"
        self.__private = "I am private"

    def get_private(self):
        return self.__private

e = Example()
print(e.public)       # Accessible
print(e._protected)   # Accessible, but intended as internal
print(e.get_private())  # Correct way to access private attribute
```

## 5. Inheritance
Inheritance: A way to form new classes using classes that have already been defined.
Base (or parent) class and Derived (or child) class.

**Example:**
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some generic sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Dog(Animal):
    def speak(self):
        print("Woof")

cat = Cat("Kitty")
dog = Dog("Buddy")
cat.speak()  # Output: Meow
dog.speak()  # Output: Woof
```

## 6. Multiple Inheritance and Mixins
Multiple Inheritance: A class can inherit from more than one base class.
Mixins: A type of multiple inheritance where classes provide additional functionality.

**Example:**
```python
class Flyer:
    def fly(self):
        print("Flying!")

class Swimmer:
    def swim(self):
        print("Swimming!")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")

duck = Duck()
duck.fly()    # Output: Flying!
duck.swim()   # Output: Swimming!
duck.quack()  # Output: Quack!
```

## 7. Polymorphism
Polymorphism: The ability to use a unified interface for different data types or classes.

**Example:**
```python
class Bird:
    def speak(self):
        print("Tweet")

class Parrot:
    def speak(self):
        print("Squawk")

def make_it_speak(animal):
    animal.speak()

bird = Bird()
parrot = Parrot()

make_it_speak(bird)    # Output: Tweet
make_it_speak(parrot)  # Output: Squawk
```
## 8. Dunder (Magic) Methods
Special methods that have double underscores before and after their names.

Common ones include:
- `__init__`: Constructor.
- `__str__`: Informal string representation.
- `__repr__`: Official string representation.
- `__add__`: Overload the addition operator.
- `__len__`: Called by `len()`.

**Example:**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1)           # Output: Point(1, 2)
print(p1 + p2)      # Output: Point(4, 6)
```

## 9. Abstract Classes and Interfaces
Abstract Classes: Classes that cannot be instantiated and typically include abstract methods.

Use the `abc` module.

**Example:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# shape = Shape()  # This would raise an error (cannot instantiate abstract class)
rect = Rectangle(3, 4)
print(rect.area())  # Output: 12
```

## 10. Properties
Properties: Allow for managed attribute access with getters, setters, and deleters.

Use the `@property` decorator.

**Example:**
```python
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value

temp = Celsius()
temp.temperature = 37
print(temp.temperature)  # Output: 37
```

## 11. Composition vs. Inheritance
Composition: A "has-a" relationship where one class is used as a part of another.
Inheritance: An "is-a" relationship where a class derives from another class.

**Example (Composition):**
```python
class Engine:
    def start(self):
        print("Engine starting...")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car starting...")

my_car = Car()
my_car.start()
```

## 12. Method Resolution Order (MRO)
MRO: Determines the order in which base classes are searched when executing a method.

Use the `mro()` method or the `__mro__` attribute.

**Example:**
```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass
print(D.mro())
# Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```
## 13. Metaclasses
A metaclass is a class of a class that defines how a class behaves.
Metaclasses are commonly used for advanced patterns such as class registration or automatic attribute creation.
The default metaclass in Python is `type`.

**Example:**
```python
# Custom metaclass that prints when a class is created
class MyMeta(type):
    def __new__(meta, name, bases, class_dict):
        print(f"Creating class {name}")
        return super().__new__(meta, name, bases, class_dict)

class MyClass(metaclass=MyMeta):
    pass

# Output: Creating class MyClass
```

## 14. Best Practices
- **Single Responsibility Principle**: Each class should have one responsibility.
- **Open/Closed Principle**: Classes should be open for extension but closed for modification.
- **DRY (Don’t Repeat Yourself)**: Reuse code through inheritance or composition.
- **Favor Composition Over Inheritance**: Use inheritance only when there is a clear "is-a" relationship.
- **Explicit is Better Than Implicit**: Clear code is easier to maintain and debug.

## 15. Additional Tips
### Duck Typing
Python follows duck typing; if an object implements the required methods, it can be used in place of another.

### Using `super()`
In derived classes, use `super()` to call methods from the parent class.

**Example:**
```python
class Base:
    def __init__(self):
        print("Base init")

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Derived init")

d = Derived()
# Output:
# Base init
# Derived init
```

### Operator Overloading
Customize built-in operators using dunder methods.

---
This document provides an overview of advanced OOP concepts in Python. Let me know if you need further explanations!
