#Data Types
# -> GETTING DATA TYPE -> type() function
#Text Type is a String  
#str

a = 'a text here'

print(a)
print(type(a))

#we have three numeric types
#int
b = 20
print(b)
print(type(b))

#float
c = 23.3
print(c)
print(type(c))

#complex
d= 2j
print(d)
print(type(d))


#list
e = ["Leonardo","Ceccil","Amanda"]
print(e)
print(type(e))

#tuple
f = (123123, -1231232)
print(f)
print(type(f))

#range
g = range(1,10)
print(g)
print(type(g))

#dict
h = {'key' : 'value',
     'another-key' : 'another-value'}
print(h)
print(type(h))

#set
i = {'this','is','a','dictionary', 20, 1j}
print(i)
print(type(i))

#frozenset
j = frozenset({"blue", "purple", "pink"})
print(j)
print(type(j))

#bool

l = True
print(l)
print(type(l))
#or
l2 = bool(1)
l3= bool(0)
print(l2)
print(l3)
print(type(l2))
print(type(l3))

#bytes
m = b"hello world"
print(m)
print(type(m))

#bytearray
n = bytearray(2)
print(n)
print(type(n))

#memoryview
o = memoryview(bytes(3))
print(o)
print(type(o))

#NoneType
p = None
print(p)
print(type(p))





