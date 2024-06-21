# Data Types
# -> GETTING DATA TYPE -> type() function
# try yourself to see the output

# Text Type is a String
# str: A sequence of characters, used to represent text.
a = 'a text here'
print(a)
print(type(a))  

# We have three numeric types

# int: An integer, a whole number without a fractional part.
b = 20
print(b)
print(type(b))  

# float: A floating-point number, a number that has a decimal point.
c = 23.3
print(c)
print(type(c))  

# complex: A complex number, a number with a real and an imaginary part.
d = 2j
print(d)
print(type(d))  

# list: A collection which is ordered and changeable. Allows duplicate members.
e = ["Leonardo", "Ceccil", "Amanda"]
print(e)
print(type(e))  

# tuple: A collection which is ordered and unchangeable. Allows duplicate members.
f = (123123, -1231232)
print(f)
print(type(f))  

# range: A sequence of numbers, often used in for loops.
g = range(1, 10)
print(g)
print(type(g))  

# dict: A collection which is unordered, changeable, and indexed. No duplicate members.
h = {
    'key': 'value',
    'another-key': 'another-value'
}
print(h)
print(type(h))  

# set: A collection which is unordered and unindexed. No duplicate members.
i = {'this', 'is', 'a', 'set', 20, 1j}
print(i)
print(type(i))  

# frozenset: An immutable version of a set.
j = frozenset({"blue", "purple", "pink"})
print(j)
print(type(j))  

# bool: A Boolean value, either True or False.
l = True
print(l)
print(type(l))  
# or
l2 = bool(1)
l3 = bool(0)
print(l2)  
print(l3)  
print(type(l2))  
print(type(l3))  

# bytes: A sequence of bytes, immutable.
m = b"hello world"
print(m)
print(type(m))  

# bytearray: A mutable sequence of bytes.
n = bytearray(2)
print(n)
print(type(n))  

# memoryview: A view object which exposes the buffer protocol for memory-efficient access.
o = memoryview(bytes(3))
print(o)
print(type(o))  

# NoneType: Represents the absence of a value.
p = None
print(p)
print(type(p))  
