
class A:
    pass

class B(A):
    pass


# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。

b = B()

print(isinstance(b, B))
print(isinstance(b, A))


print(type(b) is B)
print(type(b) is A)

a1 = 1
v = type(a1) is int
print("整形", v)


a2 = 1.5
v = type(a2) is float
print("浮点型", v)

a3 = ["a", "b"]

v = type(a3) is list
print("list", v)


a4 = {"a":"alice", "b":"bob"}

v = type(a4) is dict
print("dict", v)