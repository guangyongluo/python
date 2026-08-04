class A:
    pass

class B(A):
    pass

b = B()

print(isinstance(b, B))
print(isinstance(b, A))

print(type(b) is B)
print(type(b) == B)
print(b == B)
print(b)
print(B)
print(b == B())
print(id(B()))
print(id(B()))
print(id(B()))
print(id(B()))
print(id(B()))